# Matching

**Matching** involves selecting a sample where exposed and unexposed groups have the same distribution of confounders.[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home) We often start with the group with fewer individuals, and then use the other group to find matches. It does not have to be **one-to-one (matching pairs)** - it can be **one-to-many (matching sets)**. Matching is often based on a combination of confounders. [[Hernán and Robins 2024]](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)

Matching can't be represented in DAG, because **non-faithfulness** - the association to a backdoor path is exactly cancelled by the matched subset.[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

We make an assumption of conditional exchangeability given L (the confounder), meaning that matching results in '(unconditional) **exchangeability** of the treated and untreated in the matched population', and so we **directly compare** their outcomes. Matching ensures **positivity** since strata with only treated or untreated individuals are excluded. [[Hernán and Robins 2024]](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)

## Matching methods

Above describes **individual matching**, but you can also use **frequency matching**. For example, randomly selected individuals but ensuring 70% have L=1 (certain value of confounder), and then repeating for the other population. [[Hernán and Robins 2024]](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)

There are a few approaches to matching, which include:
* **Propensity score matching** - matched based on propensity scores
    * This is commonly one-to-one matching based on similar values of the propensity score, which can be done with or without replacement, but **with replacement can decrease** bias and is helpful where the numbers of controls are limited. [[Valojerdi et al. 2018]](https://doi.org/10.14196%2Fmjiri.32.122)
    * Selecting the propensity score 'close' to the treated subject is done using either **nearest neighbour matching** or nearest neighbour matching within a specific caliper distance.
    * You can choose between **greed matching** or **optimal matching**
    * Outcomes...
        * 'If the outcome is continuous (e.g., a depression scale), the effect of treatment can be estimated as the difference between the mean outcome for treated subjects and the mean outcome for untreated subjects in the matched sample'
        * 'If the outcome is dichotomous (self-report of the presence or absence of depression), the effect of treatment can be estimated as the difference between the proportion of subjects experiencing the event in each of the two groups (treated vs. untreated) in the matched sample. With binary outcomes, the effect of treatment can also be described using the relative risk or the NNT.'
        * 'Once the effect of treatment has been estimated in the propensity score matched sample, the variance of the estimated treatment effect and its statistical significance can be estimated.' [[Austin 2011]](https://doi.org/10.1080%2F00273171.2011.568786)
* **Matched difference-in-differences** - perform matching then compute difference-in-differences - this controls for unobserved, time-invariant characteristics between the groups
* **Synthetic control method** - weight one group in a manner to it closely resembles the other group
Above, we are describing the **synthetic control method**. [[source]](https://dimewiki.worldbank.org/Matching)

## Limitations

* Requires extensive datasets to properly match, with detailed information on baseline characteristics, but this is not always available
* Assumes there are no unobserved characteristics between the matched groups. Possible solution: Matched difference-in-differences. [[source]](https://dimewiki.worldbank.org/Matching)
* Computes **conditional** effect measures (not average effect measures) - i.e. only for certain subset of population [[Hernán and Robins 2024]](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)