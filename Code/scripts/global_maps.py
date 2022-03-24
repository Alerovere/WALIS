rsl_data = Summary.copy()
rsl_data.drop_duplicates(subset=['WALIS_ID'],inplace=True)
rsl_data = geopandas.GeoDataFrame(rsl_data, geometry=geopandas.points_from_xy(map_data.Longitude, map_data.Latitude))

coral_rsl=rsl_data.loc[(rsl_data['Type of datapoint'] == 'Sea Level Indicator') & (rsl_data['RSL Indicator'] == 'Single Coral')]
speleo_rsl=rsl_data.loc[(rsl_data['Type of datapoint'] == 'Sea Level Indicator') & (rsl_data['RSL Indicator'] == 'Single Speleothem')]
MLI=rsl_data.loc[(rsl_data['Type of datapoint'] == 'Marine Limiting')]
TLI=rsl_data.loc[(rsl_data['Type of datapoint'] == 'Terrestrial Limiting')]
SLI=rsl_data.loc[(rsl_data['Type of datapoint'] == 'Sea Level Indicator') & (rsl_data['RSL Indicator'] != 'Single Coral') & (rsl_data['RSL Indicator'] != 'Single Speleothem')]

#set CRS
coral_rsl = coral_rsl.set_crs('EPSG:4326')
speleo_rsl = speleo_rsl.set_crs('EPSG:4326')
MLI = MLI.set_crs('EPSG:4326')
TLI = TLI.set_crs('EPSG:4326')
SLI = SLI.set_crs('EPSG:4326')

#create map
fig, ax = plt.subplots(figsize=(15,10), subplot_kw={'projection': ccrs.crs.Robinson()})
ax.set_title('Sea-level proxies in WALIS',fontsize=18)

ax.set_global()

plt.text(0.3, -0.02,'Made with Natural Earth. Free vector and raster map data @naturalearthdata.com.',
     horizontalalignment='left',
     verticalalignment='center',
     transform = ax.transAxes,
    fontsize=8)

#Project and plot the points on the map
coral_rsl = coral_rsl.to_crs('ESRI:54030')
speleo_rsl = speleo_rsl.to_crs('ESRI:54030')
MLI = MLI.to_crs('ESRI:54030')
TLI = TLI.to_crs('ESRI:54030')
SLI = SLI.to_crs('ESRI:54030')

TLI.plot(ax=ax,
               markersize=70,
               marker=7,
               edgecolor='white',
               c='lightcoral',label='Terrestrial limiting',zorder=100000,alpha=0.5)

coral_rsl.plot(ax=ax,
               markersize=80,
               marker='o',
               edgecolor='white',
               c='darkgreen',label='Single coral',zorder=1000,alpha=0.5)

speleo_rsl.plot(ax=ax,
               markersize=80,
               marker='o',
               edgecolor='white',
               c='saddlebrown',label='Single speleothem',zorder=100000,alpha=0.5)
SLI.plot(ax=ax,
               markersize=80,
               marker='o',
               c='steelblue',
               edgecolor='white',
               alpha=0.5,
               label='Coastal stratigraphy')
MLI.plot(ax=ax,
               markersize=70,
               marker=6,
               edgecolor='white',
               c='dodgerblue',label='Marine limiting',zorder=100000,alpha=0.5)




    
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.LAKES, alpha=0.5)
ax.add_feature(cfeature.RIVERS)

ax.legend()

filename1='Output/Images/svg/global_map.svg'
filename2='Output/Images/jpg/global_map.jpg'
plt.savefig(filename1, dpi=300)
plt.savefig(filename2, dpi=300)
plt.show()