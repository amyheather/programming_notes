# Multivariable regression

*Also referred to as covariate adjustment*

The conventional multivariable regression approach - where **confounders are included as covariates** - can be used to estimate causal effects, and can be referred to as "selection on observables". This requires you meet certain *assumptions* however - namely, "*Do we have data on the minimum number of variables needed to **satisfy the backdoor path criterion**?*". [[source]](https://vivdas.medium.com/regression-and-causal-inference-which-variables-should-be-added-to-the-model-fd95a759f78) This is described in [this section of this book](../causal_concepts/3_dags.md), but to recap, we want to identify a **minimal set of covariates** that:
1. Block all backdoor paths - so would want to block the open back door path that is in the image on the left
2. Do not inadvertenly open closed pathways by conditioning on colliders or descendents - as is the case in the image on the right (not conditoning on the collider, so the path remains blocked - but if you did, it would open it)

````{mermaid}
  flowchart TD;

    block:::outline;
    subgraph block["`**Path blocked at collider**`"]
      a("Treatment"):::green;
      y("Outcome"):::green;
      x("Collider"):::white;
    end

    a --> y;
    a --> x;
    y --> x;

    open:::outline;
    subgraph open["`**Path open at confounder**`"]
      a2("Treatment"):::green;
      y2("Outcome"):::green;
      x2("Confounder"):::white;
    end

    a2 --> y2;
    x2 --> a2;
    x2 --> y2;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
    classDef outline fill:#FFFFFF
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

Alike the methods above, we assume **conditional exchangeability given measured convariates** - i.e. only addresses confounding caused by measured covaries and can be biases by unmeasured covariates.[[Shiba and Kawahara 2021]](https://doi.org/10.2188/jea.JE20210145)

Shiba and Kawahara 2021 explain the benefits, however, of propensity score methods (propensity score matching, inverse probability weighting) over multivariable regression:
* Modeling decisions for propensity score methods typically come before looking at data (hence minimises p-hacking and tweaking of spec to align with expectations)
* 'Potential positivity violations tend to become more visible in the propensity score methods as extreme propensity score values can signal covariate pattenrs in which only the exposed or the unexposed are present'
* For rare outcomes, conditioning on lots of covariates in a regression can produce imprecise estimates - whereas propensity score methods convert lots of covariates into a single value
* Modelling assumptions (don't fully understand... it's around misspecification, knowledge of relationships with exposure or outcome, doubly-robust methods, conditional and marginal effect estimates)
* Inverse probability weighting can be expanded to account for time-varying confounding [[Shiba and Kawahara 2021]](https://doi.org/10.2188/jea.JE20210145)

Confounders can be included as **individual covariaties**, or by just including the estimated **propensity score as a covariate** in the regression model. Propensity score:
* Can be attractive as it allows the incorporation of many covariates
* Should be used with caution, as 'bias may increase when the variance in the treated and untreated groups are very different (actually, the untreated group variance is much larger than the treated groups variance).' [[Valojerdi et al. 2018]](https://doi.org/10.14196%2Fmjiri.32.122)

In the context of an intervention effect (i.e. the treatment paradox), [Schuit et al. 2013](https://doi.org/10.1503/cmaj.120812) recommend **inclusion of the intervention in the predictor model** as a solution - as we do for multivariable regression. They note that 'if an intervention is equally effective in all patients, modelling the intervention effect doesn’t require an interaction between predictor and intervention in the model. If the intervention is more effective in, for example, those having the predictor, then an interaction between intervention and predictor is required'.[[Schuit et al. 2013]](https://doi.org/10.1503/cmaj.120812)

## All possible confounders

'Many analysts take the strategy of putting in **all possible confounders**. This can be bad news, because adjusting for **colliders and mediators can introduce bias**, as we’ll discuss shortly. Instead, we’ll look at **minimally sufficient adjustment sets**: sets of covariates that, when adjusted for, block all back-door paths, but include no more or no less than necessary. That means there can be many minimally sufficient sets, and if you remove even one variable from a given set, a back-door path will open.'[[source]](https://cran.r-project.org/web/packages/ggdag/vignettes/intro-to-dags.html)

[Schisterman et al. 2009](https://doi.org/10.1097/EDE.0b013e3181a819a1) 'define **unnecessary adjustment** as control for a variable that does not affect bias of the causal relation between exposure and outcome but may affect its precision.' - so:
* Adjusting for a variable completely outside the system of interest (C1)
* Adjusting for a variable that causes the exposure only (C2)
* Adjusting for a variable whose only causal association with variables of interest is as a descendent of the exposure and not in the causal pathway (C3)
* Adjusting for a variable whose only causal association with variables of interest is as a cause of the outcome (C4)

Adjusting for these varaibles should not impact the total causal effect on the outcome, but may be gain or loss in precision of relationship between exposure of interest, the unnecessary adjustment variables, and the outcome of interest.[[Schisterman et al. 2009]](https://doi.org/10.1097/EDE.0b013e3181a819a1)

````{mermaid}
  flowchart LR;

    C1:::white
    C2:::white
    C3:::white
    C4:::white
    E(Exposure):::white
    D(Outcome):::white

    C2 --> E;
    E --> C3;
    E --> D;
    C4 --> D;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
````

## Data-driven selection of confounders

'Though generally not advisable, data-driven confounder selection may be employed in small datasets, under the condition that the data has been pre-processed to entail that covariates fed into the statistical selection method are only potential confounders and free of mediators'.[[Ramspek et al. 2021 (supplementary)]](https://doi.org/10.1007/s10654-021-00794-w)