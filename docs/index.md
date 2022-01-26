# WALIS

This is the public repository page for the World Atlas of Last Interglacial Shorelines (WALIS). It contains python scripts and Jupyter notebooks to download, query and analyse the data included in the Atlas. More information on the project can be found at [this page](https://warmcoasts.eu/world-atlas).

## Data
The data in WALIS is organized in a [Zenodo Community](https://zenodo.org/communities/walis_database/). A series of manuscripts in a Special Issue of the journal [Earth System Science Data](https://essd.copernicus.org/articles/special_issue1055.html)
 describes each region included in the database.
 
## Repository organization
The notebooks are stored in the root (/WALIS). Within the root, there are three su-folders, as listed below.

**Output.** This folder stores the files exported by the notebooks. The **/data** subfolder contains the database in various formats.

**scripts.** This folder stores all the python scripts called by the notebooks.

**Conda_env.** In this folder are stored two files: _requirements.txt_ _and WALIS_env.yml_ that can be used to download the python packages required to run the scripts and creating the Conda environment.


## Other useful resources
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


![logo](./img/ERC.png)
