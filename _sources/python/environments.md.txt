# Python environments

Python -
\begin{itemize}
    \item Conda, VirtualEnv, etc.
    \item Docker - to do development inside container, VSCode Dev Containers extension allows you to open folder inside container - \href{https://code.visualstudio.com/docs/devcontainers/containers}{source 1}
\end{itemize}

Poetry - you specify python version BUT you have to have it already
Venv - no python version
Conda - you specific python version and it gets it for you
Mamba - quicker version of conda
https://alpopkes.com/posts/python/packaging_tools/ 

## Conda

To see conda environments: `conda env list`  
To see packages in current environment: `conda list`  
To activate environment: `conda activate env_name`  
To create environment from yml file: `conda env create --name env_name --file environment.yml`  
To edit yml file from terminal: `nano environment.yml`  
To update current environment from yml file: `conda env update --file environment.yml --prune`  
To delete environment: deactivate then `conda remove -n env_name --all`  

## Virtualenv

### Virtualenvwrapper

Recommend using virtualenvwrapper so all your environments are stored in the same place, otherwise its easy to forget what you named it

1. `pip install virtualenvwrapper`
2. Go to Home
3. `nano .bashrc`
4. Add the following:
```
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
source /usr/local/bin/virtualenvwrapper.sh
```
5. Reload with `source ~/.bashrc`
6. Create environment with `mkvirtualenv env_name`. This will be located in home/.virtualenvs.
7. Environment activated with `workon env_name`
8. See list of all available environments with command `workon`
9. Delete environment - `rmvirtualenv env_name`

### Virtualenv
**WARNING: NEVER NAME YOUR ENVIRONMENT THE SAME AS YOUR FOLDER** - as the command for deleting the environment would delete the folder...!

Steps for setting up virtual environment:
1. If not already installed, `pip install virtualenv`
2. Create new environment: `virtualenv env_name`
3. Enter the environment: `source env_name/bin/activate`
4. Install requirements into environment: `pip install -r requirements.txt`
5. Update environment from requirements: `pip install -r requirements.txt --upgrade`
6. Delete environment: `deactivate` then `rm -r env_name` **be careful! will delete folder of same name!**
7. List packages in environment: `pip list`

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