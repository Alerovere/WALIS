<script src="https://kit.fontawesome.com/f4ba202135.js" crossorigin="anonymous"></script>

This is the public repository page for the World Atlas of Last Interglacial Shorelines (WALIS). It contains python scripts and Jupyter notebooks to download, query and analyse the data included in the Atlas. WALIS is part of the [WARMCOASTS project](www.warmcoasts.eu), funded by the European Research Council. WALIS is compiled in collaboration with PALSEA (a PAGES-INQUA working group).

WALIS aims at collecting existing and new data on Last Interglacial sea-level indicators reviewed following a standardized template, that can be filled using an online interface.

# How does it work? <link rel="icon" href="http://[percorso]/favicon.ico"/>
1. **Contribute data**. Geoscientists wishing to contribute data should register to our interface. This will allow them to use an intuitive interface to insert both published and new sea level indicators, ages and metadata. During the compilation process, data remain private and are accessible only by the registered user. This is done to allow registered users to keep inserting and modifying data points until they are ready for publication. Registration to the system is (and will always be) free.
2. **Data publication**. WALIS aims to make Last Interglacial sea level data open-access and readily available. Data creators are encouraged, once their work is finalized, to submit their data to a repository under a CC BY license, and give it a DOI. To this purpose, we set up a [Zenodo Repository](https://zenodo.org/communities/walis_database/). Users are free to decide to submit to another open-access repository and let us know writing to alessio.rovere@unive.it
3. **Download WALIS data**. Once the data inserted by a data creator has been assigned a DOI from an open-access repository, it can be downloaded and re-used freely (complying with the simple rules at the bottom of this page). 
4. **Periodical database collations**. Periodically, WALIS data will be collated into a single release, containing all the data that were assigned a DOI up to the release date. The release will contain WALIS data in different formats, as well as scripts to query the database. The first release is planned to coincide with the closing of an ongoing Special Issue in the journal Earth System Science Data. 

# Download data <i class="fa-solid fa-cloud-arrow-down"></i>
The data in WALIS is organized in a [Zenodo Community](https://zenodo.org/communities/walis_database/). A series of manuscripts in a Special Issue of the journal [Earth System Science Data](https://essd.copernicus.org/articles/special_issue1055.html)
 describes each region included in the database. The database is also included in this GitHub repository.
 
# Contribute


### Folders
The notebooks are stored in the root (/WALIS). Within the root, there are three sub-folders, as listed below.

1. **Output** This folder stores the files exported by the notebooks. The **/data** subfolder contains the database in various formats.
2. **scripts** This folder stores all the python scripts called by the notebooks.
3. **Conda_env** In this folder are stored two files: _requirements.txt_ _and WALIS_env.yml_ that can be used to download the python packages required to run the scripts and creating the Conda environment.

### Jupyter Notebooks
#### Query and explore data
This notebook contains scripts that allow querying and extracting data from the "World Atlas of Last Interglacial Shorelines" (WALIS) database. The notebook calls scripts contained in the /scripts folder. After downloading the database (internet connection required), field headers are renamed, and field values are substituted, following 1:n or n:n relationships. The tables composing the database are then saved in CSV, XLSS (multi-sheet), and geoJSON formats. The notebook also contains some plotting functions.
#### Export data for ShinyAppp
This notebook contains the scripts to download the full WALIS database and prepare a CSV file for the R Shiny App hosted [here](https://warmcoasts.shinyapps.io/WALIS_Visualization/). 

## Other WALIS resources
We maintain a repository with the scripts for a [visualization interface](https://github.com/Alerovere/WALIS_Visualization) for WALIS data, coded in R. Field descriptors for the WALIS database are available in a [ReadTheDocs](https://walis-help.readthedocs.io) webpage.
These are also deposited in Zenodo:

Garzón and Rovere (2021) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4943541.svg)](https://doi.org/10.5281/zenodo.4943541)

Rovere et al. (2020) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3961544.svg)](https://doi.org/10.5281/zenodo.3961544)

### Suggested acknowledgments
WALIS is the result of the work of several people, within different projects. For this reason, we kindly ask you to follow these simple rules to properly acknowledge those who worked on it:

1. Cite the original authors - Please maintain the original citations for each datapoint, to give proper credit to those who worked to collect the original data in the field or in the lab.
2. Acknowledge the database contributor - The name of each contributor is listed in all public datapoints. This is the data creator, who spent time to make sure the data is standardized and (as much as possible) free of errors.
3. Acknowledge the database structure and interface creators - The database template used in this study was developed by the ERC Starting Grant "WARMCOASTS" (ERC-StG-802414) and is a community effort under the PALSEA (PAGES / INQUA) working group.

Example of acknowledgments: The data used in this study were *extracted from / compiled in* WALIS, a sea-level database interface developed by the ERC Starting Grant "WARMCOASTS" (ERC-StG-802414), in collaboration with PALSEA (PAGES / INQUA) working group. The database structure was designed by A. Rovere, D. Ryan, T. Lorscheid, A. Dutton, P. Chutcharavan, D. Brill, N. Jankowski, D. Mueller, M. Bartz, E. Gowan and K. Cohen. The data points used in this study were contributed to WALIS by *list names of contributors here*.

### Funding
This software is part of a project that has received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (Grant agreement No. ERC-StG-802414)

[![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/walisdatabase.svg?style=social&label=Follow%20%40walisdatabase)](https://twitter.com/walisdatabase)

![logo](./img/ERC.png)
