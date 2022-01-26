if sel.value == 'RSL datapoints':
 map_data = Summary.copy()
 map_data.drop_duplicates(subset=['WALIS_ID'],inplace=True)
 map_data = geopandas.GeoDataFrame(map_data, geometry=geopandas.points_from_xy(map_data.Longitude, map_data.Latitude))

if sel.value == 'U-series (corals)':
 map_data = useries_corals.copy()
 map_data = geopandas.GeoDataFrame(map_data, 
                                   geometry=geopandas.points_from_xy(map_data['Longitude (decimal degrees)'].astype(float),
                                                                     map_data['Latitude (decimal degrees)'].astype(float)))

if sel.value == 'U-series (oolites)':
 map_data = useries_oolite.copy()
 map_data = geopandas.GeoDataFrame(map_data, 
                                   geometry=geopandas.points_from_xy(map_data['Longitude (decimal degrees)'].astype(float),
                                                                     map_data['Latitude (decimal degrees)'].astype(float)))


if sel.value == 'U-series (speleothems)':
 map_data = useries_speleo.copy()
 map_data = geopandas.GeoDataFrame(map_data, 
                                   geometry=geopandas.points_from_xy(map_data['Longitude (decimal degrees)'].astype(float),
                                                                     map_data['Latitude (decimal degrees)'].astype(float)))

if sel.value == 'U-series (mollusks)':
 map_data = useries_moll.copy()
 map_data = geopandas.GeoDataFrame(map_data, 
                                   geometry=geopandas.points_from_xy(map_data['Longitude (decimal degrees)'].astype(float),
                                                                     map_data['Latitude (decimal degrees)'].astype(float)))

if sel.value == 'AAR':
 map_data = aar.copy()
 map_data = geopandas.GeoDataFrame(map_data, 
                                   geometry=geopandas.points_from_xy(map_data['Longitude (decimal degrees)'].astype(float),
                                                                     map_data['Latitude (decimal degrees)'].astype(float)))

if sel.value == 'Luminescence':
 map_data = lum.copy()
 map_data = geopandas.GeoDataFrame(map_data, 
                                   geometry=geopandas.points_from_xy(map_data['Sample longitude (decimal degrees)'].astype(float),
                                                                     map_data['Sample latitude (decimal degrees)'].astype(float)))

if sel.value == 'ESR':
 map_data = esr.copy()
 map_data = geopandas.GeoDataFrame(map_data, 
                                   geometry=geopandas.points_from_xy(map_data['Longitude (decimal degrees)'].astype(float),
                                                                     map_data['Latitude (decimal degrees)'].astype(float)))

if sel.value == 'Stratigraphy':
 map_data = map_strat.copy()
 map_data = geopandas.GeoDataFrame(map_data, 
                                   geometry=geopandas.points_from_xy(map_data['Longitude (decimal degrees)'].astype(float),
                                                                     map_data['Latitude (decimal degrees)'].astype(float)))

if sel.value == 'Other dating':
 map_data = map_other.copy()
 map_data = geopandas.GeoDataFrame(map_data, 
                                   geometry=geopandas.points_from_xy(map_data['Longitude (decimal degrees)'].astype(float),
                                                                     map_data['Latitude (decimal degrees)'].astype(float)))


map_data = map_data.set_crs('EPSG:4326')

fig, ax = plt.subplots(figsize=(15,10), subplot_kw={'projection': ccrs.crs.Robinson()})
ax.set_title(sel.value,fontsize=12)

if choice.value == 'yes':
 ax.set_global()

plt.text(0, -0.02,'Made with Natural Earth. Free vector and raster map data @naturalearthdata.com.',
     horizontalalignment='left',
     verticalalignment='center',
     transform = ax.transAxes,
    fontsize=8)

#Project and plot the points on the map
map_data = map_data.to_crs('ESRI:54030')

if sel_display.value == 'Highlight':
 map_data.plot(ax=ax,
               markersize=100,
               marker='o',
               c='yellow')
else:
 map_data.plot(ax=ax,
               markersize=150,
               marker='o',
               c='white',edgecolor='k')
    
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.LAKES, alpha=0.5)
ax.add_feature(cfeature.RIVERS)

filename1='Output/Images/svg/'+str(sel.value)+'.svg'
filename2='Output/Images/jpg/'+str(sel.value)+'.jpg'
plt.savefig(filename1, dpi=300)
plt.savefig(filename2, dpi=300)
plt.show()