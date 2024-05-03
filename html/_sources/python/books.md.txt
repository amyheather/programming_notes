# Books

## Jupyter book
Install jupyter-book package.  
To create sample book stored in current location: `jupyter-book create book_name/`  

To build/rebuild book: `jupyter-book build book_name`  
If add new page and book table of contents doesn't update upon rebuild, try: `jupyter-book build --all book_name`  

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

## Package documentation using Sphinx

To convert from Jupyter book to sphinx, run: `jupyter-book config sphinx path/to/book`. This will generate a conf.py file from your _config.yml and _toc.yml files. You can then run `sphinx-build path/to/book path/to/book/_build/html -b html.

1. Add to environment:
    * `sphinx`
    * `sphinx-rtd-theme`
    * `myst-parser`
    * `sphinx-autoapi`
2. Create directory called `docs` and enter it - e.g. `mkdir docs` and `cd docs`.
3. Add/create any files you want to include in the docs (e.g. how to guides, descriptions) - can be markdown or rst - e.g. guide1.md and guide2.md
4. Run `sphinx-quickstart`
5. Modify **index.rst** file - this is used as home page - e.g.
```
Documentation for package name
==============================

This package...

.. note::

   This project is under active development.
```
6. If you don't want toctree within the home page, and just want it to be in the sidebar, then produce a `contents.rst` - e.g.
```
Site contents
*************

.. toctree::

   Home <index>
   guide1
   guide2
```
7. Modify conf.py - e.g.
```
# -- General configuration ---------------------------------------------------

extensions = [
    'myst_parser',  # To use markdown as well as reStructuredText
    'autoapi.extension'  # Auto generate module and function documentation
]

# Location of files for auto API
autoapi_dirs = ['../kailo_beewell_dashboard']

# File types for documentation
source_suffix = ['.rst', '.md']

templates_path = ['_templates']

# Location of toctree
master_doc = 'contents'

exclude_patterns = ['_build', '_templates', 'Thumbs.db', '.DS_Store']

language = 'English'

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

```
8. Produce the documentation. Any time you want to do this, from the docs folder, run:
    * `make clean` (to clear out build folder, else might not update everything fully)
    * `make html`

## Markdown

Add image with text alongside it: `<img align='left' src='image file path' alt='alt_name' width='900'> Text alongside image `

Admonitions are created using MyST [[see documentation]](https://mystmd.org/spec/admonitions)...

[This page](https://gist.github.com/amyheather/44b5520e4fa601f6dfcc739561929a03) explains how to make custom admonitions.

Blue:

`````{admonition} Note
:class: note

This is the class "note".
`````

Orange:

`````{admonition} Important
:class: important

This is the class "important".
`````

`````{admonition} Caution
:class: caution

This is the class "caution".
`````

`````{admonition} Warning
:class: warning

This is the class "warning".
`````

`````{admonition} Attention
:class: attention

This is the class "attention".
`````

Red:

`````{admonition} Error
:class: error

This is the class "error".
`````

`````{admonition} Danger
:class: danger

This is the class "danger".
`````

Green:

`````{admonition} See Also
:class: seealso

This is the class "seealso".
`````

`````{admonition} Hint
:class: hint

This is the class "hint".
`````

`````{admonition} Tip
:class: tip

This is the class "tip".
`````
