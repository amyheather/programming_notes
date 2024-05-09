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