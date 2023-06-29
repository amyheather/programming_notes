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
To lint within notebook: `%load_ext pycodestyle_magic` and `%pycodestyle_on`

## Unit testing
Note: unit testing is typically for testing function outputs - so although the code below works, you wouldn't typically write unit tests for this purpose.

Example:
```
import numpy as np
import os
import pandas as pd
import unittest

class DataTests(unittest.TestCase):
    '''Class for running unit tests'''

    # Run set up once for whole class
    @classmethod
    def setUpClass(self):
        '''Set up - runs prior to each test'''
        # Paths and filenames
        raw_path: str = './data'
        raw_filename: str = 'SAMueL ssnap extract v2.csv'
        clean_path: str = './output'
        clean_filename: str = 'reformatted_data.csv'
        # Import dataframes
        raw_data = pd.read_csv(os.path.join(raw_path, raw_filename),
                               low_memory=False)
        clean_data = pd.read_csv(os.path.join(clean_path, clean_filename),
                                 low_memory=False)
        # Save to DataTests class
        self.raw = raw_data
        self.clean = clean_data

    def freq(self, raw_col, raw_val, clean_col, clean_val):
        '''
        Test that the frequency of a value in the raw data is same as
        the frequency of a value in the cleaned data
        Inputs:
        - self
        - raw_col and clean_col = string
        - raw_val and clean_val = string, number, or list
        Performs assertEqual test.
        '''
        # If values are not lists, convert to lists
        if type(raw_val) != list:
            raw_val = [raw_val]
        if type(clean_val) != list:
            clean_val = [clean_val]
        # Find frequencies and check if equal
        raw_freq = (self.raw[raw_col].isin(raw_val).values).sum()
        clean_freq = (self.clean[clean_col].isin(clean_val).values).sum()
        self.assertEqual(raw_freq, clean_freq)

    def time_neg(self, time_column):
        '''
        Function for testing that times are not negative when expected
        to be positive.
        Input: time_column = string, column with times
        '''
        self.assertEqual(sum(self.clean[time_column] < 0), 0)

    def equal_array(self, df, col, exp_array):
        '''
        Function to check that the only possible values in a column are
        those provided by exp_array.
        Inputs:
        - df = dataframe (raw or clean)
        - col = string (column name)
        - exp_array = array (expected values for column)
        '''
        # Sorted so that array order does not matter
        self.assertEqual(sorted(df[col].unique()), sorted(exp_array))

    def test_raw_shape(self):
        '''Test the raw dataframe shape is as expected'''
        self.assertEqual(self.raw.shape, (360381, 83))
        
    def test_id(self):
        '''Test that ID numbers are all unique'''
        self.assertEqual(len(self.clean.id.unique()),
                         len(self.clean.index))

    def test_onset(self):
        '''Test that onset_known is equal to precise + best estimate'''
        self.freq('S1OnsetTimeType', ['P', 'BE'], 'onset_known', 1)
        self.freq('S1OnsetTimeType', 'NK', 'onset_known', 0)
        
    def test_time_negative(self):
        '''Test that times are not negative when expected to be positive'''
        time_col = ['onset_to_arrival_time',
                    'call_to_ambulance_arrival_time',
                    'ambulance_on_scene_time',
                    'ambulance_travel_to_hospital_time',
                    'ambulance_wait_time_at_hospital',
                    'scan_to_thrombolysis_time',
                    'arrival_to_thrombectomy_time']
        for col in time_col:
            with self.subTest(msg=col):
                self.time_neg(col)

    def test_no_ambulance(self):
        '''
        Test that people who do not arrive by ambulance therefore have
        no ambulance times
        '''
        amb_neg = self.clean[(self.clean['arrive_by_ambulance'] == 0) & (
            (self.clean['call_to_ambulance_arrival_time'].notnull()) |
            (self.clean['ambulance_on_scene_time'].notnull()) |
            (self.clean['ambulance_travel_to_hospital_time'].notnull()) |
            (self.clean['ambulance_wait_time_at_hospital'].notnull()))]
        self.assertEqual(len(amb_neg.index), 0)



if __name__ == '__main__':
    unittest.main()

```

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