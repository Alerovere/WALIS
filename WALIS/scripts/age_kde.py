density_age=Summary.copy()

density_age['ageMU'] = np.where(~density_age['U-Series recalculated age (ka)'].isnull(),
                                       density_age['U-Series recalculated age (ka)'],
                                       density_age['Reported age (ka)'])
density_age['age2S'] = np.where(~density_age['U-Series recalculate age uncertainty (ka)'].isnull(),
                                density_age['U-Series recalculate age uncertainty (ka)'],
                                density_age['Reported age uncertainty (ka)'])

density_age['ageMU'] = np.where(~density_age['U-Series corrected age (speleothems, ka)'].isnull(),
                                          density_age['U-Series corrected age (speleothems, ka)'],
                                          density_age['Reported age (ka)'])
density_age['age2S'] = np.where(~density_age['U-Series corrected age uncertainty (speleothems, ka)'].isnull(),
                                          density_age['U-Series corrected age uncertainty (speleothems, ka)'],
                                          density_age['Reported age uncertainty (ka)'])
density_age['age1S']=density_age['age2S']/2


density_age.dropna(subset=['Reported age (ka)'],inplace=True)

#Delete AAR (considered a relative dating)
density_age = density_age[density_age['Dating technique'] != 'AAR']
#Delete not originally accepted ages
density_age = density_age[density_age['Originally accepted?'] == 'Yes']
#Delete 'Older than' 
density_age = density_age[density_age['Timing constraint'] != 'Older than']
#Delete 'Younger than' 
density_age = density_age[density_age['Timing constraint'] != 'Younger than']
#Drop duplicates
density_age=density_age.drop_duplicates(subset=['Originally reported ID', 'Analysis ID'], keep='first')
#substitute RSL lat/lon if no sample lat/lon is given
density_age['Sample Latitude'] = np.where(~density_age['Sample Latitude'].isnull(),
                                       density_age['Sample Latitude'],
                                       density_age['Latitude'])
density_age['Sample Longitude'] = np.where(~density_age['Sample Longitude'].isnull(),
                                       density_age['Sample Longitude'],
                                       density_age['Longitude'])


density_age = density_age[['Sample Latitude','Sample Longitude','Originally reported ID','Dating technique','ageMU','age1S']]
#density_age
#condense 

time=[]
method=[]
val = np.linspace(0, 100000, num=100001)

for x in val:
    rnd = density_age.sample(n=1)
    age=np.random.normal(rnd['ageMU'], rnd['age1S'], 1)
    dating=rnd['Dating technique'].iloc[0]
    time.append(age)
    method.append(dating)

age_df = pd.DataFrame({'Time':time, 'Method':method})
age_df['Time'] = age_df['Time'].astype(float)
age_df['Method'] = age_df['Method'].astype(str)

#http://www1.ncdc.noaa.gov/pub/data/paleo/paleocean/by_contributor/spratt2016/spratt2016.txt
plt.rcParams.update({'font.size': 15})




f, axes = plt.subplots(2, sharex=True, figsize=(8,8),gridspec_kw={'height_ratios': [1,2]})
sns.kdeplot(data=age_df, x="Time", hue="Method",
            fill=True, common_norm=False,
            alpha=.3, linewidth=1, ax=axes[0])

url ='http://www1.ncdc.noaa.gov/pub/data/paleo/paleocean/by_contributor/spratt2016/spratt2016.txt'
SprLis2016= pd.read_csv(url,sep='\t',skiprows=95,encoding='cp1252')
SprLis2016_short=SprLis2016[['age_calkaBP','SeaLev_shortPC1','SeaLev_shortPC1_err_lo','SeaLev_shortPC1_err_up']]
SprLis2016_short.columns = ['Time (ka)','Sea Level (m)','95% bottom CI (m)','95% top CI (m)']

axes[1].plot( 'Time (ka)', 'Sea Level (m)', data=SprLis2016_short,alpha=0.6, color='k',linewidth=1,label='Spratt and Lisiecki, 2016 (Climate of the Past)')
axes[1].fill_between('Time (ka)', '95% top CI (m)','95% bottom CI (m)', data=SprLis2016_short, facecolor='lightgrey', alpha=0.6)
axes[1].set_title('Data: Spratt and Lisiecki, 2016 (Climate of the Past)', fontsize=8,loc='left')
plt.setp(axes, xlim=(min_age,max_age))
axes[0].yaxis.set_ticklabels([])
plt.xlabel('Time (ka)')
plt.ylabel('Sea level (m)')
axes[0].set_title('Radiometric ages - WALIS', fontsize=8,loc='left')

plt.tight_layout()
filename1='Output/Images/svg/age_kde.svg'
filename2='Output/Images/jpg/age_kde.jpg'
plt.savefig(filename1, dpi=300)
plt.savefig(filename2, dpi=300)
plt.show()