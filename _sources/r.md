# R

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