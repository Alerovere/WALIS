# Plot quality 
quality_tot = Summary.copy()
quality_tot.drop_duplicates(subset=['WALIS_ID'],inplace=True)


quality = quality_tot[quality_tot['Quality of RSL information'] != '']
quality = quality_tot[quality_tot['Quality of age information'] != '']
quality=quality.groupby(['Quality of RSL information', 'Quality of age information']).size().reset_index(name='Nb of sites')

ageinfo = [0,1,2,3,4,5]
rslinfo = [0,1,2,3,4,5]

quality=quality.pivot('Quality of RSL information', 'Quality of age information',
                      'Nb of sites').reindex(ageinfo, axis=1).reindex(rslinfo, axis=0)

dict_rsl= {0:'Rejected (or limiting point)',1:'Very poor',2:'Poor',3:'Average',4:'Good',5:'Excellent'}
dict_age= {0:'Rejected',1:'Very poor',2:'Poor',3:'Average',4:'Good',5:'Excellent'}

quality=quality.rename(columns=dict_age,index=dict_rsl)


# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots()
sns.heatmap(quality, annot=True,linewidths=1, linecolor='k',ax=ax, cmap='YlGnBu',fmt=".6g",
           cbar_kws={'label': 'Number of datapoints'},
            xticklabels=['Rejected','Very poor','Poor','Average','Good','Excellent'],
            yticklabels=['Rejected (or limiting point)','Very poor','Poor','Average','Good','Excellent'])
ax.invert_yaxis()

plt.savefig('Output/Images/svg/quality_heatmap.svg', dpi=300)
plt.savefig('Output/Images/jpg/quality_heatmap.jpg', dpi=300)
