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

## Create a list of users who have compiled RSL datapoints and U-Series RSL data 
rslCreators = walis_dict[0].copy()
rslCreators=pd.DataFrame(rslCreators.Createdby)
useriesCreators = walis_dict[9].copy()
useriesCreators.drop(useriesCreators[useriesCreators.RSL_Estimate_avaliable != 'Yes'].index, inplace=True)
useriesCreators=pd.DataFrame(useriesCreators.Createdby)
users = pd.concat([rslCreators, useriesCreators]).drop_duplicates('Createdby').reset_index()
users.loc[-1] = ['','WALIS Admin']
users.index = users.index + 1
users_dict = dict(zip(user.login, user.name))
users['Createdby']=users['Createdby'].map(users_dict)
users.sort_values(['Createdby'],inplace=True)

multiUsr = widgets.SelectMultiple(
    options=users.Createdby,
    rows=15,
    columns=3,
    disabled=False,
    value=['WALIS Admin'])