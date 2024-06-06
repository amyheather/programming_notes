# General

```{toctree}
:hidden: True

self
packages
```

R -
\begin{itemize}
    \item Renv
    \item Posit Public Package Manager - can use Snapshot (earliest is Oct 2017, and 5 most recent versions of R), for Linux can install binary packages (which is much quicker, as usually R installs from source rather than binary unlike for Windows and Mac which makes it really slow) - \href{https://packagemanager.posit.co/client/#/repos/cran/setup}{source 1}, \href{https://docs.posit.co/faq/p3m-faq/#frequently-asked-questions}{source 2}
    \item Groundhog - can go back to R 3.2 and April 2015 (and apparently can patch to go earlier) - \href{https://www.brodrigues.co/blog/2023-01-12-repro_r/}{source 1}
    \item miniCRAN - \href{https://learn.microsoft.com/en-us/sql/machine-learning/package-management/create-a-local-package-repository-using-minicran?view=sql-server-ver16}{source 1}
    \item Docker - requires license for non-academic (e.g. NHS) use - but Podman can drop in as replacement. To do development inside a container isn't natively supported by RStudio but can use RStudioServer via Rocker. By default, it runs in ephemeral mode - any code created or saved is lost when close - but you can use volume argument to mount local folders - \href{https://towardsdatascience.com/running-rstudio-inside-a-container-e9db5e809ff8}{source 1}
\end{itemize}


## Function setting default inputs  
If default input is different to the input name, you won't have an issue. If it's the same you'll have an error.  
```
# Fine:
x <- function(T = 1){}
# Problem:
x <- function(T = T){}
```
In that case, you can resolve this by doing...  
```
x <- function(T = parent.frame()$T)
```

## Function returning multiple objects  
In python, you can return multiple objects as follows:  
```
def fun():
    str = "example"
    x = 20
    return str, x; # Return tuple, we could also write (str, x)
str_1, x_1 = fun() # Assign returned tuple
print(str_1)
print(x_1)
```  

This is not possible in R. Instead, a good work around is:  
```
fun <- function(suffix) {
    str <- "example"
    x <- 20
    return_names <- c("str", "x")
    return_objects <- mget(return_names)
    return_new_names <- paste0(return_names, "_", suffix)
    return(list(return_new_names, return_objects))
}
output <- fun("1")
for (i in seq_along(output[[1]])){
    assign(output[[1]][i], output[[2]][i])
}
```

## Reproducible environment: renv  
To start new project environment, creating .RProfile: `renv::init()`  
To save state of project library to lockfile renv.lock: `renv::snapshot()`  
To return to environment in lockfile:  `renv::restore()`  

## Reproducible environment: binder
Created using instructions from [here](https://ajstewartlang.github.io/23_introduction_to_binder/slides/23_introduction_to_binder.pdf) and [here](https://github.com/binder-examples/r).  
1. Create runtime.txt file with R version  
2. Create install.R file with package installations  
3. Navigate to https://mybinder.org/, paste in GitHub repository, set to "URL to open (optional)" and type in "rstudio", then launch  

## Linting
```
install.packages("lintr")
library(lintr)
lint("filename.R")
```