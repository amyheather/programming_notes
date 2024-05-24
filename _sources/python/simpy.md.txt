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

## Alternatives layouts

Mostly below explains modifications based on the HSMA model layout. However, there are lots of different ways you can choose to lay out a SimPy model. Some more examples are provided below...

:::{dropdown} Basic example from Tom on MSc

[Example source.](https://github.com/health-data-science-OR/stochastic_systems/blob/master/labs/simulation/lab1/simulation_lab1_SOLUTIONS.ipynb)

You can see it's pretty similar. Ignoring the slight differences in what is being modelled (and that is not collecting results), the main differences in how code is structured are:
* No class for global parameters - defined within script
* Function for patient attending clinic (service()) is within Patient rather than Model
* Environment, Resource, run and process outside of the Model

```
class Patient:
    '''
    Encapsulates the process a patient caller undergoes when they dial 111
    and speaks to an operator who triages their call.
    '''
    def __init__(self, identifier, env, operators):
        '''
        Constructor method
        
        Params:
        -----
        identifier: int
            a numeric identifier for the patient.
            
        env: simpy.Environment
            the simulation environment
            
        operators: simpy.Resource
            the call operators
        '''
        self.identifier = identifier
        self.env = env
        self.operators = operators
         
    def service(self):
        '''
        simualtes the service process for a call operator
        
        1. request and wait for a call operator
        2. phone triage (triangular)
        3. exit system
        '''
        # record the time that call entered the queue
        start_wait = env.now

        # request an operator 
        with self.operators.request() as req:
            yield req
            
            # record the waiting time for call to be answered
            self.waiting_time = self.env.now - start_wait
            print(f'operator answered call {self.identifier} at ' \
                      + f'{self.env.now:.3f}')
            
            # sample call duration.
            call_duration = np.random.triangular(left=0.01, mode=0.12, 
                                                 right=0.16)
            yield self.env.timeout(call_duration)
            
            print(f'call {self.identifier} ended {self.env.now:.3f}; ' \
                      + f'waiting time was {self.waiting_time:.3f}')


class UrgentCareCallCentre:
    '''
    111 call centre model
    '''
    def __init__(self, env, operators):
        '''
        Constructor method
        
        Params:
        --------
        env: simpy.Environment
        
        operators: simpy.Resource
            A pool of call operators triage incoming patient calls.
        '''
        self.env = env
        self.operators = operators 
            
    def arrivals_generator(self):
        '''
        IAT is exponentially distributed with mean

        Parameters:
        ------
        env: simpy.Environment

        operators: simpy.Resource
            the call operators.
        '''

        # use itertools as it provides an infinite loop with a counter variable
        for caller_count in itertools.count(start=1):

            # 100 calls per hour (units = hours). Time between calls is 1/100
            inter_arrival_time = np.random.exponential(1/100)
            yield env.timeout(inter_arrival_time)

            print(f'call arrives at: {env.now:.3f}')
            new_caller = Patient(caller_count, self.env, self.operators)
            env.process(new_caller.service())


# model parameters
RUN_LENGTH = 0.25
N_OPERATORS = 13

# create simpy environment and operator resources
env = simpy.Environment()
operators = simpy.Resource(env, capacity=N_OPERATORS)

# create a model
model = UrgentCareCallCentre(env, operators)

env.process(model.arrivals_generator())
env.run(until=RUN_LENGTH)
print(f'end of run. simulation clock time = {env.now}')
```

:::

## Producing entity arrivals (using generator functions)

:::{dropdown} What are generator functions?

In a normal function we **return** values, which returns a value then terminates the function. In a **generator function** we **yield** values, which returns a value then pauses execution by saving states.
* Local variables and their states are **remembered** between successive calls of the generator function.
* A generator function is creating an **iterator** and returning an iterator object
* We can use **multiple yield** statements in the generator function

Example:

```
# Source: https://www.geeksforgeeks.org/generators-in-python/

# Generator function
def simple_generator(): 
    yield 1
    yield 2
    yield 3

# Generator object
x = simple_generator()

# Iterating over the generator object using next
print(next(x))
print(next(x))
print(next(x))
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

## Variable arrival rates (i.e. time-dependent arrivals)

You could have variable arrival rates (e.g. high in afternoon, low at night). To model this you can use sim-tools which has a class that creates a **non-stationary poisson process via thinning**. [[source]](https://hsma-programme.github.io/hsma6_des_book/modelling_variable_arrival_rates.html)

:::{dropdown} What is a non-stationary Poisson process with thinning?

First, we define a **random process** (or **stochastic process**) as a collection of random variables usually indexed by time. For each time point, the value is a random variable. They can be classified as continuous-time or discrete-time.

One example of a random process is the **Poisson process**. This is a continuous-time random process.[[source]](https://dlsun.github.io/probability/random-process.html) It is typically used when we want to account the occurence of something that happens **at a certain rate over some time interval** but is also completely at **random**, with occurences **independent** of each other (e.g. know that area has rate of 2 earthquakes a month, although their timing is otherwise completely random).[[source]](https://www.probabilitycourse.com/chapter11/11_1_2_basic_concepts_of_the_poisson_process.php)

A Poisson process - also known as **stationary or time-stationary or time-homogenous** Poisson process - has a fixed and **constant rate** over time. However, if the rate varies over time (e.g. higher rate of arrivals in afternoon than at night), then it is a **non-stationary Poisson process**.[[source]](http://www.columbia.edu/~ks20/4404-Sigman/4404-Notes-NSP.pdf) Hence, a **non-stationary Poisson process** is an arrival process with an arrival rate that varies by time.[[source]](https://github.com/health-data-science-OR/stochastic_systems/blob/master/labs/simulation/lab4/sim_lab4_nspp_SOLUTIONS.ipynb)

A non-stationary Poisson process can be generated either by **thinning** or **rate inversion**. The thinning method involves first generating a stationary Poisson process with a constant rate, but then rejecting potential arrivals at a given time by a given probability. [[source]](https://rossetti.github.io/RossettiArenaBook/ch6-sec-NSPP.html) In other words, thinning is an acceptance-rejection sampling method[[source]](https://github.com/health-data-science-OR/stochastic_systems/blob/master/labs/simulation/lab4/sim_lab4_nspp_SOLUTIONS.ipynb) from a time dependent distribution where each time period follows its own exponential distribution.[[source]](https://hsma-programme.github.io/hsma6_des_book/modelling_variable_arrival_rates.html)

:::

To set this up we:
* Provide dataframe with mean IAT at various time points
* Set up arrival distribution in Model class with NSPPThinning() [[source]](https://hsma-programme.github.io/hsma6_des_book/modelling_variable_arrival_rates.html)

## Tracking resource utilisation

### Method 1. Simple average across the run

We can track how long each entity spends using a resource, then sum time spent, divide by time elapsed in model, and multiply by number of resources in model.

This may slightly overestimate utilisation though as we record time spent with the resource prior to that time elapsing - e.g. “If we have a model run time of 600 time units, and someone reaches the nurse at unit 595 but has an activity time of 30, we will record that and use it in our calculations - even though only 5 minutes of that time actually took place during our model run.” You could adapt code to account for that (e.g. check if time remaining in model is greater than activity time sampled, and record whichever of those is smaller). [[source]](https://hsma-programme.github.io/hsma6_des_book/tracking_resource_utilisation.html)

### Method 2. Interval audit process

For this, we create a function that takes:
1. A list of resources to monitor, and
2. A time interval at which to snapshot utilisation

This is integrated into the code, and then set up as a process. [[source]](https://hsma-programme.github.io/hsma6_des_book/tracking_resource_utilisation.html)

Overview of how [HSMA code](https://hsma-programme.github.io/hsma6_des_book/tracking_resource_utilisation.html) is modified for auditing:

| Class | Changes |
| --- | --- |
| Global model parameters | • Set audit interval (e.g. 5 min) |
| Patient | - |
| Model | • Generator function to get metrics at given intervals, storing results as attribute<br>• Add audit process to run i.e. self.env.process() |
| Trial | • Get audit results from model attributes

That is a HSMA example. We can also look at a different example from Tom (basic code structure differs - see above). In his example, he does not modify the Model or Patient classes, but instead creates an **Auditor class**. It performs the same job - getting metrics at given intervals.
* Audits occur at first_obs and then interval time units apart
* Queues and services are lists that will store a tuple identifying what want to audit
* Metrics is a dict to store audits
* Scheduled_audit - env.timeout() for delay between aduits, record_queue_length() finds length of queues (for each service, append length of their queue to dictionary)

[[source]](https://github.com/health-data-science-OR/stochastic_systems/blob/master/labs/simulation/lab1/simulation_lab1_SOLUTIONS.ipynb)

:::{dropdown} Tom's Auditor class

```
class Auditor:
    def __init__(self, env, run_length, first_obs=None, interval=None):
        '''
        Auditor Constructor
        
        Params:
        -----
        env: simpy.Environment
            
        first_obs: float, optional (default=None)
            Time of first scheduled observation.  If none then no scheduled
            audit will take place
        
        interval: float, optional (default=None)
            Time period between scheduled observations. If none then no scheduled
            audit will take place
        '''
        self.env = env
        self.first_observation = first_obs
        self.interval = interval
        self.run_length = run_length
        
        self.queues = []
        self.service = []
        
        # dict to hold states
        self.metrics = {}
        
        # scheduled the periodic audits
        if not first_obs is None:
            env.process(self.scheduled_observation())
            env.process(self.process_end_of_run())
            
    def add_resource_to_audit(self, resource, name, audit_type='qs'):
        if 'q' in audit_type:
            self.queues.append((name, resource))
            self.metrics[f'queue_length_{name}'] = []
        
        if 's' in audit_type:
            self.service.append((name, resource))
            self.metrics[f'system_{name}'] = []           
            
    def scheduled_observation(self):
        '''
        simpy process to control the frequency of 
        auditor observations of the model.  
        
        The first observation takes place at self.first_obs
        and subsequent observations are spaced self.interval
        apart in time.
        '''
        # delay first observation
        yield self.env.timeout(self.first_observation)
        self.record_queue_length()
        self.record_calls_in_progress()
        
        while True:
            yield self.env.timeout(self.interval)
            self.record_queue_length()
            self.record_calls_in_progress()
    
    def record_queue_length(self):
        for name, res in self.queues:
            self.metrics[f'queue_length_{name}'].append(len(res.queue)) 
        
        
    def record_calls_in_progress(self):
        for name, res in self.service:
            self.metrics[f'system_{name}'].append(res.count + len(res.queue)) 
               
        
    def process_end_of_run(self):
        '''
        Create an end of run summary
        
        Returns:
        ---------
            pd.DataFrame
        '''
        
        yield self.env.timeout(self.run_length - 1)
        
        run_results = {}

        for name, res in self.queues:
            queue_length = np.array(self.metrics[f'queue_length_{name}'])
            run_results[f'mean_queue_{name}'] = queue_length.mean()
            
        for name, res in self.service:
            total_in_system = np.array(self.metrics[f'system_{name}'])
            run_results[f'mean_system_{name}'] = total_in_system.mean()
        
#         #mean number in system and in queue (specific to operations)        
#         queue_length = np.array(self.metrics['queue_length_ops'])
#         total_in_system = queue_length + np.array(self.metrics['service_ops'])

#         run_results['mean_queue'] = queue_length.mean()
#         run_results['mean_system'] = total_in_system.mean()

        self.summary_frame = pd.Series(run_results).to_frame()
        self.summary_frame.columns = ['estimate']
```

:::

## Testing a large number of scenarios

We run scenarios with different levels of resources, etc. To test a large number, [recommend the method here](https://hsma-programme.github.io/hsma6_des_book/testing_large_numbers_scenarios.html). It involves you having:
* Dictionary of scenarios
* Use itertools to create all possible permutations of scenarios
* Add scenario name to g class, then enumerate through the scenarios and run each one, storing the results as you go [[source]](https://hsma-programme.github.io/hsma6_des_book/testing_large_numbers_scenarios.html)

## Determining how many replications to run.

'You will now use the confidence interval method to select the number replications to run in order to get a good estimate the models mean performance. The narrower the confidence interval the more precise our estimate of the mean. In general, the more replications you run the narrower the confidence interval. The method requires you to set a predefined width of the confidence interval' - e.g. 5% or 10% either side of mean. Use the following function to implement in Python...[[source]](https://github.com/health-data-science-OR/stochastic_systems/blob/master/labs/simulation/lab6/sim_lab6_output_analysis_SOLUTIONS.ipynb)

:::{dropdown} Confidence interval method to determine replication number

[[source]](https://github.com/health-data-science-OR/stochastic_systems/blob/master/labs/simulation/lab6/sim_lab6_output_analysis_SOLUTIONS.ipynb)

'The method is less useful for values very close to zero. As the utilisation measures are between 0 and 1 it is recommended that you multiple the values by 100.'

Function:

```
def confidence_interval_method(replications, alpha=0.05, desired_precision=0.05, 
                               min_rep=5, decimal_place=2):
    '''
    The confidence interval method for selecting the number of replications
    to run in a simulation.
    
    Finds the smallest number of replications where the width of the confidence
    interval is less than the desired_precision.  
    
    Returns both the number of replications and the full results dataframe.
    
    Parameters:
    ----------
    replications: arraylike
        Array (e.g. np.ndarray or list) of replications of a performance metric
        
    alpha: float, optional (default=0.05)
        procedure constructs a 100(1-alpha) confidence interval for the 
        cumulative mean.
        
    desired_precision: float, optional (default=0.05)
        Desired mean deviation from confidence interval.
        
    min_rep: int, optional (default=5)
        set to a integer > 0 and ignore all of the replications prior to it 
        when selecting the number of replications to run to achieve the desired
        precision.  Useful when the number of replications returned does not
        provide a stable precision below target.
        
    decimal_places: int, optional (default=2)
        sets the number of decimal places of the returned dataframe containing
        the results
    
    Returns:
    --------
        tuple: int, pd.DataFrame
    
    '''
    n = len(replications)
    cumulative_mean = [replications[0]]
    running_var = [0.0]
    for i in range(1, n):
        cumulative_mean.append(cumulative_mean[i-1] + \
                       (replications[i] - cumulative_mean[i-1] ) / (i+1))
        
        # running biased variance
        running_var.append(running_var[i-1] + (replications[i] 
                                               - cumulative_mean[i-1]) \
                            * (replications[i] - cumulative_mean[i]))
        
    # unbiased std dev = running_var / (n - 1)
    with np.errstate(divide='ignore', invalid='ignore'):
        running_std = np.sqrt(running_var / np.arange(n))
    
    # half width of interval
    dof = len(replications) - 1
    t_value = t.ppf(1 - (alpha / 2),  dof)    
    with np.errstate(divide='ignore', invalid='ignore'):
        std_error = running_std / np.sqrt(np.arange(1, n+1))
        
    half_width = t_value * std_error
        
    # upper and lower confidence interval
    upper = cumulative_mean + half_width
    lower = cumulative_mean - half_width
    
    # Mean deviation
    with np.errstate(divide='ignore', invalid='ignore'):
        deviation = (half_width / cumulative_mean) * 100
    
    # commbine results into a single dataframe
    results = pd.DataFrame([replications, cumulative_mean, 
                            running_std, lower, upper, deviation]).T
    results.columns = ['Mean', 'Cumulative Mean', 'Standard Deviation', 
                       'Lower Interval', 'Upper Interval', '% deviation']
    results.index = np.arange(1, n+1)
    results.index.name = 'replications'
    
    # get the smallest no. of reps where deviation is less than precision target
    try:
        n_reps = results.iloc[min_rep:].loc[results['% deviation'] 
                             <= desired_precision*100].iloc[0].name
    except:
        # no replications with desired precision
        message = 'WARNING: the replications do not reach desired precision'
        warnings.warn(message)
        n_reps = -1 

    
    return n_reps, results.round(2)
```

Using function:

```
# run the method on the operator_wait replications
n_reps, conf_ints = \
    confidence_interval_method(replications['operator_wait'].to_numpy(),
                               desired_precision=0.05)

# print out the min number of replications to achieve precision
print(f'\nminimum number of reps for 5% precision: {n_reps}\n')

# peek at table of results
conf_ints.head()

def plot_confidence_interval_method(n_reps, conf_ints, metric_name, 
                                    figsize=(12,4)):
    '''
    Plot the confidence intervals and cumulative mean
    
    Parameters:
    ----------
    n_reps: int
        minimum number of reps selected
        
    conf_ints: pandas.DataFrame
       results of the `confidence_interval_method` function
       
    metric_name: str
        Name of the performance measure
        
    figsize: tuple, optional (default=(12,4))
        The size of the plot
        
    Returns:
    -------
        matplotlib.pyplot.axis
    '''
    # plot cumulative mean + lower/upper intervals
    ax = conf_ints[['Cumulative Mean', 'Lower Interval', 
                         'Upper Interval']].plot(figsize=figsize)
    # add the 
    ax.axvline(x=n_reps, ls='--', color='red')
    
    ax.set_ylabel(f'cumulative mean: {metric_name}')
    
    return ax

# plot the confidence intervals
ax = plot_confidence_interval_method(n_reps, conf_ints, 
                                     metric_name='operator_wait')

# quick check if the % deviation remains below 5% for the next 10 reps?
lookahead = 15
conf_ints.iloc[n_reps-1:n_reps+lookahead]
# run the method on the operator_wait replications
n_reps, conf_ints = \
    confidence_interval_method(replications['operator_wait'].to_numpy(),
                               desired_precision=0.05, min_rep=36)


# print out the min number of replications to achieve precision
print(f'\nminimum number of reps for 5% precision: {n_reps}\n')

# plot the confidence intervals
ax = plot_confidence_interval_method(n_reps, conf_ints, 
                                     metric_name='operator_wait', figsize=(9,6))
```

:::

## Appointment booking (i.e. scheduling)

We may want to model appointment booking (i.e. delay between enter system to book appointment, and attending appointment), rather than immediate attendance. [See example from HSMA](https://hsma-programme.github.io/hsma6_des_book/appointment_style_booking_models.html), which is based on [Tom's example](https://github.com/health-data-science-OR/stochastic_systems/tree/master/labs/simulation/lab5).

Overview of core changes to [HSMA code](https://hsma-programme.github.io/hsma6_des_book/appointment_style_booking_models.html) for appointment booking (with time unit here being **days** rather than minutes):

| Class | Modifications |
| --- | --- |
| Global parameters | New attributes:<br>• Annual demand rather than IAT<br>• Shifts dataframe with number of available appointments per day<br>• Minimum wait (so can't get appointment immediately) |
| Patient | New attributes:<br>• Booker<br>• Arrival time<br>• Wait time |
| Booker | Attributes:<br>• Priority<br>• Model<br><br>Functions:<br>• <b>find_slot():</b> Find available slot in diary<br>• <b>book_slot():</b> Book the slot |
| Model | New attributes:<br>•Available slots<br>• Bookings<br>• Run create_slots()<br>• Run create_bookings()<br>• Arrival distribution<br>• Monitoring of patient queue time and mean<br><br>New functions:<br>• <b>create_slots()</b>: extrapolate shift dataframe to cover run time + longer (so can book ahead)<br>• <b>create_bookings()</b>: create blank dataframe of same dimensions so can use to track number of patients booked<br><br>Changed functions:<br>• <b>generator_patient_arrivals():</b> instead of generate patient then wait until next, instead sample arrivals per day, loop through referrals and make patients, start booker for each patient, then run attend clinic for each patient<br>• <b>attend_clinic():</b> find_slot(), book_slot(), env.timeout() until appointment, then save time between enter system and appointment  |
| Trial | Save new metrics (appointment wait) |

You can allow patients to have a range of possible clinics that they can book into. You can do this by having a **pooling matrix** which is a simple table of 0s and 1s determining whether a patient can access each clinic. The package sim_utility has some premade Booker classes. To work with pooled booking, you could use the class one of their pooled booker classes e.g. `LowPriorityPooledBooker` from sim_utility (rather than `LowPriorityBooker`). [[source]](https://github.com/health-data-science-OR/stochastic_systems/blob/master/labs/simulation/lab5/sim_lab5_scheduling_models_SOLUTIONS.ipynb)

## Parallelisation

By default, Python code will run everything sequentially on a single core. We can run code in parallel to reduce run length. Use **Joblib** to split SimPy code to run across multiple processor cores. May not be possible when deploying on web.

:::{dropdown} How does Joblib work?

We can illustrate this with a simple function:

```
import time
import math
from joblib import Parallel, delayed

def my_function(i):
    # Wait one second
    time.sleep(1)
    # Return square root of i**2
    return math.sqrt(i**2)
```

If we run this function with a **for loop**, it takes ten seconds:

```
i = num
start = time.time()

# Run function in for loop
for i in range(num):
    my_function(i)

end = time.time()
# Print time elapsed
print('{:.4f} s'.format(end-start))

10.0387 s
```

If we run it using **Parallel** and **delayed** functions from joblib, it takes five seconds.[[source]](https://measurespace.medium.com/use-joblib-to-run-your-python-code-in-parallel-ad82abb26954) We use the delayed() function as it prevents the function from running. If we just had `Parallel(n_jobs=2)(my_function(i) for i in range(num))`, by the time it gets passed to Paralell, the `my_function(i)` calls have already returned, and there's nothing left to execute in Parallel. [[source]](https://stackoverflow.com/questions/42220458/what-does-the-delayed-function-do-when-used-with-joblib-in-python)

```
start = time.time()

# Run function using parallel processing
# n_jobs is the number of parallel jobs
Parallel(n_jobs=2)(delayed(my_function(i) for i in range(num)))

end = time.time()
# Print time elapsed
print('{:.4f} s'.format(end-start))

5.6560 s
```

[[source]](https://measurespace.medium.com/use-joblib-to-run-your-python-code-in-parallel-ad82abb26954)

:::

An overview of the changes we make to implement this for our SimPy model are below. These are from [this HSMA example](https://hsma-programme.github.io/hsma6_des_book/running_parallel_cpus.html), which is based on an [example from Mike](https://github.com/MichaelAllen1966/2004_simple_simpy_parallel).

| Class | Changes |
| --- | --- |
| Global parameters | - |
| Patient | - |
| Model | - |
| Trial | • Changes for how save results, so save dictionary of results from run into list (rather than setting up a dummy dataframe and using .loc to write results into correct row, as will just end up with empty results list, when running parallel)<br>• Split run_trial() into two functions, with <b>run_trial()</b> containing `self.df_trial_results = Parallel(n_jobs=-1)(delayed(self.run_single)(run) for run in range(g.number_of_runs))` (-1 means every available core will run code)

## Input modelling

Mike write some code (archived but copied below) which fits various distributions to the data, then conductes Chi-Squared and KS-Test and ranks by the Chi-Squared statistics. It produces histograms, p-p plots, and q-q plots of the data against the theoretical distributions

:::{dropdown} Auto fit

[[source]](https://github.com/health-data-science-OR/stochastic_systems/blob/master/labs/simulation/lab3/input_modelling/fitting.py)

```
import warnings
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

def auto_fit(data_to_fit, hist=False, pp=False, dist_names=None):

    y = data_to_fit.dropna().to_numpy()
    size = len(y)
    sc = StandardScaler() 
    yy = y.reshape(-1, 1)
    sc.fit(yy)
    y_std = sc.transform(yy)
    y_std = y_std.flatten()
    del yy

    if dist_names is None:
        dist_names = ['beta',
                      'expon',
                      'gamma',
                      'lognorm',
                      'norm',
                      'pearson3',
                      'weibull_min', 
                      'weibull_max']

    # Set up empty lists to store results
    chi_square = []
    p_values = []

    # Set up 50 bins for chi-square test
    # Observed data will be approximately evenly distrubuted aross all bins
    percentile_bins = np.linspace(0,100,50)
    percentile_cutoffs = np.percentile(y_std, percentile_bins)
    
    #"fix": sometimes np.percentile produces cut-off that are not sorted!?  
    #Why?  The test data was synthetic LoS in an ED and they are rounded numbers...
    observed_frequency, bins = (np.histogram(y_std, bins=np.sort(percentile_cutoffs)))
    cum_observed_frequency = np.cumsum(observed_frequency)

    # Loop through candidate distributions

    for distribution in dist_names:
        # Set up distribution and get fitted distribution parameters
        dist = getattr(scipy.stats, distribution)
        param = dist.fit(y_std)

        # Obtain the KS test P statistic, round it to 5 decimal places
        p = scipy.stats.kstest(y_std, distribution, args=param)[1]
        p = np.around(p, 5)
        p_values.append(p)    

        # Get expected counts in percentile bins
        # This is based on a 'cumulative distrubution function' (cdf)
        cdf_fitted = dist.cdf(percentile_cutoffs, *param[:-2], loc=param[-2], 
                              scale=param[-1])
        expected_frequency = []
        for bin in range(len(percentile_bins)-1):
            expected_cdf_area = cdf_fitted[bin+1] - cdf_fitted[bin]
            expected_frequency.append(expected_cdf_area)

        # calculate chi-squared
        expected_frequency = np.array(expected_frequency) * size
        cum_expected_frequency = np.cumsum(expected_frequency)
        ss = sum (((cum_expected_frequency - cum_observed_frequency) ** 2) / cum_observed_frequency)
        chi_square.append(ss)

    # Collate results and sort by goodness of fit (best at top)

    results = pd.DataFrame()
    results['Distribution'] = dist_names
    results['chi_square'] = chi_square
    results['p_value'] = p_values
    results.sort_values(['chi_square'], inplace=True)

    # Report results

    print('\nDistributions sorted by goodness of fit:')
    print('----------------------------------------')
    print(results)
    
    if hist:
        fitted_histogram(y, results)
        
    if pp:
        pp_qq_plots(y, y_std, dist_names)
        
def fitted_histogram(y, results):    
    size = len(y)
    x = np.arange(len(y))


    # Divide the observed data into 100 bins for plotting (this can be changed)
    number_of_bins = 100
    bin_cutoffs = np.linspace(np.percentile(y,0), np.percentile(y,99),number_of_bins)

    # Create the plot
    h = plt.hist(y, bins = bin_cutoffs, color='0.75')

    # Get the top three distributions from the previous phase
    number_distributions_to_plot = 5
    dist_names = results['Distribution'].iloc[0:number_distributions_to_plot]

    # Create an empty list to stroe fitted distribution parameters
    parameters = []

    # Loop through the distributions ot get line fit and paraemters

    for dist_name in dist_names:
        # Set up distribution and store distribution paraemters
        dist = getattr(scipy.stats, dist_name)
        param = dist.fit(y)
        parameters.append(param)

        # Get line for each distribution (and scale to match observed data)
        pdf_fitted = dist.pdf(x, *param[:-2], loc=param[-2], scale=param[-1])
        scale_pdf = np.trapz (h[0], h[1][:-1]) / np.trapz (pdf_fitted, x)
        pdf_fitted *= scale_pdf

        # Add the line to the plot
        plt.plot(pdf_fitted, label=dist_name)

        # Set the plot x axis to contain 99% of the data
        # This can be removed, but sometimes outlier data makes the plot less clear
        plt.xlim(0,np.percentile(y,99))

    # Add legend and display plot

    plt.legend()
    plt.show()

    # Store distribution paraemters in a dataframe (this could also be saved)
    dist_parameters = pd.DataFrame()
    dist_parameters['Distribution'] = (
            results['Distribution'].iloc[0:number_distributions_to_plot])
    dist_parameters['Distribution parameters'] = parameters

    # Print parameter results
    print ('\nDistribution parameters:')
    print ('------------------------')

    for index, row in dist_parameters.iterrows():
        print ('\nDistribution:', row[0])
        print ('Parameters:', row[1] )
        
def pp_qq_plots(y, y_std, dist_names):
    ## qq and pp plots
    data = y_std.copy()
    data.sort()
    size = len(y)
    x = np.arange(len(y))

    x = x.reshape(-1, 1)
    y = y.reshape(-1, 1)

    # Loop through selected distributions (as previously selected)

    for distribution in dist_names:
        # Set up distribution
        dist = getattr(scipy.stats, distribution)
        param = dist.fit(y_std)

        # Get random numbers from distribution
        norm = dist.rvs(*param[0:-2],loc=param[-2], scale=param[-1],size = size)
        norm.sort()

        # Create figure
        fig = plt.figure(figsize=(8,5)) 

        # qq plot
        ax1 = fig.add_subplot(121) # Grid of 2x2, this is suplot 1
        ax1.plot(norm,data,"o")
        min_value = np.floor(min(min(norm),min(data)))
        max_value = np.ceil(max(max(norm),max(data)))
        ax1.plot([min_value,max_value],[min_value,max_value],'r--')
        ax1.set_xlim(min_value,max_value)
        ax1.set_xlabel('Theoretical quantiles')
        ax1.set_ylabel('Observed quantiles')
        title = 'qq plot for ' + distribution +' distribution'
        ax1.set_title(title)

        # pp plot
        ax2 = fig.add_subplot(122)

        # Calculate cumulative distributions
        bins = np.percentile(norm,range(0,101))
        data_counts, bins = np.histogram(data,bins)
        norm_counts, bins = np.histogram(norm,bins)
        cum_data = np.cumsum(data_counts)
        cum_norm = np.cumsum(norm_counts)
        cum_data = cum_data / max(cum_data)
        cum_norm = cum_norm / max(cum_norm)

        # plot
        ax2.plot(cum_norm,cum_data,"o")
        min_value = np.floor(min(min(cum_norm),min(cum_data)))
        max_value = np.ceil(max(max(cum_norm),max(cum_data)))
        ax2.plot([min_value,max_value],[min_value,max_value],'r--')
        ax2.set_xlim(min_value,max_value)
        ax2.set_xlabel('Theoretical cumulative distribution')
        ax2.set_ylabel('Observed cumulative distribution')
        title = 'pp plot for ' + distribution +' distribution'
        ax2.set_title(title)

        # Display plot    
        plt.tight_layout(pad=4)
        plt.show()
```

We can then run the code as follows: [[source]](https://github.com/health-data-science-OR/stochastic_systems/blob/master/labs/simulation/lab3/sim_lab3_autofit_intro.ipynb)

```
from input_modelling.fitting import auto_fit

rng = np.random.default_rng(42)
samples = rng.exponential(scale=32, size=10_000)
samples = pd.DataFrame(samples)
samples.head()

auto_fit(samples)

# Plot the distributions and use a few extra options
dists_to_test = ['expon', 'gamma']
auto_fit(samples, hist=True, pp=True, dist_names=dists_to_test)
```

:::

## Viewing results from the model

I have made limited notes on output analysis, mainly focussing this on how the model is set up. However, you can see more about output analysis from each the HSMA DES book pages (which typically shows the output from all the different variants of model setup, using varying visualisations).