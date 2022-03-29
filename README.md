# WALIS - The World Atlas of Last Interglacial Shorelines

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5979520.svg)](https://doi.org/10.5281/zenodo.5979520)

This is the repository for the World Atlas of Last Interglacial Shorelines (WALIS). It contains the full database in various formats, and python scripts and Jupyter notebooks to download, query and analyse the data included in the Atlas.

Find more information on the project [here](https://alerovere.github.io/WALIS/)

# Other repositories
Visualization - [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4943541.svg)](https://doi.org/10.5281/zenodo.4943541)

ReadTheDocs - [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3961544.svg)](https://doi.org/10.5281/zenodo.3961544)

# WALIS in GitHub

The notebooks are stored in the root (/WALIS). Within the root, there are three sub-folders, as listed below.

1. **Output** This folder stores the files exported by the notebooks. The **/data** subfolder contains the database in various formats.
2. **scripts** This folder stores all the python scripts called by the notebooks.
3. **Conda_env** In this folder are stored two files: _requirements.txt_ _and WALIS_env.yml_ that can be used to download the python packages required to run the scripts and creating the Conda environment.

### Jupyter Notebooks
#### Query and explore data
This notebook contains scripts that allow querying and extracting data from the "World Atlas of Last Interglacial Shorelines" (WALIS) database. The notebook calls scripts contained in the /scripts folder. After downloading the database (internet connection required), field headers are renamed, and field values are substituted, following 1:n or n:n relationships. The tables composing the database are then saved in CSV, XLSS (multi-sheet), and geoJSON formats. The notebook also contains some plotting functions.
#### Export data for ShinyAppp
This notebook contains the scripts to download the full WALIS database and prepare a CSV file for the R Shiny App hosted [here](https://warmcoasts.shinyapps.io/WALIS_Visualization/). 

### Funding
This software is part of a project that has received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (Grant agreement No. ERC-StG-802414)
