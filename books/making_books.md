# Making books

```{toctree}
:hidden: True

self
hosting_books
markdown
```

<mark>need to sort out</mark>

## Jupyter book

Install jupyter-book package.  

To create sample book stored in current location: `jupyter-book create book_name/`  

To build/rebuild book: `jupyter-book build book_name`  

If add new page and book table of contents doesn't update upon rebuild, try: `jupyter-book build --all book_name`  

## Sphinx

*Note: Written for package documentation*

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
