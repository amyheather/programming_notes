# Python

## Markdown
Add image with text alongside it: `<img align='left' src='image file path' alt='alt_name' width='900'> Text alongside image `

## Environments - conda
To see conda environments: `conda env list`  
To see packages in current environment: `conda list`  
To activate environment: `conda activate env_name`  
To create environment from yml file: `conda env create --name env_name --file environment.yml`  
To edit yml file from terminal: `nano environment.yml`  
To update current environment from yml file: `conda env update --file environment.yml --prune`  
To delete environment: deactivate then `conda remove -n env_name --all`  

## Environments - pip, venv, requirements.txt

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

## Package

https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/
* Make setup.py - if you read from requirements for it, will need to make MANIFEST.in file which includes the line `include requirements.txt`
* `python setup.py check`
* `python setup.py sdist bdist_wheel`
* `pip install twine`
* `twine upload --repository-url https://test.pypi.org/legacy/ dist/*`
* When want to update package:
    * Delete dist folder
    * `python setup.py sdist bdist_wheel`
    * `twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/*`
* Above uses test pypi URL - for real pypi upload, use `https://upload.pypi.org/legacy/`
* To install the package locally (rather than from pypi) using your requirements.txt file, if for example it was in a sister directory, add to the text file `../foldername/dist/filename.whl`
* If you are simultaneously working on the package and other code - so if you want to be getting live changes to the package rather than having to rebuild and reinstall the package each time - use `pip install -e /path/to/repo/` - this will use a symbolic link to the repository meaning any changes to the code will also be automatically reflected. For example, when its in a sister directory, `pip install -e ../kailo_beewell_dashboard_package`. You can also do this from your **requirements.txt** by adding `-e ../packagefolder`. If the package was already in your environment, you'll need to delete it, and make just delete and remake the environment

## Package documentation using Sphinx

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

## Using VS Code  
To open VS Code from terminal: `code .`  
To activate conda environment in VS Code: Ctrl+Shift+P > Python Interpreter, then select correct environment  
To view/create settings.json in .vscode folder: Ctrl+Shift+P > Preferences: Open Workspace Settings (JSON)  

## Type hinting in VS Code with Pylance  
Extension > Pylance should be installed  
In settings.json, set `"python.analysis.typeCheckingMode": "strict"` or to `"None"` or `"basic"` 

## Violin plot
```
df = data.groupby('quarter_year')['stroke_severity'].agg(lambda x: list(x))
fig, ax = plt.subplots()
ax.violinplot(df)
ax.set_xticks(np.arange(1, len(df.index)+1), labels=df.index)
plt.show()
```

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

To set this up to just run from the command `book`:
* `cd` to go to top of directory (i.e. above documents)
* `nano .bashrc`
* At bottom of file, add `alias book="jupyter-book build ./ && ghp-import -n -p -f _build/html"`, then save the file
* Run `source .bashrc` to refresh
* Then, when you want to recreate the jupyter book and push to GH pages, go to where the book is (i.e. where build and config is) and run `book`
* Also set up config file if desired to execute pages `off` if don't want to re-run all the notebooks each time


## Comparing two dataframes
Simple check if match: `df1.equals(df2)`
Drop duplicate columns: `pd.concat([df1, df2]).drop_duplicates(keep=False)`

## Linting
Install flake8 and nbqa packages.  
To lint file: `flake8 filename.py`  
To lint jupyter notebook: `nbqa flake8 filename.ipynb`  
To lint within notebook: `%load_ext pycodestyle_magic` and `%pycodestyle_on`

## Compare dataframes
True/False of difference (note: sometimes False but no actual difference - then try assertion below)
```
df1.equals(df2)
```
Show differences between them
```
df1.compare(df2)
```
Get feedback on exactly what is missing
```
from pandas.testing import assert_frame_equal
assert_frame_equal(df1, df2)
```

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

## Colour scales

```  
'''
Helper functions for creating discrete colour scale sampling in the
continuous scale between two provided colours.
Source: https://bsouthga.dev/posts/color-gradients-with-python
Directly copied from that webpage, all credit to them.
'''

def hex_to_RGB(hex):
  ''' "#FFFFFF" -> [255,255,255] '''
  # Pass 16 to the integer function for change of base
  return [int(hex[i:i+2], 16) for i in range(1,6,2)]

def RGB_to_hex(RGB):
  ''' [255,255,255] -> "#FFFFFF" '''
  # Components need to be integers for hex to make sense
  RGB = [int(x) for x in RGB]
  return "#"+"".join(["0{0:x}".format(v) if v < 16 else
            "{0:x}".format(v) for v in RGB])

def color_dict(gradient):
  ''' Takes in a list of RGB sub-lists and returns dictionary of
    colors in RGB and hex form for use in a graphing function
    defined later on '''
  return {"hex":[RGB_to_hex(RGB) for RGB in gradient],
      "r":[RGB[0] for RGB in gradient],
      "g":[RGB[1] for RGB in gradient],
      "b":[RGB[2] for RGB in gradient]}

def linear_gradient(start_hex, finish_hex="#FFFFFF", n=10):
  ''' returns a gradient list of (n) colors between
    two hex colors. start_hex and finish_hex
    should be the full six-digit color string,
    inlcuding the number sign ("#FFFFFF") '''
  # Starting and ending colors in RGB form
  s = hex_to_RGB(start_hex)
  f = hex_to_RGB(finish_hex)
  # Initilize a list of the output colors with the starting color
  RGB_list = [s]
  # Calcuate a color at each evenly spaced value of t from 1 to n
  for t in range(1, n):
    # Interpolate RGB vector for color at the current value of t
    curr_vector = [
      int(s[j] + (float(t)/(n-1))*(f[j]-s[j]))
      for j in range(3)
    ]
    # Add it to our list of output colors
    RGB_list.append(curr_vector)

  return color_dict(RGB_list)
```  

### Save HTML to csv and then import again and convert to PDF (this is not ideal tbh)
```
import weasyprint
import csv

with open("out.csv", "w", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([html_content])

with open("out.csv", "r") as csv_file:
    csv_text = csv_file.readlines()

html_check = ''.join(csv_text)[1:-1]
weasyprint.HTML(string=html_check).write_pdf('report/report.pdf')
```