###### Initial message ######
print('We are substituting values in your dataframes....')

#### Set RSL fields to null if marine or terrestrial limiting
RSL_Datapoints.loc[RSL_Datapoints.Limiting == 'Marine Limiting', ['ULmodAn', 'LLmodAn','RWL','IR','PaleoRSL','PaleoRSLunc']] = '', '','','','',''
RSL_Datapoints.loc[RSL_Datapoints.Limiting == 'Terrestrial Limiting', ['ULmodAn', 'LLmodAn','RWL','IR','PaleoRSL','PaleoRSLunc']] = '', '','','','',''

###### Work on RSL_Datapoints dataframe ######
RSL_Datapoints['Ref'] = RSL_Datapoints.Ref.astype(int)
# Update country field with country name (and save ID to separate column)
#RSL_Datapoints['Nation_ID']=RSL_Datapoints['Nation']
m = countries.set_index('id')['name'].to_dict()
v = RSL_Datapoints.filter(items=['Nation'])
RSL_Datapoints[v.columns] = v.replace(m)

# Update region field with country name (and save ID to separate column)
#RSL_Datapoints['Region_ID']=RSL_Datapoints['Region']
m = regions.set_index('id')['name'].to_dict()
v = RSL_Datapoints.filter(items=['Region'])
RSL_Datapoints[v.columns] = v.replace(m)

# Update references field with short reference
#Update main reference column
m = references.set_index('Ref_ID')['ShortRef'].to_dict()
v = RSL_Datapoints.filter(items=['Ref'])
RSL_Datapoints[v.columns] = v.replace(m)
#Update additional references column
RSL_Datapoints['addRef']=RSL_Datapoints['addRef'].replace('', '9999999').astype(str) #####
df1 = pd.DataFrame([[np.nan] * len(references.columns)], columns=references.columns)
ref = df1.append(references, ignore_index=True)
ref.loc[[0],'Ref_ID'] = 9999999
ref.loc[[0],'ShortRef'] = 'N/A'
ref['Ref_ID'] = ref['Ref_ID'].astype(int)
RSL_Datapoints['addRef'] = (RSL_Datapoints['addRef'].str.split(',')
                                .explode()
                                .map(ref.assign(Ref_ID=ref.Ref_ID.astype(str))
                                     .set_index('Ref_ID')['ShortRef'])
                                .groupby(level=0).agg('\n '.join))

# Update Horizontal positioning technique with technique name (and save ID in separate column)
#RSL_Datapoints['HrzPosTech_ID']=RSL_Datapoints['HrzPosTech']
m = hrzpos.set_index('idposhrz')['HrzType'].to_dict()
v = RSL_Datapoints.filter(items=['HrzPosTech'])
RSL_Datapoints[v.columns] = v.replace(m)
RSL_Datapoints['HrzPosTech'] = RSL_Datapoints.HrzPosTech.astype(str)
RSL_Datapoints['HrzPosTech']=RSL_Datapoints['HrzPosTech'].str.replace('0','N/A')

# Update the sea level indicators column (and save ID in separate column)
#RSL_Datapoints['Indicator_ID']=RSL_Datapoints['Indicator']
m = rslind.set_index('idrsl_ind')['Ind_name'].to_dict()
v = RSL_Datapoints.filter(items=['Indicator'])
RSL_Datapoints[v.columns] = v.replace(m)

# Update the sea level datum column (and save ID in separate column)
#RSL_Datapoints['SLdatum_ID']=RSL_Datapoints['SLdatum']
m = sldatum.set_index('SLdatum_ID')['SLdatumname'].to_dict()
v = RSL_Datapoints.filter(items=['SLdatum'])
RSL_Datapoints[v.columns] = v.replace(m)

# Update the elevation measurement column (and save ID in separate column)
#RSL_Datapoints['VrtMeasTech_ID']=RSL_Datapoints['VrtMeasTech']
m = vrt_meas.set_index('idvrtpostech')['VrtType'].to_dict()
v = RSL_Datapoints.filter(items=['VrtMeasTech'])
RSL_Datapoints[v.columns] = v.replace(m)

#Update the age selection column
ageselect = pd.DataFrame({'ID':[1,2,3,4,5,6], 'Technique':['U-Series',
                                                       'Amino Acid Racemization',
                                                       'Luminescence',
                                                       'Electro Spin Resonance',
                                                       'Chronostratigraphy',
                                                       'Other dating']})
RSL_Datapoints['SelectAge']=RSL_Datapoints['SelectAge'].astype(str) #####
RSL_Datapoints['SelectAge'] = (RSL_Datapoints['SelectAge'].str.split(',')
                                .explode()
                                .map(ageselect.assign(ID=ageselect.ID.astype(str))
                                     .set_index('ID')['Technique'])
                                .groupby(level=0).agg('\n '.join))


#Update Useries sample list with ID names (saving original ID list separately)
#RSL_Datapoints['Useries_ID_list']=RSL_Datapoints['Useries']
RSL_Datapoints['Useries']=RSL_Datapoints['Useries'].astype(str).replace('', '9999999') #####
df1 = pd.DataFrame([[np.nan] * len(useries.columns)], columns=useries.columns)
useries_mod = df1.append(useries, ignore_index=True)
useries_mod.loc[[0],'ID_Useries'] = 9999999
useries_mod.loc[[0],'AnalysisID'] = ''
useries_mod['ID_Useries'] = useries_mod['ID_Useries'].astype(int)

RSL_Datapoints['Useries'] = (RSL_Datapoints['Useries'].str.split(',')
                                .explode()
                                .map(useries_mod.assign(ID_Useries=useries_mod.ID_Useries.astype(str))
                                     .set_index('ID_Useries')['AnalysisID'])
                                .groupby(level=0).agg('\n '.join))

# Update AAR sample list with ID names (saving original ID list separately)
#RSL_Datapoints['AAR_ID_list']=RSL_Datapoints['AAR']
RSL_Datapoints['AAR']=RSL_Datapoints['AAR'].astype(str).replace('', '9999999')
df1 = pd.DataFrame([[np.nan] * len(aar.columns)], columns=aar.columns)
aar_mod = df1.append(aar, ignore_index=True)
aar_mod.loc[[0],'ID AAR'] = 9999999
aar_mod.loc[[0],'AnalysisID'] = ''
aar_mod['ID AAR'] = aar_mod['ID AAR'].astype(int)
aar_mod.rename(columns={'ID AAR': 'ID_AAR'}, inplace=True)
RSL_Datapoints['AAR'] = (RSL_Datapoints['AAR'].str.split(',')
                                .explode()
                                .map(aar_mod.assign(ID_AAR=aar_mod.ID_AAR.astype(str))
                                     .set_index('ID_AAR')['AnalysisID'])
                                .groupby(level=0).agg('\n '.join))

# Update luminescence sample list with ID names (saving original ID list separately)
#RSL_Datapoints['Lum_ID_list']=RSL_Datapoints['Luminescence']
RSL_Datapoints['Luminescence']=RSL_Datapoints['Luminescence'].astype(str).replace('', '9999999')
df1 = pd.DataFrame([[np.nan] * len(luminescence.columns)], columns=luminescence.columns)
luminescence_mod = df1.append(luminescence, ignore_index=True)
luminescence_mod.loc[[0],'LUM_ID'] = 9999999
luminescence_mod.loc[[0],'AnalysisID'] = ''
luminescence_mod['LUM_ID'] = luminescence_mod['LUM_ID'].astype(int)
RSL_Datapoints['Luminescence'] = (RSL_Datapoints['Luminescence'].str.split(',')
                                .explode()
                                .map(luminescence_mod.assign(LUM_ID=luminescence_mod.LUM_ID.astype(str))
                                     .set_index('LUM_ID')['AnalysisID'])
                                .groupby(level=0).agg('\n '.join))

# Update luminescence sample list with ID names (saving original ID list separately)
#RSL_Datapoints['ESR_ID_list']=RSL_Datapoints['ESR']
RSL_Datapoints['ESR']=RSL_Datapoints['ESR'].astype(str).replace('', '9999999')
df1 = pd.DataFrame([[np.nan] * len(esr.columns)], columns=esr.columns)
esr_mod = df1.append(esr, ignore_index=True)
esr_mod.loc[[0],'ESR_ID'] = 9999999
esr_mod.loc[[0],'AnalysisID'] = ''
esr_mod['ESR_ID'] = esr_mod['ESR_ID'].astype(int)
RSL_Datapoints['ESR'] = (RSL_Datapoints['ESR'].str.split(',')
                                .explode()
                                .map(esr_mod.assign(ESR_ID=esr_mod.ESR_ID.astype(str))
                                     .set_index('ESR_ID')['AnalysisID'])
                                .groupby(level=0).agg('\n '.join))

# Update luminescence sample list with ID names (saving original ID list separately)
#RSL_Datapoints['Strat_ID_list']=RSL_Datapoints['Stratcontext']
RSL_Datapoints['Stratcontext']=RSL_Datapoints['Stratcontext'].astype(str).replace('', '9999999')
df1 = pd.DataFrame([[np.nan] * len(strat.columns)], columns=strat.columns)
strat_mod = df1.append(strat, ignore_index=True)
strat_mod.loc[[0],'Strat_ID'] = 9999999
strat_mod.loc[[0],'StratName'] = ''
strat_mod['Strat_ID'] = strat_mod['Strat_ID'].astype(int)
RSL_Datapoints['Stratcontext'] = (RSL_Datapoints['Stratcontext'].str.split(',')
                                .explode()
                                .map(strat_mod.assign(Strat_ID=strat_mod.Strat_ID.astype(str))
                                     .set_index('Strat_ID')['StratName'])
                                .groupby(level=0).agg('\n '.join))

# Update luminescence sample list with ID names (saving original ID list separately)
#RSL_Datapoints['Other_age_ID_list']=RSL_Datapoints['Other_age']
RSL_Datapoints['Other_age']=RSL_Datapoints['Other_age'].astype(str).replace('', '9999999')
df1 = pd.DataFrame([[np.nan] * len(other.columns)], columns=other.columns)
other_mod = df1.append(other, ignore_index=True)
other_mod.loc[[0],'idOther_dating'] = 9999999
other_mod.loc[[0],'Short name'] = ''
other_mod['idOther_dating'] = other_mod['idOther_dating'].astype(int)
RSL_Datapoints['Other_age'] = (RSL_Datapoints['Other_age'].str.split(',')
                                .explode()
                                .map(other_mod.assign(idOther_dating=other_mod.idOther_dating.astype(str))
                                     .set_index('idOther_dating')['Short name'])
                                .groupby(level=0).agg('\n '.join))

# Created and Updated by
m = user.set_index('login')['name'].to_dict()
v = RSL_Datapoints.filter(items=['Createdby'])
RSL_Datapoints[v.columns] = v.replace(m)
m = user.set_index('login')['name'].to_dict()
v = RSL_Datapoints.filter(items=['Updatedby'])
RSL_Datapoints[v.columns] = v.replace(m)

RSL_Datapoints['Elev_upper'] = pd.to_numeric(RSL_Datapoints['Elev_upper'], errors='coerce')
RSL_Datapoints['Elev_lower'] = pd.to_numeric(RSL_Datapoints['Elev_lower'], errors='coerce')
RSL_Datapoints['UppLowErr'] = pd.to_numeric(RSL_Datapoints['UppLowErr'], errors='coerce')

###### Work on RSL_Ind dataframe ######
#Update references
RSL_Ind['Ref_indicator']=RSL_Ind['Ref_indicator'].astype(str).replace('', '9999999')
df1 = pd.DataFrame([[np.nan] * len(references.columns)], columns=references.columns)
ref = df1.append(references, ignore_index=True)
ref.loc[[0],'Ref_ID'] = 9999999
ref.loc[[0],'ShortRef'] = ''
ref['Ref_ID'] = ref['Ref_ID'].astype(int)
RSL_Ind['Ref_indicator'] = (RSL_Ind['Ref_indicator'].str.split(',')
                                .explode()
                                .map(ref.assign(Ref_ID=ref.Ref_ID.astype(str))
                                     .set_index('Ref_ID')['ShortRef'])
                                .groupby(level=0).agg('\n '.join))

#Update Createdby and Updatedby
m = user.set_index('login')['name'].to_dict()
v = RSL_Ind.filter(items=['Createdby'])
RSL_Ind[v.columns] = v.replace(m)
m = user.set_index('login')['name'].to_dict()
v = RSL_Ind.filter(items=['Updatedby'])
RSL_Ind[v.columns] = v.replace(m)

###### Work on vrt_meas dataframe ######
#Update Createdby and Updatedby
m = user.set_index('login')['name'].to_dict()
v = vrt_meas.filter(items=['Createdby'])
vrt_meas[v.columns] = v.replace(m)
m = user.set_index('login')['name'].to_dict()
v = vrt_meas.filter(items=['Updatedby'])
vrt_meas[v.columns] = v.replace(m)

###### Work on hrz_meas dataframe ######
#Update Createdby and Updatedby
m = user.set_index('login')['name'].to_dict()
v = hrz_meas.filter(items=['Createdby'])
hrz_meas[v.columns] = v.replace(m)
m = user.set_index('login')['name'].to_dict()
v = hrz_meas.filter(items=['Updatedby'])
hrz_meas[v.columns] = v.replace(m)

###### Work on sl_datum dataframe ######
#Update references
sl_datum['Ref_SLdatum']=sl_datum['Ref_SLdatum'].astype(str).replace('', '9999999')
df1 = pd.DataFrame([[np.nan] * len(references.columns)], columns=references.columns)
ref = df1.append(references, ignore_index=True)
ref.loc[[0],'Ref_ID'] = 9999999
ref.loc[[0],'ShortRef'] = ''
ref['Ref_ID'] = ref['Ref_ID'].astype(int)
sl_datum['Ref_SLdatum'] = (sl_datum['Ref_SLdatum'].str.split(',')
                                .explode()
                                .map(ref.assign(Ref_ID=ref.Ref_ID.astype(str))
                                     .set_index('Ref_ID')['ShortRef'])
                                .groupby(level=0).agg('\n '.join))

#Update Createdby
m = user.set_index('login')['name'].to_dict()
v = sl_datum.filter(items=['Createdby'])
sl_datum[v.columns] = v.replace(m)
m = user.set_index('login')['name'].to_dict()
v = sl_datum.filter(items=['Updatedby'])
sl_datum[v.columns] = v.replace(m)

###### Work on esr dataframe ######
#Update references
esr['Refs']=esr['Refs'].astype(str).replace('', '9999999')
df1 = pd.DataFrame([[np.nan] * len(references.columns)], columns=references.columns)
ref = df1.append(references, ignore_index=True)
ref.loc[[0],'Ref_ID'] = 9999999
ref.loc[[0],'ShortRef'] = ''
ref['Ref_ID'] = ref['Ref_ID'].astype(int)
esr['Refs'] = (esr['Refs'].str.split(',')
                                .explode()
                                .map(ref.assign(Ref_ID=ref.Ref_ID.astype(str))
                                     .set_index('Ref_ID')['ShortRef'])
                                .groupby(level=0).agg('\n '.join))

#Update Accepted
accepted = pd.DataFrame({'ID':[0,1], 'Answer':['No','Yes']})
m = accepted.set_index('ID')['Answer'].to_dict()
v = esr.filter(items=['Accepted'])
esr[v.columns] = v.replace(m)

#Update the sea level datum column
esr['Original_datum']=esr['Original_datum'].replace('', '0')
esr['Original_datum'] = esr.Original_datum.astype(int)
m = sl_datum.set_index('SLdatum_ID')['SLdatumname'].to_dict()
v = esr.filter(items=['Original_datum'])
esr[v.columns] = v.replace(m)
esr['Original_datum'] = esr.Original_datum.astype(str)
esr['Original_datum']=esr['Original_datum'].str.replace('0', 'N/A')

#Update the elevation measurement column
esr['Elev_meas_method']=esr['Elev_meas_method'].replace('', '0')
esr['Elev_meas_method'] = esr.Elev_meas_method.astype(int)
m = vrt_meas.set_index('idvrtpostech')['VrtType'].to_dict()
v = esr.filter(items=['Elev_meas_method'])
esr[v.columns] = v.replace(m)
esr['Elev_meas_method'] = esr.Elev_meas_method.astype(str)
esr['Elev_meas_method'] = esr['Elev_meas_method'].str.replace('0','N/A')

#Update Createdby
m = user.set_index('login')['name'].to_dict()
v = esr.filter(items=['Createdby'])
esr[v.columns] = v.replace(m)
m = user.set_index('login')['name'].to_dict()
v = esr.filter(items=['Updatedby'])
esr[v.columns] = v.replace(m)

#Update MIS choice
esr['MISchoice']=esr['MISchoice'].replace('', '9999')
esr['MISchoice'] = esr.MISchoice.astype(int)
m = MIS_ages.set_index('MIS ID')['MIS name'].to_dict()
v = esr.filter(items=['MISchoice'])
esr[v.columns] = v.replace(m)

###### Work on lum dataframe ######
#Update references
lum['lum_ref']=lum['lum_ref'].astype(str).replace('', '9999999')
df1 = pd.DataFrame([[np.nan] * len(references.columns)], columns=references.columns)
ref = df1.append(references, ignore_index=True)
ref.loc[[0],'Ref_ID'] = 9999999
ref.loc[[0],'ShortRef'] = ''
ref['Ref_ID'] = ref['Ref_ID'].astype(int)
lum['lum_ref'] = (lum['lum_ref'].str.split(',')
                                .explode()
                                .map(ref.assign(Ref_ID=ref.Ref_ID.astype(str))
                                     .set_index('Ref_ID')['ShortRef'])
                                .groupby(level=0).agg('\n '.join))

#Update the sea level datum column
lum['Original_datum']=lum['Original_datum'].replace('', '0')
lum['Original_datum'] = lum.Original_datum.astype(int)
m = sl_datum.set_index('SLdatum_ID')['SLdatumname'].to_dict()
v = lum.filter(items=['Original_datum'])
lum[v.columns] = v.replace(m)
lum['Original_datum'] = lum.Original_datum.astype(str)
lum['Original_datum']=lum['Original_datum'].str.replace('0', 'N/A')

#Update the elevation measurement column
lum['Elev_meas_method']=lum['Elev_meas_method'].replace('', '0')
lum['Elev_meas_method'] = lum.Elev_meas_method.astype(int)
m = vrt_meas.set_index('idvrtpostech')['VrtType'].to_dict()
v = lum.filter(items=['Elev_meas_method'])
lum[v.columns] = v.replace(m)
lum['Elev_meas_method'] = lum.Elev_meas_method.astype(str)
lum['Elev_meas_method'] = lum['Elev_meas_method'].str.replace('0','N/A')

#Update Createdby
m = user.set_index('login')['name'].to_dict()
v = lum.filter(items=['Createdby'])
lum[v.columns] = v.replace(m)
m = user.set_index('login')['name'].to_dict()
v = lum.filter(items=['Updatedby'])
lum[v.columns] = v.replace(m)

#Update MIS choice
lum['MISchoice']=lum['MISchoice'].replace('', '9999')
lum['MISchoice'] = lum.MISchoice.astype(int)
m = MIS_ages.set_index('MIS ID')['MIS name'].to_dict()
v = lum.filter(items=['MISchoice'])
lum[v.columns] = v.replace(m)

###### Work on strat dataframe ######
#Update references
strat['StratRef']=strat.StratRef.astype(str)
strat['StratRef']=strat['StratRef'].replace('', '9999999')
df1 = pd.DataFrame([[np.nan] * len(references.columns)], columns=references.columns)
ref = df1.append(references, ignore_index=True)
ref.loc[[0],'Ref_ID'] = 9999999
ref.loc[[0],'ShortRef'] = ''
ref['Ref_ID'] = ref['Ref_ID'].astype(int)
strat['StratRef'] = (strat['StratRef'].str.split(',')
                                .explode()
                                .map(ref.assign(Ref_ID=ref.Ref_ID.astype(str))
                                     .set_index('Ref_ID')['ShortRef'])
                                .groupby(level=0).agg('\n '.join))
#Update Createdby
m = user.set_index('login')['name'].to_dict()
v = strat.filter(items=['Createdby'])
strat[v.columns] = v.replace(m)
m = user.set_index('login')['name'].to_dict()
v = strat.filter(items=['Updatedby'])
strat[v.columns] = v.replace(m)

#Update MIS choice
strat['MISchoice']=strat['MISchoice'].replace('', '9999')
strat['MISchoice'] = strat.MISchoice.astype(int)
m = MIS_ages.set_index('MIS ID')['MIS name'].to_dict()
v = strat.filter(items=['MISchoice'])
strat[v.columns] = v.replace(m)

###### Work on other dataframe ######
#Update references
other['Ref']=other['Ref'].astype(str).replace('', '9999999')
df1 = pd.DataFrame([[np.nan] * len(references.columns)], columns=references.columns)
ref = df1.append(references, ignore_index=True)
ref.loc[[0],'Ref_ID'] = 9999999
ref.loc[[0],'ShortRef'] = ''
ref['Ref_ID'] = ref['Ref_ID'].astype(int)
other['Ref'] = (other['Ref'].str.split(',')
                                .explode()
                                .map(ref.assign(Ref_ID=ref.Ref_ID.astype(str))
                                     .set_index('Ref_ID')['ShortRef'])
                                .groupby(level=0).agg('\n '.join))

#Update Createdby
m = user.set_index('login')['name'].to_dict()
v = other.filter(items=['Createdby'])
other[v.columns] = v.replace(m)
m = user.set_index('login')['name'].to_dict()
v = other.filter(items=['Updatedby'])
other[v.columns] = v.replace(m)

#Update MIS choice
other['MISchoice']=other['MISchoice'].replace('', '9999')
other['MISchoice'] = other.MISchoice.astype(int)
m = MIS_ages.set_index('MIS ID')['MIS name'].to_dict()
v = other.filter(items=['MISchoice'])
other[v.columns] = v.replace(m)

###### Work on useries dataframe ######
useries['Original_elevation_datum_used']=useries['Original_elevation_datum_used'].replace('', '0')
useries['Original_elevation_datum_used'] = useries.Original_elevation_datum_used.astype(int)
useries['How_elevation_derived']=useries['How_elevation_derived'].replace('', '0')
useries['How_elevation_derived']=useries.How_elevation_derived.astype(int)

#Update references
useries['Source']=useries['Source'].astype(str).replace('', '9999999')
df1 = pd.DataFrame([[np.nan] * len(references.columns)], columns=references.columns)
ref = df1.append(references, ignore_index=True)
ref.loc[[0],'Ref_ID'] = 9999999
ref.loc[[0],'ShortRef'] = ''
ref['Ref_ID'] = ref['Ref_ID'].astype(int)
useries['Source'] = (useries['Source'].str.split(',')
                            .explode()
                            .map(ref.assign(Ref_ID=ref.Ref_ID.astype(str))
                            .set_index('Ref_ID')['ShortRef'])
                            .groupby(level=0).agg('\n '.join))

#Update 'other study' references
#something makes this explode when querying by country. This is the quick fix
if query_type=='user':
 useries.fillna('',inplace=True)
 print('querying by user')
else:
 print('querying by country')
useries['Other ref'] = useries['Other ref'].replace('N/A', '')
useries['Other ref'] = useries['Other ref'].replace('', '0')
useries['Other ref'] = useries['Other ref'].astype(int)
m = references.set_index('Ref_ID')['ShortRef'].to_dict()
v = useries.filter(items=['Other ref'])
useries[v.columns] = v.replace(m)
useries['Other ref'] = useries['Other ref'].astype(str)
useries['Other ref'] = useries['Other ref'].replace('0', 'n/a')

#Update the sea level datum column
m = sl_datum.set_index('SLdatum_ID')['SLdatumname'].to_dict()
v = useries.filter(items=['Original_elevation_datum_used'])
useries[v.columns] = v.replace(m)
useries['Original_elevation_datum_used'] = useries.Original_elevation_datum_used.astype(str)
useries['Original_elevation_datum_used'] = useries['Original_elevation_datum_used'].str.replace('0',' ')

#Update the elevation measurement column
m = vrt_meas.set_index('idvrtpostech')['VrtType'].to_dict()
v = useries.filter(items=['How_elevation_derived'])
useries[v.columns] = v.replace(m)
useries['How_elevation_derived'] = useries.How_elevation_derived.astype(str)
useries['How_elevation_derived'] = useries['How_elevation_derived'].str.replace('0',' ')

#Update MIS choice
useries['MISchoice']=useries['MISchoice'].replace('', '9999')
useries['MISchoice'] = useries.MISchoice.astype(int)
m = MIS_ages.set_index('MIS ID')['MIS name'].to_dict()
v = useries.filter(items=['MISchoice'])
useries[v.columns] = v.replace(m)

#Update Createdby
m = user.set_index('login')['name'].to_dict()
v = useries.filter(items=['Createdby'])
useries[v.columns] = v.replace(m)
m = user.set_index('login')['name'].to_dict()
v = useries.filter(items=['Updatedby'])
useries[v.columns] = v.replace(m)

###### Work on aar dataframe ######
aar['Accepted'] = aar.Accepted.astype(int)
#Update references
aar['AARRef']=aar['AARRef'].astype(str).replace('', '9999999')
df1 = pd.DataFrame([[np.nan] * len(references.columns)], columns=references.columns)
ref = df1.append(references, ignore_index=True)
ref.loc[[0],'Ref_ID'] = 9999999
ref.loc[[0],'ShortRef'] = 'N/A'
ref['Ref_ID'] = ref['Ref_ID'].astype(int)
aar['AARRef'] = (aar['AARRef'].str.split(',')
                                .explode()
                                .map(ref.assign(Ref_ID=ref.Ref_ID.astype(str))
                                     .set_index('Ref_ID')['ShortRef'])
                                .groupby(level=0).agg('\n '.join))

#Update Accepted
accepted = pd.DataFrame({'ID':[0,1], 'Answer':['No','Yes']})
m = accepted.set_index('ID')['Answer'].to_dict()
v = aar.filter(items=['Accepted'])
aar[v.columns] = v.replace(m)

#Update the sea level datum column
aar['Original_datum']=aar['Original_datum'].replace('', '9999')
aar['Original_datum'] = aar.Original_datum.astype(int)
m = sl_datum.set_index('SLdatum_ID')['SLdatumname'].to_dict()
v = aar.filter(items=['Original_datum'])
aar[v.columns] = v.replace(m)
aar['Original_datum'] = aar.Original_datum.astype(str)
aar['Original_datum']=aar['Original_datum'].str.replace('9999', '')

#Update the elevation measurement column
aar['Elev_meas_method']=aar['Elev_meas_method'].replace('', '9999')
aar['Elev_meas_method'] = aar.Elev_meas_method.astype(int)
m = vrt_meas.set_index('idvrtpostech')['VrtType'].to_dict()
v = aar.filter(items=['Elev_meas_method'])
aar[v.columns] = v.replace(m)
aar['Elev_meas_method'] = aar.Elev_meas_method.astype(str)
aar['Elev_meas_method'] = aar['Elev_meas_method'].str.replace('9999',' ')

#Update MIS choice
aar['MISchoice'] = aar.MISchoice.astype(int)
m = MIS_ages.set_index('MIS ID')['MIS name'].to_dict()
v = aar.filter(items=['MISchoice'])
aar[v.columns] = v.replace(m)

#Update Whole-rock radio button
accepted = pd.DataFrame({'ID':[0,1], 'Answer':['No','Yes']})
m = accepted.set_index('ID')['Answer'].to_dict()
v = aar.filter(items=['WRock'])
aar[v.columns] = v.replace(m)

#Update Independent age constraints
aar['ShowIndep'] = aar.ShowIndep.astype(int)
v = aar.filter(items=['ShowIndep'])
aar[v.columns] = v.replace(m)

#Update Calibration data
aar['Showblock'] = aar.Showblock.astype(int)
v = aar.filter(items=['Showblock'])
aar[v.columns] = v.replace(m)

#Update calibration references
aar['IndepAgeRef']=aar['IndepAgeRef'].astype(str).replace('', '9999999')
df1 = pd.DataFrame([[np.nan] * len(references.columns)], columns=references.columns)
ref = df1.append(references, ignore_index=True)
ref.loc[[0],'Ref_ID'] = 9999999
ref.loc[[0],'ShortRef'] = ''
ref['Ref_ID'] = ref['Ref_ID'].astype(int)
aar['IndepAgeRef'] = (aar['IndepAgeRef'].str.split(',')
                                .explode()
                                .map(ref.assign(Ref_ID=ref.Ref_ID.astype(str))
                                     .set_index('Ref_ID')['ShortRef'])
                                .groupby(level=0).agg('\n '.join))

#Update Useries sample list
aar['Useries constraint']=aar['Useries constraint'].astype(str).replace('', '9999999')
df1 = pd.DataFrame([[np.nan] * len(useries.columns)], columns=useries.columns)
useries_mod = df1.append(useries, ignore_index=True)
useries_mod.loc[[0],'ID_Useries'] = 9999999
useries_mod.loc[[0],'AnalysisID'] = ''
useries_mod['ID_Useries'] = useries_mod['ID_Useries'].astype(int)
aar['Useries constraint'] = (aar['Useries constraint'].str.split(',')
                                .explode()
                                .map(useries_mod.assign(ID_Useries=useries_mod.ID_Useries.astype(str))
                                     .set_index('ID_Useries')['AnalysisID']
                                     .drop_duplicates(keep='first'))
                                .groupby(level=0).agg('\n '.join))

#Update luminescence sample list
aar['Luminescene constraint']=aar['Luminescene constraint'].astype(str).replace('', '9999999')
df1 = pd.DataFrame([[np.nan] * len(luminescence.columns)], columns=luminescence.columns)
luminescence_mod = df1.append(luminescence, ignore_index=True)
luminescence_mod.loc[[0],'LUM_ID'] = 9999999
luminescence_mod.loc[[0],'AnalysisID'] = ''
luminescence_mod['LUM_ID'] = luminescence_mod['LUM_ID'].astype(int)
aar['Luminescene constraint'] = (aar['Luminescene constraint'].str.split(',')
                                .explode()
                                .map(luminescence_mod.assign(LUM_ID=luminescence_mod.LUM_ID.astype(str))
                                     .set_index('LUM_ID')['AnalysisID'])
                                .groupby(level=0).agg('\n '.join))

#Update ESR sample list
aar['ESR constraint']=aar['ESR constraint'].astype(str).replace('', '9999999')
df1 = pd.DataFrame([[np.nan] * len(esr.columns)], columns=esr.columns)
esr_mod = df1.append(esr, ignore_index=True)
esr_mod.loc[[0],'ESR_ID'] = 9999999
esr_mod.loc[[0],'AnalysisID'] = ''
esr_mod['ESR_ID'] = esr_mod['ESR_ID'].astype(int)
aar['ESR constraint'] = (aar['ESR constraint'].str.split(',')
                                .explode()
                                .map(esr_mod.assign(ESR_ID=esr_mod.ESR_ID.astype(str))
                                     .set_index('ESR_ID')['AnalysisID'])
                                .groupby(level=0).agg('\n '.join))

#Update Stratigraphic ages sample list
aar['Strat constraint']=aar['Strat constraint'].astype(str).replace('', '9999999')
df1 = pd.DataFrame([[np.nan] * len(strat.columns)], columns=strat.columns)
strat_mod = df1.append(strat, ignore_index=True)
strat_mod.loc[[0],'Strat_ID'] = 9999999
strat_mod.loc[[0],'StratName'] = ''
strat_mod['Strat_ID'] = strat_mod['Strat_ID'].astype(int)
aar['Strat constraint'] = (aar['Strat constraint'].str.split(',')
                                .explode()
                                .map(strat_mod.assign(Strat_ID=strat_mod.Strat_ID.astype(str))
                                     .set_index('Strat_ID')['StratName'])
                                .groupby(level=0).agg('\n '.join))

#Update Createdby
m = user.set_index('login')['name'].to_dict()
v = aar.filter(items=['Createdby'])
aar[v.columns] = v.replace(m)
m = user.set_index('login')['name'].to_dict()
v = aar.filter(items=['Updatedby'])
aar[v.columns] = v.replace(m)

###### Work on references_query dataframe ######
#Update Createdby
m = user.set_index('login')['name'].to_dict()
v = References_query.filter(items=['Createdby'])
References_query[v.columns] = v.replace(m)
m = user.set_index('login')['name'].to_dict()
v = References_query.filter(items=['Updatedby'])
References_query[v.columns] = v.replace(m)

###### Obtain list of creators / updaters ######
creators=pd.DataFrame()
creators['usrs']=pd.concat([RSL_Datapoints['Createdby'],RSL_Datapoints['Updatedby'],
                                aar['Createdby'],aar['Updatedby'],
                                esr['Createdby'],esr['Updatedby'],
                                lum['Createdby'],lum['Updatedby'],
                                useries['Createdby'],useries['Updatedby'],
                                strat['Createdby'],strat['Updatedby'],
                                other['Createdby'],other['Updatedby'],
                                RSL_Ind['Createdby'],RSL_Ind['Updatedby'],
                                vrt_meas['Createdby'],vrt_meas['Updatedby'],
                                hrz_meas['Createdby'],hrz_meas['Updatedby'],
                                sl_datum['Createdby'],sl_datum['Updatedby'],
                                References_query['Createdby'],References_query['Updatedby']
                                ])
creators = creators[creators.usrs != '']
user_contrib=creators['usrs'].value_counts()
user_contrib_df = pd.DataFrame(data=user_contrib).reset_index()

###### Work on Summary dataframe ######
#Nation and region substitution
Summary['Nation'] = Summary.Nation.replace('', '999')
Summary['Nation'] = Summary.Nation.astype(int)
m = countries.set_index('id')['name'].to_dict()
v = Summary.filter(items=['Nation'])
Summary[v.columns] = v.replace(m)
Summary['Region'] = Summary.Region.astype(int)
m = regions.set_index('id')['name'].to_dict()
v = Summary.filter(items=['Region'])
Summary[v.columns] = v.replace(m)

#RSL Indicator substitution
Summary['RSL Indicator'] = Summary['RSL Indicator'].astype(str).replace('Yes', '9999')
df1 = pd.DataFrame([[np.nan] * len(rslind.columns)], columns=rslind.columns)
rslind = df1.append(rslind, ignore_index=True)
rslind.loc[[0],'idrsl_ind'] = 9999
rslind.loc[[0],'Ind_name'] = 'Single sample RSL estimate'
Summary['RSL Indicator'] = Summary['RSL Indicator'].astype(int)
m = rslind.set_index('idrsl_ind')['Ind_name'].to_dict()
v = Summary.filter(items=['RSL Indicator'])
Summary[v.columns] = v.replace(m)

# Update the sea level datum column (and save ID in separate column)
Summary['Vertical datum'] = Summary['Vertical datum'].replace('', '9999')
Summary['Vertical datum'] = Summary['Vertical datum'].astype(int)
df1 = pd.DataFrame([[np.nan] * len(sldatum.columns)], columns=sldatum.columns)
sldatum = df1.append(sldatum, ignore_index=True)
sldatum.loc[[0],'SLdatum_ID'] = 9999
sldatum.loc[[0],'SLdatumname'] = 'Not reported'
m = sldatum.set_index('SLdatum_ID')['SLdatumname'].to_dict()
v = Summary.filter(items=['Vertical datum'])
Summary[v.columns] = v.replace(m)

#Update MIS choice
Summary['Marine Isotopic Stage']=Summary['Marine Isotopic Stage'].replace('', '9999')
Summary['Marine Isotopic Stage'] = Summary['Marine Isotopic Stage'].astype(int)
m = MIS_ages.set_index('MIS ID')['MIS name'].to_dict()
v = Summary.filter(items=['Marine Isotopic Stage'])
Summary[v.columns] = v.replace(m)

# Update the elevation measurement column (and save ID in separate column)
Summary['Elevation measurement technique'] = Summary['Elevation measurement technique'].astype(int)
df1 = pd.DataFrame([[np.nan] * len(vrt_meas.columns)], columns=vrt_meas.columns)
elev_meas = df1.append(vrt_meas, ignore_index=True)
elev_meas.loc[[0],'idvrtpostech'] = 9999
elev_meas.loc[[0],'Measurement technique'] = 'Not reported'
m = elev_meas.set_index('idvrtpostech')['VrtType'].to_dict()
v = Summary.filter(items=['Elevation measurement technique'])
Summary[v.columns] = v.replace(m)

#References
Summary['Reference(s)'].replace({',,': ','}, inplace=True, regex=True)
Summary['Reference(s)'].replace({',,,': ','}, inplace=True, regex=True)
Summary['Reference(s)'].replace({',,,,': ','}, inplace=True, regex=True)
Summary['Reference(s)'].replace({',,,,,': ','}, inplace=True, regex=True)
Summary['Reference(s)'].replace({',,,,,,': ','}, inplace=True, regex=True)
Summary['Reference(s)'].replace({',,,,,,,': ','}, inplace=True, regex=True)
Summary['Reference(s)'].replace({',,,,,,,,': ','}, inplace=True, regex=True)
Summary['Reference(s)'].replace({',,,,,,,,,': ','}, inplace=True, regex=True)

Summary['Reference(s)']=Summary['Reference(s)'].astype(str)
def remove_dup(strng):
    '''
     Input a string and split them 
    '''
    return ','.join(list(dict.fromkeys(strng.split(','))))
Summary['Reference(s)'] = Summary['Reference(s)'].apply(lambda x: remove_dup(x))
Summary['Reference(s)']=Summary['Reference(s)'].str.rstrip(',')
Summary['Reference(s)'] = (Summary['Reference(s)'].str.split(',')
                                .explode()
                                .map(ref.assign(Ref_ID=ref.Ref_ID.astype(str))
                                     .set_index('Ref_ID')['ShortRef'])
                                .groupby(level=0).agg('\n '.join))
#Update record creator
m = user.set_index('login')['name'].to_dict()
v = Summary.filter(items=['Record Created by'])
Summary[v.columns] = v.replace(m)

#Housekeeping
Summary['Reported age (ka)'].replace('N/A', '',inplace=True)
Summary['Reported age uncertainty (ka)'].replace('N/A', '',inplace=True)
Summary['U-Series recalculated age (ka)'].replace('N/A', '',inplace=True)
Summary['U-Series corrected age (speleothems, ka)'].replace('N/A', '',inplace=True)
Summary['U-Series corrected age uncertainty (speleothems, ka)'].replace('N/A', '',inplace=True)
Summary['Stratigraphy Upper Age (ka)'] = pd.to_numeric(Summary['Stratigraphy Upper Age (ka)'],errors='coerce')
Summary['Stratigraphy Lower Age (ka)'] = pd.to_numeric(Summary['Stratigraphy Lower Age (ka)'],errors='coerce')

Summary['Marine Isotopic Stage'].replace('N/A', '',inplace=True)
Summary['Site']=Summary['Site'].str.cat(Summary[['Subsite']].astype(str), sep="\n")

#### Rename columns with labels from the interface
print ('Putting nice names to the database columns....')
rsl_dict=pd.Series(walis_cols[0].Field.values,index=walis_cols[0].Comment).to_dict()
rsl_dict = {v: k for k, v in rsl_dict.items()}
RSL_Datapoints.rename(columns=rsl_dict,inplace=True)

useries_dict=pd.Series(walis_cols[9].Field.values,index=walis_cols[9].Comment).to_dict()
useries_dict = {v: k for k, v in useries_dict.items()}
useries.rename(columns=useries_dict,inplace=True)

RSL_Ind_dict=pd.Series(walis_cols[6].Field.values,index=walis_cols[6].Comment).to_dict()
RSL_Ind_dict = {v: k for k, v in RSL_Ind_dict.items()}
RSL_Ind.rename(columns=RSL_Ind_dict,inplace=True)

vrt_meas_dict=pd.Series(walis_cols[8].Field.values,index=walis_cols[8].Comment).to_dict()
vrt_meas_dict = {v: k for k, v in vrt_meas_dict.items()}
vrt_meas.rename(columns=vrt_meas_dict,inplace=True)

hrz_meas_dict=pd.Series(walis_cols[5].Field.values,index=walis_cols[5].Comment).to_dict()
hrz_meas_dict = {v: k for k, v in hrz_meas_dict.items()}
hrz_meas.rename(columns=hrz_meas_dict,inplace=True)

sl_datum_dict=pd.Series(walis_cols[7].Field.values,index=walis_cols[7].Comment).to_dict()
sl_datum_dict = {v: k for k, v in sl_datum_dict.items()}
sl_datum.rename(columns=sl_datum_dict,inplace=True)

aar_dict=pd.Series(walis_cols[10].Field.values,index=walis_cols[10].Comment).to_dict()
aar_dict = {v: k for k, v in aar_dict.items()}
aar.rename(columns=aar_dict,inplace=True)

esr_dict=pd.Series(walis_cols[12].Field.values,index=walis_cols[12].Comment).to_dict()
esr_dict = {v: k for k, v in esr_dict.items()}
esr.rename(columns=esr_dict,inplace=True)

lum_dict=pd.Series(walis_cols[11].Field.values,index=walis_cols[11].Comment).to_dict()
lum_dict = {v: k for k, v in lum_dict.items()}
lum.rename(columns=lum_dict,inplace=True)

strat_dict=pd.Series(walis_cols[13].Field.values,index=walis_cols[13].Comment).to_dict()
strat_dict = {v: k for k, v in strat_dict.items()}
strat.rename(columns=strat_dict,inplace=True)

other_dict=pd.Series(walis_cols[14].Field.values,index=walis_cols[14].Comment).to_dict()
other_dict = {v: k for k, v in other_dict.items()}
other.rename(columns=other_dict,inplace=True)

ref_dict=pd.Series(walis_cols[4].Field.values,index=walis_cols[4].Comment).to_dict()
ref_dict = {v: k for k, v in ref_dict.items()}
References_query.rename(columns=ref_dict,inplace=True)

###### Create dataframes for RSL from corals and speleothems ######
useries_corals = useries[useries['Material type'] == 'Coral']
useries_moll = useries[useries['Material type'] == 'Mollusk or algae']
useries_speleo = useries[useries['Material type'] == 'Speleothem']
useries_oolite = useries[useries['Material type'] == 'Oolite']
useries_corals_RSL = useries[useries['Material type'] == 'Coral']
useries_corals_RSL = useries_corals_RSL[useries_corals_RSL['Are RSL estimates available for this record?'] == 'Yes']
useries_speleo_RSL = useries[useries['Material type'] == 'Speleothem']
useries_speleo_RSL = useries_speleo_RSL[useries_speleo_RSL['Are RSL estimates available for this record?'] == 'Yes']

##### Drop columns that are not used in certain U-Series instances #####
useries_corals_RSL.drop(columns=['How was speleothem mineralogy determined?','Speleothem mineralogy','Reported in situ?',
                             'Type of deposit','Distance from base of deposit (m)','Sampled material',
                             'Additional sample context','paleo RSL (m)','paleo RSL uncertainty (m)',
                             'Corrected reported age (ka)','Corrected reported age uncert. (ka, ±2σ)',
                             'Initial 234U/238U','Initial 234U/238U uncertainty (±2σ)','Measured 234U/238U',
                             'Measured 234U/238U uncertainty (±2σ)','Measured delta234U','Measured delta234U uncertainty (±2σ)',
                             'Age is Older/Equal/Younger than','Marine Isotopic Stage','Age determination'],inplace=True)
   
useries_speleo_RSL.drop(columns=['Are data on tectonics available?',
                             'Interpreted elevation relative to mllw/mlws (m)','Tectonic category',
                             'Published uplift rate (m/ky)','Published uncertainty in uplift rate (m/ky)',
                             'Interpreted uplift rate (m/ky)','Interpreted uplift rate uncertainty (m/ky)',
                             'Comments (uplift), including sources of uplift rates','Terrace ID',
                             'Facies description','Reported as in situ?','Reported as in growth position?',
                             'Taxa information (as reported)','Family','Genus','Species',
                             'Original palaeodepth interpretation','Ecological metadata',
                             'Paleo water depth estimate (m)','Upper limit of living range (m)',
                             'Lower limit of living range (m)',
                             'Paleo water depth comments','Age is Older/Equal/Younger than',
                             'Marine Isotopic Stage','Age determination','Is this datapoint public?','Were U-Series data recalculated?',
                             'Are RSL estimates available for this record?','IGSN','Date of analysis',
                             'Reason for rejection','Accepted in other study?','Reason for rejection in other studies',
                             'Other study ID','Screening','Additional site information',
                             'Reported Latitude','Reported Longitude','Are Lat/Long estimated?','Comments on geographic coordinates',
                             'Elevation comments','Reported in situ?', 'Distance from base of deposit (m)',
                             'Sampled material','Additional sample context',
                             'How was speleothem mineralogy determined?','Speleothem mineralogy','Pa/Th age?','14C age?','Instrument','Decay constants',
                             'Comments on decay constants','Calibration method for 230Th/238U ratio',
                             'Calibration method for 234U/238U ratio','Comments on spike calibration',
                             'Other screening techniques applied','Published % calcite',
                             'Interpreted % calcite','[230Th/232Th]ACT backcalculated?',
                             '[232Th/238U]ACT backcalculated?','[230Th/238U]ACT backcalculated?',
                             '[234Th/238U]ACT backcalculated?','[232Th] (ppb)',
                             '[232Th] (ppb) uncertainty (±2σ)','[238U] (ppm)','[238U] (ppm) uncertainty (±2σ)',
                             'Atomic ratio (232Th/238U)*10^5','Initial 230Th/232Th','[230Th/232Th]ACT',
                             '[230Th/232Th]ACT uncertainty (±2σ)','[232Th/238U]ACT',
                             '[232Th/238U]ACT uncertainty (±2σ)','[230Th/234U]ACT',
                             '[230Th/234U]ACT uncertainty (±2σ)','[230Th/238U]ACT',
                             '[230Th/238U]ACT uncertainty (±2σ)','[234U/238U]ACT','[234U/238U]ACT uncertainty (±2σ)',
                             'Reported delta 234U initial (‰)','Reported delta 234U (‰) uncertainty (±2σ)',
                             'Comments on age determination','Reference material name for 230Th/238U',
                             'Reference material name for 234U/238U','Correction factor for 230Th/238U',
                             'Correction factor for 230Th/238U uncertainty (±2σ)','Correction factor for 234U/238U',
                             'Correction factor for 234U/238U uncertainty (±2σ)','Comments',
                             '[230Th/238U]ACT','[230Th/238U]ACT uncertainty (±2σ)','[234U/238U]ACT','[234U/238U]ACT uncertainty (±2σ)',
                             'Recalculated delta 234Ui (‰)','Recalculated delta 234Ui uncertainty (±2σ)',
                             'Recalculated Conventional Age uncert. w/ decay constant uncertainties (±2σ)',
                             'Recalculated delta 234Ui uncert. (±2σ) w/ decay constant uncertainties',
                             'Comments (age and delta234i)','Initial 234U/238U',
                             'Initial 234U/238U uncertainty (±2σ)','Measured 234U/238U',
                             'Measured 234U/238U uncertainty (±2σ)','Measured delta234U','Measured delta234U uncertainty (±2σ)'],inplace=True)

useries_corals.drop(columns=['How was speleothem mineralogy determined?','Speleothem mineralogy','Reported in situ?',
                             'Type of deposit','Distance from base of deposit (m)','Sampled material',
                             'Additional sample context','paleo RSL (m)','paleo RSL uncertainty (m)',
                             'Corrected reported age (ka)','Corrected reported age uncert. (ka, ±2σ)',
                             'Initial 234U/238U','Initial 234U/238U uncertainty (±2σ)','Measured 234U/238U',
                             'Measured 234U/238U uncertainty (±2σ)','Measured delta234U','Measured delta234U uncertainty (±2σ)',
                             'Age is Older/Equal/Younger than','Marine Isotopic Stage','Age determination'],inplace=True)
                             
useries_moll.drop(columns=['Were U-Series data recalculated?','Are RSL estimates available for this record?',
                           'Are data on tectonics available?','Accepted in other study?','Reason for rejection in other studies','Other study ID','Location','Site','Additional site information','Interpreted elevation relative to mllw/mlws (m)',
                           'Tectonic category','Published uplift rate (m/ky)',
                           'Published uncertainty in uplift rate (m/ky)','Interpreted uplift rate (m/ky)',
                           'Interpreted uplift rate uncertainty (m/ky)',
                           'Comments (uplift), including sources of uplift rates',
                           'Reported in situ?','Type of deposit','Distance from base of deposit (m)',
                           'Sampled material','Additional sample context','paleo RSL (m)',
                           'paleo RSL uncertainty (m)','Original palaeodepth interpretation',
                           'Ecological metadata','Paleo water depth estimate (m)',
                           'Upper limit of living range (m)','Lower limit of living range (m)',
                           'Paleo water depth comments','How was speleothem mineralogy determined?',
                           'Speleothem mineralogy','Other screening techniques applied','Reported age (ka)',
                           'Reported ageuncertainty (ka, ±2σ)','Corrected reported age (ka)',
                           'Corrected reported age uncert. (ka, ±2σ)',
                           'Reported delta 234U initial (‰)','Reported delta 234U (‰) uncertainty (±2σ)',
                           'Initial 234U/238U','Initial 234U/238U uncertainty (±2σ)','Measured 234U/238U',
                           'Measured 234U/238U uncertainty (±2σ)','Measured delta234U','Measured delta234U uncertainty (±2σ)',
                           'Comments on age determination','[230Th/238U]ACT','[230Th/238U]ACT uncertainty (±2σ)',
                           '[234U/238U]ACT','[234U/238U]ACT uncertainty (±2σ)','Recalculated Conventional Age (ka)',
                           'Recalculated Conventional Age uncert. (±2σ)','Recalculated delta 234Ui (‰)',
                           'Recalculated delta 234Ui uncertainty (±2σ)',
                           'Recalculated Conventional Age uncert. w/ decay constant uncertainties (±2σ)',
                           'Recalculated delta 234Ui uncert. (±2σ) w/ decay constant uncertainties',
                           'Comments (age and delta234i)'],inplace=True)
                           
useries_speleo.drop(columns=['Are data on tectonics available?',
                             'Interpreted elevation relative to mllw/mlws (m)','Tectonic category',
                             'Published uplift rate (m/ky)','Published uncertainty in uplift rate (m/ky)',
                             'Interpreted uplift rate (m/ky)','Interpreted uplift rate uncertainty (m/ky)',
                             'Comments (uplift), including sources of uplift rates','Terrace ID',
                             'Facies description','Reported as in situ?','Reported as in growth position?',
                             'Taxa information (as reported)','Family','Genus','Species',
                             'Original palaeodepth interpretation','Ecological metadata',
                             'Paleo water depth estimate (m)','Upper limit of living range (m)',
                             'Lower limit of living range (m)',
                             'Paleo water depth comments','Age is Older/Equal/Younger than',
                             'Marine Isotopic Stage','Age determination'],inplace=True)

useries_oolite.drop(columns=['How was speleothem mineralogy determined?','Speleothem mineralogy','Reported in situ?',
                             'Type of deposit','Distance from base of deposit (m)','Sampled material',
                             'Additional sample context','paleo RSL (m)','paleo RSL uncertainty (m)',
                             'Corrected reported age (ka)','Corrected reported age uncert. (ka, ±2σ)',
                             'Initial 234U/238U','Initial 234U/238U uncertainty (±2σ)','Measured 234U/238U',
                             'Measured 234U/238U uncertainty (±2σ)','Measured delta234U','Measured delta234U uncertainty (±2σ)',
                             'Age is Older/Equal/Younger than','Marine Isotopic Stage','Age determination','Are data on tectonics available?',
                             'Interpreted elevation relative to mllw/mlws (m)','Tectonic category',
                             'Published uplift rate (m/ky)','Published uncertainty in uplift rate (m/ky)',
                             'Interpreted uplift rate (m/ky)','Interpreted uplift rate uncertainty (m/ky)',
                             'Comments (uplift), including sources of uplift rates','Terrace ID',
                             'Facies description','Reported as in situ?','Reported as in growth position?',
                             'Taxa information (as reported)','Family','Genus','Species',
                             'Original palaeodepth interpretation','Ecological metadata',
                             'Paleo water depth estimate (m)','Upper limit of living range (m)',
                             'Lower limit of living range (m)',
                             'Paleo water depth comments'],inplace=True)
                             
print('Done!!')