import folium
#Creating a base map
m = folium.Map(zoom_start=12,control_scale = True)

##################################################################### Create geodataframes
if not Summary.empty:
 Summary['geometry'] = Summary.apply(lambda x: Point((float(x['Longitude']), 
                                                           float(x['Latitude']))), axis=1)
 
 Summary['Last Update']=Summary['Last Update'].astype(str)                                                           
 Summary = geopandas.GeoDataFrame(Summary, geometry='geometry')
 Summary.crs={'init': 'epsg:4326'}
 
if not RSL_Datapoints.empty:
 RSL_Datapoints['geometry'] = RSL_Datapoints.apply(lambda x: Point((float(x['Longitude (decimal degrees)']), 
                                                           float(x['Latitude (decimal degrees)']))), axis=1)
 RSL_Datapoints['Last Update']=RSL_Datapoints['Last Update'].astype(str)                                                           
 RSL_Datapoints = geopandas.GeoDataFrame(RSL_Datapoints, geometry='geometry')
 RSL_Datapoints.crs= {'init': 'epsg:4326'}

if not useries_corals.empty:
 useries_corals['Date of analysis']=useries_corals['Date of analysis'].astype(str)
 useries_corals['geometry'] = useries_corals.apply(lambda x: Point((float(x['Longitude (decimal degrees)']), 
                                                           float(x['Latitude (decimal degrees)']))), axis=1)
                                                           
 useries_corals['Last Update']=useries_corals['Last Update'].astype(str)                                                           
 useries_corals = geopandas.GeoDataFrame(useries_corals, geometry='geometry')
 useries_corals.crs= {'init': 'epsg:4326'}

if not useries_speleo.empty:
 useries_speleo['Date of analysis']=useries_speleo['Date of analysis'].astype(str)
 useries_speleo['geometry'] = useries_speleo.apply(lambda x: Point((float(x['Longitude (decimal degrees)']), 
                                                           float(x['Latitude (decimal degrees)']))), axis=1)
 useries_speleo['Last Update']=useries_speleo['Last Update'].astype(str)                                                           
 useries_speleo = geopandas.GeoDataFrame(useries_speleo, geometry='geometry')
 useries_speleo.crs= {'init': 'epsg:4326'}
 
if not useries_oolite.empty:
 useries_oolite['Date of analysis']=useries_oolite['Date of analysis'].astype(str)
 useries_oolite['geometry'] = useries_oolite.apply(lambda x: Point((float(x['Longitude (decimal degrees)']), 
                                                           float(x['Latitude (decimal degrees)']))), axis=1)
 useries_oolite['Last Update']=useries_oolite['Last Update'].astype(str)                                                           
 useries_oolite = geopandas.GeoDataFrame(useries_oolite, geometry='geometry')
 useries_oolite.crs= {'init': 'epsg:4326'}

if not useries_moll.empty:
 useries_moll['Date of analysis']=useries_speleo['Date of analysis'].astype(str) 
 useries_moll['geometry'] = useries_moll.apply(lambda x: Point((float(x['Longitude (decimal degrees)']), 
                                                           float(x['Latitude (decimal degrees)']))), axis=1)
 useries_moll['Last Update']=useries_moll['Last Update'].astype(str)                                                           
 useries_moll = geopandas.GeoDataFrame(useries_moll, geometry='geometry')
 useries_moll.crs= {'init': 'epsg:4326'}

if not aar.empty:
 aar['geometry'] = aar.apply(lambda x: Point((float(x['Longitude (decimal degrees)']), 
                                                           float(x['Latitude (decimal degrees)']))), axis=1)
 aar['Last Update']=aar['Last Update'].astype(str)                                                            
 aar = geopandas.GeoDataFrame(aar, geometry='geometry')
 aar.crs= {'init': 'epsg:4326'}
 
if not esr.empty:
 esr['geometry'] = esr.apply(lambda x: Point((float(x['Longitude (decimal degrees)']), 
                                                           float(x['Latitude (decimal degrees)']))), axis=1)
 esr['Last Update']=esr['Last Update'].astype(str)                                                            
 esr = geopandas.GeoDataFrame(esr, geometry='geometry')
 esr.crs= {'init': 'epsg:4326'}
 
if not lum.empty:
 lum['geometry'] = lum.apply(lambda x: Point((float(x['Sample longitude (decimal degrees)']), 
                                                           float(x['Sample latitude (decimal degrees)']))), axis=1)
 lum['Last Update']=lum['Last Update'].astype(str)                                                             
 lum = geopandas.GeoDataFrame(lum, geometry='geometry')
 lum.crs= {'init': 'epsg:4326'}

##################################################################### Add RSL from stratigrapy datapoints
if not RSL_Datapoints.empty:
    RSL_Datapoints_web=RSL_Datapoints.copy()
    cols = ['Site', 'Subsite']
    RSL_Datapoints_web['Subsite'].replace('', np.nan,inplace=True)
    RSL_Datapoints_web['geopos'] = RSL_Datapoints_web[cols].apply(lambda x:', '.join(x.dropna()), axis=1)
    RSL_Datapoints_web['Additional references'].replace('N/A','',inplace=True)
    RSL_Datapoints_web['Additional references'].replace('\n','; ',inplace=True,regex=True)
    RSL_Datapoints_web['Age attribution'].replace('\n',' <br> ',inplace=True,regex=True)
    RSL_Datapoints_web['U-series age IDs'].replace('\n',' <br> ',inplace=True,regex=True)
    RSL_Datapoints_web['U-series age IDs'].replace('','-',inplace=True,regex=True)
    RSL_Datapoints_web['Amino Acid Racemization age IDs'].replace('\n',' <br> ',inplace=True,regex=True)
    RSL_Datapoints_web['Amino Acid Racemization age IDs'].replace('','-',inplace=True,regex=True)
    RSL_Datapoints_web['Electro Spin Resonance age IDs'].replace('\n',' <br> ',inplace=True,regex=True)
    RSL_Datapoints_web['Electro Spin Resonance age IDs'].replace('','-',inplace=True,regex=True)
    RSL_Datapoints_web['Luminescence age IDs'].replace('\n',' <br> ',inplace=True,regex=True)
    RSL_Datapoints_web['Luminescence age IDs'].replace('','-',inplace=True,regex=True)
    RSL_Datapoints_web['Stratigraphic context/age IDs'].replace('\n',' <br> ',inplace=True,regex=True)
    RSL_Datapoints_web['Stratigraphic context/age IDs'].replace('','-',inplace=True,regex=True)
    RSL_Datapoints_web['Other age constraints IDs'].replace('\n',' <br> ',inplace=True,regex=True)
    RSL_Datapoints_web['Other age constraints IDs'].replace('','-',inplace=True,regex=True)

    def html_RSL(r):
        """
        Create some neat HTML for popup.
        Argument: pd.Series (row, use df.apply(html, axis=1))
        Returns: html string
        """
        return """
        <b>WALIS RSL ID {0}</b><br>
        <b>Site:</b> {1}<br>
        <b>Nation - Region: </b>{2}<br>
        <b>Type of RSL Indicator: </b>{3}<br>
        <b>Age attribution method(s): </b><br>
        {4}<br>
        <b>Age constraints</b><br>
        <i><b>U-Series</b></i><br>{5}<br><br>
        <i><b>AAR</b></i><br>{6}<br><br>
        <i><b>ESR</b></i><br>{7}<br><br>
        <i><b>Luminescence</b></i><br>{8}<br><br>
        <i><b>Chronostratigrapy</b></i><br>{9}<br><br>
        <i><b>Other constraints</b></i><br>{10}<br><br>
        <b>Reference(s): </b>{11} {12}<br>
        <b>Record Created by: </b>{13}
        """\
            .format(r['WALIS RSL ID']#0
                    ,r.geopos
                    ,str(r.Nation)+'-'+str(r.Region)#2
                    ,r['Type of RSL Indicator']#3
                    ,r['Age attribution']#4
                    ,r['U-series age IDs']#5
                    ,r['Amino Acid Racemization age IDs']#6
                    ,r['Electro Spin Resonance age IDs']#7
                    ,r['Luminescence age IDs']#8
                    ,r['Stratigraphic context/age IDs']#9
                    ,r['Other age constraints IDs']#10
                    ,r['Main reference']#11
                    ,r['Additional references']#12
                    ,r['Record created by'])#13

    def marker_RSL(r):
        """
        Creates marker for folium use.
        Argument: pd.Series (row, use df.apply(marker, axis=1)
        Returns: folium.Marker object
        """
        popup_html = html_RSL(r)
        iframe = folium.IFrame(html=popup_html, width=350, height=450)
        popup = folium.Popup(iframe, max_width=2650)
        if r ['Is this a marine/terrestrial limiting record?'] == 'Sea Level Indicator':
            icon = folium.Icon(color='blue', icon='circle',prefix='fa')
        elif r ['Is this a marine/terrestrial limiting record?'] == 'Marine Limiting':
            icon = folium.Icon(color='blue', icon='arrow-up',prefix='fa')
        else:
            icon = folium.Icon(color='blue', icon='arrow-down',prefix='fa')
        return folium.Marker((r.geometry.y, r.geometry.x),popup=popup,icon=icon,)

    RSL_Datapoints_web['marker'] = RSL_Datapoints_web.apply(marker_RSL, axis=1)

    #create zoomable clusters
    cluster = folium.plugins.MarkerCluster(name='RSL datapoints from stratigraphy',show=True)
    RSL_Datapoints_web.marker.apply(lambda x: cluster.add_child(x))
    m.add_child(cluster)
    
##################################################################### Add RSL from single corals datapoints
if not useries_corals_RSL.empty:
    useries_corals_RSL_web=useries_corals_RSL.copy()
    useries_corals_RSL_web['geometry'] = useries_corals_RSL_web.apply(lambda x: Point((float(x['Longitude (decimal degrees)']), 
                                                               float(x['Latitude (decimal degrees)']))), axis=1)
    useries_corals_RSL_web = geopandas.GeoDataFrame(useries_corals_RSL_web, geometry='geometry')
    useries_corals_RSL_web['Reference(s)'].replace('\n',';  ',inplace=True,regex=True)
    useries_corals_RSL_web = useries_corals_RSL_web.replace('', np.nan)
    cols = ['Location', 'Site', 'Additional site information']
    useries_corals_RSL_web['geopos'] = useries_corals_RSL_web[cols].apply(lambda x:' <br> '.join(x.dropna()), axis=1)
    cols = ['Family', 'Genus', 'Species']
    useries_corals_RSL_web['ecology'] = useries_corals_RSL_web[cols].apply(lambda x:'/'.join(x.dropna()), axis=1)

    def html_corals_RSL(r):
        """
        Create some neat HTML for popup.
        Argument: pd.Series (row, use df.apply(html, axis=1))
        Returns: html string
        """
        return """
        <b>WALIS U-Series ID {0}</b><br>
        <b>Site: </b>{1}<br>
        <b>Family / Genus / Species: </b>{2}<br>
        <b>Facies: </b>{3}<br>
        <b>Analysis ID: </b>{4}<br>
        <b>Originally reported ID:</b>{5}<br>
        <b>Reference(s): </b>{6}<br>
        <b>Record Created by: </b>{7}
        """\
            .format(r['WALIS U-Series ID']#0
                    ,r['geopos']#1
                    ,r['ecology']#2
                    ,r['Facies description']#3
                    ,r['Analysis ID']#4
                    ,r['Reported ID']#5
                    ,r['Reference(s)']#6
                    ,r['Record created by'])#7

    def marker_corals_RSL(r):
        """
        Creates marker for folium use.
        Argument: pd.Series (row, use df.apply(marker, axis=1)
        Returns: folium.Marker object
        """
        popup_html = html_corals_RSL(r)
        iframe = folium.IFrame(html=popup_html, width=250, height=300)
        popup = folium.Popup(iframe, max_width=2650)    
        icon = folium.Icon(color='orange', icon='circle',prefix='fa')
        return folium.Marker((r.geometry.y, r.geometry.x),icon=icon,popup=popup)

    useries_corals_RSL_web['marker'] = useries_corals_RSL_web.apply(marker_corals_RSL, axis=1)

    #create zoomable clusters
    cluster2 = folium.plugins.MarkerCluster(name='RSL datapoints from single corals',show=True)
    useries_corals_RSL_web.marker.apply(lambda x: cluster2.add_child(x))
    m.add_child(cluster2)

##################################################################### Add RSL from single speleothems
if not useries_speleo_RSL.empty:
    useries_speleo_RSL_web=useries_speleo_RSL.copy()
    useries_speleo_RSL_web['geometry'] = useries_speleo_RSL_web.apply(lambda x: Point((float(x['Longitude (decimal degrees)']), 
                                                               float(x['Latitude (decimal degrees)']))), axis=1)
    useries_speleo_RSL_web = geopandas.GeoDataFrame(useries_speleo_RSL_web, geometry='geometry')
    useries_speleo_RSL_web['Reference(s)'].replace('\n','; ',inplace=True,regex=True)
    useries_speleo_RSL_web = useries_speleo_RSL_web.replace('', np.nan)
    cols = ['Location', 'Site']
    useries_speleo_RSL_web['geopos'] = useries_speleo_RSL_web[cols].apply(lambda x:' <br> '.join(x.dropna()), axis=1)

    def html_speleo_RSL(r):
        """
        Create some neat HTML for popup.
        Argument: pd.Series (row, use df.apply(html, axis=1))
        Returns: html string
        """
        return """
        <b>WALIS U-Series ID {0}</b><br>
        <b>Site: </b>{1}<br>
        <b>Type of deposit: </b>{2}<br>
        <b>Analysis ID: </b>{3}<br>
        <b>Originally reported ID: </b>:{4}<br>
        <b>Reference(s): </b>{5}<br>
        <b>Record Created by: </b>{6}
        """\
            .format(r['WALIS U-Series ID']#0
                    ,r['geopos']#1
                    ,r['Details on dated material']#2
                    ,r['Analysis ID']#3
                    ,r['Reported ID']#4
                    ,r['Reference(s)']#5
                    ,r['Record created by'])#6

    def marker_speleo_RSL(r):
        """
        Creates marker for folium use.
        Argument: pd.Series (row, use df.apply(marker, axis=1)
        Returns: folium.Marker object
        """
        popup_html = html_speleo_RSL(r)
        iframe = folium.IFrame(html=popup_html, width=250, height=300)
        popup = folium.Popup(iframe, max_width=2650)    
        icon = folium.Icon(color='green', icon='circle',prefix='fa')
        return folium.Marker((r.geometry.y, r.geometry.x),icon=icon,popup=popup)

    useries_speleo_RSL_web['marker'] = useries_speleo_RSL_web.apply(marker_speleo_RSL, axis=1)

    #create zoomable clusters
    cluster3 = folium.plugins.MarkerCluster(name='RSL datapoints from single speleothems',show=True)
    useries_speleo_RSL_web.marker.apply(lambda x: cluster3.add_child(x))
    m.add_child(cluster3)

##################################################################### Add AAR Samples
if not aar.empty:
    
    aar_web=aar.copy()
    aar_web['Dating method']='Amino Acid Racemization'
    aar_web['WALIS AAR ID']='AAR_'+aar_web['WALIS AAR ID'].astype(str)
    aar_web.rename(columns={'WALIS AAR ID':'WALIS ID'},inplace=True)
    aar_web['Reference(s)'].replace('\n','; ',inplace=True,regex=True)

    def html_sample(r):
        """
        Create some neat HTML for popup.
        Argument: pd.Series (row, use df.apply(html, axis=1))
        Returns: html string
        """
        return """
        <b>WALIS ID {0}</b><br>
        <b>Dating method: </b>{1}<br>
        <b>Analysis ID: </b>{2}<br>
        <b>Originally reported ID: </b>{3}<br>
        <b>Reference(s): </b>{4}<br>
        <b>Record Created by: </b>{5}
        """\
            .format(r['WALIS ID']#0
                    ,r['Dating method']#1
                    ,r['Analysis ID']#2
                    ,r['Reported ID']#3
                    ,r['Reference(s)']#4
                    ,r['Record created by'])#5

    def marker_sample(r):
        """
        Creates marker for folium use.
        Argument: pd.Series (row, use df.apply(marker, axis=1)
        Returns: folium.Marker object
        """
        popup_html = html_sample(r)
        iframe = folium.IFrame(html=popup_html, width=250, height=300)
        popup = folium.Popup(iframe, max_width=2650)  

        if r['Accepted?'] == 'No':
            icon = folium.Icon(color='gray', icon='times',prefix='fa')     
        elif r['Dating method'] == 'Amino Acid Racemization' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='purple', icon='flask',prefix='fa') 
        elif r['Dating method'] == 'Electron Spin Resonance' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='darkblue', icon='flask',prefix='fa') 
        elif r['Dating method'] == 'Luminescence' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='lightgreen', icon='flask',prefix='fa')
        elif r['Dating method'] == 'U-Series on mollusk/algae' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='darkred', icon='flask',prefix='fa')
        elif r['Dating method'] == 'U-Series on coral' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='darkred', icon='flask',prefix='fa')
        else:
            icon = folium.Icon(color='darkred', icon='flask',prefix='fa')

        return folium.Marker((r.geometry.y, r.geometry.x),icon=icon,popup=popup)

    aar_web['marker'] = aar_web.apply(marker_sample, axis=1)

    #create zoomable clusters
    cluster4 = folium.plugins.MarkerCluster(name='AAR samples',show=False)
    aar_web.marker.apply(lambda x: cluster4.add_child(x))
    m.add_child(cluster4)

##################################################################### Add ESR Samples
if not esr.empty:
    esr_web=esr.copy()
    esr_web['Dating method']='Electron Spin Resonance'
    esr_web['WALIS ESR ID']='ESR_'+esr_web['WALIS ESR ID'].astype(str)
    esr_web.rename(columns={'WALIS ESR ID':'WALIS ID'},inplace=True)
    esr_web['Reference(s)'].replace('\n','; ',inplace=True,regex=True)

    def html_sample(r):
        """
        Create some neat HTML for popup.
        Argument: pd.Series (row, use df.apply(html, axis=1))
        Returns: html string
        """
        return """
        <b>WALIS ID {0}</b><br>
        <b>Dating method: </b>{1}<br>
        <b>Analysis ID: </b>{2}<br>
        <b>Originally reported: ID</b>{3}<br>
        <b>Reference(s): </b>{4}<br>
        <b>Record Created by: </b>{5}
        """\
            .format(r['WALIS ID']#0
                    ,r['Dating method']#1
                    ,r['Analysis ID']#2
                    ,r['Reported ID']#3
                    ,r['Reference(s)']#4
                    ,r['Record created by'])#5

    def marker_sample(r):
        """
        Creates marker for folium use.
        Argument: pd.Series (row, use df.apply(marker, axis=1)
        Returns: folium.Marker object
        """
        popup_html = html_sample(r)
        iframe = folium.IFrame(html=popup_html, width=250, height=300)
        popup = folium.Popup(iframe, max_width=2650)  

        if r['Accepted?'] == 'No':
            icon = folium.Icon(color='gray', icon='times',prefix='fa')     
        elif r['Dating method'] == 'Amino Acid Racemization' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='purple', icon='flask',prefix='fa') 
        elif r['Dating method'] == 'Electron Spin Resonance' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='darkblue', icon='flask',prefix='fa') 
        elif r['Dating method'] == 'Luminescence' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='lightgreen', icon='flask',prefix='fa')
        elif r['Dating method'] == 'U-Series on mollusk/algae' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='darkred', icon='flask',prefix='fa')
        elif r['Dating method'] == 'U-Series on coral' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='darkred', icon='flask',prefix='fa')
        else:
            icon = folium.Icon(color='darkred', icon='flask',prefix='fa')

        return folium.Marker((r.geometry.y, r.geometry.x),icon=icon,popup=popup)

    esr_web['marker'] = esr_web.apply(marker_sample, axis=1)

    #create zoomable clusters
    cluster5 = folium.plugins.MarkerCluster(name='ESR samples',show=False)
    esr_web.marker.apply(lambda x: cluster5.add_child(x))
    m.add_child(cluster5)

##################################################################### Add LUM Samples
if not lum.empty:
    lum_web=lum.copy()
    lum_web['Dating method']='Luminescence'
    lum_web['WALIS LUM ID']='LUM_'+lum_web['WALIS LUM ID'].astype(str)
    lum_web=lum_web.rename(columns={'Reference (s)': 'Reference(s)','WALIS LUM ID':'WALIS ID'})
    lum_web['Reference(s)'].replace('\n','; ',inplace=True,regex=True)

    def html_sample(r):
        """
        Create some neat HTML for popup.
        Argument: pd.Series (row, use df.apply(html, axis=1))
        Returns: html string
        """
        return """
        <b>WALIS ID {0}</b><br>
        <b>Dating method: </b>{1}<br>
        <b>Analysis ID: </b>{2}<br>
        <b>Originally reported ID: </b>{3}<br>
        <b>Reference(s): </b>{4}<br>
        <b>Record Created by: </b>{5}
        """\
            .format(r['WALIS ID']#0
                    ,r['Dating method']#1
                    ,r['Analysis ID']#2
                    ,r['Reported ID']#3
                    ,r['Reference(s)']#4
                    ,r['Record created by'])#5

    def marker_sample(r):
        """
        Creates marker for folium use.
        Argument: pd.Series (row, use df.apply(marker, axis=1)
        Returns: folium.Marker object
        """
        popup_html = html_sample(r)
        iframe = folium.IFrame(html=popup_html, width=250, height=300)
        popup = folium.Popup(iframe, max_width=2650)  

        if r['Accepted?'] == 'No':
            icon = folium.Icon(color='gray', icon='times',prefix='fa')     
        elif r['Dating method'] == 'Amino Acid Racemization' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='purple', icon='flask',prefix='fa') 
        elif r['Dating method'] == 'Electron Spin Resonance' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='darkblue', icon='flask',prefix='fa') 
        elif r['Dating method'] == 'Luminescence' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='lightgreen', icon='flask',prefix='fa')
        elif r['Dating method'] == 'U-Series on mollusk/algae' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='darkred', icon='flask',prefix='fa')
        elif r['Dating method'] == 'U-Series on coral' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='darkred', icon='flask',prefix='fa')
        else:
            icon = folium.Icon(color='darkred', icon='flask',prefix='fa')

        return folium.Marker((r.geometry.y, r.geometry.x),icon=icon,popup=popup)

    lum_web['marker'] = lum_web.apply(marker_sample, axis=1)

    #create zoomable clusters
    cluster6 = folium.plugins.MarkerCluster(name='Luminescence samples',show=False)
    lum_web.marker.apply(lambda x: cluster6.add_child(x))
    m.add_child(cluster6)    

##################################################################### Add Useries mollusk samples
if not useries_moll.empty:
    useries_moll_web=useries_moll.copy()
    useries_moll_web['Dating method']='U-Series on mollusk/algae'
    useries_moll_web['WALIS U-Series ID']='USeries_'+useries_moll_web['WALIS U-Series ID'].astype(str)
    useries_moll_web.rename(columns={'WALIS U-Series ID':'WALIS ID'},inplace=True)
    useries_moll_web['Reference(s)'].replace('\n','; ',inplace=True,regex=True)

    def html_sample(r):
        """
        Create some neat HTML for popup.
        Argument: pd.Series (row, use df.apply(html, axis=1))
        Returns: html string
        """
        return """
        <b>WALIS ID {0}</b><br>
        <b>Dating method: </b>{1}<br>
        <b>Analysis ID: </b>{2}<br>
        <b>Originally reported ID: </b>{3}<br>
        <b>Reference(s): </b>{4}<br>
        <b>Record Created by: </b>{5}
        """\
            .format(r['WALIS ID']#0
                    ,r['Dating method']#1
                    ,r['Analysis ID']#2
                    ,r['Reported ID']#3
                    ,r['Reference(s)']#4
                    ,r['Record created by'])#5

    def marker_sample(r):
        """
        Creates marker for folium use.
        Argument: pd.Series (row, use df.apply(marker, axis=1)
        Returns: folium.Marker object
        """
        popup_html = html_sample(r)
        iframe = folium.IFrame(html=popup_html, width=250, height=300)
        popup = folium.Popup(iframe, max_width=2650)  

        if r['Accepted?'] == 'No':
            icon = folium.Icon(color='gray', icon='times',prefix='fa')     
        elif r['Dating method'] == 'Amino Acid Racemization' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='purple', icon='flask',prefix='fa') 
        elif r['Dating method'] == 'Electron Spin Resonance' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='darkblue', icon='flask',prefix='fa') 
        elif r['Dating method'] == 'Luminescence' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='lightgreen', icon='flask',prefix='fa')
        elif r['Dating method'] == 'U-Series on mollusk/algae' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='darkred', icon='flask',prefix='fa')
        elif r['Dating method'] == 'U-Series on coral' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='darkred', icon='flask',prefix='fa')
        else:
            icon = folium.Icon(color='darkred', icon='flask',prefix='fa')

        return folium.Marker((r.geometry.y, r.geometry.x),icon=icon,popup=popup)

    useries_moll_web['marker'] = useries_moll_web.apply(marker_sample, axis=1)

    #create zoomable clusters
    cluster7 = folium.plugins.MarkerCluster(name='Useries on mollsuk samples',show=False)
    useries_moll_web.marker.apply(lambda x: cluster7.add_child(x))
    m.add_child(cluster7)
    
##################################################################### Add Useries mollusk samples
if not useries_corals.empty:
    useries_corals_web = useries_corals
    useries_corals_web['Dating method']='U-Series on coral'
    useries_corals_web['WALIS U-Series ID']='USeries_'+useries_corals_web['WALIS U-Series ID'].astype(str)
    useries_corals_web.rename(columns={'WALIS U-Series ID':'WALIS ID'},inplace=True)
    useries_corals_web['Reference(s)'].replace('\n',' <br> ',inplace=True,regex=True)

    def html_sample(r):
        """
        Create some neat HTML for popup.
        Argument: pd.Series (row, use df.apply(html, axis=1))
        Returns: html string
        """
        return """
        <b>WALIS ID {0}</b><br>
        <b>Dating method: </b>{1}<br>
        <b>Analysis ID: </b>{2}<br>
        <b>Originally reported ID: </b>{3}<br>
        <b>Reference(s): </b>{4}<br>
        <b>Record Created by: </b>{5}
        """\
            .format(r['WALIS ID']#0
                    ,r['Dating method']#1
                    ,r['Analysis ID']#2
                    ,r['Reported ID']#3
                    ,r['Reference(s)']#4
                    ,r['Record created by'])#5

    def marker_sample(r):
        """
        Creates marker for folium use.
        Argument: pd.Series (row, use df.apply(marker, axis=1)
        Returns: folium.Marker object
        """
        popup_html = html_sample(r)
        iframe = folium.IFrame(html=popup_html, width=250, height=300)
        popup = folium.Popup(iframe, max_width=2650)  

        if r['Accepted?'] == 'No':
            icon = folium.Icon(color='gray', icon='times',prefix='fa')     
        elif r['Dating method'] == 'Amino Acid Racemization' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='purple', icon='flask',prefix='fa') 
        elif r['Dating method'] == 'Electron Spin Resonance' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='darkblue', icon='flask',prefix='fa') 
        elif r['Dating method'] == 'Luminescence' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='lightgreen', icon='flask',prefix='fa')
        elif r['Dating method'] == 'U-Series on mollusk/algae' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='darkred', icon='flask',prefix='fa')
        elif r['Dating method'] == 'U-Series on coral' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='darkred', icon='flask',prefix='fa')
        else:
            icon = folium.Icon(color='darkred', icon='flask',prefix='fa')

        return folium.Marker((r.geometry.y, r.geometry.x),icon=icon,popup=popup)

    useries_corals_web['marker'] = useries_corals_web.apply(marker_sample, axis=1)

    #create zoomable clusters
    cluster8 = folium.plugins.MarkerCluster(name='Useries on coral samples',show=False)
    useries_corals_web.marker.apply(lambda x: cluster8.add_child(x))
    m.add_child(cluster8)  
    
##################################################################### Add Useries mollusk samples
if not useries_speleo.empty:
    useries_speleo_web = useries_speleo
    useries_speleo_web['Dating method']='U-Series on speleothem'
    useries_speleo_web['WALIS U-Series ID']='USeries_'+useries_speleo_web['WALIS U-Series ID'].astype(str)
    useries_speleo_web.rename(columns={'WALIS U-Series ID':'WALIS ID'},inplace=True)
    useries_speleo_web['Reference(s)'].replace('\n','; ',inplace=True,regex=True)

    def html_sample(r):
        """
        Create some neat HTML for popup.
        Argument: pd.Series (row, use df.apply(html, axis=1))
        Returns: html string
        """
        return """
        <b>WALIS ID {0}</b><br>
        <b>Dating method: </b>{1}<br>
        <b>Analysis ID: </b>{2}<br>
        <b>Originally reported ID: </b>{3}<br>
        <b>Reference(s): </b>{4}<br>
        <b>Record Created by: </b>{5}
        """\
            .format(r['WALIS ID']#0
                    ,r['Dating method']#1
                    ,r['Analysis ID']#2
                    ,r['Reported ID']#3
                    ,r['Reference(s)']#4
                    ,r['Record created by'])#5

    def marker_sample(r):
        """
        Creates marker for folium use.
        Argument: pd.Series (row, use df.apply(marker, axis=1)
        Returns: folium.Marker object
        """
        popup_html = html_sample(r)
        iframe = folium.IFrame(html=popup_html, width=250, height=300)
        popup = folium.Popup(iframe, max_width=2650)  

        if r['Accepted?'] == 'No':
            icon = folium.Icon(color='gray', icon='times',prefix='fa')     
        elif r['Dating method'] == 'Amino Acid Racemization' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='purple', icon='flask',prefix='fa') 
        elif r['Dating method'] == 'Electron Spin Resonance' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='darkblue', icon='flask',prefix='fa') 
        elif r['Dating method'] == 'Luminescence' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='lightgreen', icon='flask',prefix='fa')
        elif r['Dating method'] == 'U-Series on mollusk/algae' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='darkred', icon='flask',prefix='fa')
        elif r['Dating method'] == 'U-Series on coral' and r['Accepted?'] == 'Yes':
            icon = folium.Icon(color='darkred', icon='flask',prefix='fa')
        else:
            icon = folium.Icon(color='darkred', icon='flask',prefix='fa')

        return folium.Marker((r.geometry.y, r.geometry.x),icon=icon,popup=popup)

    useries_speleo_web['marker'] = useries_speleo_web.apply(marker_sample, axis=1)

    #create zoomable clusters
    cluster9 = folium.plugins.MarkerCluster(name='Useries on speleothem samples',show=False)
    useries_speleo_web.marker.apply(lambda x: cluster9.add_child(x))
    m.add_child(cluster9) 

####################################################################################################################
style_function = lambda x: {'fillOpacity': 0
                           ,'weight': 1
                           ,'opacity': 0.2
                           ,'color': 'black'
                           }


# Add Category Legend
legend_html = """
<div style="position:fixed;
     bottom: 15px; 
     left: 15px; 
     width: 200px; 
     height: 220px; 
     border:2px solid grey; 
     z-index: 9999;
     font-size:12px;">
     &nbsp;<b>RSL datapoints</b><br>
     &nbsp;<i class="fa fa-circle fa-1x" style="color:blue"></i>&nbsp;Stratigraphy index points<br>
     &nbsp;<i class="fa fa-circle fa-1x" style="color:orange"></i>&nbsp;Coral index points<br>
     &nbsp;<i class="fa fa-circle fa-1x" style="color:green"></i>&nbsp;Speleothem index points<br>
     &nbsp;<i class="fa fa-arrow-down fa-1x" style="color:blue"></i>&nbsp;Terrestrial limiting<br>
     &nbsp;<i class="fa fa-arrow-up fa-1x" style="color:blue"></i>&nbsp;Marine limiting<br>
     &nbsp;<b>Dated samples</b><br>
     &nbsp;<i class="fa fa-times fa-1x" style="color:gray"></i>&nbsp;Not accepted<br>
     &nbsp;<i class="fa fa-flask fa-1x" style="color:purple"></i>&nbsp;Amino Acid Racemization<br>
     &nbsp;<i class="fa fa-flask fa-1x" style="color:darkblue"></i>&nbsp;Electron Spin Resonance<br>
     &nbsp;<i class="fa fa-flask fa-1x" style="color:lightgreen"></i>&nbsp;Luminescence<br>
     &nbsp;<i class="fa fa-flask fa-1x" style="color:darkred"></i>&nbsp;U-Series<br>
</div>"""
 
        
# Add Legend
m.get_root().html.add_child(folium.Element(legend_html))

#Add title
loc = 'WALIS Version 1.0'
title_html = '''
             <h3 align="center" style="font-size:16px"><b>{}</b></h3>
             '''.format(loc)   
m.get_root().html.add_child(folium.Element(title_html))

# Add layer control to toggle on/off
folium.LayerControl(collapsed=False).add_to(m)
filename=('Output/html/Folium_map.html')
m.save(filename)
m