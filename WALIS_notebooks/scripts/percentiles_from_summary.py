Summary=pd.read_csv('Summary.csv')
age_df=Summary.copy()
# Create U-Series from corals dataframe 
age_df_Ucoral=age_df[(age_df['Dating technique']=='U-Series')&(age_df['Material_type']=='Coral')]
if not age_df_Ucoral.empty:
    # Select the "best" U_series to keep, if recalculated values are present keep those.
    age_df_Ucoral['Useries_mu'] = np.where(~age_df_Ucoral['U-Series recalculated age (ka)'].isnull(),
                                 age_df_Ucoral['U-Series recalculated age (ka)'],age_df_Ucoral['Reported age (ka)'])
    age_df_Ucoral['Useries_2s'] = np.where(~age_df_Ucoral['U-Series recalculate age uncertainty (ka)'].isnull(),
                                     age_df_Ucoral['U-Series recalculate age uncertainty (ka)'],
                                            age_df_Ucoral['Reported age uncertainty (ka)'])

    # Calculate percentiles from sigma values
    age_df_Ucoral['Lower age']=np.nan
    age_df_Ucoral['Age (ka) 0.1 perc']  = age_df_Ucoral['Useries_mu']-(age_df_Ucoral['Useries_2s']/2)*3
    age_df_Ucoral['Age (ka) 2.3 perc']  = age_df_Ucoral['Useries_mu']-age_df_Ucoral['Useries_2s']
    age_df_Ucoral['Age (ka) 15.9 perc'] = age_df_Ucoral['Useries_mu']-(age_df_Ucoral['Useries_2s'])/2
    age_df_Ucoral['Age (ka) 50 perc']   = age_df_Ucoral['Useries_mu']
    age_df_Ucoral['Age (ka) 84.1 perc'] = age_df_Ucoral['Useries_mu']+(age_df_Ucoral['Useries_2s'])/2
    age_df_Ucoral['Age (ka) 97.7 perc'] = age_df_Ucoral['Useries_mu']+age_df_Ucoral['Useries_2s']
    age_df_Ucoral['Age (ka) 99.5 perc'] = age_df_Ucoral['Useries_mu']+(age_df_Ucoral['Useries_2s']/2)*3
    age_df_Ucoral['Upper age']=np.nan
    age_df_Ucoral['Age_mu']=age_df_Ucoral['Useries_mu']
    age_df_Ucoral['Age_2s']=age_df_Ucoral['Useries_2s']
    age_df_Ucoral.drop(columns=['Useries_mu','Useries_2s'],inplace=True)

# Create U-Series from Speleothems dataframe 
age_df_Uspeleo=age_df[(age_df['Dating technique']=='U-Series')&(age_df['Material_type']=='Speleothem')]
if not age_df_Uspeleo.empty:
    # Select the "best" U_series to keep, if recalculated values are present keep those.
    age_df_Uspeleo['Useries_mu'] = np.where(~age_df_Uspeleo['U-Series corrected age (speleothems, ka)'].isnull(),
                                          age_df_Uspeleo['U-Series corrected age (speleothems, ka)'],
                                          age_df_Uspeleo['Reported age (ka)'])
    age_df_Uspeleo['Useries_2s'] = np.where(~age_df_Uspeleo['U-Series corrected age uncertainty (speleothems, ka)'].isnull(),
                                          age_df_Uspeleo['U-Series corrected age uncertainty (speleothems, ka)'],
                                          age_df_Uspeleo['Reported age uncertainty (ka)'])
    # Calculate percentiles from sigma values
    age_df_Uspeleo['Lower age']=np.nan
    age_df_Uspeleo['Age (ka) 0.1 perc']  = age_df_Uspeleo['Useries_mu']-(age_df_Uspeleo['Useries_2s']/2)*3
    age_df_Uspeleo['Age (ka) 2.3 perc']  = age_df_Uspeleo['Useries_mu']-age_df_Uspeleo['Useries_2s']
    age_df_Uspeleo['Age (ka) 15.9 perc'] = age_df_Uspeleo['Useries_mu']-(age_df_Uspeleo['Useries_2s'])/2
    age_df_Uspeleo['Age (ka) 50 perc']   = age_df_Uspeleo['Useries_mu']
    age_df_Uspeleo['Age (ka) 84.1 perc'] = age_df_Uspeleo['Useries_mu']+(age_df_Uspeleo['Useries_2s'])/2
    age_df_Uspeleo['Age (ka) 97.7 perc'] = age_df_Uspeleo['Useries_mu']+age_df_Uspeleo['Useries_2s']
    age_df_Uspeleo['Age (ka) 99.5 perc'] = age_df_Uspeleo['Useries_mu']+(age_df_Uspeleo['Useries_2s']/2)*3
    age_df_Uspeleo['Upper age']=np.nan
    age_df_Uspeleo['Age_mu']=age_df_Uspeleo['Useries_mu']
    age_df_Uspeleo['Age_2s']=age_df_Uspeleo['Useries_2s']
    age_df_Uspeleo.drop(columns=['Useries_mu','Useries_2s'],inplace=True)

# Create U-Series from Oolites dataframe 
age_df_Uoolites=age_df[(age_df['Dating technique']=='U-Series')&(age_df['Material_type']=='Oolite')]
if not age_df_Uoolites.empty:
    # Select the "best" U_series to keep, if recalculated values are present keep those.
    age_df_Uoolites['Useries_mu'] = np.where(~age_df_Uoolites['U-Series corrected age (speleothems, ka)'].isnull(),
                                          age_df_Uoolites['U-Series corrected age (speleothems, ka)'],
                                          age_df_Uoolites['Reported age (ka)'])
    age_df_Uoolites['Useries_2s'] = np.where(~age_df_Uoolites['U-Series corrected age uncertainty (speleothems, ka)'].isnull(),
                                          age_df_Uoolites['U-Series corrected age uncertainty (speleothems, ka)'],
                                          age_df_Uoolites['Reported age uncertainty (ka)'])
    # Calculate percentiles from sigma values
    age_df_Uoolites['Lower age']=np.nan
    age_df_Uoolites['Age (ka) 0.1 perc']  = age_df_Uoolites['Useries_mu']-(age_df_Uoolites['Useries_2s']/2)*3
    age_df_Uoolites['Age (ka) 2.3 perc']  = age_df_Uoolites['Useries_mu']-age_df_Uoolites['Useries_2s']
    age_df_Uoolites['Age (ka) 15.9 perc'] = age_df_Uoolites['Useries_mu']-(age_df_Uoolites['Useries_2s'])/2
    age_df_Uoolites['Age (ka) 50 perc']   = age_df_Uoolites['Useries_mu']
    age_df_Uoolites['Age (ka) 84.1 perc'] = age_df_Uoolites['Useries_mu']+(age_df_Uoolites['Useries_2s'])/2
    age_df_Uoolites['Age (ka) 97.7 perc'] = age_df_Uoolites['Useries_mu']+age_df_Uoolites['Useries_2s']
    age_df_Uoolites['Age (ka) 99.5 perc'] = age_df_Uoolites['Useries_mu']+(age_df_Uoolites['Useries_2s']/2)*3
    age_df_Uoolites['Upper age']=np.nan
    age_df_Uoolites['Age_mu']=age_df_Uoolites['Useries_mu']
    age_df_Uoolites['Age_2s']=age_df_Uoolites['Useries_2s']
    age_df_Uoolites.drop(columns=['Useries_mu','Useries_2s'],inplace=True)

# Create U-Series from mollusks dataframe 
age_df_Umoll=age_df[(age_df['Dating technique']=='U-Series')&(age_df['Material_type']=='Mollusk or algae')]
if not age_df_Umoll.empty:
    # Calculate percentiles from sigma values
    age_df_Umoll['Lower age']=age_df_Umoll['Stratigraphy Lower Age (ka)']
    age_df_Umoll['Age (ka) 0.1 perc']  = np.nan
    age_df_Umoll['Age (ka) 2.3 perc']  = np.nan
    age_df_Umoll['Age (ka) 15.9 perc'] = np.nan
    age_df_Umoll['Age (ka) 50 perc']   = np.nan
    age_df_Umoll['Age (ka) 84.1 perc'] = np.nan
    age_df_Umoll['Age (ka) 97.7 perc'] = np.nan
    age_df_Umoll['Age (ka) 99.5 perc'] = np.nan
    age_df_Umoll['Upper age']=age_df_Umoll['Stratigraphy Upper Age (ka)']

# Create AAR from age dataframe 
age_df_aar=age_df[(age_df['Dating technique']=='AAR')]
if not age_df_aar.empty:
    age_df_aar['AAR_mu']=age_df_aar['Reported age (ka)']
    age_df_aar['AAR_2sd']=age_df_aar['Reported age uncertainty (ka)']
    #If no reported age is given for AAR, substitute it with MIS age
    age_df_aar['Lower age'] = np.where(~age_df_aar['Reported age (ka)'].isnull(),
                                          np.nan,
                                          age_df_aar['Stratigraphy Lower Age (ka)'])
    # Calculate percentiles from sigma values
    age_df_aar['Age (ka) 0.1 perc']  = age_df_aar['AAR_mu']-(age_df_aar['AAR_2sd'])/2*3
    age_df_aar['Age (ka) 2.3 perc']  = age_df_aar['AAR_mu']- age_df_aar['AAR_2sd']
    age_df_aar['Age (ka) 15.9 perc'] = age_df_aar['AAR_mu']-(age_df_aar['AAR_2sd']/2)
    age_df_aar['Age (ka) 50 perc']   = age_df_aar['AAR_mu']
    age_df_aar['Age (ka) 84.1 perc'] = age_df_aar['AAR_mu']+(age_df_aar['AAR_2sd']/2)
    age_df_aar['Age (ka) 97.7 perc'] = age_df_aar['AAR_mu']+ age_df_aar['AAR_2sd']
    age_df_aar['Age (ka) 99.5 perc'] = age_df_aar['AAR_mu']+(age_df_aar['AAR_2sd'])/2*3
    age_df_aar['Upper age'] = np.where(~age_df_aar['Reported age uncertainty (ka)'].isnull(),
                                          np.nan,
                                          age_df_aar['Stratigraphy Upper Age (ka)'])
    age_df_aar['Age_mu']=age_df_aar['AAR_mu']
    age_df_aar['Age_2s']=age_df_aar['AAR_2sd']    
    age_df_aar.drop(columns=['AAR_mu','AAR_2sd'],inplace=True)

# Create ESR from age dataframe 
age_df_esr=age_df[(age_df['Dating technique']=='ESR')]
if not age_df_esr.empty:
    age_df_esr['ESR_mu']=age_df_esr['Reported age (ka)']
    age_df_esr['ESR_2sd']=age_df_esr['Reported age uncertainty (ka)']
    #If no reported age is given for AAR, substitute it with MIS age
    age_df_esr['Lower age'] = np.where(~age_df_esr['Reported age (ka)'].isnull(),
                                          np.nan,
                                          age_df_esr['Stratigraphy Lower Age (ka)'])

    # Calculate percentiles from sigma values
    age_df_esr['Age (ka) 0.1 perc']  = age_df_esr['ESR_mu']-(age_df_esr['ESR_2sd'])/2*3
    age_df_esr['Age (ka) 2.3 perc']  = age_df_esr['ESR_mu']- age_df_esr['ESR_2sd']
    age_df_esr['Age (ka) 15.9 perc'] = age_df_esr['ESR_mu']-(age_df_esr['ESR_2sd']/2)
    age_df_esr['Age (ka) 50 perc']   = age_df_esr['ESR_mu']
    age_df_esr['Age (ka) 84.1 perc'] = age_df_esr['ESR_mu']+(age_df_esr['ESR_2sd']/2)
    age_df_esr['Age (ka) 97.7 perc'] = age_df_esr['ESR_mu']+ age_df_esr['ESR_2sd']
    age_df_esr['Age (ka) 99.5 perc'] = age_df_esr['ESR_mu']+(age_df_esr['ESR_2sd'])/2*3
    age_df_esr['Upper age'] = np.where(~age_df_esr['Reported age uncertainty (ka)'].isnull(),
                                          np.nan,
                                          age_df_esr['Stratigraphy Upper Age (ka)'])
    age_df_esr['Age_mu']=age_df_esr['ESR_mu']
    age_df_esr['Age_2s']=age_df_esr['ESR_2sd']    
    age_df_esr.drop(columns=['ESR_mu','ESR_2sd'],inplace=True)

# Create LUM from age dataframe 
age_df_lum=age_df[(age_df['Dating technique']=='Luminescence')]
if not age_df_lum.empty:
    age_df_lum['LUM_mu']=age_df_lum['Reported age (ka)']
    age_df_lum['LUM_2sd']=age_df_lum['Reported age uncertainty (ka)']
    #If no reported age is given for AAR, substitute it with MIS age
    age_df_lum['Lower age'] = np.where(~age_df_lum['Reported age (ka)'].isnull(),
                                          np.nan,
                                          age_df_lum['Stratigraphy Lower Age (ka)'])
    # Calculate percentiles from sigma values
    age_df_lum['Age (ka) 0.1 perc']  = age_df_lum['LUM_mu']-(age_df_lum['LUM_2sd'])/2*3
    age_df_lum['Age (ka) 2.3 perc']  = age_df_lum['LUM_mu']- age_df_lum['LUM_2sd']
    age_df_lum['Age (ka) 15.9 perc'] = age_df_lum['LUM_mu']-(age_df_lum['LUM_2sd']/2)
    age_df_lum['Age (ka) 50 perc']   = age_df_lum['LUM_mu']
    age_df_lum['Age (ka) 84.1 perc'] = age_df_lum['LUM_mu']+(age_df_lum['LUM_2sd']/2)
    age_df_lum['Age (ka) 97.7 perc'] = age_df_lum['LUM_mu']+ age_df_lum['LUM_2sd']
    age_df_lum['Age (ka) 99.5 perc'] = age_df_lum['LUM_mu']+(age_df_lum['LUM_2sd'])/2*3
    age_df_lum['Upper age'] = np.where(~age_df_lum['Reported age uncertainty (ka)'].isnull(),
                                          np.nan,
                                          age_df_lum['Stratigraphy Upper Age (ka)'])
    age_df_lum['Age_mu']=age_df_lum['LUM_mu']
    age_df_lum['Age_2s']=age_df_lum['LUM_2sd']      
    age_df_lum.drop(columns=['LUM_mu','LUM_2sd'],inplace=True)

# Create strat from age dataframe 
age_df_strat=age_df[(age_df['Dating technique']=='Stratigraphic constraint')]
if not age_df_strat.empty:
    # Calculate percentiles from sigma values
    age_df_strat['Lower age']=age_df_strat['Stratigraphy Lower Age (ka)']
    age_df_strat['Age (ka) 0.1 perc']  = np.nan
    age_df_strat['Age (ka) 2.3 perc']  = np.nan
    age_df_strat['Age (ka) 15.9 perc'] = np.nan
    age_df_strat['Age (ka) 50 perc']   = np.nan
    age_df_strat['Age (ka) 84.1 perc'] = np.nan
    age_df_strat['Age (ka) 97.7 perc'] = np.nan
    age_df_strat['Age (ka) 99.5 perc'] = np.nan
    age_df_strat['Upper age']=age_df_strat['Stratigraphy Upper Age (ka)']

# Create other from age dataframe 
age_df_other=age_df[(age_df['Dating technique']=='Other age constraint')]
if not age_df_other.empty:
    # Calculate percentiles from sigma values
    age_df_other['Lower age']=age_df_other['Stratigraphy Lower Age (ka)']
    age_df_other['Age (ka) 0.1 perc']  = np.nan
    age_df_other['Age (ka) 2.3 perc']  = np.nan
    age_df_other['Age (ka) 15.9 perc'] = np.nan
    age_df_other['Age (ka) 50 perc']   = np.nan
    age_df_other['Age (ka) 84.1 perc'] = np.nan
    age_df_other['Age (ka) 97.7 perc'] = np.nan
    age_df_other['Age (ka) 99.5 perc'] = np.nan
    age_df_other['Upper age']=age_df_other['Stratigraphy Upper Age (ka)']

age_df=pd.concat([age_df_Ucoral,age_df_Uspeleo,age_df_Umoll,age_df_aar,
                   age_df_esr,age_df_lum,age_df_strat,age_df_other])

age_df['Age calculation from'] = ""
recalculated = ~np.isnan(age_df['Age (ka) 0.1 perc'])
age_df.loc[recalculated,['Age calculation from']] = "Radiometric dating"

# Set uniform distribution if no other values are available
subset = np.isnan(age_df['Age (ka) 0.1 perc'])
age_df.loc[age_df['Lower age']>age_df['Upper age']]

# Switch lower age and upper age if not in same format ( lower < upper)
error_subset = age_df['Lower age']>age_df['Upper age']
if sum(error_subset)>0:
    lower_age_fix = age_df.loc[error_subset,"Lower age"].copy()
    upper_age_fix = age_df.loc[error_subset,"Upper age"].copy()
    age_df.loc[error_subset,"Lower age"] = upper_age_fix
    age_df.loc[error_subset,"Upper age"] = lower_age_fix

lower_age = age_df[subset]['Lower age']
upper_age = age_df[subset]['Upper age'] 
age_df.loc[subset,['Age (ka) 0.1 perc']] = lower_age + (abs(upper_age-lower_age)*0.001)
age_df.loc[subset,['Age (ka) 2.3 perc']] = lower_age + (abs(upper_age-lower_age)*0.023)
age_df.loc[subset,['Age (ka) 15.9 perc']] = lower_age + (abs(upper_age-lower_age)*0.159)
age_df.loc[subset,['Age (ka) 50 perc']] = lower_age + (abs(upper_age-lower_age)*0.50)
age_df.loc[subset,['Age (ka) 84.1 perc']] = lower_age + (abs(upper_age-lower_age)*0.841)
age_df.loc[subset,['Age (ka) 97.7 perc']] = lower_age + (abs(upper_age-lower_age)*0.977)
age_df.loc[subset,['Age (ka) 99.5 perc']] = lower_age + (abs(upper_age-lower_age)*0.995)
age_df.loc[subset,['Age calculation from']] = "Uniform distribution from MIS assignment"

# Set negative values from the percentiles to zero
age_df['Age (ka) 0.1 perc'][age_df['Age (ka) 0.1 perc'] < 0] = 0
age_df['Age (ka) 2.3 perc'][age_df['Age (ka) 2.3 perc'] < 0] = 0
age_df['Age (ka) 15.9 perc'][age_df['Age (ka) 15.9 perc'] < 0] = 0

rsl_df=age_df.copy()

print ('Age substitutions done!')

# RSL indicator from stratigraphy
rsl_df_RSL=rsl_df[(rsl_df['RSL Indicator']!='Single Coral')&(rsl_df['RSL Indicator']!='Single Speleothem')&(rsl_df['Type of datapoint']=='Sea Level Indicator')]
# Paleo RSL and uncertainty are recalculated. This passage is done to fix potential errors in the database.
rsl_df_RSL['Paleo RSL (m)']=rsl_df_RSL['Elevation (m)']-rsl_df_RSL['RWL']
rsl_df_RSL['Paleo RSL uncertainty (m)']=np.sqrt((rsl_df_RSL['Elevation error (m)']**2)+((rsl_df_RSL['IR']/2)**2))
# Calculation of RSL percentiles
rsl_df_RSL['RSL (m) 0.1 perc']  = rsl_df_RSL['Paleo RSL (m)']-rsl_df_RSL['Paleo RSL uncertainty (m)']*3
rsl_df_RSL['RSL (m) 2.3 perc']  = rsl_df_RSL['Paleo RSL (m)']-rsl_df_RSL['Paleo RSL uncertainty (m)']*2
rsl_df_RSL['RSL (m) 15.9 perc'] = rsl_df_RSL['Paleo RSL (m)']-rsl_df_RSL['Paleo RSL uncertainty (m)']
rsl_df_RSL['RSL (m) 50 perc']   = rsl_df_RSL['Paleo RSL (m)']
rsl_df_RSL['RSL (m) 84.1 perc'] = rsl_df_RSL['Paleo RSL (m)']+rsl_df_RSL['Paleo RSL uncertainty (m)']
rsl_df_RSL['RSL (m) 97.7 perc'] = rsl_df_RSL['Paleo RSL (m)']+rsl_df_RSL['Paleo RSL uncertainty (m)']*2
rsl_df_RSL['RSL (m) 99.5 perc'] = rsl_df_RSL['Paleo RSL (m)']+rsl_df_RSL['Paleo RSL uncertainty (m)']*3

print ('RSL indicators from stratigraphy done!')

print ('Starting calculations of gamma distribution for corals (will take a while...)')
# RSL indicator from single coral
rsl_df_coral=rsl_df[(rsl_df['RSL Indicator']=='Single Coral')]

# Cull 'not in situ' corals from the database
rsl_df_coral.dropna(subset=['Paleo water depth estimate (m)'], inplace=True)

# Flip negative values
rsl_df_coral['Paleo water depth estimate (m)']=rsl_df_coral['Paleo water depth estimate (m)'].abs()*-1
rsl_df_coral['Upper limit of living range (m)']=rsl_df_coral['Upper limit of living range (m)'].abs()*-1
rsl_df_coral['Lower limit of living range (m)']=rsl_df_coral['Lower limit of living range (m)'].abs()*-1

# replace zeros to avoid gamma distribution fail
rsl_df_coral.replace(0,-0.01,inplace=True)

def gamma_parameters(x1, p1, x2, p2):
    # from https://www.codeproject.com/Articles/56371/Finding-Probability-Distribution-Parameters-from-P
    # Standardize so that x1 < x2 and p1 < p2
    if p1 > p2:
        (p1, p2) = (p2, p1)
        (x1, x2) = (x2, x1)
    # function to find roots of for gamma distribution parameters
    def objective(alpha):
        return stats.gamma.ppf(p2, alpha) / stats.gamma.ppf(p1, alpha) - x2/x1
    # The objective function we're wanting to find a root of is decreasing.
    # We need to find an interval over which is goes from positive to negative.
    left = right = 1.0
    while objective(left) < 0.0:
        left /= 2
    while objective(right) > 0.0:
        right *= 2
    alpha = optimize.bisect(objective, left, right)
    beta = x1 / stats.gamma.ppf(p1, alpha)
    return (alpha, beta)

rsl_df_coral['RSL (m) 0.1 perc']=np.nan
rsl_df_coral['RSL (m) 2.3 perc']=np.nan
rsl_df_coral['RSL (m) 15.9 perc']=np.nan
rsl_df_coral['RSL (m) 50 perc']=np.nan
rsl_df_coral['RSL (m) 84.1 perc']=np.nan
rsl_df_coral['RSL (m) 97.7 perc']=np.nan
rsl_df_coral['RSL (m) 99.5 perc']=np.nan

for ind in rsl_df_coral.index:
    x1=rsl_df_coral['Upper limit of living range (m)'][ind]
    x2=rsl_df_coral['Lower limit of living range (m)'][ind]
    a=gamma_parameters(x1,0.023,x2,0.977)
    pRSL=[]
    val=np.linspace(0, 10000, num=10001)
    for x in val:
     k=np.random.gamma(a[0], scale=a[1]*-1) #RWL
     n=np.random.normal(rsl_df_coral['Elevation (m)'][ind],rsl_df_coral['Elevation error (m)'][ind])  #Elevation
     pRSL.append(n+k)
    rsl_df_coral['RSL (m) 0.1 perc'][ind]=np.percentile(pRSL, 0.1)
    rsl_df_coral['RSL (m) 2.3 perc'][ind]=np.percentile(pRSL, 2.3)
    rsl_df_coral['RSL (m) 15.9 perc'][ind]=np.percentile(pRSL, 15.9)
    rsl_df_coral['RSL (m) 50 perc'][ind]=np.percentile(pRSL, 50)
    rsl_df_coral['RSL (m) 84.1 perc'][ind]=np.percentile(pRSL, 84.1)
    rsl_df_coral['RSL (m) 97.7 perc'][ind]=np.percentile(pRSL, 97.7)
    rsl_df_coral['RSL (m) 99.5 perc'][ind]=np.percentile(pRSL, 99.5)

print ('Done!')

# RSL indicator from single speleothem
rsl_df_speleo=rsl_df[(rsl_df['RSL Indicator']=='Single Speleothem')]
# Calculation of RSL percentiles
rsl_df_speleo['RSL (m) 0.1 perc']  = rsl_df_speleo['Paleo RSL (m)']-rsl_df_speleo['Paleo RSL uncertainty (m)']*3
rsl_df_speleo['RSL (m) 2.3 perc']  = rsl_df_speleo['Paleo RSL (m)']-rsl_df_speleo['Paleo RSL uncertainty (m)']*2
rsl_df_speleo['RSL (m) 15.9 perc'] = rsl_df_speleo['Paleo RSL (m)']-rsl_df_speleo['Paleo RSL uncertainty (m)']
rsl_df_speleo['RSL (m) 50 perc']   = rsl_df_speleo['Paleo RSL (m)']
rsl_df_speleo['RSL (m) 84.1 perc'] = rsl_df_speleo['Paleo RSL (m)']+rsl_df_speleo['Paleo RSL uncertainty (m)']
rsl_df_speleo['RSL (m) 97.7 perc'] = rsl_df_speleo['Paleo RSL (m)']+rsl_df_speleo['Paleo RSL uncertainty (m)']*2
rsl_df_speleo['RSL (m) 99.5 perc'] = rsl_df_speleo['Paleo RSL (m)']+rsl_df_speleo['Paleo RSL uncertainty (m)']*3

rsl_df_limiting=rsl_df[(rsl_df['Type of datapoint']!='Sea Level Indicator')]
rsl_df_limiting['RSL (m) 0.1 perc']=np.nan
rsl_df_limiting['RSL (m) 2.3 perc']=np.nan
rsl_df_limiting['RSL (m) 15.9 perc']=np.nan
rsl_df_limiting['RSL (m) 50 perc']=np.nan
rsl_df_limiting['RSL (m) 84.1 perc']=np.nan
rsl_df_limiting['RSL (m) 97.7 perc']=np.nan
rsl_df_limiting['RSL (m) 99.5 perc']=np.nan

print ('RSL indicators for speleothems done!')

extended_df=pd.concat([rsl_df_limiting,rsl_df_speleo,rsl_df_coral,rsl_df_RSL])

#Delete rows with no elevation or age
noel=extended_df['Elevation (m)'].isna()
print('The dataframe has {} points with no Elevation'.format(noel.sum()))
noel_list=extended_df[extended_df['Elevation (m)'].isna()]

noelerr=extended_df['Elevation error (m)'].isna()
print('The dataframe has {} points with no Elevation error'.format(noelerr.sum()))
noelerr_list=extended_df[extended_df['Elevation error (m)'].isna()]

noage=extended_df['Age (ka) 50 perc'].isna()
print('The dataframe has {} points with no age'.format(noage.sum()))
noage_list=extended_df[extended_df['Age (ka) 50 perc'].isna()]

print('Data with no Elevation information or age has been discarded')

extended_df.dropna(subset=['Elevation (m)','Elevation error (m)','Age (ka) 50 perc'],inplace=True)

extended_df.to_csv('analysis_summary.csv',index = False) 
print('Your file has been saved!')