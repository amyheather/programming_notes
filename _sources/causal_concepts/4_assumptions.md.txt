# Assumptions

`````{admonition} Executive summary
:class: info

Causal assumptions:
* **Exchangeability** = groups are equivalent (as randomised / no confounders)
* Stable Unit Treatment Value Assumption (SUTVA), which combines
    * **Non-interference** = treatment of one group cannot influence outcome of another (eg. violated for vaccinations)
    * **Consistency** = no hidden versions of treatment (eg. no undefined dose variation)
* **Positivity** = no factors deterministic of treatment (eg. violated if treatment never prescribed with particular contraindication)
* **Ignorability** = among people with same characteristics, can think of treatment as being randomly assigned

`````

'Causal effects are impossible to measure directly, since they involve comparing unobserved counterfactual outcomes that would have happened under different circumstances. A causal effect is identifiable if it can be **estimated** using observable data, given certain **assumptions** about the data and the underlying causal relationships. Such identifying assumptions typically cannot be fully tested statistically but have to be justified based on theory and/or existing evidence about the real-world processes under study'.[[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

These assumptions include:
* Exchangeability assumption
* Stable Unit Treatment Value Assumption (SUTVA), which combines
    * Non-interference assumption
    * Consistency assumption
* Positivity assumption
* Ignorability assumption

## Exchangeability assumption

'The **exchangeability** (or "no confounding") assumption requires that individuals who were exposed and unexposed have the same potential outcomes on average.'[[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267) In other words, whatever treatment group each person was randomised too, we still would've seen the same outcomes in whichever were treated v.s. not, the groups are exchangeable, as no confounders are present.[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

This allows the observed outcomes in an unexposed group to be used as a proxy for the counterfactual (unobservable) outcomes in an exposed group. RCTs strive to achieve exchangeability by randomly assigning the exposure, while observational studies often rely on achieving **conditional exchangeability** (or ‘no unmeasured confounding’), which means that exchangeability holds after conditioning on some set of variables'. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

## Stable Unit Treatment Value Assumption (SUTVA)

**SUTVA** is composed of two assumptions.

**(1) No interference between units** (or "**non-interference assumption**"). This assumption requires that an individuals potential outcomes do 'not depend on the exposure status of anyone else. This assumption can be violated by ‘spillover effects’ of some exposures (eg, **vaccination**), where an individual’s outcomes are affected by the exposure status of those around them. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

**(2) There is only one version of treatment** (or "**consistency assumption**").  This is also referred to as "no multiple versions of treatment" or "no hidden treatments". This means that you do not have a scenario where each treatment condition has more than one version, and thus each unit may have more than one potential outcome per treatment condition. Hence, to satisfy, you need to:
* Define each version as treatment, or
* Restrict treatments to a subset of versions, or
* Randomise versions and take average across versions, or
* Redefine causal effect, acknowledgeing that estimated effect is conditional on an unknown distribution of versions. [[Kimmell et al. 2021]](https://doi.org/10.1016/j.tree.2021.08.008)

In practice, it can be impossible to achieve perfect consistency, and so the focus is instead on whether these differences are small enough for the averaged estimate to be meaningful.[[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

## Positivity assumption

**Positivity** means that, **for every set of values for X, treatment assignment was not deterministic**. If, for some values of X, treatment was deterministic, then **we would have no observed values of Y** for one of the treatment groups for those values of X. [[Coursera]](https://www.coursera.org/learn/crash-course-in-causality/lecture/f5LPB/causal-assumptions)

'When conditioning on other variables, positivity needs to hold for each combination of covariates. This means that for every combination of covariates, it is possible to be either exposed or unexposed. The combination of covariates where this assumption holds can be called the ‘**region of common support**’.'

Violations can be either:
* **Structural positivity violation** - if some combinations are impossible (eg, if a treatment is never prescribed when a particular contraindication is present)
* **Random positivity violation** - if combination is possible but is missing from the study sample by chance. The term ‘positivity’ may refer to both of these or only to structural positivity; the latter is usually more relevant in theoretical causal inference literature.' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

## Ignorability assumption

**Ignorability** means that, given pre-treatment covariates X, treatment assignment is independent from the potential outcomes - i.e. **among people with the same values of X, we can think of treatment A being randomly assigned**. This is sometimes referred to as the 'no unmeasured confounders' assumption.

Example: Older people more likely to have treatment, and more likely to have outcome (hip fracture), so treatment assignment is not marginally independent from outcome - BUT within levels of age, treatment might be randomly assigned. [[Coursera]](https://www.coursera.org/learn/crash-course-in-causality/lecture/f5LPB/causal-assumptions)
