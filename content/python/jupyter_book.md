# Jupyter book

Install jupyter-book package.  

To create sample book stored in current location: `jupyter-book create book_name/`  

To build/rebuild book: `jupyter-book build book_name`  

If add new page and book table of contents doesn't update upon rebuild, try: `jupyter-book build --all book_name`  

## GitHub pages

To publish book on GitHub Pages:  
* Install ghp-import  
* Navigate to book's root directory (contains `_build/html`) and run: `ghp-import -n -p -f _build/html` (if a directory above, can do `bookname/_build/html` instead)    
* View book at `https://<user>.github.io/<myonlinebook>/`  

To update book, make changes in main branch, rebuild book, then use `ghp-import -n -p -f _build/html` as before to push newly built HTML to gh-pages branch. Will take a few minutes for page to update.  

To set this up to just run from the command `book`:
* `cd` to go to top of directory (i.e. above documents)
* `nano .bashrc`
* At bottom of file, add `alias book="jupyter-book build ./ && ghp-import -n -p -f _build/html"`, then save the file
* Run `source .bashrc` to refresh
* Then, when you want to recreate the jupyter book and push to GH pages, go to where the book is (i.e. where build and config is) and run `book`
* Also set up config file if desired to execute pages `off` if don't want to re-run all the notebooks each time
