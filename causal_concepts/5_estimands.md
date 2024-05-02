# Causal estimands

`````{admonition} Executive summary
:class: info

Possible causal effect measures:
* Causal mean difference
* Causal mean ratio
* Causal risk difference
* Causal risk ratio

Possible causal effects - i.e. causal estimand - choice of which can be guided by thinking of target trial you are trying to emulate:
* Average treatment effect (ATE)
* Average treatment effect in the treated (ATT)
* Average treatment effect in the untreated (ATU/ATUT)
* Intention-to-treat effect (ITT)
* Complier average causal effect (CACE) or local average treatment effect

`````

## Average causal effect
In causal inference studies, you are estimating the **average causal effect** of the treatment/exposure when comparing between groups of individuals. This is because it is generally impossible to estimate the causal effect for an individual, as you can't go back in time and not give them an outcome.[[source]](https://hummedia.manchester.ac.uk/institutes/methods-manchester/docs/CausalInference.pdf)

The terminology used varies, with [Lederer et al. 2018](https://doi.org/10.1513/AnnalsATS.201808-564PS) suggesting that we refer to finding **causal associations** and **effect estimates** - but not **actual** causal effects, or saying that the "exposure has an 'effect' or 'impact' on outcome", or that the "exposure 'protects against' or 'promotes' outcome". They suggest these are avoided without substantial evidence of a true causal effect.[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS)

## Causal effect estimands

### Choosing a causal estimand

Before you estimate the causal effect, you have to choose which effect you are trying to estimate (i.e. **the causal estimand**).[[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267) Things to consider...

**Target population** - different methods 'allow you to estimate effects that can generalise to different target populations' (e.g. difference between the various causal treatment effects below)

Whether effect is **marginal or conditional**
* **Marginal** - 
    * Relevant to whole population
    * Involves comparing potential outcome under treatment to potential outcome under control (as in randomised trials)
    * Useful for finding overall effect
* **Conditional**
    * Specific to certain population
    * Involves comparing potential outcomes within strata
    * Useful for finding treatment effect in particular subset of population

The **outcome type** (continuous, binary, or time-to-event).

Whether the effect measure is **non-collapsible or collapsible**.[[Greifer 2023]](https://cran.r-project.org/web/packages/MatchIt/vignettes/estimating-effects.html)
* **Non-collapsible**
    * This is when the conditional effect measure differs from the marginal effect measure even in the absence of confounding. This is true for certain non-linear effect measures like the odds ratio.
    * It means that conditional measures are more **difficult to compare** between studies (since different studies typically adjust for different sets of covariates), and that marginal effects may be **less transportable** between populations[[Vansteelandt and Keiding 2011]](https://doi.org/10.1093/aje/kwq474)
    * In these cases, it is very important to distinguish between marginal and conditional effects, as different methods target different types of effect
* **Collapsible**
    * Same methods can be used to estimate marginal and conditional effects [[Greifer 2023]](https://cran.r-project.org/web/packages/MatchIt/vignettes/estimating-effects.html)

It can be challenging to identify the appropriate causal estimand. However, specifying a **target trial** (i.e. hypothetical RCT you are trying to emulate), can help with figuring this out. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

### Effect measures

| Effect measure | Outcome type | Collapsiblility | Example |
| --- | --- | --- | --- |
| Mean difference | Continuous | Collapsible | 'An average increase in systolic blood pressure by 10 mmHg' |
| Risk difference (RD) | Binary | Collapsible | 'An average increase in the risk of stroke by 5%' |
| Risk ratio (RR) | Binary | Non-collapsible | 'An average increase in the risk of stroke by a factor of 1.5' |
| Odds ratio (OR) | Binary | Non-collapsible | - |
| Hazard ratio (HR) | Time-to-event (i.e. survival) | Non-collapsible [[Greifer 2023]](https://cran.r-project.org/web/packages/MatchIt/vignettes/estimating-effects.html) | - [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267) |

### Treatment effects

| Causal treatment effect | Definition |
| --- | --- |
| **Average treatment effect (ATE)** | Difference between average outcome, when EVERYONE is exposed v.s. when NO-ONE is exposed |
| **Average treatment effect in the treated (ATT)** | ATE calculated only in sub-population of individuals who were actually exposed |
| **Average treatment effect in the untreated (ATU/ATUT)** | ATE calculated only in sub-population of individuals who were actually unexposed |
| **Intention-to-treat effect (ITT)** | Average effect of being assigned to (but not necessarilly receiving) the exposure |
| **Complier average causal effect (CACE) or local average treatment effect** | ATE calculated only among 'compliers' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267) |


## More on: Intention-to-treat

**Intention-to-treat analysis** is the preferred analysis strategy for RCTs. This means that the analysis includes all participants, all retained in the group to which they were allocated.

However, this can be hard to achieve due to:
1. **Missing outcomes**
    * A "complete case" (or "available case") analysis only includes participants with no missing outcomes, and whilst only a few missing outcomes won't cause a problem, in half of trials more than 10% of randomised patients may have missing outcomes. Hence, exclusion will reduce the sample size, and may introduce bias if loss to follow-up is related to a patient's response to treatment.
    * Participants with missing outcomes can be included if their outcomes are imputed - but this requires strong assumptions. Common example is to use "last observation carried forward", but this may introduce bias and makes no allowance for uncertainty imputation.
2. **Non-adherence to protocol**
    * Examples include participants who didn't meet inclusion criteria (e.g. wrong diagnosis, too young), did not take all of the intended treatment, received a different treatment, or received no treatment
    * Intention-to-treat analysis ignores protocol deviations, including participants in their assigned groups regardless. Modified intention-to-treat (or 'per protocol analysis') is an analysis that excludes participants who didn't adequately adhere (e.g. minimum amount of intervention) - but this would need to be labelled as a non-randomised, observational comparison, and be aware that the exclusion of patients compromises randomisation.[[CONSORT]](https://www.bmj.com/content/340/bmj.c869)

These two problems can introduce **non-random selection effects** - i.e. randomisation isn't the only cause for treatment - hence introducing confounding (bias), and meaning that exchangeability would no longer holder - and hence why intention-to-treat is recommended (i.e. ignore protocol deviations).

The **Complier-Average Causal Effect (CACE) estimate** is the comparison of the average outcome of the compliers in the treatment arm compared with the average outcome of the comparable group of would-be compliers in the control arm. It is the intention-to-treat effect in the sub-group of participants who would always have complied with their treatment allocation, and is not subject to confounding.[[source]](https://hummedia.manchester.ac.uk/institutes/methods-manchester/docs/CausalInference.pdf)