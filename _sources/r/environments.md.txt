# R environments

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