# General Python Stuff

## Jupyter notebook merge conflicts

```
pip install nbdime
nbdime config-git --enable --global
git merge branchname
```

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