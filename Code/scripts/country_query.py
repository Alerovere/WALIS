###### Take nations from existing dataframe ######
stringbit=', '.join(map(str,select_country.value))
print('Extracting values for the following nation(s): {}'.format(stringbit))
print('')
list_nations = list(select_country.value)

###### Initialize the empty dataframes ######
RSL_Datapoints = pd.DataFrame()
RSL_Ind = pd.DataFrame()
hrz_meas = pd.DataFrame()
aar_df = pd.DataFrame()
esr_df = pd.DataFrame()
lum_df = pd.DataFrame()
strat_df = pd.DataFrame()
other_df = pd.DataFrame()
useries_df = pd.DataFrame()
vrt_meas_df = pd.DataFrame()
sl_datum_df = pd.DataFrame()
References_query = pd.DataFrame()
Summary_df = pd.DataFrame()

###### Proceed to the extraction ######
for Nation in list_nations: 
 # RSL datapoints
 RSL_Datapoints=RSL_Datapoints.append(rsl_location[rsl_location.name == str(Nation)])
 RSL_Datapoints=pd.DataFrame(RSL_Datapoints).drop(columns=['geometry','continent','name'])
 #RSL indicators
 RSL_Ind=RSL_Ind.append(rslind.loc[rslind['idrsl_ind'].isin(RSL_Datapoints['Indicator']),:])
 #Geographic positioning
 hrz_meas=hrz_meas.append(hrzpos.loc[hrzpos['idposhrz'].isin(RSL_Datapoints['HrzPosTech']),:])
 #keep AAR in RSL datapoints in the nation
 AAR_1=pd.DataFrame(RSL_Datapoints['AAR'].str.split(',').explode()).replace('', np.nan).dropna(subset=['AAR']).astype(float)
 aar_df=aar.loc[aar['ID AAR'].isin(AAR_1['AAR']),:]
 #Electron Spin Resonance
 #keep ESR in RSL datapoints in nation
 ESR_1=pd.DataFrame(RSL_Datapoints['ESR'].str.split(',').explode()).replace('', np.nan).dropna(subset=['ESR']).astype(float)
 ESR_filter1=esr.loc[esr['ESR_ID'].isin(ESR_1['ESR']),:]
 #keep ESR used as constraints in AAR table
 ESR_2=pd.DataFrame(aar_df['ESR constraint'].str.split(',').explode()).replace('', np.nan).dropna(subset=['ESR constraint']).astype(float)
 ESR_filter3=esr.loc[esr['ESR_ID'].isin(ESR_2['ESR constraint']),:]    
 esr_df = esr_df.append(pd.concat([ESR_filter1,ESR_filter3]).drop_duplicates(['ESR_ID']).reset_index())
 #Optically Stimulated Luminescence
 #keep OSL in RSL datapoints in the nation
 OSL_1=pd.DataFrame(RSL_Datapoints['Luminescence'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Luminescence']).astype(float)
 OSL_filter1=luminescence.loc[luminescence['LUM_ID'].isin(OSL_1['Luminescence']),:]
 #keep OSL used as constraints in AAR table
 OSL_2=pd.DataFrame(aar_df['Luminescene constraint'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Luminescene constraint']).astype(float)
 OSL_filter3=luminescence.loc[luminescence['LUM_ID'].isin(OSL_2['Luminescene constraint']),:]    
 lum_df = lum_df.append(pd.concat([OSL_filter1,OSL_filter3]).drop_duplicates(['LUM_ID']).reset_index())
 #Stratigraphy
 #keep strat in RSL datapoints in the nation
 STR_1=pd.DataFrame(RSL_Datapoints['Stratcontext'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Stratcontext']).astype(float)
 STR_filter1=strat.loc[strat['Strat_ID'].isin(STR_1['Stratcontext']),:]
 #keep strat used as constraints in AAR table
 STR_2=pd.DataFrame(aar_df['Strat constraint'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Strat constraint']).astype(float)
 STR_filter3=strat.loc[strat['Strat_ID'].isin(STR_2['Strat constraint']),:]    
 strat_df = strat_df.append(pd.concat([STR_filter1,STR_filter3]).drop_duplicates(['Strat_ID']).reset_index())
 #keep other in RSL datapoints created by the user
 OTH_1=pd.DataFrame(RSL_Datapoints['Other_age'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Other_age']).astype(float)
 other_df=other.loc[other['idOther_dating'].isin(OTH_1['Other_age']),:]
 # U-Series
 #keep UTH in RSL datapoints in nation
 UTH_1=pd.DataFrame(RSL_Datapoints['Useries'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Useries']).astype(float)
 UTH_filter1=useries.loc[useries['ID_Useries'].isin(UTH_1['Useries']),:]
 #keep UTH in the nation
 UTH_filter2=useries_location[useries_location.name == str(Nation)]
 UTH_filter2=pd.DataFrame(UTH_filter2).drop(columns=['geometry','continent','name'])
 #keep UTH used as constraints in AAR table
 UTH_2=pd.DataFrame(aar_df['Useries constraint'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Useries constraint']).astype(float)
 UTH_filter3=useries.loc[useries['ID_Useries'].isin(UTH_2['Useries constraint']),:]    
 useries_df = useries_df.append(pd.concat([UTH_filter1,UTH_filter2,UTH_filter3]).drop_duplicates(['ID_Useries']).reset_index())
 # Elevation measurement
 #keep VRT in RSL datapoints created by the user
 VRT1=vrt_meas.loc[vrt_meas['idvrtpostech'].isin(RSL_Datapoints['VrtMeasTech']),:]
 #keep VRT in AAR list
 VRT2=vrt_meas.loc[vrt_meas['idvrtpostech'].isin(aar_df['Elev_meas_method']),:]
 #keep VRT in ESR list
 VRT3=vrt_meas.loc[vrt_meas['idvrtpostech'].isin(esr_df['Elev_meas_method']),:]    
 #keep VRT in luminescence list
 VRT4=vrt_meas.loc[vrt_meas['idvrtpostech'].isin(lum_df['Elev_meas_method']),:]    
 #keep VRT in U Series list
 VRT5=vrt_meas.loc[vrt_meas['idvrtpostech'].isin(useries_df['How_elevation_derived']),:]    
 vrt_meas_df = vrt_meas_df.append(pd.concat([VRT1,VRT2,VRT3,VRT4,VRT5]).drop_duplicates(['idvrtpostech']).reset_index())
 # Sea Level datum
 #keep Sea level datum in RSL datapoints created by the user
 SLD1=sldatum.loc[sldatum['SLdatum_ID'].isin(RSL_Datapoints['SLdatum']),:]
 #keep Sea level datum in AAR list
 SLD2=sldatum.loc[sldatum['SLdatum_ID'].isin(aar_df['Original_datum']),:]
 #keep Sea level datum in ESR list
 SLD3=sldatum.loc[sldatum['SLdatum_ID'].isin(esr_df['Original_datum']),:]
 #keep Sea level datum in luminescence list
 SLD4=sldatum.loc[sldatum['SLdatum_ID'].isin(lum_df['Original_datum']),:]
 #keep Sea level datum in U-Series list
 SLD5=sldatum.loc[sldatum['SLdatum_ID'].isin(useries_df['Original_elevation_datum_used']),:]
 sl_datum_df = sl_datum_df.append(pd.concat([SLD1,SLD2,SLD3,SLD4,SLD5]).drop_duplicates(['SLdatum_ID']).reset_index())

 # References
 #keep references in RSL datapoints created by the user
 REF1=references.loc[references['Ref_ID'].isin(RSL_Datapoints['Ref']),:]
 REF_2=pd.DataFrame(RSL_Datapoints['addRef'].str.split(',').explode()).replace('', np.nan).dropna(subset=['addRef'])
 REF2=references.loc[references['Ref_ID'].isin(REF_2['addRef']),:]
 #keep references in RSL indicators
 REF_3=pd.DataFrame(RSL_Ind['Ref_indicator'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Ref_indicator'])
 REF3=references.loc[references['Ref_ID'].isin(REF_3['Ref_indicator']),:]
 #keep references in SL datum
 REF_4=pd.DataFrame(sl_datum_df['Ref_SLdatum'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Ref_SLdatum'])
 REF4=references.loc[references['Ref_ID'].isin(REF_4['Ref_SLdatum']),:]
 #keep references in U-Series corals
 REF_5=pd.DataFrame(useries_df['Source'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Source'])
 REF5=references.loc[references['Ref_ID'].isin(REF_5['Source']),:]
 REF_6=pd.DataFrame(useries_df['Other ref'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Other ref'])
 REF6=references.loc[references['Ref_ID'].isin(REF_6['Other ref']),:]
 #keep references in aar
 REF_7=pd.DataFrame(aar_df['AARRef'].str.split(',').explode()).replace('', np.nan).dropna(subset=['AARRef'])
 REF7=references.loc[references['Ref_ID'].isin(REF_7['AARRef']),:]
 REF_8=pd.DataFrame(aar_df['IndepAgeRef'].str.split(',').explode()).replace('', np.nan).dropna(subset=['IndepAgeRef'])
 REF8=references.loc[references['Ref_ID'].isin(REF_8['IndepAgeRef']),:]
 REF_9=pd.DataFrame(aar_df['CalibRef'].str.split(',').explode()).replace('', np.nan).dropna(subset=['CalibRef'])
 REF9=references.loc[references['Ref_ID'].isin(REF_9['CalibRef']),:]
 #keep references in esr
 REF_10=pd.DataFrame(esr_df['Refs'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Refs'])
 REF10=references.loc[references['Ref_ID'].isin(REF_10['Refs']),:]
 #keep references in luminescence
 REF_11=pd.DataFrame(lum_df['lum_ref'].str.split(',').explode()).replace('', np.nan).dropna(subset=['lum_ref'])
 REF11=references.loc[references['Ref_ID'].isin(REF_11['lum_ref']),:]
 #keep references in stratigraphy
 REF_12=pd.DataFrame(strat_df['StratRef'].str.split(',').explode()).replace('', np.nan).dropna(subset=['StratRef'])
 REF12=references.loc[references['Ref_ID'].isin(REF_12['StratRef']),:]
 #keep references in other
 REF_13=pd.DataFrame(other_df['Ref'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Ref'])
 REF13=references.loc[references['Ref_ID'].isin(REF_13['Ref']),:]
 References_query=References_query.append(pd.concat([REF1,REF2,REF3,REF4,REF5,REF6,REF7,REF8,REF9,REF10,REF11,REF12,REF13]).drop_duplicates(['Ref_ID']).reset_index())
 # Summary
 Summary_df=Summary_df.append(Summary_location[Summary_location.name == str(Nation)])
 Summary_df=pd.DataFrame(Summary_df).drop(columns=['geometry','continent','name'])

###### Consolidate the dataframes ######
RSL_Datapoints = RSL_Datapoints.reset_index(drop=True).drop_duplicates(subset=['RSL_ID']).drop(columns='coord')
RSL_Ind = RSL_Ind.reset_index(drop=True).drop_duplicates(subset=['idrsl_ind'])
hrz_meas = hrz_meas.reset_index(drop=True).drop_duplicates(subset=['idposhrz'])
aar = aar_df.reset_index(drop=True).drop_duplicates(subset=['ID AAR']).drop(['index'], axis=1,errors='ignore').drop(columns='coord')
esr = esr_df.reset_index(drop=True).drop_duplicates(subset=['ESR_ID']).drop(['index'], axis=1,errors='ignore').drop(columns='coord')
lum = lum_df.reset_index(drop=True).drop_duplicates(subset=['LUM_ID']).drop(['index'], axis=1,errors='ignore').drop(columns='coord')
strat = strat_df.reset_index(drop=True).drop_duplicates(subset=['Strat_ID']).drop(['index'], axis=1,errors='ignore')
other = other_df.reset_index(drop=True).drop_duplicates(subset=['idOther_dating']).drop(['index'], axis=1,errors='ignore')
useries = useries_df.reset_index(drop=True).drop_duplicates(subset=['ID_Useries']).drop(['index'], axis=1,errors='ignore').drop(columns='coord')
vrt_meas = vrt_meas_df.reset_index(drop=True).drop_duplicates(subset=['idvrtpostech']).drop(['index'], axis=1,errors='ignore')
sl_datum = sl_datum_df.reset_index(drop=True).drop_duplicates(subset=['SLdatum_ID']).drop(['index'], axis=1,errors='ignore')
References_query = References_query.reset_index(drop=True).drop_duplicates(subset=['Ref_ID']).drop(['index'], axis=1,errors='ignore')
Summary = Summary_df.reset_index(drop=True)

###### Print message ######	
print('The database you are exporting contains:')
print('{} RSL datapoints from stratigraphy'.format(len(RSL_Datapoints)))
useries_Cor_RSL_select = useries.apply(lambda x : True if ((x['Material_type'] == "Coral") & (x['RSL_Estimate_avaliable'] == "Yes")) else False, axis = 1)
print('{} RSL datapoints from single corals'.format(len(useries_Cor_RSL_select[useries_Cor_RSL_select == True].index)))
useries_Spel_RSL_select = useries.apply(lambda x : True if ((x['Material_type'] == "Speleothem") & (x['RSL_Estimate_avaliable'] == "Yes")) else False, axis = 1)
print('{} RSL datapoints from single speleothems'.format(len(useries_Spel_RSL_select[useries_Spel_RSL_select == True].index)))
print('{} RSL indicators'.format(len(RSL_Ind)))
print('{} Elevation measurement techniques'.format(len(vrt_meas)))
print('{} Geographic positioning techniques'.format(len(hrz_meas)))
print('{} Sea level datums'.format(len(sl_datum)))
print('{} U-Series ages (including RSL datapoints from corals and speleothems)'.format(len(useries)))
print('{} Amino Acid Racemization samples'.format(len(aar)))
print('{} Electron Spin Resonance ages'.format(len(esr)))
print('{} Luminescence ages'.format(len(lum)))
print('{} Chronostratigraphic constraints'.format(len(strat)))
print('{} Other age constraints'.format(len(other)))
print('{} References'.format(len(References_query)))