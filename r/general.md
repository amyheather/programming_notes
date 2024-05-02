# General

```{toctree}
:hidden: True

self
packages
```

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