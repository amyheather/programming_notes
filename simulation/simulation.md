```{toctree}
:hidden: True

self
discrete_event
```

# Simulation

You can think of there as being three models for healthcare systems:
1. **Analytical queueing models (i.e. mathematical models)** - easy and fast inference for simple models, model require minimal data, maths can become complex… may be too simplified, or intractable (hard to control or direct)
2. **Computer simulation** - very flexible, doesn’t have limits of analytical models, easier for healthcare clients to understand theoretically, can be easy to include too much detail, and complex models require lots of data and have complex output
3. **Real experimentation on healthcare systems** - high risk, may be unethical, expensive, will be lots of other interventions happening at once [TomL7]

This section focusses on simulation...

## Simulation

"A simulation imitates the operation of real world processes or systems with the use of models. The model represents the key behaviours and characteristics of the selected process or system while the simulation represents how the model evolves under different conditions over time." [[source]](https://www.twi-global.com/technical-knowledge/faqs/faq-what-is-simulation)

### Characteristics of a simulation

#### Stochastic or deterministic
* **Stochastic** - use random variables as inputs. Also known as probablistic models. Incorporate randomness/information about uncertainty. [[source]](https://www.preventionweb.net/understanding-disaster-risk/key-concepts/deterministic-probabilistic-risk)
* **Deterministic** - model behaviour is completely predictable from inputs

#### Static or dynamic
* **Static** - represents one point in time [[source]](https://bookdown.org/manuele_leonelli/SimBook/types-of-simulations.html) (e.g. calculating stress on a bridge) [[source]](http://www.edscave.com/static-vs.-dynamic-models)
* **Dynamic** - represents changes in system over time 

#### Discrete or continuous
* **Discrete** - variables change at discrete points in time (e.g. customer arrivals)
* **Continuous** - variables continuously change over time (e.g. speed of car) [[source]](https://bookdown.org/manuele_leonelli/SimBook/types-of-simulations.html)

## Types of simulation models

**Monte Carlo** - 'use random sampling techniques to model uncertainty and vaiability in a system' - often 'to estimate the probability of different outcomes in situations with many uncertain variables' [[source]](https://www.quora.com/What-is-the-difference-between-Monte-Carlo-and-discrete-event-simulation)
* Stochastic [[source]](https://softwaresim.com/blog/types-of-simulation-models-choosing-the-right-approach-for-your-simulation-project/)
* Static [[source]](https://bookdown.org/manuele_leonelli/SimBook/types-of-simulations.html)

**Agent-based modelling**

**Discrete event simulation** - models 'behaviour of a system as a sequence of events in time' [[source]](https://www.quora.com/What-is-the-difference-between-Monte-Carlo-and-discrete-event-simulation)
* Stochastic
* Dynamic
* Discrete

**System dynamic modelling**

## Advice on modelling care pathways

Advice:
1. Clarify modelling objectives and **what the clinical team wants to achieve**
2. Identify the **patient populations** to model
3. Use the initial meeting to sketch out an overview of the **pathway** (e.g. how does patient arrive to patient, what resources, what order do they see, etc. etc.)
4. Spend some time **observing** how the operations of the pathway are managed (and they likely operate differently to how you have been told!)
5. Meet with the **data controller** for the pathway [TomL7]

Typical data requirements:
* **Demand** - e.g. referrals to an outpatient clinic, ambulance callouts, pharmacy orders. Useful to have a continuous (time series) sample over a sustained period
* **Process times** - e.g. medical assessments, operation durations, workforce travel times. A sample of data is usually sufficient, but may not be available (in that case, may be able to set up short term data collection (limitations) or make some assumptions about the distribution we will sample from)
* **Resource** - e.g. number of staff on shirt, inventory (blood, medical supplies, PPE, beds). These may be specialist or shared Patient routing
* **Trajectories of patients** - Often complication… pathways may straddle multiple serivices or have different routes for classes of patients. e.g. 80% of patients who have been to ICU may need step-down high dependency care whilst 20% don’t
* **Queueing rules** e.g. prioritisation of more severe cases
* **Disease progression**. In some disease areas, patients may be undergoing treatment while their disease state is progressin, e.g. diabetic retinopathy… care pathway where check at right time to identify it early and successfully treat [TomL7]