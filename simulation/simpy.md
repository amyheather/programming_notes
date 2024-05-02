# DES using SimPy

## Basic model structure (using object-oriented programming)

Two main ways to programme in python:
* **Functional** - write functions (designed to do one thing)
* **Object oriented** - create objects which have attributes and methods. These objects are created as classes. This is useful when have lots of logic to use, or when want to make copies of a similar thing.

A basic structure of a SimPy model:
* Class to store **global model parameters** (which you won’t create instances of, but instead will refer to directly when need to access something, hence might be lower case)
* Class to represent **entity** (which will have their attributes)
* Class to represent **system** (which will have generators, entity journeys, and store simpy environment)
* Class to represent **trial** (i.e. batch of simulation runs with methods to run them, and to store, record and display results from the trial) [[source]](https://hsma-programme.github.io/hsma6_des_book/recommended_structure_classes_for_des_models.html)

````{mermaid}
  flowchart TD;

    param("<b>Global model parameters</b>");
    entity("<b>Entity</b><br>Attributes");
    system("<b>System</b><br>Generators<br>Resources<br>Entity journeys<br>Stores simpy environment");
    trial("<b>Trial</b><br>Run model<br>Record and display result")
````

Where store results:
````{mermaid}
  flowchart TD;

    param("<b>Global model parameters</b>");
    entity("<b>Entity</b><br>Entity queue time");
    system("<b>System</b><br>Create and populate<br>results dataframe<br>with row for each entity");
    trial("<b>Trial</b><br>Run model<br>Record and display result")
````

:::{dropdown} View full code example

Code source: [HSMA](https://hsma-programme.github.io/hsma6_des_book/an_example_simpy_model.html)

This is a basic example (e.g. doesn't have sim-tools distributions with reproducibility)

```
import simpy
import random
import pandas as pd


# Global parameter values
# Don't make instance of this class, just access it directly
class g:
    patient_inter = 5
    mean_n_consult_time = 6
    number_of_nurses = 1
    sim_duration = 120
    number_of_runs = 5


# Entity (Patient) with two attributes: ID and time queueing
class Patient:
    def __init__(self, p_id):
        self.id = p_id
        self.q_time_nurse = 0


class Model:
    # Constructor to set up model for run
    def __init__(self, run_number):
        self.env = simpy.Environment()
        self.patient_counter = 0
        self.nurse = simpy.Resource(self.env, capacity=g.number_of_nurses)
        self.run_number = run_number
        # Blank dataframe for results
        self.results_df = pd.DataFrame()
        self.results_df["Patient ID"] = [1]
        self.results_df["Q Time Nurse"] = [0.0]
        self.results_df["Time with Nurse"] = [0.0]
        self.results_df.set_index("Patient ID", inplace=True)
        # Blank attribute to store mean queue time of run
        self.mean_q_time_nurse = 0

    # Generator function for patient arriving
    def generator_patient_arrivals(self):
        # Infinite loop does this indefinitely during simulation run
        while True:
            self.patient_counter += 1
            # Create a new patient
            p = Patient(self.patient_counter)
            # Send through process
            self.env.process(self.attend_clinic(p))
            # Sample time to next patient (inter-arrival time)
            sampled_inter = random.expovariate(1.0 / g.patient_inter)
            # Freeze this instance of this function until time has elapsed
            yield self.env.timeout(sampled_inter)

    # Generator function for patient going through clinic
    def attend_clinic(self, patient):
        # Wait start time
        start_q_nurse = self.env.now
        # Request a nurse resource
        with self.nurse.request() as req:
            # Queue until resource available
            yield req
            # Wait end time
            end_q_nurse = self.env.now
            patient.q_time_nurse = end_q_nurse - start_q_nurse
            # Sample time with nurse
            sampled_nurse_act_time = random.expovariate(1.0 /
                                                        g.mean_n_consult_time)
            # Store queue time and time with nurse in results
            self.results_df.at[patient.id, "Q Time Nurse"] = (
                patient.q_time_nurse)
            self.results_df.at[patient.id, "Time with Nurse"] = (
                sampled_nurse_act_time)
            # Freeze this instance of this function (i.e. for this entity) for the time spent with nurse
            yield self.env.timeout(sampled_nurse_act_time)
            # Sink


    def calculate_run_results(self):
        # Find mean queue time
        self.mean_q_time_nurse = self.results_df["Q Time Nurse"].mean()


    def run(self):
        # Start up DES entity generators that create new patients
        self.env.process(self.generator_patient_arrivals())
        # Run the model
        self.env.run(until=g.sim_duration)
        # Calculate results
        self.calculate_run_results()
        # Print results
        print (f"Run Number {self.run_number}")
        print (self.results_df)


class Trial:
    # Set up dataframe to store results from each run
    def  __init__(self):
        self.df_trial_results = pd.DataFrame()
        self.df_trial_results["Run Number"] = [0]
        self.df_trial_results["Mean Q Time Nurse"] = [0.0]
        self.df_trial_results.set_index("Run Number", inplace=True)

    # Print trial results
    def print_trial_results(self):
        print ("Trial Results")
        print (self.df_trial_results)

    def run_trial(self):
        for run in range(g.number_of_runs):
            # Conduct run of model
            my_model = Model(run)
            my_model.run()
            # Store results from run
            self.df_trial_results.loc[run] = [my_model.mean_q_time_nurse]
        # Print trial results
        self.print_trial_results()

# To run the above, create instance of trial class and run it
my_trial = Trial()
my_trial.run_trial()
```
:::

When we use **env.timeout**, it is specification to each entity (i.e. time passes for just that entity), and so if you kill a process, only that entity is affected. However, it is possible to have some specific types of process that interrupt each other. [[source]](https://stackoverflow.com/questions/76635524/timeout-function-in-simpy-how-does-it-work)

To add another activity, just write it after the first one in the pathway generator function (although outside the with statement, else will drag resource from previous activity with it, unless you want that) - [see example.](https://hsma-programme.github.io/hsma6_des_book/an_example_simpy_model_multiple_steps.html)

You can model **branching paths** using conditional logic - [see example.](https://hsma-programme.github.io/hsma6_des_book/an_example_simpy_model_branching.html)


## Producing entity arrivals (using generator functions)

:::{dropdown} What are generator functions?

In a normal function we **return** values, which returns a value then terminates the function. In a **generator function** we **yield** values, which returns a value then pauses execution by saving states.
* Local variables and their states are **remembered** between successive calls of the generator function.
* A generator function is creating an **iterator** and returning an iterator object
* We can use **multiple yield** statements in the generator function

Example:

```
def seq(x):
    for i in range(x):
        yield i

range = seq(10)

# If you called this eleven times, on the final time it would stop with the error StopIteration
```

[[source]](https://www.scaler.com/topics/python/python-generators/)

**Why use them?**
* **Easier to implement then iterators**
* **Memory efficient** - a normal function can return a sequence of items but it has to create a sequence in memory before it can give result - whilst a generator function produces one output at a time
* **Infinite sequence** - can’t store infinite sequences in a given memory, but as generators only produce one item at a time, they can present an infinite stream of data [[source]](https://www.scaler.com/topics/python/python-generators/)

You can make a python **generator expression **(instead of a function) which is a short-hand form of a generator function. You implement them similar to lambda functions but use round brackets. The difference here is:
* List comprehension returns list of items
* Generator expression returns an iterable object

Example:
```
# List comprehension
list_ = [i for i in range(x) if i % 2 == 0]

# Generator expression
list_ = (i for i in range(x) if i % 2 == 0)
```

[[source]](https://www.scaler.com/topics/python/python-generators/)

:::


The generator functions are used **for entities arriving into a process**
* Set up simpy environment, customer counter, resource, run number, dataframe to store results
* Create **generator function to represent customer arrivals**, which creates new customer, uses another generator (for calls), then moves time forward by inter-arrival time (which know from sampling from distribution)
* Have **generator function to represent customer calling helpline** - requests resource, calculates time they had queued, samples time then spent with resource, then move forward by that amount of time (i.e. free that function in place for the activity time sample above) [[source]](https://hsma-programme.github.io/hsma6_des_book/recommended_structure_classes_for_des_models.html)

## Resources

### Requesting multiple resources simultaneously

For example, if you need to request a nurse and a room, before can proceed with appointment.

To set this up, create the resources, with attributes and columns in the results dataframe to record queue time and appointment time.

You'll have **conditional** logic to check if have one resource (and need to wait for other), or have both resources available at once.

We request the resources without indentation, and so **manually specifying when to stop using the resource** which makes it easier when you are writing code that requests multiple resources at once.

```
# There are two ways to request a resource in SimPy...

# Method 1
with self.receptionist.request() as req:
    yield req
    # Rest of code here, to run whilst holding resource

# Method 2
nurse_request = self.receptionist.request()
yield nurse_request
# Rest of code here, to run whilst holding resource
self.nurse.release(nurse_request)
```

[[source]](https://hsma-programme.github.io/hsma6_des_book/requesting_multiple_resources.html)

### Priority queue

Create priority based queueing with **PriorityResource**. It’s like the standard SimPy Resource class, but has functionality that allows it to select which entity to pull out of queue based on a priority value. To use:
1. Set up resource using **PriorityResource** rather than Resource
2. Have **attribute** in each entity that gives their priority (**lower value = higher priority**)
When request PriorityResource, tell it what attribute it should use to determine priority in queue
3. If there are a few people waiting, it will just the person with the highest priority. If people have the same priority, it will choose the oldest of those.

Remember that our results only include people who get seen by the nurse - and so when the model stops, there could still be loads of people waiting in a queue - you'll want to account for that. [[source]](https://hsma-programme.github.io/hsma6_des_book/priority_based_queueing.html)

### Resource unavailability

If the **level of resource varies** (e.g. its not 5 doctors constantly available 24/7), then you can model this in SimPy by **"obstructing" a resource** for a certain amount of time.

Example: Nurse takes 15 minute break every 2 hours
1. Set **frequency and duration of unavailability** as parameter values in parameter class
2. Set up nurse as **PriorityResource**
3. Create **entity generator to demand the nurse resource with a higher priority than any patient every 2 hours** (i.e. use a **negative** value), which will freeze the nurse with them for 15 minutes (but this means the nurse will complete the current patient and won’t walk out midway through)
4. Set up the new generator running in the run method of the Model class [[source]](https://hsma-programme.github.io/hsma6_des_book/modelling_resource_unavailability.html)

## Reproducibility

You could set one seed per run. We then do 100 runs. Then we repeat that again. We want the results to be the same - and they are, yay!

Now we do a scenario where we **change the number of nurses**. We expect this to:
* **Change the queues** for nurses and doctors - yes 🙂
* Number of **arrivals remain unchanged** - **no**! 🙁

This is because all the methods are using one seed. The order that the random numbers are generated in matters. As the order of events changes (e.g. as have more nurses, they can see more patients quicker, changing the order that subsequent events happen).

Hence, a robust way to do this is to **set seeds for each type of event that we are generating random numbers for**. This means that each event has a separate random number stream for each part of process (e.g. for the inter-arrival times, for the consult times, for our probabilities when branching). [[source]](https://hsma-programme.github.io/hsma6_des_book/reproducibility.html)

## Sampling from distributions

[Sim-tools](https://github.com/TomMonks/sim-tools) contains a bunch of functions you can use. This are set up to have individual seeds, to esaily enable reproducibility.

Example: 

```
from sim_tools.distributions import Exponential

# Later in code...

self.patient_inter_arrival_dist = Exponential(mean = g.patient_inter, random_seed = self.run_number*2)
```

The Exponential Class from the package (you'll see there's actually only a few lines of code):

```
class Exponential(Distribution):
    """
    Convenience class for the exponential distribution.
    packages up distribution parameters, seed and random generator.
    """

    def __init__(self, mean: float, random_seed: Optional[int] = None):
        """
        Constructor

        Params:
        ------
        mean: float
            The mean of the exponential distribution

        random_seed: int, optional (default=None)
            A random seed to reproduce samples.  If set to none then a unique
            sample is created.
        """
        super().__init__(random_seed)
        self.mean = mean

    @abstractmethod
    def sample(self, size: Optional[int] = None) -> float | np.ndarray:
        """
        Generate a sample from the exponential distribution

        Params:
        -------
        size: int, optional (default=None)
            the number of samples to return.  If size=None then a single
            sample is returned.
        """
        return self.rng.exponential(self.mean, size=size)
```

[[source]](https://hsma-programme.github.io/hsma6_des_book/choosing_distributions.html)

## Variable arrival rates

You could have variable arrival rates (e.g. high in afternoon, low at night). To model this you can use sim-tools which has a class that creates a non-stationary poisson process via thinning
* “Thinning is an acceptance-rejection approach to sampling inter-arrival times (IAT) from a time dependent distribution where each time period follows its own exponential distribution.”
* Provide dataframe with mean IAT at various time points
* Set up arrival distribution in Model class with NSPPThinning() [[source]](https://hsma-programme.github.io/hsma6_des_book/modelling_variable_arrival_rates.html)

## Performance tracking

### Resource utilisation

We want to track resource utilisation **overall** as well as at **specific time points**. We often won't want utilisation to be close to 100%, although what we do want depends on the type and size of service (e.g. emergency service want lower utilisation so can safely cope with spike in demand).

#### Method 1. Simple average across the run

We can track how long each entity spends using a resource, then sum time spent, divide by time elapsed in model, and multiply by number of resources in model.

This may slightly overestimate utilisation though as we record time spent with the resource prior to that time elapsing - e.g. “If we have a model run time of 600 time units, and someone reaches the nurse at unit 595 but has an activity time of 30, we will record that and use it in our calculations - even though only 5 minutes of that time actually took place during our model run.” You could adapt code to account for that (e.g. check if time remaining in model is greater than activity time sampled, and record whichever of those is smaller). [[source]](https://hsma-programme.github.io/hsma6_des_book/tracking_resource_utilisation.html)

#### Method 2. Interval audit process

For this, we create a function that takes:
1. A list of resources to monitor, and
2. A time interval at which to snapshot utilisation

This is integrated into the code, and then set up as a process. [[source]](https://hsma-programme.github.io/hsma6_des_book/tracking_resource_utilisation.html)

### Other metrics

**Arrivals** (as in the simple example above).

**Percentage of entities meeting a target** (e.g. 4 hour arrival to admission). Consider whether anything in historical data patterns is because of trying to meet targets (e.g. 17% of admissions to a&e between 3h50 and 4h). "If the target was removed, would this result in a change in behaviour? How might the predictions of our model be affected by this?"

**Throughput - % of people entering system who have left by time model stops running** - low throughput suggests a bottleneck - "can be a useful measure to track as a quick way of assessing whether different scenarios are leading to severe bottlenecks, but it is not that useful as a standalone measure." [[source]](https://hsma-programme.github.io/hsma6_des_book/other_model_metrics.html)

## Testing a large number of scenarios

We run scenarios with different levels of resources, etc. To test a large number, [recommend the method here](https://hsma-programme.github.io/hsma6_des_book/testing_large_numbers_scenarios.html). It involves you having:
* Dictionary of scenarios
* Use itertools to create all possible permutations of scenarios
* Add scenario name to g class, then enumerate through the scenarios and run each one, storing the results as you go [[source]]((https://hsma-programme.github.io/hsma6_des_book/testing_large_numbers_scenarios.html))