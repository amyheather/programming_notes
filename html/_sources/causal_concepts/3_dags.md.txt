# Directed acyclic graphs

`````{admonition} Executive summary
:class: info

In a DAG, you can identify:
* **Confounders** - common cause both treatment and outcome
* **Mediators** - lie on causal path between variables, inclusion depends on whether you are interested in direct effect of treatment and outcome that doesn't pass through mediator
* **Colliders** - common effect of two other variables
* **Moderators** - change size or direction of relationship between variables

You start the diagram with your research question (i.e. two nodes whose relationship you are interested) and then add all **common** causes for those nodes, and for any other nodes you add to the graph.

**D-seperation rules** determine whether paths will be open (expect associations) or blocked (independent), which are based on whether condition or not on confounders and colliders.

If you have **time-varying treatment** (takes different values over time), then you will have other time-varying components (e.g. time-varying confounding). If there is **treatment-confounder feedback** (i.e. earlier treatment impacts value of later confounder), then you will need to use a special type of method to adjust for confounders, referred to as **G-methods**.

Since you have designed the study to appropriate control for confounding for your relationship of interest - between a given treatment/exposure and outcome - the other variables included may have residual confounding or other biases that affect their associations, and it is important that these effect estimates are not presented (or are explained) - otherwise this is called '**Table 2 fallacy**'.
`````

This page continues on from the introduction to directed acyclic graphs on the prior [causal inference page](./2_intro_to_causality.md).

## Naming conventions

There are naming conventions for particular components of the DAG:
* **A (or E)** = Exposure / Treatment / Intervention / Primary IV
* **Y (or D)** = Outcome
* **C** = Covariates / Confounders
* **U** = Unmeasured relevant variables

When letters are not used, the exposure and outcome will often be highlighted using a "?" on the arrow, or through coloured boxes or arrows.

Example:

````{mermaid}
  flowchart LR;

    A:::green;
    Y:::green;
    C:::white;
    U:::white;
    
    A -->|?| Y;
    C --> A;
    C --> Y;
    U --> A;
    U --> C;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

Nodes can also be described as:
* **Ancestor** = direct cause (**parent**) or indirect cause (e.g. **grandparent**) of a variable
* **Descendent** = direct effect (**child**) or indirect effect (e.g. **grandchild**) of a variable [[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

## Key components

### Confounders

**Confounders** are variables that **cause BOTH the treatment/exposure and outcomes**. 

*Informally, it occurs when there is an open backdoor path between the treatment/exposure and outcome, and you could say a confounder is a variable that - possibly together with other variables - can be used to block the backdoor path between the treatment and outcome.*

We included **measured and unmeasured** confounders in our DAG.[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

We can use **conditioning** to control for confounding. This involves examining the relationship between A and Y within levels of the conditioning variable, using either: (a) sample restriction, (b) stratification, (c) adjustment, or (d) matching. If we don't do this, we will get **confounding bias** (where a common cause of A and Y is not blocked). When you condition on something, you **draw a box** around it on the DAG.

Other terms like "adjusting" or "controlling" suggest a misleading interpretation of the model - although there does seem to be variability in terminology, with many sources using these terms. [[source]](https://med.stanford.edu/content/dam/sm/s-spire/documents/WIP-DAGs_ATrickey_Final-2019-01-28.pdf) Igelström et al. 2022 explain that 'conditioning on a variable is analogous to controlling for, adjusting for or stratifying by it (although in practice, different methods of conditioning may have different effects on the results and their interpretation).'[[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

Example: smoking causes yellow fingers and lung cancer
* If we don't condition on it, we expect to see an association between yellow fingers and lung cancer (known as a **marginal/unconditional** association)
* If we do condition on smoking, we expect to see no association between yellow fingers and lung cancers (i.e. they are "**not associated conditional on** smoking)[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

````{mermaid}
  flowchart TD;

    con:::outline;
    subgraph con["`**Conditional**`"]
      cig2("Smoking"):::black;
      lung2("Lung cancer"):::white;
      yellow2("Yellow fingers"):::white;
    end

    cig2 --> lung2;
    cig2 --> yellow2;

    uncon:::outline;
    subgraph uncon["`**Unconditional**`"]
      cig("Smoking"):::white;
      lung("Lung cancer"):::white;
      yellow("Yellow fingers"):::white;
    end

    cig --> lung;
    cig --> yellow;

    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
    classDef outline fill:#FFFFFF;
````

### Moderators

**Moderators** are variables that change the **size or direction** of the relationship between variables. These could also be referred to as **effect modifiers** or statistical interaction. [[source]](https://med.stanford.edu/content/dam/sm/s-spire/documents/WIP-DAGs_ATrickey_Final-2019-01-28.pdf)
* If it impacts the **size** of the relationship, this is called **non-qualitative effect modification**
* If it impacts the **direction** of the relationship, this is called **qualitative effect modification** [[Hernán and Robins 2024]](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)
* These can also be referred to as **effect measure modification (EMM)**. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

They usually help you judge the external validity of your study by identifying the limitations of when the relationship between variables holds. [[source]](https://www.scribbr.co.uk/faqs/why-should-you-include-mediators-and-moderators-in-your-study/) 

There has been some disagreement on how these should be included/notation within DAGs. [[source]](https://med.stanford.edu/content/dam/sm/s-spire/documents/WIP-DAGs_ATrickey_Final-2019-01-28.pdf)[[Weinberg 2007]](https://pubmed.ncbi.nlm.nih.gov/17700243/)

'The presence and extent of EMM mathematically depends on the choice of an additive or multiplicative scale linking exposure and outcome; EMM may be present on either one of these scales or both'

'If both the exposure and effect modifier are causes of the outcome, then EMM will always be present on at least one scale.'

'**Interaction** denotes that the **joint effect of two exposures is different from the sum of the individual effects of each exposure**. Like EMM, the presence and extent of interaction depends on the choice of an additive or multiplicative scale and does not necessarily have a meaningful causal interpretation. ‘Interaction’ is sometimes used interchangeably with EMM, but it is helpful to think of these as different concepts:
* Interaction focuses on the **joint causal effect** of two exposures (eg, the combined effect of smoking and asbestos exposure on lung cancer)
* EMM focuses on the effect of one exposure whose effect differs across levels of another variable (eg, the effect of asbestos exposure on lung cancer in smokers vs non-smokers); with EMM, the **causal effect of the effect modifier itself is not of interest**.' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

````{mermaid}
  flowchart LR;

    A("A (treatment/exposure)"):::green;
    Y("Y (outcome)"):::green;
    Empty[ ]:::empty;
    Mod("Moderator"):::white;

    Mod --> Empty;
    A --- Empty;
    Empty -->|?| Y;

    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
    classDef empty width:0px,height:0px;
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

**Why do we care about modifiers/effect modification?**

(1) The average causal effect will differ between populations with different prevalence of the modifier - i.e. it depends on the distribution of individual causal effects in the population
* **Example: If average causal effect of exposure is harmful in women and beneficial in mean, a study with an equal gender split would find null causal effect, and a study with majority women would find harmful causal effect.*
* Hence, 'there is generally no such thing as “the average causal effect of treatment A on outcome Y (period)”, but “the average causal effect of treatment A on outcome Y in a population with a particular mix of causal effect modifiers.”' The ability to extrapolate causal effects between populations is referred to as the **transportability** of causal inferences across populations.
* However, there will often be unmeasured effect modifiers, and so 'transportability of causal effects is an unverifiable assumption that relives heavily on subject-matter experts'.[[Hernán and Robins 2024]](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)

(2) Additive (but not multiplicative) effect modification can help identify groups who would most benefit from an intervention [[Hernán and Robins 2024]](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)

(3) Identifying effect modification may help us to understand the biological, social, or other mechanisms leading to the outcome. [[Hernán and Robins 2024]](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)


### Mediators

**Mediators** are variables that lie in the causal path between the two other variables (e.g. between exposure and outcome), and they tell you how or why an effect takes place.[[source]](https://www.scribbr.co.uk/faqs/why-should-you-include-mediators-and-moderators-in-your-study/)
* A path that includes a mediator is often called an **indirect effect** or indirect causal path
* In contrast, the arrow directly connecting the treatment and outcome represents the **direct causal effect** of the treatment on the outcome that is not due to changes in the mediator.[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS) This is also referred to as the **controlled direct effect (CDE)** [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)
* If you do not have a direct arrow between the treatment and outcome, and only via the mediator, this implies that this is the only way in which the treatment can cause the outcome, and that if you know the mediator is present, knowing whether or not the treatment was present should have no impact on the outcome.

````{mermaid}
  flowchart LR;

    treat("Treatment"):::white;
    med("Mediator"):::white;
    out("Outcome"):::white;

    treat --> med;
    med --> out;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

You might **condition** on a mediator if you are interested in the **direct effect of treatment on outcome that doesn't pass through mediator**. Example: In racial disparity studies, will condition on mediators like socioeconomic, education, location (often though **matching** on these characteristics),  to allow you to isolate the unique effect of race that is not explainable by those pathways. [[source]](https://stats.stackexchange.com/questions/488048/dag-are-there-situations-where-adjusting-for-mediators-is-reasonable) This is referred to as **mediation analysis** - when you're trying to 'quantify how much of the total effect of A on Y is explained by a particular mediator (the indirect effect), and how much is not (the direct effect)'.

````{mermaid}
  flowchart LR;

    race("Race"):::white;
    outcome("Outcome"):::white;
    ses("Socioeconomic status"):::black;
    ed("Education"):::black;
    loc("Location"):::black;

    race -->|?| outcome;
    race --> ses; ses --> outcome;
    race --> ed; ed --> outcome;
    race --> loc; loc --> outcome;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

#### How is CDE estimated?
* 'Assuming no interaction between exposure and mediator, and no confounding between mediator and outcome, the indirect effect can be obtained by subtracting the CDE from the total effect'
* 'When interaction is present between exposure and mediator, the CDE will take on different values for different levels of the mediator, and the effect obtained by subtracting the CDE from the total effect no longer has a meaningful causal interpretation.'
* 'To address this problem, alternative definitions of causal direct and indirect effects have been proposed, such that their sum adds up to the total effect even in the presence of interactions, generally by allowing one or more of these effects to include the interaction effect.' These include:
  * Controlled direct effect (CDE)
  * Natural direct effect or pure direct effect
  * Natural indirect effect or total indirect effect
  * Pure indirect effect
  * Total direct effect
* 'These effect estimands can be defined theoretically in counterfactual terms, but can only be estimated given additional assumptions that are difficult to verify and may lack applicability for estimating policy-relevant mediation quantities (eg, how much the effect of A on Y could be reduced by intervening on the mediator).'[[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

#### Over-adjustment bias

[Schisterman et al. 2009](https://doi.org/10.1097/EDE.0b013e3181a819a1) defined **over-adjustment bias** as 'control for an intermediate variable (or a descending proxy for an intermediate variable) on a causal path from exposure to outcome' (i.e. controlling for a mediator).

### Colliders

**Colliders** are descendents of two other variables - i.e. common effect - with two arrows from the parents pointing to ("colliding with") the descendent node. Colliders naturally block back-door paths. **Controlling for a collider will open the back-door path, thereby introducing confounding**.[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS) This is referred to as **collider bias**

Example: A genetic factor and an environmental factor causing cancer.
* Scenario #1: No conditioning - These are **independent** - i.e. genetic factor doesn't have causal effect on environmental factor - and so we don't expect to see an association between genetic and environment (unconditional/marginal association).
* Scenario #2: Condition on cancer - If we condition on cancer - such as by just selecting people who have cancer - we will find an **inverse association** between genetics and environment (as if cancer wasn't caused by one, it was by the other). This biased effect estimate is referred to as **selection bias**.
* Scenario #3: Condition on surgery - We can **induce** selection bias by conditioning on the downstream consequence of a collider - e.g. if cancer is collider, and surgery is consequence of cancer, if we condition on surgery, we expect to see inverse association between genetic and environment conditional on surgery (just as we did for the collider cancer).[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

````{mermaid}
  flowchart TD;

    con_sur:::outline;
    subgraph con_sur["`**Condition on surgery**`"]
      gene3("Genetic<br>factor"):::white;
      env3("Environmental<br>factor"):::white;
      cancer3("Cancer"):::white;
      surgery3("Surgery"):::black;
    end

    gene3 --> cancer3;
    env3 --> cancer3;
    cancer3 --> surgery3;

    con_cancer:::outline;
    subgraph con_cancer["`**Condition on cancer**`"]
      gene2("Genetic<br>factor"):::white;
      env2("Environmental<br>factor"):::white;
      cancer2("Cancer"):::black;
      surgery2("Surgery"):::white;
    end

    gene2 --> cancer2;
    env2 --> cancer2;
    cancer2 --> surgery2;

    none:::outline;
    subgraph none["`**No conditioning**`"]
      gene("Genetic<br>factor"):::white;
      env("Environmental<br>factor"):::white;
      cancer("Cancer"):::white;
      surgery("Surgery"):::white;
    end

    gene --> cancer;
    env --> cancer;
    cancer --> surgery;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
    classDef outline fill:#FFFFFF;
````

Collider bias may also be present when neither the exposure nor the outcome is a direct cause of the collider variable. An example is **M-bias**. In this example...
* Focus: beta-blocker use and risk of ARDS
* Might be tempted to adjust for crackles as you might think its a confounder... 1) heart failure leads to both chronic β-blocker therapy and crackles, and 2) pneumonia causes both ARDS and crackles
* However, crackles is actually a collider on the **back-door path** of **chronic β-blocker therapy** ← heart failure → crackles ← pneumonia → **ARDS**. Adjusting for the presence of crackles opens this back-door path, introducing confounding. Ignoring the presence of crackles would be the right thing to do.[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS)

````{mermaid}
  flowchart TD;

    beta("Beta blocker use"):::white;
    ards("Acute respiratory distress syndrome (ARDS)"):::white;
    hf("Heart failure"):::white;
    pneu("Pneumonia"):::white;
    crackles("Crackles"):::black;

    hf --> beta;
    hf --> crackles;
    pneu --> crackles;
    pneu --> ards;
    beta -->|?| ards;
  
    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

Another type of collider bias - specifically, a type of selection bias - is **Berkson's bias**. This is when the selection of cases into the study depends on hospitalisation, and the treatment is another disease, or a cause of another disease, which also results in hospitalisation.[[source]](https://med.stanford.edu/content/dam/sm/s-spire/documents/WIP-DAGs_ATrickey_Final-2019-01-28.pdf)

### Selection nodes

**Selection nodes** - by definition - are **always conditioned on**. This is because they reflect a restriction for inclusion such as:
* **Loss to follow-up** - e.g. if some people lost to follow-up (C1) and some remain to end (C0), our analysis is restricted to C0. This means that only individuals with certain values of C are included in the analysis, as we're essentially conditioning on it.
* **Inclusion/exclusion criteria for the study** - e.g. if only include men, then gender --> study enrollment

### Measurement error (mis-measured variables)

**Measurement error** is the degree to which we mismeasure a variable. If believe a variable is mismeasured, we have a node with a "*" that points from variable, with another representing measurement error.[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home) There are two types:
* **Non-differential error** - if error is not in exposure or outcome - this will bias the estimate of effect towards the null (so for small effects or studies with little power, it can make a true effect disappear)
* **Differential error** - if there is error in exposure and outcome - then, errors themselvse can be associated, opening a back-door path between exposure and outcome[[source]](https://cran.r-project.org/web/packages/ggdag/vignettes/bias-structures.html) - i.e. it is when measurement error varies in size depending on another variable. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

Example: **Recall bias**. Does taking multivitamins in childhood help protect against bladder cancer later in life?
* Bias in outcome depends only on how well diagnosis of bladder cancer represents actually having it
* Bias in exposure depends on both (a) memory of vitamin uptake, and (b) bladder cancer, since they might have spent more time reflecting on what could have caused the illness
* If there is no effect of vitamins on bladder cancer, this dependency will make it seem as if vitamins are a **risk** for bladder cancer. If it is, in fact, **protective**, recall bias can reduce or even reverse the association.

````{mermaid}
  flowchart TD;

    me_diag("<b>Measurement error</b><br>in diagnosis"):::white;
    diag("Diagnosis of bladder cancer *"):::white;
    cancer("Bladder cancer"):::white;
    me_vit("<b>Measurement error</b><br>in vitamin uptake"):::white;
    mem_vit("Memory of<br>vitamin uptake *"):::white;
    vit("Childhood vitamin intake"):::white;

    me_diag --> diag;
    cancer --> diag;
    cancer --> me_vit;
    me_vit --> mem_vit;
    vit --> mem_vit;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
    classDef outline fill:#FFFFFF
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

## How do you know what to include in your DAG?

### DAG completeness

A DAG is said to represent a complete causal structure between a treatment and outcome if:
* **Treatment and outcome** are presented
* **For any two nodes on the graph, all common causes** of those two nodes are represented
* All **selection variables** are represented (i.e. selection node) [[Rogers et al. 2022]](https://doi.org/10.1002/psp4.12894)

What do we mean by including common causes? Illustrating with an example...
* In **RCT** where people were randomised to receive Aspirin, we **don't need to include other variables** that can cause stroke (e.g. coronary heart disease (CHD)), as they didn't cause why people got aspirin.
* In an **observational study**, there will be other variables that would explain why people received aspirin (e.g. CHD), which we would need to include for it to be a causal DAG (i.e. **aspirin AND stroke BOTH caused by CHD**). [[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

You don't need variables that **cause Y but not A** (although might include if for example you want to compare to other studies that did adjust for that variable).

````{mermaid}
  flowchart TD;

    ob:::outline;
    subgraph ob["`**Observational**`"]
      asp2("Aspirin"):::green;
      str2("Stroke"):::green;
      chd2("Coronary heart disease (CHD)"):::white;
    end

    asp2 --> str2;
    chd2 --> asp2;
    chd2 --> str2;

    rct:::outline;
    subgraph rct["`**RCT**`"]
      asp("Aspirin"):::green;
      str("Stroke"):::green;
    end

    asp --> str;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
    classDef outline fill:#FFFFFF
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

### How do you know when to include mediators?

* If we are interested in the **total effect of A on Y**, we don't need to specify the mechanisms through which A may affect Y (i.e. don't need any m ediators between A and Y)
* However, if we are interested in the **direct effect of A on Y** that doesn't pass through the mediator, then we should include it. [[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

### When should you draw arrows?

The DAG is drawn based on **expert knowledge**, including arrows when you believe that something causes something else. If expert knowledge is **insufficient** for us to rule out a direct effect of E on D, then we should draw an arrow.

Arrows on causal graphs are **not deterministic** - i.e. doesn't mean every person with exposure will see outcome - as some will never, and some without outcome will develop it. [[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

### Can you use variable selection methods?

No - it is important that these are based on expert knowledge. For causal inference, it is **NOT** recommended to choose included variables/relationships based on:
* P value-based and model-based **variable selection methods** (including forward, backward, and stepwise selection) - since they ignore the causal structure underlying the hypothesis and treat confounders and colliders similarly
* Use methods that **rely on model** fit or related constructs (e.g. R<sup>2</sup>, Akaike information criterion, and Bayesian information criterion) - since these rely heavily on the available data, in which causal relationships may or may not have been captured and may or may not be evident, and specification of model and arbitrary variables included will drive observed associations with outcome
* Use selection of variables that, when included in a model, change the magnitude of the effect estimate of the exposure of interest, to identify confounders
* Identify multiple 'independent predictors' through purposeful or automated variable selection

**If the authors have hypotheses about each variable, then a separate model for each variable should be generated** - or a prediction model could be developed, if prediction, rather than causal inference, is the goal of the analysis[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS)

## How do you create a DAG?

First, start with your **research question**. This should be A (treatment/exposure) and Y (outcome), identificated by letters, "?" or colours.

Then add the key components as detailed above...
* Measured confounders (L)
* Unmeasured confounders (U)
* Selection nodes
* Moderators
* Mediators
* Mismeasured variables

**Everytime you add a new node** to the DAG, you need to conside whether it has common causes with any other variables (its not just about common causes of A and Y). For example, if you believe measurement of Y is affected by whether person is on treatment, draw arrow from A to measurement error for Y.

There can often be **more than one appropriate DAG**, and alternate DAGs can make excellent sensitivity analyses.[[source]](https://med.stanford.edu/content/dam/sm/s-spire/documents/WIP-DAGs_ATrickey_Final-2019-01-28.pdf) [[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

````{mermaid}
  flowchart LR;

    A("A (treatment/exposure)"):::green;
    Y("Y (outcome)"):::green;
    Empty[ ]:::empty;
    Mod("Moderator"):::white;
    M("Mediator"):::white;
    L("L (confounder)"):::white;
    U("U (unmeasured confounder)"):::white;
    C("C (selection node)"):::black;
    Y*("Y* (mismeasured outcome)"):::white;
    UY("U<sub>Y</sub> (measurement error for Y)"):::white;

    Mod --> Empty;
    A --- Empty; Empty -->|?| Y;
    A --> M; M --> Y;
    L --> A; L --> Y;
    U --> L; U --> Y;
    A --> C;
    L --> C;
    Y --> Y*;
    UY --> Y*;
    A --> UY;

    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
    classDef empty width:0px,height:0px;
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

## Paths

A **path** is any route through graph - it **doesn't have to follow** the direction of the arrows. Paths can be either be:
* **Open** paths - represent statistical associations between two variables
  * E.g. If don't condition on confounder, will be an open path, and see association with confounder
* **Blocked** (or "closed" paths) - represent the absence of associations 
  * E.g. An unconditioned collider should have no association [[Williams et al. 2018]](https://doi.org/10.1038/s41390-018-0071-3)

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

The **target (causal) paths** are the directed paths from the exposure to the outcome which transmit the target effect. **Biasing paths** are non-directed open paths between the exposure and the outcome, which transmit bias for estimating the effect of the exposure on the outcome.[[source]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3733703/)

## D-seperation rules

### Rules

**D-seperation** rules are used to determine whether paths are **open or blocked** - i.e. whether variables will be **associated or independent**.

If **all paths are blocked** between two variables on the DAG, then they are **d-seperated** (i.e. not associated / statistical independence).[[source]](https://sgfin.github.io/2019/06/19/Causal-Inference-Book-All-DAGs/) Otherwise, they are **d-connected**.[[source]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3733703/)

When identified here, these are structural sources of association. Another cause of association - beyond it being a causal relationship - is by chance. However, increasing our sample size, chance associations should disappear (whilst structural remain and become sharper). [[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

Rules:
1. If there are **no** variables being conditioned on
    * A path is only **blocked** if it contains a **collider**
    * A path is **open** if it does not contain a collider

2. Path is **blocked** if it contains a **non-collider** that **is** conditioned on

3. Path is **open** if **collider is** conditioned on

4. Path is **open** if **descendent** of collider **is** conditioned on.[[source]](https://sgfin.github.io/2019/06/19/Causal-Inference-Book-All-DAGs/)

### Examples of each rule

Rule 1: L to Y open
````{mermaid}
  flowchart LR;

    l("L"):::white;
    a("A"):::white;
    y("Y"):::white;

    l --> a;
    a --> y;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
    classDef outline fill:#FFFFFF
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

Rule 1: L to A blocked
````{mermaid}
  flowchart LR;

    l("L"):::white;
    a("A"):::white;
    y("Y"):::white;

    l --> y;
    a --> y;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
    classDef outline fill:#FFFFFF
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

Rule 2: A to Y blocked.
````{mermaid}
  flowchart LR;

    a("A"):::white;
    b("B"):::black;
    y("Y"):::white;
    
    a --> b; b--> y;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

Rule 3: A to Y open.
````{mermaid}
  flowchart LR;

    a("A"):::white;
    y("Y"):::white;
    l("L"):::black;
    
    a --> l; y--> l;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

Rule 4: A to Y open.
````{mermaid}
  flowchart LR;

    a("A"):::white;
    y("Y"):::white;
    l("L"):::white
    d("D"):::black;
    
    a --> l; y--> l; l --> d;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

## Faithfulness

Faithfulness is the result of **opposite effects of exactly equal magnitude** - e.g. if aspirin caused stroke for half of poppulation and prevented it in the other half, then causal dag is correct (as aspirin affects stroke) but **no association is observed (as they cancel each other out**). In that case, we say the joint distribution of the data is not faithful to the causal DAG. These perfect cancellations are **rare** and we don't expect them to happen in practice. [[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

## Time-varying treatments and confounders

### What is a time-varying treatment?

A **time-varying treatment** is treatment that can take different values over time - such as:
* Whether or not receive medicine at each timepoint
* Dose of medicine at each time point

This is as opposed to **fixed treatments** that do not vary over time (e.g. whether took vitamin D at time of conception).

We can represent this using two arbritary time points, K and K+1. Actual study includes many more weeks but for most purposes, two time points are enough to represent the main features of the causal structure when there is time varying treatment.

You'll notice that a consequence of the time-varying treatment is **time-varying confounder and outcome**. A confounder is time-varying when it can take different values at different timepoint, and confound at different timepoints.

Example: EPO used to treat anemia, dose is based on haemoglobin level at time of appointment (which itself depends on disease severity, but we've just represented that as a single timepoint). To show that we have **time-varying** components, we refer to:
* L and A at timepoint K (e.g. week 0)
* Y, L and A at timepoint K+1 (e.g. week 1)
* Y at timepoint K+2 (e.g. week 2)

````{mermaid}
  flowchart LR;

    ak("A<sub>K</sub>: EPO dose"):::white;
    ak1("A<sub>K+1</sub>: EPO dose"):::white;
    yk1("Y<sub>K+1</sub>: Death"):::white;
    yk2("Y<sub>K+2</sub>: Death"):::white;
    lk("L<sub>K</sub>: Haemoglobin"):::white;
    lk1("L<sub>K+1</sub>: Haemoglobin"):::white;
    u("U: Disease severity"):::white;

    ak --> yk1;
    u --> yk1;
    u --> lk;
    lk --> ak;
    lk --> ak1;
    ak --> ak1;
    u --> lk1;
    lk1 --> ak1;
    ak1 --> yk2;
    u --> yk2;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

### Treatment-confounder feedback

Our DAG above was incomplete - in this scenario, treatment at timepoint K will impact the confounder (levels of haemoglobin) at timepoint K+1. This is referred to as **treatment-confounder feedback** - when the later confounder is impacted by prior treatment.[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home) This is also referred to as **intermediate confounding** - when a confoudner is affected by prior exposure/treatment status.[[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

When there is **treatment-confounder feedback**, then conventional adjustment methods, since:
In other words:
1. Confounding on an intermediate confounder blocks part of the effect of prior exposure/treatment.
2. Conditioning on an intermediate confounder can introduce collider bias, opening additional back-door paths between exposure/treatment and outcome.[[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)
  * e.g. We'll get a biased estimate if we condition on the Ls, as conditioning on L<sub>K+1</sub> will open a path that was previously blocked: A<sub>K</sub> to L<sub>K+1</sub> to U to Y<sub>K</sub>. Hence, we have introduced selection bias.[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

This means we will be unable to yield an unbiased estimate and, if the time-varying confounder also affects the outcome (e.g. L<sub>K+1</sub> --> Y<sub>K+2</sub>), it will be impossible to estimate the total effect of the treatment.[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

We need other methods to handle these settings: **G-methods**. [[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)


````{mermaid}
  flowchart LR;

    ak("A<sub>K</sub>: EPO dose"):::white;
    ak1("A<sub>K+1</sub>: EPO dose"):::white;
    yk1("Y<sub>K+1</sub>: Death"):::white;
    yk2("Y<sub>K+2</sub>: Death"):::white;
    lk("L<sub>K</sub>: Haemoglobin"):::black;
    lk1("L<sub>K+1</sub>: Haemoglobin"):::black;
    u("U: Disease severity"):::white;

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

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

## Presenting results from causal inference studies

'Causal models are typically designed to test an association between a **single exposure and an outcome**. The additional independent variables in a model (often called “covariates”) **serve to control for confounding**. The observed associations between these covariates and the outcome have not been subject to the same approach to control of confounding as the exposure' (i.e. they themselves have not been corrected for confounding - *and they shouldn't and didn't have to be*). 'Therefore, **residual confounding and other biases often heavily influence these associations**.'

'This situation is known as “**Table 2 fallacy**,” a term arising from the practice of presenting effect estimates for all independent variables in “Table 2”.' It is strongly recommended that these effect estimates are **not presented**.[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS)

Hartig 2019 discusses how this may not be practical in some fields (they give example of ecology) where you rarely have a clear target variable/hypothesis, but suggest instead that's important to explicitly state/seperate reasonablly controlled varaibles from possibly confounded variables.[[source]](https://theoreticalecology.wordpress.com/2019/04/14/mediators-confounders-colliders-a-crash-course-in-causal-inference/)

## Minimal set of covariates

We want to identify a **minimal set of covariates** that:
1. Blocks all backdoor paths.
2. Doesn't inadvertenly open closed pathways by conditioning on colliders or descendents. [[source]](https://med.stanford.edu/content/dam/sm/s-spire/documents/WIP-DAGs_ATrickey_Final-2019-01-28.pdf)

With the example below, the minimal set of variables you'd need to condition for would be **L0 and L1 - wouldn't need to for U** as doing for L0 and L1 blocks the backdoor paths.[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

````{mermaid}
  flowchart LR;

    ak("A<sub>K</sub>: EPO dose"):::white;
    ak1("A<sub>K+1</sub>: EPO dose"):::white;
    yk1("Y<sub>K+1</sub>: Death"):::white;
    yk2("Y<sub>K+2</sub>: Death"):::white;
    lk("L<sub>K</sub>: Haemoglobin"):::white;
    lk1("L<sub>K+1</sub>: Haemoglobin"):::white;
    u("U: Disease severity"):::white;

    ak --> yk1;
    u --> yk1;
    u --> lk;
    lk --> ak;
    lk --> ak1;
    ak --> ak1;
    u --> lk1;
    lk1 --> ak1;
    ak1 --> yk2;
    u --> yk2;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

## Example cases

These examples help demonstrate the utility of causal diagrams.

### Example: Oestrogen and endometrial cancer

In 1970s, women began to receive oestrogren after menopause. Some studies in 1975/6 found that women receiving oestrogen had higher risk of diagnosis with endometrical cancer than women not receiving them. Why? Possibilities include...
1. Oestrogens cause cancer
2. Oestrogens can cause uterine bleeding, so women receive a uterine exam, during which the cancer (which is often silent, asymptomatic, and otherwise not diagnosed) is noticed and diagnosed - this phenomenon is called **ascertainment bias**

How do we decide which explanation is right?

* Yale researchers restricted the data analysis to women with uterine bleeding (regardless of whether they were on oestrogens), since they should all have the same likelihood of uterine exams and existing cancer being diagnosed. If there still an association, oestrogen causative.
* Boston researchers argued we would find association even in women who bleed and even if they don't cause cancer, and so that this approach would still have ascertainment bias.

Explanation one.
````{mermaid}
  flowchart LR;

    a("A: Oestrogens"):::white;
    u("U: Cancer (unmeasured)"):::white;
    y("Y: Cancer (diagnosed)"):::white;

    a --> u;
    u --> y;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

Explanation two.
````{mermaid}
  flowchart LR;

    a("A: Oestrogens"):::white;
    u("U: Cancer (unmeasured)"):::white;
    y("Y: Cancer (diagnosed)"):::white;
    c("C: Uterine bleeding"):::white;

    a --> c;
    u --> c;
    c --> y;
    u --> y;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

Restrict analysis to women who bleed. If association still found, must be path of A --> U --> Y. Boston argued could still exist.
* Conditioning on C blocks path A-C-Y
* However, we still have path of A-C-U-Y, and C is collider on that path, so when condition on C, it becomes open (and conditioning on C is what we do when we restrict analysis to bleeders)

So Boston were right. 

````{mermaid}
  flowchart LR;

    a("A: Oestrogens"):::white;
    u("U: Cancer (unmeasured)"):::white;
    y("Y: Cancer (diagnosed)"):::white;
    c("C: Uterine bleeding"):::black;

    a --> c;
    u --> c;
    c --> y;
    u --> y;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

What can you do then? You can design study where C-Y doesn't exist as you require all women to be screened for cancer frequently regardless of whether they bleed. If no association between A and Y, then we know there is no causal effect of A on U. If you still found association, then A must cause U.

````{mermaid}
  flowchart LR;

    a("A: Oestrogens"):::white;
    u("U: Cancer (unmeasured)"):::white;
    y("Y: Cancer (diagnosed)"):::white;
    c("C: Uterine bleeding"):::white;

    a --> c;
    u --> c;
    u --> y;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

### Example: HIV and ART

Randomised controlled trials of new antiretroviral therapy (ART) for HIV found it was effective and reduced morality by more than half.

Observational of clinical data to look at real world effect of ART did not detect much benefit for new combination therapies - no increased survival among those taking ART. What was wrong with the studies?

They were adjusting for lots of confounders - e.g. CD4 count - and yet could not eliminate the bias. Some people say there must be lots of unmeasured confounding. However, the more time-varying confounders were adjusted for, the more biased the effect estimate seemed to be. The problem was treatment-confounder feedback - the value of CD4 count was impacted by earlier treatment - in this case, the bias was in the opposite direction.

There is a way to identify whether the bias is due to incomplete adjustment for confounding or for incorrect adjustment for time-varying confounders - and that is to use G-methods to adjust for the time-varying confounders. When they used G-methods, the effect estimates were much closer to the ARTs.

````{mermaid}
  flowchart LR;

    ak("A<sub>K</sub><br>ART"):::white;
    
    lk("L<sub>K</sub><br>CD4 count"):::black;
    u("U<br>Immuno-suppression status"):::white;
    yk1("Y<sub>K+1</sub><br>Mortality"):::white;
    lk1("L<sub>K+1</sub><br>CD4 count"):::black;
    ak1("A<sub>K+1</sub><br>ART"):::white;
    yk2("Y<sub>K+2</sub><br>Mortality"):::white;
    
    lk --> ak;
    u --> lk; 
    u --> yk1;
    u --> lk1;
    lk1 --> ak1;
    u --> yk2;
    ak --> lk1;
    
    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)