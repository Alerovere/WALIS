query_type='user'

if str(User) != 'WALIS Admin':
 ###### Take users from existing dataframe ######
 stringbit=', '.join(map(str,multiUsr.value))
 print('Extracting values for user(s): {}'.format(stringbit))
 print('')
 list_users = list(multiUsr.value)
 users_dict_inv = {v: k for k, v in users_dict.items()}
 list_users=list(map(users_dict_inv.get, list_users))
 multiUsr = tuple(list_users)
else:
 print('Extracting the Whole WALIS database')

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
for User in multiUsr: 
 # RSL datapoints
 if str(User) != 'WALIS Admin':
  RSL_Datapoints=RSL_Datapoints.append(rsl[rsl.Createdby == str(User)])  
 else:
  RSL_Datapoints = rsl.copy()
 #RSL indicators
 if str(User) != 'WALIS Admin':
  RSL_Ind=RSL_Ind.append(rslind.loc[rslind['idrsl_ind'].isin(RSL_Datapoints['Indicator']),:])		
 else:
  RSL_Ind = rslind.copy()
 #Geographic positioning
 if str(User) != 'WALIS Admin':
  hrz_meas=hrz_meas.append(hrzpos.loc[hrzpos['idposhrz'].isin(RSL_Datapoints['HrzPosTech']),:])
 else:
  hrz_meas = hrzpos.copy()
 #Amino Acid Racemization
 if str(User) != 'WALIS Admin':
  #keep AAR in RSL datapoints created by the user
  AAR_1=pd.DataFrame(RSL_Datapoints['AAR'].str.split(',').explode()).replace('', np.nan).dropna(subset=['AAR']).astype(float)
  AAR_filter1=aar.loc[aar['ID AAR'].isin(AAR_1['AAR']),:]
  #keep AAR created by the user
  AAR_filter2=aar[aar.Createdby == str(User)]
  aar_df = aar_df.append(pd.concat([AAR_filter1,AAR_filter2]).drop_duplicates(['ID AAR']).reset_index())
 else:
  aar_df=aar.copy()
 #Electron Spin Resonance
 if str(User) != 'WALIS Admin':
 #keep ESR in RSL datapoints created by the user
  ESR_1=pd.DataFrame(RSL_Datapoints['ESR'].str.split(',').explode()).replace('', np.nan).dropna(subset=['ESR']).astype(float)
  ESR_filter1=esr.loc[esr['ESR_ID'].isin(ESR_1['ESR']),:]
  #keep ESR created by the user
  ESR_filter2=esr[esr.Createdby == str(User)]
  #keep ESR used as constraints in AAR table
  ESR_2=pd.DataFrame(aar_df['ESR constraint'].str.split(',').explode()).replace('', np.nan).dropna(subset=['ESR constraint']).astype(float)
  ESR_filter3=esr.loc[esr['ESR_ID'].isin(ESR_2['ESR constraint']),:]    
  esr_df = esr_df.append(pd.concat([ESR_filter1,ESR_filter2,ESR_filter3]).drop_duplicates(['ESR_ID']).reset_index())
 else:
  esr_df=esr.copy() 
 #Optically Stimulated Luminescence
 if str(User) != 'WALIS Admin':
  #keep OSL in RSL datapoints created by the user
  OSL_1=pd.DataFrame(RSL_Datapoints['Luminescence'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Luminescence']).astype(float)
  OSL_filter1=luminescence.loc[luminescence['LUM_ID'].isin(OSL_1['Luminescence']),:]
  #keep OSL created by the user
  OSL_filter2=luminescence[luminescence.Createdby == str(User)]
  #keep OSL used as constraints in AAR table
  OSL_2=pd.DataFrame(aar_df['Luminescene constraint'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Luminescene constraint']).astype(float)
  OSL_filter3=luminescence.loc[luminescence['LUM_ID'].isin(OSL_2['Luminescene constraint']),:]    
  lum_df = lum_df.append(pd.concat([OSL_filter1,OSL_filter2,OSL_filter3]).drop_duplicates(['LUM_ID']).reset_index())
 else:
  lum_df = luminescence.copy()
 #Stratigraphy
 if str(User) != 'WALIS Admin':
  #keep strat in RSL datapoints created by the user
  STR_1=pd.DataFrame(RSL_Datapoints['Stratcontext'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Stratcontext']).astype(float)
  STR_filter1=strat.loc[strat['Strat_ID'].isin(STR_1['Stratcontext']),:]
  #keep strat created by the user
  STR_filter2=strat[strat.Createdby == str(User)]
  #keep strat used as constraints in AAR table
  STR_2=pd.DataFrame(aar_df['Strat constraint'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Strat constraint']).astype(float)
  STR_filter3=strat.loc[strat['Strat_ID'].isin(STR_2['Strat constraint']),:]    
  strat_df = strat_df.append(pd.concat([STR_filter1,STR_filter2]).drop_duplicates(['Strat_ID']).reset_index())
 else:
  strat_df=strat.copy()
 #Other
 if str(User) != 'WALIS Admin':
  #keep other in RSL datapoints created by the user
  OTH_1=pd.DataFrame(RSL_Datapoints['Other_age'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Other_age']).astype(float)
  OTH_filter1=other.loc[other['idOther_dating'].isin(OTH_1['Other_age']),:]
  #keep strat created by the user
  OTH_filter2=other[other.Createdby == str(User)]
  other_df = other_df.append(pd.concat([OTH_filter1,OTH_filter2]).drop_duplicates(['idOther_dating']).reset_index())
 else:
  other_df=other.copy() 
 # U-Series
 if str(User) != 'WALIS Admin':
  #keep UTH in RSL datapoints created by the user
  UTH_1=pd.DataFrame(RSL_Datapoints['Useries'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Useries']).astype(float)
  UTH_filter1=useries.loc[useries['ID_Useries'].isin(UTH_1['Useries']),:]
  #keep UTH created by the user
  UTH_filter2=useries[useries.Createdby == str(User)]
  #keep UTH used as constraints in AAR table
  UTH_2=pd.DataFrame(aar_df['Useries constraint'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Useries constraint']).astype(float)
  UTH_filter3=useries.loc[useries['ID_Useries'].isin(UTH_2['Useries constraint']),:]    
  useries_df = useries_df.append(pd.concat([UTH_filter1,UTH_filter2,UTH_filter3]).drop_duplicates(['ID_Useries']).reset_index())
 else:
  useries_df=useries.copy() 
 # Elevation measurement
 if str(User) != 'WALIS Admin':
  #keep VRT in RSL datapoints created by the user
  VRT1=vrt_meas.loc[vrt_meas['idvrtpostech'].isin(RSL_Datapoints['VrtMeasTech']),:]
  #keep VRT in AAR list
  VRT2=vrt_meas.loc[vrt_meas['idvrtpostech'].isin(aar_df['Elev_meas_method']),:]
  #keep VRT in ESR list
  VRT3=vrt_meas.loc[vrt_meas['idvrtpostech'].isin(esr_df['Elev_meas_method']),:]    
  #keep VRT in luminescence list
  VRT4=vrt_meas.loc[vrt_meas['idvrtpostech'].isin(lum_df['Elev_meas_method']),:]    
  #keep VRT in U Series list
  VRT5=vrt_meas.loc[vrt_meas['idvrtpostech'].isin(useries_df['How_elevation_derived'].replace('',np.nan).dropna().astype(int))]    
  vrt_meas_df = vrt_meas_df.append(pd.concat([VRT1,VRT2,VRT3,VRT4,VRT5]).drop_duplicates(['idvrtpostech']).reset_index())
 else:
  vrt_meas_df=vrt_meas.copy() 
 # Sea Level datum
 if str(User) != 'WALIS Admin':
  #keep Sea level datum in RSL datapoints created by the user
  SLD1=sldatum.loc[sldatum['SLdatum_ID'].isin(RSL_Datapoints['SLdatum']),:]
  #keep Sea level datum in AAR list
  SLD2=sldatum.loc[sldatum['SLdatum_ID'].isin(aar_df['Original_datum']),:]
  #keep Sea level datum in ESR list
  SLD3=sldatum.loc[sldatum['SLdatum_ID'].isin(esr_df['Original_datum']),:]
  #keep Sea level datum in luminescence list
  SLD4=sldatum.loc[sldatum['SLdatum_ID'].isin(lum_df['Original_datum']),:]
  #keep Sea level datum in U-Series list
  SLD5=sldatum.loc[sldatum['SLdatum_ID'].isin(useries_df['Original_elevation_datum_used'].replace('',np.nan).dropna().astype(int)),:]
  sl_datum_df = sl_datum_df.append(pd.concat([SLD1,SLD2,SLD3,SLD4,SLD5]).drop_duplicates(['SLdatum_ID']).reset_index())
 else:
  sl_datum_df=sldatum.copy()
 # References
 if str(User) != 'WALIS Admin':
  #keep references in RSL datapoints created by the user
  REF1=references.loc[references['Ref_ID'].isin(RSL_Datapoints['Ref']),:]
  REF_2=pd.DataFrame(RSL_Datapoints['addRef'].str.split(',').explode()).replace('', np.nan).dropna(subset=['addRef']).astype(float)
  REF2=references.loc[references['Ref_ID'].isin(REF_2['addRef']),:]
  #keep references in RSL indicators
  REF_3=pd.DataFrame(RSL_Ind['Ref_indicator'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Ref_indicator']).astype(float)
  REF3=references.loc[references['Ref_ID'].isin(REF_3['Ref_indicator']),:]
  #keep references in SL datum
  REF_4=pd.DataFrame(sl_datum_df['Ref_SLdatum'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Ref_SLdatum']).astype(float)
  REF4=references.loc[references['Ref_ID'].isin(REF_4['Ref_SLdatum']),:]
  #keep references in U-Series corals
  REF_5=pd.DataFrame(useries_df['Source'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Source']).astype(float)
  REF5=references.loc[references['Ref_ID'].isin(REF_5['Source']),:]
  REF_6=pd.DataFrame(useries_df['Other ref'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Other ref']).astype(float)
  REF6=references.loc[references['Ref_ID'].isin(REF_6['Other ref']),:]
  #keep references in aar
  REF_7=pd.DataFrame(aar_df['AARRef'].str.split(',').explode()).replace('', np.nan).dropna(subset=['AARRef']).astype(float)
  REF7=references.loc[references['Ref_ID'].isin(REF_7['AARRef']),:]
  REF_8=pd.DataFrame(aar_df['IndepAgeRef'].str.split(',').explode()).replace('', np.nan).dropna(subset=['IndepAgeRef']).astype(float)
  REF8=references.loc[references['Ref_ID'].isin(REF_8['IndepAgeRef']),:]
  REF_9=pd.DataFrame(aar_df['CalibRef'].str.split(',').explode()).replace('', np.nan).dropna(subset=['CalibRef']).astype(float)
  REF9=references.loc[references['Ref_ID'].isin(REF_9['CalibRef']),:]
  #keep references in esr
  REF_10=pd.DataFrame(esr_df['Refs'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Refs']).astype(float)
  REF10=references.loc[references['Ref_ID'].isin(REF_10['Refs']),:]
  #keep references in luminescence
  REF_11=pd.DataFrame(lum_df['lum_ref'].str.split(',').explode()).replace('', np.nan).dropna(subset=['lum_ref']).astype(float) 
  REF11=references.loc[references['Ref_ID'].isin(REF_11['lum_ref']),:]
  #keep references in stratigraphy
  REF_12=pd.DataFrame(strat_df['StratRef'].str.split(',').explode()).replace('', np.nan).dropna(subset=['StratRef']).astype(float)
  REF12=references.loc[references['Ref_ID'].isin(REF_12['StratRef']),:]
  #keep references in other
  REF_13=pd.DataFrame(other_df['Ref'].str.split(',').explode()).replace('', np.nan).dropna(subset=['Ref']).astype(float)
  REF13=references.loc[references['Ref_ID'].isin(REF_13['Ref']),:]
  References_query=References_query.append(pd.concat([REF1,REF2,REF3,REF4,REF5,REF6,REF7,REF8,REF9,REF10,REF11,REF12,REF13]).drop_duplicates(['Ref_ID']).reset_index())
 else:
  References_query = references.copy()
 #Summary sheets
 if str(User) != 'WALIS Admin':
  Summary_df = Summary_df.append(Summary[Summary['Record Created by'] == str(User)])
 else:
  Summary_df=Summary.copy()

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