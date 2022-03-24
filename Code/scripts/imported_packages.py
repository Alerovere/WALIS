#Main packages
import pandas as pd
import pandas.io.sql as psql
import geopandas
import pygeos
import numpy as np
import mysql.connector
from datetime import date
import xlsxwriter as writer
import math
from scipy import optimize
from scipy import stats

#Plots
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

#Jupyter data display
import tqdm
from tqdm.notebook import tqdm_notebook
from IPython.display import *
import ipywidgets as widgets
from ipywidgets import *

#Geographic 
from shapely.geometry import Point
from shapely.geometry import box
import cartopy as ccrs
import cartopy.feature as cfeature

#System
import os
import glob
import shutil

#pandas options for debugging
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#Set a date string for exported file names
date=date.today()
dt_string = date.strftime("_%d_%m_%Y")

# Ignore warnings
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings('ignore')