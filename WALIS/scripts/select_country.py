query_type='country'
## From the dictionary in connection.py, extract the dataframes
rsl=walis_dict[0].copy()
countries=walis_dict[1].copy()
regions=walis_dict[2].copy()
MIS_ages=walis_dict[3].copy()
references=walis_dict[4].copy()
hrzpos=walis_dict[5].copy()
rslind=walis_dict[6].copy()
sldatum=walis_dict[7].copy()
vrt_meas=walis_dict[8].copy()
useries=walis_dict[9].copy()
aar=walis_dict[10].copy()
luminescence=walis_dict[11].copy()
esr=walis_dict[12].copy()
strat=walis_dict[13].copy()
other=walis_dict[14].copy()
user=walis_dict[15].copy()
Summary=walis_dict[18].copy()

# Define which datasets need to be assigned nation 
RSL_Datapoints = rsl.copy()
useries_df=useries.copy() 

#Assign nations to points via reverse geocoding offline
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
gdf = geopandas.GeoDataFrame(rsl,geometry=geopandas.points_from_xy(rsl.RSLlon, rsl.RSLlat))
rsl_location = geopandas.sjoin_nearest(gdf, world, how='left').drop(columns=['index_right','pop_est','iso_a3','gdp_md_est'])

gdf = geopandas.GeoDataFrame(useries,geometry=geopandas.points_from_xy(useries.SampleLon, useries.SampleLat))
useries_location=geopandas.sjoin_nearest(gdf, world, how='left').drop(columns=['index_right','pop_est','iso_a3','gdp_md_est']) 

gdf = geopandas.GeoDataFrame(Summary,geometry=geopandas.points_from_xy(Summary.Longitude,Summary.Latitude))
Summary_location=geopandas.sjoin_nearest(gdf, world, how='left').drop(columns=['index_right','pop_est','iso_a3','gdp_md_est']) 

# Make list of nations with data
df1=useries_location['name']
df2=rsl_location['name']

frames = [df1, df2]
nations = pd.concat(frames)
nations.drop_duplicates(inplace=True)

select_country = widgets.SelectMultiple(
    options=sorted(nations),
    rows=15,
    columns=3,
    disabled=False)