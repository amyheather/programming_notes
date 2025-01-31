# General

## Comparing two dataframes

```
waldo::compare(df1, df2)
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

## Linting

```
install.packages("lintr")
library(lintr)
lint("filename.R")
lintr::lint_dir("foldername")
lintr::lint_package()
```