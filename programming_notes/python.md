# Python

## Environments - conda
To see conda environments: `conda env list`  
To see packages in current environment: `conda list`  
To activate environment: `conda activate env_name`  
To create environment from yml file: `conda env create --name env_name --file environment.yml`  
To edit yml file from terminal: `nano environment.yml`  
To update current environment from yml file: `conda env update --file environment.yml --prune`  

## Jupyter lab
Install jupyterlab package.  
Where you want to open, in terminal, type `jupyter lab`  

## Jupyter book
Install jupyter-book package.  
To create sample book stored in current location: `jupyter-book create book_name/`  
To build/rebuild book: `jupyter-book build book_name`  

## Linting
Install flake8 and nbqa packages.  
To lint file: `flake8 filename.py`  
To lint jupyter notebook: `nbqa flake8 filename.ipynb`  

## Streamlit
Install streamlit package.  
To run: `streamlit run main.py`  