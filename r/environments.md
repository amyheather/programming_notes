# Dependency management in R

CRAN won't let you use old versions of packages.

People like R because they can just use one R environment and everything works in that latest environment. General recommendation is just to use the latest stuff

"A big reason R doesn't have as rich an ecosystem for package installation tools (as compared to other languages) is because CRAN's design alleviates many of the challenges traditionally faced in package installation. As an example, CRAN checks new package updates to ensure they work with their upstream reverse dependencies. If updates fail to pass these "revdep checks", the package author must shoulder the burden of getting those reverse dependencies in line. Overall, this ensures that users going to install.packages get a set of packages that work together. Other languages push more of this work onto the person (and client) installing the package. However, as the R package ecosystem has grown, and people have developed more mission-critical workflows that require reproducibility, we have seen an uptick in the need for package management (as opposed to installation) tools." [[source]](https://forum.posit.co/t/what-is-the-current-state-of-r-package-mangers-in-2019/25143/2)

Binary packages, pre-compiled, etc. etc.

[CRAN Task View Initiative](https://cran.r-project.org/web/views/ReproducibleResearch.html) suggests checkpoint, containerit, dateback, groundhog, liftr, miniCRAN, packrat, rang, renv, Require, switchr.

* box
* capsule
* checkpoint
    * 874 monthly downloads, last published 28 January 2022, [[source]](https://www.rdocumentation.org/packages/checkpoint/versions/1.0.2)
    * can't use packages hosted elsewhere
    * depends on maintenance of mRAN (which is now dead)
* conda
* containerit: Automatically generate Dockerfile from current R session
    * Requires `R (>= 3.5.0)` [[source]](https://github.com/o2r-project/containerit/)
    * Last updated 20 August 2019 [[source]](https://github.com/o2r-project/containerit)
    * "Uses the posit.packagemanager.co servers hosted by Posit" [[source]](https://www.rdocumentation.org/packages/Require/versions/0.3.1)
* dateback
    * Developed after MRAN closed, "miniCRAN package would be a better choice if you want to archive the current packages and will use them in the future. dateback will be helpful if you haven't archived packages in advance"
    * Suggests Posit Package Manager for Windows and Mac users
* deps
* docker
    * Needs root access
* groundhog
    * From v3.0.0, relies on GRAN instead of MRAN
    * 1071 monthly downloads, last published 3 February 2024, [[source]](https://www.rdocumentation.org/packages/groundhog/versions/3.2.0)
* jetpak
* liftr
    * 237 monthly downloads, last published 19 June 2019, [[source]](https://www.rdocumentation.org/packages/liftr/versions/0.9.2)
* miniCRAN
    * 1557 monhtly downloads, last published 28 March 2024, [[source]](https://www.rdocumentation.org/packages/miniCRAN/versions/0.3.0)
* packrat
    * `packrat has been soft-deprecated and is now supseded by renv` [[source]](https://www.rdocumentation.org/packages/packrat/versions/0.9.2)
* pak
    * "focuses on fast installations of current versions of packages on CRAN-like packages and GitHub.com and other similar code-sharing pages. This works well if the objective is to keep current. It is fast." [[source]](https://www.rdocumentation.org/packages/Require/versions/0.3.1)
* pkgr
* Posit Public Package Manager
    * Posit has a free service (Posit Public Package Manager (P3M)) and a paid service (Posit Package Manager (PPM))
    * You can set to install from Posit Package Manager instead of CRAN
    * "Posit Public Package Manager is a free, hosted instance of Posit Package Manager." [[source]](https://docs.posit.co/rspm/admin/)
    * You might see this referred to previously as RStudio's Package Manager (which now redirects to Posit)
* rang: Resolve the dependency graph of R packages at a specific time point in order to reconstruct the R computational environment.
    * 180 monthly downloads, last published 8 October 2023, [[source]](https://www.rdocumentation.org/packages/rang/versions/0.3.0)
* rbundler
* remotes
* renv
    * 455,641 monthly downloads, last published 11 April 2024, [[source]](https://www.rdocumentation.org/packages/renv/versions/1.0.7)
    * As in their [old package documentation](https://www.rdocumentation.org/packages/renv/versions/0.3.0-40), renv aims to "be a robust, stable replacement for pakrat"
* Require
    * 1936 monthly downloads, last published 22 May 2024, [[source]](https://www.rdocumentation.org/packages/Require/versions/0.3.1)
* rig
* rocker
    * Pre-configured images
* roo
* r_portable
* switchr
    * 464 monthly downloads, last published 21 March 2023, [[source]](https://www.rdocumentation.org/packages/switchr/versions/0.14.8)
* versions

## How to set-up renv for reproducible research

Create `DESCRIPTION` file e.g.

```
Title: quarto_huang_2019
Depends: 
    R (>= 3.7)
Imports:
    knitr (==1.47),
    rmarkdown (==2.27),
    remotes (==2.5.0),
    tiff (==0.1-12)
```

Then start new empty environment with `renv::init(bare=TRUE)`.

When initialising, you should be prompted to only install from the `DESCRIPTION` - select yes to this. Otherwise, run the command yourself: `renv::settings$snapshot.type("explicit")`.

You can then install the packages from DESCRIPTION by running `renv::install()`, and then create the lock file by running `renv::snapshot`.

If you make any changes to the packages and versions, simply modified the `DESCRIPTION` file and then run `renv::install()` followed by `renv::snapshot`.

If you run into issues where it cannot find a specific package/version, this may be due to the formatting of the version number. For example, for the package `tiff`:

* `tiff` - installs latest version (0.1.12)
* `tiff (==0.1.11)` - cannot find package
* `tiff (==0.1-11)` - installs older version (0.1.11)

The error was due to how those versions are formatted on CRAN, as you can see on the [tiff archive](https://cran.r-project.org/src/contrib/Archive/tiff/).

## Basic renv commands

To start new project environment, creating .RProfile: `renv::init()`  
To save state of project library to lockfile renv.lock: `renv::snapshot()`  
To return to environment in lockfile:  `renv::restore()`  

## Binder

Created using instructions from [here](https://ajstewartlang.github.io/23_introduction_to_binder/slides/23_introduction_to_binder.pdf) and [here](https://github.com/binder-examples/r).  

1. Create runtime.txt file with R version  
2. Create install.R file with package installations  
3. Navigate to https://mybinder.org/, paste in GitHub repository, set to "URL to open (optional)" and type in "rstudio", then launch  

## A few other options...

* **Posit Public Package Manager**- can use Snapshot (earliest is Oct 2017, and 5 most recent versions of R), for Linux can install binary packages (which is much quicker, as usually R installs from source rather than binary unlike for Windows and Mac which makes it really slow) - [source 1](https://packagemanager.posit.co/client/#/repos/cran/setup), [source 2](https://docs.posit.co/faq/p3m-faq/#frequently-asked-questions)
* **Groundhog** - can go back to R 3.2 and April 2015 (and apparently can patch to go earlier) - [source 1](https://www.brodrigues.co/blog/2023-01-12-repro_r/)
* **miniCRAN** - [source 1](https://learn.microsoft.com/en-us/sql/machine-learning/package-management/create-a-local-package-repository-using-minicran?view=sql-server-ver16)
    *  - requires license for non-academic (e.g. NHS) use - but Podman can drop in as replacement. To do development inside a container isn't natively supported by RStudio but can use RStudioServer via Rocker. By default, it runs in ephemeral mode - any code created or saved is lost when close - but you can use volume argument to mount local folders [source 1](https://towardsdatascience.com/running-rstudio-inside-a-container-e9db5e809ff8)