# Quarto

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

## `stlite`

Sammi mentioned that the stlite quarto extension can be a nice way of including simple interactivity in quarto books to demonstrate concepts.

Using this extension: https://github.com/whitphx/quarto-stlite

Though she flagged that it would say matplotlib was not installed when it was, and the answer was:

> `import matplotlib.pyplot as plt` = bad
> `from matplotlib import pyplot as plt` = good

And likewise with other imports (e.g. needing `from plotly import express as px`).

She used to fix the broken embedded streamlit apps in the streamlit HSMA book (https://webapps.hsma.co.uk/).

From Sammi: There's basically two subtly different versions of each example in my streamlit book - the standard streamlit code shown to the user, and the one that actually renders the embedded app.

Main changes tend to be:

* import micropip
* install any packages that aren't in there by default with await micropip.install("some_package")
  * there are a few limitations around certain packages not being installable due to not having pure python requirements or wheels available, but that list seems to be getting smaller over time
* import (mostly) as normal (today's issue excluded :joy: )
* if you need to reference an external file, I've had some issues with it accessing my usual options (files stored in a github repo, dropbox, google drive)
  * I've ended up resorting to a free site called https://catbox.moe/ as it was the only one that didn't seem to run into security issues - not ideal and I will eventually get around to checking whether the issue that was previously preventing me using other options are still present

They're scattered throughout this book but there's a few on this page, with the last one having a dropdown to properly demonstrate the interactivity: https://webapps.hsma.co.uk/interactive_charts.html