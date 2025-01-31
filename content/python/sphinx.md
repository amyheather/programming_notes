# Sphinx

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

## Example Makefile

```
# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    +=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
```

## Example requirements.txt

```
jupyter-book
matplotlib
numpy
pydata-sphinx-theme
sphinxcontrib-mermaid
```

## Example index.md

Start with

"```{toctree}
:hidden: True"

Then

```
Books <books/making_books>
Python <python/general>
R <r/general>
programming_notes/git
simulation/simulation
Causality <causal_concepts/1_predict_vs_causal>
Other <programming_notes/latex>
```

## Example conf.py

```
# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'Amy Notes'
copyright = '2024, Amy Heather'
author = 'Amy Heather'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinxcontrib.mermaid',  # To render mermaid diagrams
    'myst_nb',
    'sphinx_copybutton', # Adds a copy button next to code blocks
    'sphinx_togglebutton', # Allows you to make admonitions toggle-able
    'sphinx_design'  # Allows grides, cards, dropdowns, tabs, badges, etc.
]

myst_enable_extensions = [
    'colon_fence'  # To use sphinx-design alongside myst_parser
]

# File types for documentation
source_suffix = ['.md']

# Files to ignore
exclude_patterns = [
    '**.ipynb_checkpoints',
    '_build',
    'README.md'
]

# Notebook execution
nb_execution_allow_errors = False
nb_execution_cache_path = ''
nb_execution_excludepatterns = []
nb_execution_in_temp = False
nb_execution_mode = 'off'
nb_execution_timeout = 30

# -- Options for HTML output -------------------------------------------------

html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    # Set logo
    'logo': {
        'text': 'Programming notes'
    },
    # Add icons to the bar across the top
    'icon_links': [
        {
            'name': 'GitHub',
            'url': 'https://github.com/amyheather/programming_notes/',
            'icon': 'fab fa-github-square'
        }
    ]
}

# Custom CSS style sheet
html_static_path = ['_static']
html_css_files = [
    'css/custom.css',
]
```

## Example custom.css

```
.navbar {
    background-color: #F0F8FF !important;
}
```