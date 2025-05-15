# Counting lines

Script to count lines of code - run with `bash count_reproduction_lines.sh`...

```{.bash}
# Install cloc if not already on machine
# e.g. sudo apt-get install cloc

# This script assumes copies of these folders are stored in the current folder

#!/bin/bash

# List of repository folders
repos=(
  stars-reproduce-shoaib-2022
  stars-reproduce-huang-2019
  stars-reproduce-lim-2020
  stars-reproduce-kim-2021
  stars-reproduce-anagnostou-2022
  stars-reproduce-johnson-2021
  stars-reproduce-hernandez-2015
  stars-reproduce-wood-2021
)

# Output files
orig_output="cloc_original_studies.txt"
repro_output="cloc_reproductions.txt"

# Empty the output files if they exist
> "$orig_output"
> "$repro_output"

for repo in "${repos[@]}"; do
  # Original study
  echo "$repo" >> "$orig_output"
  cloc "$repo/original_study" >> "$orig_output"
  echo "" >> "$orig_output"

  # Reproduction
  echo "$repo" >> "$repro_output"
  cloc "$repo/reproduction" >> "$repro_output"
  echo "" >> "$repro_output"
done
```

Example output...

```
stars-reproduce-shoaib-2022
github.com/AlDanial/cloc v 1.98  T=0.02 s (1341.8 files/s, 557050.6 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Python                           4            220            342           1487
Jupyter Notebook                 8              0           7978            860
Markdown                         2             73              9            132
CSV                             10              0              0             39
YAML                             1              0              0             22
Bourne Shell                     1              3              6             11
Dockerfile                       1              8             10              9
-------------------------------------------------------------------------------
SUM:                            27            304           8345           2560
-------------------------------------------------------------------------------
stars-reproduce-huang-2019
github.com/AlDanial/cloc v 1.98  T=0.04 s (2818.8 files/s, 324900.0 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
HTML                            13            404             23           5089
R                               15            746            485           1884
Markdown                         3            642              0           1439
CSV                             31              0              0            569
YAML                             1             45              0            320
CSS                              1             24              0            106
Rmd                             11            486           1217             80
JSON                            38              0              0             74
Dockerfile                       1              9             14             28
Bourne Shell                     2              4              0             11
DOS Batch                        2              5              0             11
SVG                              1              0              0              1
-------------------------------------------------------------------------------
SUM:                           119           2365           1739           9612
-------------------------------------------------------------------------------
stars-reproduce-lim-2020
github.com/AlDanial/cloc v 1.98  T=0.04 s (568.7 files/s, 1005060.2 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
CSV                             14              0              0          34214
Jupyter Notebook                 1              0           1791            498
Python                           3             63            177            176
Markdown                         1             54              0             96
Dockerfile                       1              9             11             15
YAML                             1              0              0             12
-------------------------------------------------------------------------------
SUM:                            21            126           1979          35011
-------------------------------------------------------------------------------
stars-reproduce-kim-2021
github.com/AlDanial/cloc v 1.98  T=0.05 s (3184.0 files/s, 494794.3 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
R                               27           1740           1652           8039
HTML                            13            404             23           5089
CSV                             60              5              0           1683
Markdown                         2            583              4           1314
Rmd                             12            616           1467            377
YAML                             1             45              0            320
CSS                              1             24              0            106
JSON                            30              0              0             48
Dockerfile                       1              9             12             29
Bourne Shell                     2              4              0             11
DOS Batch                        2              5              0             11
SVG                              1              0              0              1
-------------------------------------------------------------------------------
SUM:                           152           3435           3158          17028
-------------------------------------------------------------------------------
stars-reproduce-anagnostou-2022
github.com/AlDanial/cloc v 1.98  T=0.01 s (1388.7 files/s, 188533.7 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Python                           9            282            439            916
Markdown                         1             48              0             88
Jupyter Notebook                 1              0            380             79
CSV                              4              0              0             36
YAML                             1              0              0             13
Dockerfile                       1              8             10              9
-------------------------------------------------------------------------------
SUM:                            17            338            829           1141
-------------------------------------------------------------------------------
stars-reproduce-johnson-2021
github.com/AlDanial/cloc v 1.98  T=0.15 s (2030.0 files/s, 585056.1 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
CSV                            163             17              0          34817
Rmd                             29           5999           4515          17220
Markdown                        21           2568              0           6140
HTML                            19            404             23           5859
R                               30           1882            891           4636
C++                              2            915            413           2978
YAML                             2             46              1            323
CSS                              1             24              0            106
JSON                            39              0              0             57
Dockerfile                       1              9             14             30
Bourne Shell                     2              4              0             11
DOS Batch                        2              5              0             11
SVG                              1              0              0              1
-------------------------------------------------------------------------------
SUM:                           312          11873           5857          72189
-------------------------------------------------------------------------------
stars-reproduce-hernandez-2015
github.com/AlDanial/cloc v 1.98  T=0.04 s (2701.0 files/s, 416118.8 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
HTML                            13            404             23           5089
Text                            38              0              0           2361
Python                          23            509            793           1730
R                               11            669            368           1575
Markdown                         3            598              0           1343
YAML                             2             45              0            335
Rmd                             12            568           1337            211
CSV                              6              5              0            129
CSS                              1             24              0            106
Dockerfile                       1              7              8             42
JSON                             4              0              0             22
Bourne Shell                     2              4              0             11
DOS Batch                        2              5              0             11
SVG                              1              0              0              1
-------------------------------------------------------------------------------
SUM:                           119           2838           2529          12966
-------------------------------------------------------------------------------
stars-reproduce-wood-2021
github.com/AlDanial/cloc v 1.98  T=0.23 s (418.8 files/s, 901826.0 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
CSV                             25              0              0         195648
HTML                            13            404             23           5089
R                               17            784            441           2215
Markdown                         2            579              0           1297
YAML                             1             45              0            320
CSS                              1             24              0            106
Rmd                             11            486           1217             80
Dockerfile                       1              9             14             29
Text                            20              0              0             20
JSON                             1              0              0             19
Bourne Shell                     2              4              0             11
DOS Batch                        2              5              0             11
SVG                              1              0              0              1
-------------------------------------------------------------------------------
SUM:                            97           2340           1695         204846
-------------------------------------------------------------------------------
```