# Python

## Environments - conda
To see conda environments: `conda env list`  
To see packages in current environment: `conda list`  
To activate environment: `conda activate env_name`  
To create environment from yml file: `conda env create --name env_name --file environment.yml`  
To edit yml file from terminal: `nano environment.yml`  
To update current environment from yml file: `conda env update --file environment.yml --prune`  
To delete environment: deactivate then `conda remove -n env_name --all`  

## Jupyter lab
Install jupyterlab package.  
Where you want to open, in terminal, type `jupyter lab`  

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

## Linting
Install flake8 and nbqa packages.  
To lint file: `flake8 filename.py`  
To lint jupyter notebook: `nbqa flake8 filename.ipynb`  

## Streamlit
Install streamlit package.  
To run: `streamlit run main.py`  