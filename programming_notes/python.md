# Python

## Environments - conda
To see conda environments: `conda env list`  
To see packages in current environment: `conda list`  
To activate environment: `conda activate env_name`  
To create environment from yml file: `conda env create --name env_name --file environment.yml`  
To edit yml file from terminal: `nano environment.yml`  
To update current environment from yml file: `conda env update --file environment.yml --prune`  
To delete environment: deactivate then `conda remove -n env_name --all`  

## Using VS Code  
To open VS Code from terminal: `code .`  
To activate conda environment in VS Code: Ctrl+Shift+P > Python Interpreter, then select correct environment  
To view/create settings.json in .vscode folder: Ctrl+Shift+P > Preferences: Open Workspace Settings (JSON)  

## Type hinting in VS Code with Pylance  
Extension > Pylance should be installed  
In settings.json, set `"python.analysis.typeCheckingMode": "strict"` or to `"None"` or `"basic"`   

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

## Docker  
Successfully installed docker on Ubuntu using following instructions: https://docs.docker.com/engine/install/ubuntu/  

Will need requirements.txt file. To create this from conda environment (with pip install in that environment and environment activated): `pip list --format=freeze > requirements.txt` (although may not have identifical packages - pip may have fewer). There is a simpler command of `pip freeze > requirements.txt` but I found that gave odd path references.  

To create dockerfile:  
* `touch Dockerfile`  
* `nano Dockerfile`  
```
# kailo_dashboards/Dockerfile

FROM python:3.10-slim

WORKDIR /kailo_dashboards

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--se>
```  

Explanation of Dockerfile:  
* FROM - sets base image, various possible - https://hub.docker.com/_/python  
* WORKDIR - sets working directory  
* RUN apt-get... to install git  
* COPY . . to get copy of all app files. If it was in a public GitHub repo, you could do `RUN git clone https://github.com/amyheather/kailo_area_dashboard .`, and if it was in a private repo, you could use SSH  
* Install dependencies from requirements.txt  
* EXPOSE - informs Docker that the container listens on the specified network ports at runtime. For streamlit, Your container needs to listen to Streamlit’s (default) port 8501  
* HEALTHCHECK - tells Docker how to test a container to check that it is still working. Your container needs to listen to Streamlit’s (default) port 8501  
* ENTRYPOINT - allows you to configure a container that will run as an executable. Here, it also contains the entire streamlit run command for your app, so you don’t have to call it from the command line  

To set up docker:  
* `sudo docker build -t streamlit .` to build an image from the Dockerfile. -t is used to tag the file, here tagged as streamlit. Can see streamlit image under repository column if run `sudo docker images`  