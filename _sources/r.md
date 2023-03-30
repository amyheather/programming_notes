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

## Reproducible environment: renv  
To start new project environment, creating .RProfile: `renv::init()`  
To save state of project library to lockfile renv.lock: `renv::snapshot()`  
To return to environment in lockfile:  `renv::restore()`  

## Linting
```
install.packages("lintr")
library(lintr)
lint("filename.R")
```

## Packages
Notes from working through: https://r-pkgs.org/  
1. Start in a fresh R session in the directory where you want to create the folder (e.g. Documents).  
2. `library(devtools)` (if not already installed, will need to run install.packages("devtools")  
3. `create_package("~/Documents/packagename")`, which will create a directory (if doesn't already exist) and populate with .gitignore, .Rbuildignore, DESCRIPTION, NAMESPACE, R folder, and packagename.Rproj. RStudio will open a new window with Rproj activated/open. As it's a fresh R session, then call `library(devtools)` again.  
4. Make it a GitHub repository - `use_git()`  
5. `use_r("strsplit1")` to create or open script strsplit1.R in R/ directory. Add the function there (only that, not libraries etc.)  
6. Normally we might use this function by defining function in global environment or calling source("R/strsplit1.R"). However, when making a package, we do `load_all()` and then can use function e.g. `strsplit1("alfa,bravo,charlie,delta", split=",")`. load_all() simulates the process of building, installing, and attaching the regexcite package.  
7. `check()` to check package is in working order. Read output! Easier to dela with problems earlier. In the example, you get 1 warning, which is non-standard license specification  
8. Edit DESCRIPTION (title, author, description)  
9. `use_mit_license` to create the license files  
10. Open strsplit1.R, click cursor within function, then do *Code > Insert Roxygen skelecton*. Edit the description. Then run `document()` so it converts the roxygen comment into man/strsplit1.Rd. Can now preview helpfile by running `?strsplit1`  
11. Install package: `install()`. Should now be able to use package. Restart R, then try `library(regexcite)` and running the function  
12. `use_testthat()`. This initializes the unit testing machinery for your package. It adds Suggests: testthat to DESCRIPTION, creates the directory tests/testthat/, and adds the script tests/testthat.R.  
13. `use_test("strsplit1")`, modify test, then `library(testthat)`, `load_all()`, `test()` to run the test. Tests will also run whenever `check()` package  
14. To use functions from another package, `use_package("stringr")`, which stringr package to the “Imports” section of DESCRIPTION. Then modify function. In example, explains the changes made because we're importing.  
15. `rename_files("strsplit1", "str_split_one")` to rename the R file and will also rename testthat file (which we also edit with new function name), to fit with convention of filename matching function name  
16. `document()` to update documentation and update NAMESPACE. Can they try it - `load_all()`, `str_split_one("a, b, c", pattern = ", ")`  
17. To set up on github, `use_github()`  
18. `use_readme_rmd()` to create basic README file, add some lines to .Rbuildignore, and creates a Git pre-commit hook to help you keep README.Rmd and README.md in sync.  
19. `build_readme()` to create README.md from README/Rmd  
20. `check()` and `install()`  

Vignettes:  
* `usethis::use_vignette("my-vignette")` - creates directory, modifies DESCRIPTION, drafts vignette Rmd, adds patterns to .gitignore  
* `library(regexcite)` then knit  

Create GitHub pages website:  
* `usethis::use_pkgdown()` and `pkgdown::build_site()` to setup  
* Remove docs from .gitignore so you can commit them to GitHub
* `usethis::use_pkgdown_github_pages()` sets everything up for you. Can now view site (may take a few minutes to deploy) e.g. https://amyheather.github.io/regexcite/  
* HOWEVER I had alot of issues with this not working - and finally realised why! It was failing to push as I hadn't set it up with the Personal Access Token (PAT). Do this using `gitcreds::gitcreds_set()`. Check settings using `usethis::gh_token_help()`. Then when you run the above command, it should succeed!    