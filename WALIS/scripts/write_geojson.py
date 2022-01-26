#GeoJson
if not Summary.empty:
 Summary['geometry'] = Summary.apply(lambda x: Point((float(x['Longitude']), 
                                                           float(x['Latitude']))), axis=1)
 
 Summary['Last Update']=Summary['Last Update'].astype(str)                                                           
 Summary = geopandas.GeoDataFrame(Summary, geometry='geometry')
 Summary.crs={'init': 'epsg:4326'}
 filename=os.path.join(path,'Output','Data','json','Summary.json')
 Summary.to_file(filename, driver="GeoJSON", encoding='utf-8')
 
if not RSL_Datapoints.empty:
 RSL_Datapoints['geometry'] = RSL_Datapoints.apply(lambda x: Point((float(x['Longitude (decimal degrees)']), 
                                                           float(x['Latitude (decimal degrees)']))), axis=1)
 RSL_Datapoints['Last Update']=RSL_Datapoints['Last Update'].astype(str)                                                           
 RSL_Datapoints = geopandas.GeoDataFrame(RSL_Datapoints, geometry='geometry')
 RSL_Datapoints.crs= {'init': 'epsg:4326'}
 filename=os.path.join(path,'Output','Data','json','RSL_proxies.json')
 RSL_Datapoints.to_file(filename, driver="GeoJSON", encoding='utf-8')

if not useries_corals.empty:
 useries_corals['Date of analysis']=useries_corals['Date of analysis'].astype(str)
 useries_corals['geometry'] = useries_corals.apply(lambda x: Point((float(x['Longitude (decimal degrees)']), 
                                                           float(x['Latitude (decimal degrees)']))), axis=1)
                                                           
 useries_corals['Last Update']=useries_corals['Last Update'].astype(str)                                                           
 useries_corals = geopandas.GeoDataFrame(useries_corals, geometry='geometry')
 useries_corals.crs= {'init': 'epsg:4326'}
 filename=os.path.join(path,'Output','Data','json','Useries_corals.json')
 useries_corals.to_file(filename, driver="GeoJSON", encoding='utf-8')

if not useries_speleo.empty:
 useries_speleo['Date of analysis']=useries_speleo['Date of analysis'].astype(str)
 useries_speleo['geometry'] = useries_speleo.apply(lambda x: Point((float(x['Longitude (decimal degrees)']), 
                                                           float(x['Latitude (decimal degrees)']))), axis=1)
 useries_speleo['Last Update']=useries_speleo['Last Update'].astype(str)                                                           
 useries_speleo = geopandas.GeoDataFrame(useries_speleo, geometry='geometry')
 useries_speleo.crs= {'init': 'epsg:4326'}
 filename=os.path.join(path,'Output','Data','json','Useries_speleothems.json')
 useries_speleo.to_file(filename, driver="GeoJSON", encoding='utf-8')
 
if not useries_oolite.empty:
 useries_oolite['Date of analysis']=useries_oolite['Date of analysis'].astype(str)
 useries_oolite['geometry'] = useries_oolite.apply(lambda x: Point((float(x['Longitude (decimal degrees)']), 
                                                           float(x['Latitude (decimal degrees)']))), axis=1)
 useries_oolite['Last Update']=useries_oolite['Last Update'].astype(str)                                                           
 useries_oolite = geopandas.GeoDataFrame(useries_oolite, geometry='geometry')
 useries_oolite.crs= {'init': 'epsg:4326'}
 filename=os.path.join(path,'Output','Data','json','Useries_oolites.json')
 useries_oolite.to_file(filename, driver="GeoJSON", encoding='utf-8')

if not useries_moll.empty:
 useries_moll['Date of analysis']=useries_speleo['Date of analysis'].astype(str) 
 useries_moll['geometry'] = useries_moll.apply(lambda x: Point((float(x['Longitude (decimal degrees)']), 
                                                           float(x['Latitude (decimal degrees)']))), axis=1)
 useries_moll['Last Update']=useries_moll['Last Update'].astype(str)                                                           
 useries_moll = geopandas.GeoDataFrame(useries_moll, geometry='geometry')
 useries_moll.crs= {'init': 'epsg:4326'}
 filename=os.path.join(path,'Output','Data','json','Useries_mollusks.json')
 useries_moll.to_file(filename, driver="GeoJSON", encoding='utf-8')

if not aar.empty:
 aar['geometry'] = aar.apply(lambda x: Point((float(x['Longitude (decimal degrees)']), 
                                                           float(x['Latitude (decimal degrees)']))), axis=1)
 aar['Last Update']=aar['Last Update'].astype(str)                                                            
 aar = geopandas.GeoDataFrame(aar, geometry='geometry')
 aar.crs= {'init': 'epsg:4326'}
 filename=os.path.join(path,'Output','Data','json','AAR.json')
 aar.to_file(filename, driver="GeoJSON", encoding='utf-8')
 
if not esr.empty:
 esr['geometry'] = esr.apply(lambda x: Point((float(x['Longitude (decimal degrees)']), 
                                                           float(x['Latitude (decimal degrees)']))), axis=1)
 esr['Last Update']=esr['Last Update'].astype(str)                                                            
 esr = geopandas.GeoDataFrame(esr, geometry='geometry')
 esr.crs= {'init': 'epsg:4326'}
 filename=os.path.join(path,'Output','Data','json','ESR.json')
 esr.to_file(filename, driver="GeoJSON", encoding='utf-8')
 
if not lum.empty:
 lum['geometry'] = lum.apply(lambda x: Point((float(x['Sample longitude (decimal degrees)']), 
                                                           float(x['Sample latitude (decimal degrees)']))), axis=1)
 lum['Last Update']=lum['Last Update'].astype(str)                                                             
 lum = geopandas.GeoDataFrame(lum, geometry='geometry')
 lum.crs= {'init': 'epsg:4326'}
 filename=os.path.join(path,'Output','Data','json','Luminescence.json')
 lum.to_file(filename, driver="GeoJSON", encoding='utf-8')