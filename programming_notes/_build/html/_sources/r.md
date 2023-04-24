# R

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
  

# Packages
Notes from working through: https://r-pkgs.org/  
**Remember:** Git commit after each change

### Packages: set up
Start in a fresh R session in the directory where you want to create the folder (e.g. Documents).  

Environment:  
* `library(devtools)` (if not already installed, will need to run install.packages("devtools")  
* `create_package("~/Documents/packagename")`, which will create a directory (if doesn't already exist) and populate with .gitignore, .Rbuildignore, DESCRIPTION, NAMESPACE, R folder, and packagename.Rproj. RStudio will open a new window with Rproj activated/open. As it's a fresh R session, then call `library(devtools)` again.  
* `renv::init()` to set up with renv  
* `install.packages(c("devtools", "roxygen2", "testthat", "knitr"))` then `renv::snapshot()`  
* `library(devtools)`, or add to .Rprofile to always library() it:
```
if (interactive()) {
  suppressMessages(require(devtools))
}
```  

GitHub:  
* Make it a GitHub repository - `usethis::use_git()`  
* Rename branch `git branch -m master main`  
* Link with GitHub - `usethis::use_github()`. May get error about personal access token if not set. To see if it is set, run `gh_token_help()`. To store, use `gitcreds::gitcreds_set()`  

Description, license and readme:  
* Edit DESCRIPTION (title, author, description)  
* `use_mit_license()` to create the license files  
* `use_readme_rmd()` to create basic README file, add some lines to .Rbuildignore, and creates a Git pre-commit hook to help you keep README.Rmd and README.md in sync. **To update README** run`build_readme()` to create README.md from README/Rmd. The advantage of having a README.Rmd file is that you can include code chunks, embed plots, etc. You can also use GitHub Actions to re-render README.Rmd every time you push, example here: <https://github.com/r-lib/actions/tree/v1/examples>. I have not tried that yet though.  

### Packages: adding functions and testing
`use_r("functionname")` to create or open script functionname.R in R/ directory. Add the function there (only that, not libraries etc.).  

Docstring:  
* Open function R file, click cursor within function, then do *Code > Insert Roxygen skelecton*.
* Edit the Rxoygen description. It will include @export. This tells Roxygen2 to add this function to the NAMESPACE file, so that it will be accessible to users. For your first R package, you’ll probably want to include @export for each of your functions.  
* Run `document()` to update documentation. It will convert the roxygen comment into man/functionname.Rd and write in NAMESPACE  
* The @example directive is used when you want to use an external file that contains the examples. If you're including the example(s) directly in your roxygen documentation then use `@examples`. If you don't want the examples to run (e.g. if providing with a fake file that doesn't exist, and hence would fail check() as it tests examples work), then use `@examplesIf interactive()`  
* Can now preview helpfile by running `?functionname`  
* Usage is derived from function specification. Can set manually with `@usage` and remove entirely with `@usage NULL`  

Testing:  
* `use_testthat()`. This initializes the unit testing machinery for your package. It adds Suggests: testthat to DESCRIPTION, creates the directory tests/testthat/, and adds the script tests/testthat.R.  
* `use_test("functionname")` to create matching testfile.  
* `library(testthat)`, `load_all()`, `test()` to run the test. Tests will also run whenever `check()` package  
* `rename_files("strsplit1", "str_split_one")` to rename the R file and will also rename testthat file (which we also edit with new function name), to fit with convention of filename matching function name  

### Packages: using other libraries  
Based on: <https://kbroman.org/pkg_primer/pages/depends.html>  
* Add libraries that are essential for package to run and that want R to install when install your package to Imports: section of DESCRIPTION FILE. Instead of manual change, can also run use_package("readxl") which adds it to Imports section of DESCRIPTION.  
* Add required imports to each function - ideally with specific functions - or just whole package - example:  
```
#' @import tidyverse
#' @importFrom readxl read_excel
```  
* Run `check()` to see if issue is resolved  

### Packages: loading and checking
* `load_all()` to simulate process of building, installing and attaching the package. You can then use functions from that package.  
* `check()` to check package is in working order. Read output - it's easier to deal with these problems earlier  
* `install()` then `library(packagename)` to install and use package in current environment  

### Packages - Vignettes:  
* `usethis::use_vignette("my-vignette")` - creates directory, modifies DESCRIPTION, drafts vignette Rmd, adds patterns to .gitignore  
* `install()`, `library(package_name)` then knit  
If you rename vignette, change VignetteIndexEntry to match title (doesn't need to match filename). When run, will create new html under docs/articles called newfilename.html. Delete old filename. Build site. Push.  

### Packages - Create GitHub pages website:  
Initial set-up:  
* First step is to ensure set up with git creds. When I first tried this, I had lots of issues with it not working, and realised this was because I hadn't set it up with the Personal Access Token (PAT). Do this using `gitcreds::gitcreds_set()`. Check settings using `usethis::gh_token_help()`.  
* Next step is to go to repository Settings > Actions > General > Workflow permissions and check "read and write permissions"  
Creating site:  
* OPTION 1. `usethis::use_pkgdown()`, then `pkgdown::build_site()`, then remove docs from .gitignore so you can commit them to GitHub, then push to main  
* OPTION 2: `usethis::use_pkgdown_github_pages()`  

To **update website**, rebuild locally using `pkgdown::build_site()` then push to GitHub and push to main branch. GitHub pages will always based on files in docs/ folder for source code of website in specified branch (default: main).
