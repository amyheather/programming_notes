# Making books

```{toctree}
:hidden: True

self
hosting_books
markdown
```

## Summary

| System | Valid input files | Compatibility with Python & R | Blog posts (tags, dates, filters) ? | Nice examples | Additional details |
| --- | --- | --- | --- | --- | --- |
| <b>Jupyter Book</b><br>[Documentation](https://jupyterbook.org/en/stable/intro.html) | - Markdown `.md`<br>- Jupyter notebook `.ipynb`<br>- MyST markdown notebook `.md`<br>- reStructured Text `.rst` (not recommended)<br>[[source]](https://jupyterbook.org/en/stable/file-types/index.html) | Python tool. Would probably only use with R if you were working with R in `.ipynb`. Possible to convert `.Rmd` to `ipynb` or MyST | Not found example | [SAMueL-1](https://samuel-book.github.io/samuel-1/introduction/intro.html)<br><br>[SAMueL-2](https://samuel-book.github.io/samuel-2/introduction/intro.html) | Easy integration with BinderHub and Google Colab [[source]](https://jupyterbook.org/en/stable/interactive/launchbuttons.html)<br><br>Uses Sphinx to build book [[source]](https://jupyterbook.org/en/stable/explain/sphinx.html) |
| <b>Sphinx</b><br>[Documentation](https://www.sphinx-doc.org/en/master/) | - reStructured Text `.rst` (default)<br>- Markdown `.md`<br>- Jupyter notebook `.ipynb` (with nbsphinx and MyST-NB) | Designed for Python, didn't easily run into R implementation, but [examples here in various languages](https://www.ericholscher.com/blog/2014/feb/11/sphinx-isnt-just-for-python/) | Yes | [pyOpenSci](https://www.pyopensci.org/python-package-guide/index.html)<br><br>[Little book of R for biomedical statistics](https://a-little-book-of-r-for-biomedical-statistics.readthedocs.io/en/latest/)<br><br>[Chris Holdgraf's blog](https://chrisholdgraf.com/blog/) | Thumbnail gallery, Binder, nbviewer [[source]](https://nbsphinx.readthedocs.io/en/latest/gallery/gallery-with-nested-documents.html)
| <b>Quarto</b><br>[Documentation](https://quarto.org/) | - Cross-language Quarto markdown `.qmd` (which combines markdown and executable code)<br>-Jupyter notebook `.ipynb`<br>- Markdown `.md`<br>- R markdown `.Rmd`<br>[[source]](https://quarto.org/docs/projects/quarto-projects.html) | Explicitly supports dynamic content from Python, R, Julia and Observable [[source]](https://quarto.org/)<br>[Comparison with Rmd](https://quarto.org/docs/faq/rmarkdown.html) | Well supported natively<br>[Tutorial 1](https://quarto.org/docs/websites/website-blog.html) <br>[Tutorial 2](https://albert-rapp.de/posts/13_quarto_blog_writing_guide/13_quarto_blog_writing_guide.html)<br>[Tutorial 3](https://samanthacsik.github.io/posts/2022-10-24-quarto-blogs/) | [ddanieltan's blog](https://github.com/ddanieltan/ddanieltan.com)<br><br>Quarto's blog - [github](https://github.com/quarto-dev/quarto-web), [site](https://quarto.org/docs/blog/)<br><br>[R for Data Science](https://r4ds.hadley.nz/)<br><br>[Python for Data Analysis](https://wesmckinney.com/book/)<br><br>HSMA DES Book - [github](https://github.com/hsma-programme/hsma6_des_book), [site](https://hsma-programme.github.io/hsma6_des_book/) | Huge range of supported output formats [[source]](https://quarto.org/docs/output-formats/all-formats.html) |
| <b>Jekyll</b> | - Markdown `.md`<br>- HTML| Written in Ruby. Creates simple static sites. | | Exeter RSE Workshop - [github](https://github.com/UniExeterRSE/intro-version-control), [site](https://uniexeterrse.github.io/intro-version-control/)<br><br>[Ruby's website](https://www.ruby-lang.org/en/) |
| <b>Mkdocs</b><br>[Documentation](https://www.mkdocs.org/) | - Markdown `.md`<br>Seems possible for others but more designed for markdown? | Designed for Python | Yes with Material for Mkdocs [plugin](https://squidfunk.github.io/mkdocs-material/plugins/blog/) | Material for MkDocs - [github](https://github.com/squidfunk/mkdocs-material), [site](https://squidfunk.github.io/mkdocs-material/)<br><br>Cookiecutter Data Science - [github](https://github.com/drivendata/cookiecutter-data-science/tree/master), [site](http://drivendata.github.io/cookiecutter-data-science/) | [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) provides additional features
| <b>Bookdown</b><br>[Documentation](https://bookdown.org/) | - R Markdown `.Rmd` | Designed for R | | [R Markdown Definitive Guide](https://bookdown.org/yihui/rmarkdown/)<br><br>[R Markdown Cookbook](https://bookdown.org/yihui/rmarkdown-cookbook/) |
| <b>Blogdown</b><br>[Documentation](https://bookdown.org/yihui/blogdown/) | - R Markdown `.Rmd` | Designed for R | | [List of blogs](https://awesome-blogdown.com/) | Built on [Hugo](https://gohugo.io/) [[source]](https://bookdown.org/yihui/blogdown/hugo.html)
| <b>Hugodown</b><br>[Documentation](https://hugodown.r-lib.org/) | - R Markdown `.Rmd` | Designed for R | | [List of blogs](https://awesome-blogdown.com/) | Built on [Hugo](https://gohugo.io/)
| <b>Distill for R Markdown</b><br>[Documentation](https://rstudio.github.io/distill/) | - R Markdown `.Rmd`| Designed for R | Yes natively (eg. set up project as blog or website) | [Piping Hot Data](https://www.pipinghotdata.com/blog)<br><br>[Tidy models](https://www.tidymodels.org/learn/)<br><br>[Before I sleep](https://milesmcbain.xyz/)

[Reflections on RMarkdown, Distill, Bookdown and Blogdown](https://education.rstudio.com/blog/2021/02/distill-it-down/).

Paid: https://www.gitbook.com/pricing

Other random noted down options not explored:
* Sandpaper, pegboard and varnish - example: https://carpentries-lab.github.io/good-enough-practices/index.html
* Sweave/LaTeX RStudio/LaTeX Pandoc SageMath Colab Notebooks Nbconvert Pelican Org mode DocOnce Scribus Madoko Texinfo

## Quarto

Getting set up...
1. Install **Quarto** - https://quarto.org/docs/get-started/ - I downloaded the Linux deb file, then ran `sudo dpkg -i packagename.deb`
2. Create **environment** with necessary requirements (*this may not be a necessary step, but this is what I decided to do*) - for me, I needed:
```
ipykernel
pyyaml
nbformat
nbclient
```
3. Install Quarto **VS Code extension** (and then perhaps open and close VS Code)
4. Within VS Code, Ctrl+Shift+P > Quarto: **Create Project**
5. Ctrl+Shift+P > **Select Interpreter** > choose the environment created

Render full .qmd: `Ctrl+Shift+K`

Render file: `quarto render hello.qmd --to html`

Render to alt. output: `quarto render hello.qmd --to docx`

Run individual cells by selecting the **Run Cell** button.

You'll see there's a few Quarto projects that pop up -
* Basic
* Book
* Blog
* Manuscript
* Website

A book is actually a special type of website - the most important difference is that it uses chapter numbers and supports cross-references between different chapters. [[source]](https://quarto.org/docs/books/)

For a blog, the posts are in seperate pages as the filename has to be index.qmd.

To change preview type when using VSCode to preview, go to Settings > Quarto > Render: Preview Type and set to external

Commands to check/make/preview book:

* `quarto check` - checks if would build successfully
* `quarto preview` - previews as-is
* `quarto render` - rebuilds whole book
* quarto preview button in VS code - will render current page, and will render other pages when you click on them, except blog posts

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
