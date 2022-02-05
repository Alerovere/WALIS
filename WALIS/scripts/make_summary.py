print ('making summary table....')
#Adjust "Summary" dataframe
Summary.rename(columns={'RSL_ID':'WALIS_ID'},inplace=True)
Summary['WALIS_ID']='RSL_' + Summary['WALIS_ID'].astype(str)
Summary.insert(loc=13, column='Paleo water depth estimate (m)', value='')
Summary.insert(loc=14, column='Upper limit of living range (m)', value='')
Summary.insert(loc=15, column='Lower limit of living range (m)', value='')
Summary['Reported age (ka)'].astype(float,errors='ignore')
Summary['Reported age uncertainty (ka)'].astype(float,errors='ignore')
Summary['U-Series recalculated age (ka)'].astype(float,errors='ignore')
Summary['U-Series recalculate age uncertainty (ka)'].astype(float,errors='ignore')
Summary['U-Series corrected age (speleothems, ka)'].astype(float,errors='ignore')
Summary['U-Series corrected age uncertainty (speleothems, ka)'].astype(float,errors='ignore')
Summary['Originally accepted?']=Summary['Originally accepted?'].replace('1', 'Yes')
Summary['Originally accepted?']=Summary['Originally accepted?'].replace('0', 'No')
#Create U-Series "Summary" dataframe
Summary_useries = pd.DataFrame()
useries_rsl=useries[useries['Are RSL estimates available for this record?']=='Yes']
Summary_useries['WALIS_ID']=useries_rsl['WALIS U-Series ID']
Summary_useries['WALIS_ID']='USeries_' + Summary_useries['WALIS_ID'].astype(str)
Summary_useries['Latitude']=useries_rsl['Latitude (decimal degrees)'].astype(float)
Summary_useries['Longitude']=useries_rsl['Longitude (decimal degrees)'].astype(float)
Summary_useries['Site']=useries_rsl['Site']
Summary_useries['Subsite']=useries_rsl['Additional site information']
Summary_useries['Nation']=''
Summary_useries['Region']=''
Summary_useries['Type of datapoint']='Sea Level Indicator'
Summary_useries['RSL Indicator']='Single '+useries_rsl['Material type']
Summary_useries['RSL indicator description']=useries_rsl['Facies description']+' '+useries_rsl['Taxa information (as reported)'] 
Summary_useries['Elevation measurement technique']=useries_rsl['Elevation measurement method']
Summary_useries['Elevation (m)']=pd.to_numeric(useries_rsl['Elevation above MSL (m)'], errors='coerce')
Summary_useries['Elevation error (m)']=pd.to_numeric(useries_rsl['Elevation uncertainty used (m)'], errors='coerce')
Summary_useries['Paleo water depth estimate (m)']=pd.to_numeric(useries_rsl['Paleo water depth estimate (m)'], errors='coerce')
Summary_useries['Upper limit of living range (m)']=pd.to_numeric(useries_rsl['Upper limit of living range (m)'], errors='coerce')
Summary_useries['Lower limit of living range (m)']=pd.to_numeric(useries_rsl['Lower limit of living range (m)'], errors='coerce')
Summary_useries['RWL']=np.nan
Summary_useries['IR']=np.nan
Summary_useries['Vertical datum']=useries_rsl['Original elevation datum used']
Summary_useries['Paleo RSL (m)']=useries_rsl['paleo RSL (m)'].astype(float,errors='ignore')
Summary_useries['Paleo RSL uncertainty (m)']=useries_rsl['paleo RSL uncertainty (m)'].astype(float,errors='ignore')
Summary_useries['Dating technique']='U-Series'
Summary_useries['Timing constraint']='Equal to'
Summary_useries['Originally reported ID']=useries_rsl['Reported ID']
Summary_useries['Analysis ID']=useries_rsl['Analysis ID']
Summary_useries['Material_type']=useries_rsl['Material type']
Summary_useries['Reported age (ka)']=useries_rsl['Reported age (ka)'].astype(float,errors='ignore')
Summary_useries['Reported age uncertainty (ka)']=useries_rsl['Reported ageuncertainty (ka, ±2σ)'].astype(float,errors='ignore')
Summary_useries['U-Series recalculated age (ka)']=useries_rsl['Recalculated Conventional Age (ka)'].astype(float,errors='ignore')
Summary_useries['U-Series recalculate age uncertainty (ka)']=useries_rsl['Recalculated Conventional Age uncert. (±2σ)'].astype(float,errors='ignore')
Summary_useries['U-Series corrected age (speleothems, ka)']=useries_rsl['Corrected reported age (ka)'].astype(float,errors='ignore')
Summary_useries['U-Series corrected age uncertainty (speleothems, ka)']=useries_rsl['Corrected reported age uncert. (ka, ±2σ)'].astype(float,errors='ignore')
Summary_useries['Stratigraphy Upper Age (ka)']=np.nan
Summary_useries['Stratigraphy Lower Age (ka)']=np.nan
Summary_useries['MIS limit']=''
Summary_useries['Marine Isotopic Stage']=''
Summary_useries['Quality of RSL information']=''
Summary_useries['Quality of age information']=''

# added for detailed summary
Summary_useries['WALIS U-series ID']=''
Summary_useries['WALIS AAR ID']=''
Summary_useries['WALIS ESR ID']=''
Summary_useries['WALIS LUM ID']=''
Summary_useries['WALIS strat ID']=''
Summary_useries['Sample Latitude']=''
Summary_useries['Sample Longitude']=''
Summary_useries['Originally accepted?']=useries_rsl['Accepted?']	
Summary_useries['Accepted by other study?']=useries_rsl['Accepted in other study?']	
# end added for detailed summary

Summary_useries['Reference(s)']=useries_rsl['Reference(s)']
Summary_useries['Record Created by']=useries_rsl['Record created by']
Summary_useries['Last Update']=useries_rsl['Last Update']
Summary2 = pd.concat([Summary,Summary_useries])
Summary = Summary2.copy()

Summary['Paleo water depth estimate (m)']=Summary['Paleo water depth estimate (m)'].replace('',np.nan).astype(float)
Summary['Upper limit of living range (m)']=Summary['Upper limit of living range (m)'].replace('',np.nan).astype(float)
Summary['Lower limit of living range (m)']=Summary['Lower limit of living range (m)'].replace('',np.nan).astype(float)

Summary['Reported age (ka)']=Summary['Reported age (ka)'].replace('Not Reported',np.nan)
Summary['Reported age (ka)']=Summary['Reported age (ka)'].replace('',np.nan).astype(float)
Summary['Reported age uncertainty (ka)'] = Summary['Reported age uncertainty (ka)'].replace('N/A','')
Summary['Reported age uncertainty (ka)'] = Summary['Reported age uncertainty (ka)'].replace('Not Reported','')
Summary['Reported age uncertainty (ka)']=Summary['Reported age uncertainty (ka)'].replace('',np.nan).astype(float)
Summary['U-Series recalculated age (ka)']=Summary['U-Series recalculated age (ka)'].replace('',np.nan).astype(float)
Summary['U-Series recalculate age uncertainty (ka)']=Summary['U-Series recalculate age uncertainty (ka)'].replace('',np.nan).astype(float)
Summary['U-Series corrected age (speleothems, ka)'] = Summary['U-Series corrected age (speleothems, ka)'].replace(['ND'],'')
Summary['U-Series corrected age (speleothems, ka)']=Summary['U-Series corrected age (speleothems, ka)'].replace('',np.nan).astype(float)
Summary['U-Series corrected age uncertainty (speleothems, ka)'] = Summary['U-Series corrected age uncertainty (speleothems, ka)'].replace(['ND'],'')
Summary['U-Series corrected age uncertainty (speleothems, ka)']=Summary['U-Series corrected age uncertainty (speleothems, ka)'].replace('',np.nan).astype(float)

# Insert standard uncertainties if not reported
Summary['Reported age uncertainty (ka)'].fillna(Summary['Reported age (ka)']*30/100, inplace = True)
Summary['U-Series recalculate age uncertainty (ka)'].fillna(Summary['U-Series recalculated age (ka)']*30/100, inplace = True)
Summary['U-Series corrected age uncertainty (speleothems, ka)'].fillna(Summary['U-Series corrected age (speleothems, ka)']*30/100, inplace = True)

# If 'Timing constraint' is empty, set it equal to 'MIS limit'
Summary['Timing constraint'] = Summary[['Timing constraint', 'MIS limit']].apply(lambda x: x[0] if x[0] else x[1], axis=1)
# If it still empty, replace with 'Equal to'
Summary['Timing constraint'].replace('','Equal to',inplace=True)

# If upper or lower ages are zero, set both to null
Summary['Stratigraphy Upper Age (ka)'].loc[(Summary['Stratigraphy Upper Age (ka)'] == 0)] = np.nan
Summary['Stratigraphy Lower Age (ka)'].loc[(Summary['Stratigraphy Lower Age (ka)'] == 0)] = np.nan
# If upper or lower ages are null, set the other to null as well
Summary['Stratigraphy Upper Age (ka)'] = np.where(Summary['Stratigraphy Lower Age (ka)'].isnull(), np.nan, Summary['Stratigraphy Upper Age (ka)'])
Summary['Stratigraphy Lower Age (ka)'] = np.where(Summary['Stratigraphy Upper Age (ka)'].isnull(), np.nan, Summary['Stratigraphy Lower Age (ka)'])

# Search the MIS definitions for age limits constraints and substitute them
MIS_ages.set_index('MIS name',inplace=True)
Summary=Summary.join(MIS_ages, on='Marine Isotopic Stage')
Summary['Stratigraphy Upper Age (ka)'].fillna(Summary['MIS start age'], inplace = True)
Summary['Stratigraphy Upper Age (ka)']=Summary['Stratigraphy Upper Age (ka)'].astype(float)
Summary['Stratigraphy Lower Age (ka)'].fillna(Summary['MIS end age'], inplace = True)
Summary['Stratigraphy Lower Age (ka)']=Summary['Stratigraphy Lower Age (ka)'].astype(float)
Summary.drop(columns=['MIS ID','MIS peak age','MIS start age','MIS end age'],inplace=True)

# Make sample to RSL index point distance
# Thanks: https://stackoverflow.com/questions/29545704/fast-haversine-approximation-python-pandas

def haversine_np(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)

    All args must be of equal length.    

    """
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2

    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c
    return km

### To solve for null values
Summary['Sample Longitude'] = np.where(Summary['Sample Longitude'] == '', 99999, Summary['Sample Longitude'])
Summary['Sample Longitude']=Summary['Sample Longitude'].astype(float)
Summary['Sample Latitude'] = np.where(Summary['Sample Latitude'] == '', 99999, Summary['Sample Latitude'])
Summary['Sample Latitude']=Summary['Sample Latitude'].astype(float)
Summary['Distance from sample'] = haversine_np(Summary['Longitude'],Summary['Latitude'],Summary['Sample Longitude'],Summary['Sample Latitude'])
Summary['Distance from sample']=np.where(Summary['Sample Longitude'] == 99999, np.nan, Summary['Distance from sample'])
Summary['Sample Longitude'] = np.where(Summary['Sample Longitude'] == 99999, np.nan, Summary['Sample Longitude'])
Summary['Sample Latitude'] = np.where(Summary['Sample Latitude'] == 99999, np.nan, Summary['Sample Latitude'])

Summary.sort_values(by=['WALIS_ID'],ascending=True)

print ('Done!')