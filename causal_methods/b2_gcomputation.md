# G-computation

## Terminology

Names for this method:
* **G-computation**
* **Parametric G-formula**
* **G-standardisation**
* **Standardisation** [[Vansteelandt and Keiding 2011]](https://doi.org/10.1093/aje/kwq474)
* **Outcome regression** [[source]](http://www.statslab.cam.ac.uk/~qz280/talk/ssrmp-2020/slides.pdf)

There has been some debate around terminology. As quoted from [Vansteelandt and Keiding 2011](https://doi.org/10.1093/aje/kwq474):
> *'The term standardization is revealing and rather well-known to epidemiologists and therefore, in our opinion, is the terminology of choice. The term G-computation has so far been mostly reserved to refer to standardization of the effects of time-varying exposures; potentially the term “G-standardization” as nomenclature for “standardization with respect to generalized exposure regimens” would have been more enlightening. Despite the essential equivalence of G-computation for point exposures and standardization with the total population as the reference, we believe that the developments from the causal inference literature add to the literature on standardization. They give a precise meaning to standardized effect measures in terms of counterfactuals, provide insight into the delicate differences between conditional and marginal epidemiologic effect measures, and suggest novel standardization techniques that combine precision with robustness against model misspecification and extrapolation.'*

## About the method

G-computation involves using a statistical model (e.g. predict) to predict **potential** outcomes (counterfactuals - with and without exposure).[[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267) 

````{mermaid}
  flowchart LR;

    X("Binary treatment (X)"):::white;
    Y("Outcome (Y)"):::white;
    W("Confounder (W)"):::white;

    X --> Y;
    W --> X;
    W --> Y;
  
    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
    classDef empty width:0px,height:0px;
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

Key steps:
1. **Fit model on observed data** - regression model with Y as outcome and X and W as predictors (perhaps also with polynomials and/or interactions if there are multiple control variables)
2. Make identical copy of observed data, but just **replace** outcome so all X=1.
3. Create another where all to X=0.
4. Use our fitted model to **predict outcomes** in the two counterfactual datasets [[source]](https://marginaleffects.com/vignettes/gcomputation.html) [[Batten 2023]](https://causallycurious.com/posts/standardization/standardization) [[source]](http://www.statslab.cam.ac.uk/~qz280/talk/ssrmp-2020/slides.pdf)
5. Estimate the **Average treatment effect (ATE)** - this is the mean difference (+ 95% CI) in the predicted outcomes between the two groups.[[Batten 2023]](https://causallycurious.com/posts/standardization/standardization)  It essentially describes the average effect, at a population level, of moving an entire population from untreated to treated.[[Chatton et al. 2020]](https://doi.org/10.1038/s41598-020-65917-x)

For **average treatment effect on the treated (ATT)**:
* This is the average effect of treatment on those subjects who ultimately received the treatement [[Chatton et al. 2020]](https://doi.org/10.1038/s41598-020-65917-x)
* To calculate ATT, use **only the treated units in steps 2 and 3**. 'The control units are still used to fit the model in 1, but only the treated units are used to compute the predicted values.' [[source]](https://stats.stackexchange.com/questions/613569/estimating-and-interpreting-the-att-with-regression-adjustment-and-marginal-effe)

You could also compute **average treatment effect on the untreated (ATU).** [[Wang et al. 2017]](https://doi.org/10.1186/s12874-016-0282-4)

To get standard errors, you can use bootstrapping or the delta method. [[source]](https://stats.stackexchange.com/questions/613569/estimating-and-interpreting-the-att-with-regression-adjustment-and-marginal-effe)

## How does this method enable us to deal with treatment-dependent confounding?

See the example of treatment-dependent confounding below.

````{mermaid}
  flowchart LR;

    ak("A<sub>K</sub>: Treatment"):::green;
    ak1("A<sub>K+1</sub>: Treatment"):::green;
    yk1("Y<sub>K+1</sub>: Outcome"):::green;
    yk2("Y<sub>K+2</sub>: Outcome"):::green;
    lk("L<sub>K</sub>: Confounder"):::white;
    lk1("L<sub>K+1</sub>: Confounder"):::white;
    u("U: Unmeasured<br>confounder"):::white;

    ak --> yk1;
    u --> yk1;
    u --> lk;
    lk --> ak;
    lk --> ak1;
    ak --> ak1;
    ak --> lk1;
    u --> lk1;
    lk1 --> ak1;
    ak1 --> yk2;
    u --> yk2;
    lk --> yk1;
    lk --> lk1;
    lk1 --> yk2;
    yk1 --> yk2;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

If we regressed A<sub>K</sub> and A<sub>K+1</sub> on Y<sub>K+2</sub> while adjusting for confounders should we adjust for the time-varying L<sub>K+1</sub> and Y<sub>K+1</sub>? We can see that:
1. **L<sub>K+1</sub> is a collider** on the non-causal path A<sub>K</sub> --> L<sub>K+1</sub> <-- U --> Y<sub>K+2</sub>

````{mermaid}
  flowchart LR;

    ak("A<sub>K</sub>: Treatment"):::red;
    ak1("A<sub>K+1</sub>: Treatment"):::white;
    yk1("Y<sub>K+1</sub>: Outcome"):::white;
    yk2("Y<sub>K+2</sub>: Outcome"):::red;
    lk("L<sub>K</sub>: Confounder"):::white;
    lk1("L<sub>K+1</sub>: Confounder"):::red;
    u("U: Unmeasured<br>confounder"):::red;

    ak --> yk1;
    u --> yk1;
    u --> lk;
    lk --> ak;
    lk --> ak1;
    ak --> ak1;
    ak --> lk1;
    u --> lk1;
    lk1 --> ak1;
    ak1 --> yk2;
    u --> yk2;
    lk --> yk1;
    lk --> lk1;
    lk1 --> yk2;
    yk1 --> yk2;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
    classDef red fill:#FFCCCB, stroke:red
    classDef green fill:#DDF2D1, stroke: #FFFFFF
    linkStyle 6,7,10 stroke:red;
````

2. **L<sub>K+1</sub> is a mediator** on the causal path A<sub>K</sub> --> L<sub>K+1</sub> --> A<sub>K+1</sub> --> Y<sub>K+2</sub>

````{mermaid}
  flowchart LR;

    ak("A<sub>K</sub>: Treatment"):::red;
    ak1("A<sub>K+1</sub>: Treatment"):::red;
    yk1("Y<sub>K+1</sub>: Outcome"):::white;
    yk2("Y<sub>K+2</sub>: Outcome"):::red;
    lk("L<sub>K</sub>: Confounder"):::white;
    lk1("L<sub>K+1</sub>: Confounder"):::red;
    u("U: Unmeasured<br>confounder"):::white;

    ak --> yk1;
    u --> yk1;
    u --> lk;
    lk --> ak;
    lk --> ak1;
    ak --> ak1;
    ak --> lk1;
    u --> lk1;
    lk1 --> ak1;
    ak1 --> yk2;
    u --> yk2;
    lk --> yk1;
    lk --> lk1;
    lk1 --> yk2;
    yk1 --> yk2;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
    classDef red fill:#FFCCCB, stroke:red
    classDef green fill:#DDF2D1, stroke: #FFFFFF
    linkStyle 6,8,9 stroke:red;
````

3. **L<sub>K+1</sub> is a confounder** on the non-causal path A<sub>K+1</sub> <-- L<sub>K+1</sub> --> Y<sub>K+2</sub>

````{mermaid}
  flowchart LR;

    ak("A<sub>K</sub>: Treatment"):::white;
    ak1("A<sub>K+1</sub>: Treatment"):::red;
    yk1("Y<sub>K+1</sub>: Outcome"):::white;
    yk2("Y<sub>K+2</sub>: Outcome"):::red;
    lk("L<sub>K</sub>: Confounder"):::white;
    lk1("L<sub>K+1</sub>: Confounder"):::red;
    u("U: Unmeasured<br>confounder"):::white;

    ak --> yk1;
    u --> yk1;
    u --> lk;
    lk --> ak;
    lk --> ak1;
    ak --> ak1;
    ak --> lk1;
    u --> lk1;
    lk1 --> ak1;
    ak1 --> yk2;
    u --> yk2;
    lk --> yk1;
    lk --> lk1;
    lk1 --> yk2;
    yk1 --> yk2;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
    classDef red fill:#FFCCCB, stroke:red
    classDef green fill:#DDF2D1, stroke: #FFFFFF
    linkStyle 8,9,13 stroke:red;
````

If we adjusted for for L<sub>K+1</sub> we would therefore:
* Eliminate confounding bias
* Introduce collider (stratification) bias
* Introduce over-adjustment bias in the effect of A<sub>K</sub> (from controlling for mediator)

The same argument applies when adjusting for the intermediate outcome Y<sub>K+1</sub>. In other words, its **impossible** as we need to simultaneously adjust for and not adjust for L<sub>K+1</sub> and Y<sub>K+1</sub>. 
'The **g-formula** resolves this problem by decoupling adjusting, and not adjusting, for treatment-dependent confounders' like L<sub>K+1</sub>.

1. **G-formula step 1** involves fitting a model with outcome, treatment and confounders. This adjusts for L<sub>K+1</sub> and Y<sub>K+1</sub>, to **avoid confounding bias**.

2. **G-formula step 2** involves predicting outcomes where all patients are set to no treatment, or all to treatment, and comparing the outcomes to get the average treatment effect. This marginalises/averages over the counterfactual distribution of L<sub>K+1</sub> and Y<sub>K+1</sub>, so they are **not adjusted for**, to avoid collider and over-adjustment biases

Hence, it simultaneously does and not adjust for L<sub>K+1</sub> and Y<sub>K+1</sub>. [[Loh et al. 2023]](https://doi.org/10.31234/osf.io/m37uc)

## Assumptions

* Sequential ignorability assumption i.e. **no unmeasured confounding** - 'when there is no causal effect, the treatment and outcome are conditionally independent given a set of pre-treatment covariates' [[Loh et al. 2023]](https://doi.org/10.31234/osf.io/m37uc)

## G-computation v.s. IPTW

'Standardization models the outcome, whereas inverse probability weighting models the treatment'.  If we were to do IPW and standardisation '**without using any models** (i.e. non-parametrically) then we would expect both methods to give the exact same result'. [[Batten 2023]](https://causallycurious.com/posts/standardization/standardization)

However, we expect them to differ if we use **models** to estimate them since some degree of misspecification is inescapable in models, 'but misspecification in the treatment model (IP weighting) and outcome model (standardisation) will not generally result in the same magnitude and direction of bias in the effect estimate'.

'Both IP weighting and standardization are estimators of the **g-formula**, a general method for causal inference first described in 1986... We say that standardization is a **plug-in g-formula** estimator because it simply replaces the conditional mean outcome in the g-formula by its estimates. When those estimates come from parametric models, we refer to the method as the **parametric g-formula**. Because here we were only interested in the average causal effect, we estimated parametrically the conditional mean outcome.'

'Often there is no need to choose between IP weighting and the parametric g-formula. When both methods can be used to estimate a causal effect, **just use both methods**. Also, whenever possible, use **doubly robust methods** that combine models for treatment and for outcome in the same estimator'. [[Hernán and Robins 2024]](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)