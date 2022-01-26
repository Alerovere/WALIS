plt.figure()
#database evolution through time
DBtimes = pd.DataFrame()
DBtimes['LastUpdate']=pd.concat([RSL_Datapoints['Last Update'],aar['Last Update'],esr['Last Update'],
                                lum['Last Update'],useries['Last Update'],strat['Last Update'],
                                other['Last Update']]).astype('datetime64')

#Statistics on users
DBuser=pd.DataFrame()
DBuser['Created by']=pd.concat([RSL_Datapoints['Record created by'],aar['Record created by'],esr['Record created by'],
                                lum['Record created by'],useries['Record created by'],strat['Record created by'],
                                other['Record created by']])
DBuser
num=DBuser['Created by'].nunique()

ax = DBtimes.groupby([DBtimes['LastUpdate'].dt.to_period(freq='M')]).count().plot(kind='area')
ax.set_xlabel('Date')
ax.set_ylabel('Number of datapoints')
ax.set_title('Monthly data insertion by {} unique users'.format(num))
ax.get_legend().remove()
plt.tight_layout()
plt.savefig('Output/Images/svg/time_creation.svg', dpi=300)
plt.savefig('Output/Images/jpg/time_creation.jpg', dpi=300)