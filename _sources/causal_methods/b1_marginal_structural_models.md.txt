# Marginal structural models (MSM)

Alternative names (often depending on method used to estimate weights):
* **Inverse probability-weighted marginal structural models** [[Naimi et a. 2017]](https://doi.org/10.1093%2Fije%2Fdyw323)
* **IPTW-based marginal structural models** [[Williamson and Ravani 2017]](https://doi.org/10.1093/ndt/gfw341)
* **Inverse probability of treatment weighting with time-varying covariates** [[Chesnaye et al. 2022]](https://doi.org/10.1093%2Fckj%2Fsfab158)
* **Marginal structural Cox proportional hazards model** (if you were using a Cox model) [[Xie et al. 2017]](https://doi.org/10.2215/CJN.00650117)

In marginal structural models, each observation is weighted, with weights most commonly estimated using IPTW.[[Williamson and Ravani 2017]](https://doi.org/10.1093/ndt/gfw341)

'Results of marginal structural models have similar interpretation as clinical trials (i.e. a marginal or population-level interpretation). Marginal structural models estimate what would happen if a person always received a certain treatment versus never, which is an idealized situation that does not reflect clinical practice, unless it is interpreted as an ‘intention to continue treatment’ similar to the ‘intention to treat’ interpretation of randomized controlled trials. Other methods that address time-varying confounding affected by previous treatment allow different types of inference based on a conditional, as opposed to marginal interpretation. For example, the sequential Cox approach estimates the effect of starting a treatment versus never, and ignoring previous treatment.' [[Williamson and Ravani 2017]](https://doi.org/10.1093/ndt/gfw341)

## Method

### Step 1. Weight observations using IPTW

* Inverse probability of treatment weighting (IPTW) can be used to 'estimate the parameters of a marginal structural model.'

* 'Unlike the procedure followed for baseline confounders, which calculates a single weight to account for baseline characteristics, a separate weight is calculated for each measurement at each time point individually. To achieve this, the **weights are calculated at each time point as the inverse probability of being exposed, given the previous exposure status, the previous values of the time-dependent confounder and the baseline confounders**. This creates a pseudopopulation in which covariate balance between groups is achieved over time and ensures that the exposure status is no longer affected by previous exposure nor confounders.' 

* Extreme weights can be dealt with as described for IPTW with baseline covariates, but for weight stablisation, the numerator would be probability of being exposed given previous exposure status and baseline confounders. 'Although including baseline confounders in the numerator may help stabilize the weights, they are not necessarily required. If the choice is made to include baseline confounders in the numerator, they should also be included in the outcome model'. [[Chesnaye et al. 2022]](https://doi.org/10.1093%2Fckj%2Fsfab158)

* **Censoring weights** can also be estimated and included.

* Create the pseudo-population with confounding removed by multiplying each observation by its individual weights. [[Williamson and Ravani 2017]](https://doi.org/10.1093/ndt/gfw341)

### Step 2. Use weights in model to estimate treatment-outcome association

* The re-weighted sample can then be used to estimate the treatment-outcome relationship. This type of weighted model where time-dependent confounding is controlled for is referred to as a **marginal structural model**.

* They are simple to implement. For example, 'a marginal structural Cox regression model is simply a Cox model using the weights as calculated in the procedure described above'[[Chesnaye et al. 2022]](https://doi.org/10.1093%2Fckj%2Fsfab158)

* Weighting each observation makes the exposed and unexposed groups groups exchangeable in terms of confounders, with the distribution of confounders similar in both groups. 'An ATE can then be calculated by a simple comparison or unadjusted regression model.' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

* 'Validity of marginal structural models is assessed with several sensitivity analyses. The distributions of treatment weights, censoring weights and final weights are usually assessed graphically. If extreme values are identified sensitivity analyses are conducted by comparing results of outcome analyses including and excluding outliers (see limitations section and alternative approaches). Often, however, marginal structural models require fitting several different variations of each of the weight-generating models to achieve optimal weight distributions.' [[Williamson and Ravani 2017]](https://doi.org/10.1093/ndt/gfw341)

## Strengths and limitations

Strengths:
* 'Don't suffer from collider stratification bias because weighting, as opposed to conditioning, is used to control for time-varying confounders affected by previous treatment' [[Williamson and Ravani 2017]](https://doi.org/10.1093/ndt/gfw341)

Limitations:
* As all causal models, MSMs can only balance on known factors, and the exchangeability assumption is not verifiable
* 'Number of balancing variables may be limited by sample size - unusual (or very common) covariates histories may result in failture to achieve stability of estimated weights' - hence the importance of sensitivity analyses - often through trimming or inc/excluding observations with extreme values
* 'IPTW-based marginal structural models need to include all covariates in the weight estimation. Interaction effect can be estimated for baseline modifiers but not for time-varying modifiers in standard marginal structural models (although history-adjusted marginal structural models have been formulated)' [[Williamson and Ravani 2017]](https://doi.org/10.1093/ndt/gfw341)
