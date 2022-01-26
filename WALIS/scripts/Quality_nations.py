quality1 = quality[quality['Nation'] == Nation1.value]
quality2 = quality[quality['Nation'] == Nation2.value]

quality1 = quality1.groupby(['Quality of RSL information',
                             'Quality of age information']).size().reset_index(name='Nb of sites')
quality2 = quality2.groupby(['Quality of RSL information',
                             'Quality of age information']).size().reset_index(name='Nb of sites')

ageinfo = [0,1,2,3,4,5]
rslinfo = [0,1,2,3,4,5]

quality1=quality1.pivot('Quality of RSL information', 'Quality of age information',
                        'Nb of sites').reindex(ageinfo, axis=1).reindex(rslinfo, axis=0)
quality2=quality2.pivot('Quality of RSL information', 'Quality of age information',
                        'Nb of sites').reindex(ageinfo, axis=1).reindex(rslinfo, axis=0)


dict_rsl= {0:'Rejected (or limiting point)',1:'Very poor',2:'Poor',3:'Average',4:'Good',5:'Excellent'}
dict_age= {0:'Rejected',1:'Very poor',2:'Poor',3:'Average',4:'Good',5:'Excellent'}

quality1=quality1.rename(columns=dict_age,index=dict_rsl)
quality2=quality2.rename(columns=dict_age,index=dict_rsl)

# Draw a heatmap with the numeric values in each cell
fig, axes = plt.subplots(1, 2, sharey=True, figsize=(10,4))
sns.heatmap(quality1, annot=True,linewidths=2, linecolor='k',ax=axes[0], cmap='YlGnBu',fmt=".6g",
           cbar_kws={'label': 'Number of datapoints'},square=True,
            xticklabels=['Rejected','Very poor','Poor','Average','Good','Excellent'],
            yticklabels=['Rejected (or limiting point)','Very poor','Poor','Average','Good','Excellent'],
            robust=True)
axes[0].invert_yaxis()

sns.heatmap(quality2, annot=True,linewidths=2, linecolor='k',ax=axes[1], cmap='YlGnBu',fmt=".6g",
           cbar_kws={'label': 'Number of datapoints'},square=True,
            xticklabels=['Rejected','Very poor','Poor','Average','Good','Excellent'],
            yticklabels=['Rejected (or limiting point)','Very poor','Poor','Average','Good','Excellent'],
            robust=True)
axes[1].invert_yaxis()

axes[0].set_title(Nation1.value)
axes[1].set_title(Nation2.value)

filename1='Output/Images/svg/Quality'+str(Nation1.value)+'_'+str(Nation2.value)+'.svg'
filename2='Output/Images/jpg/Quality'+str(Nation1.value)+'_'+str(Nation2.value)+'.jpg'

plt.savefig(filename1, dpi=300)
plt.savefig(filename2, dpi=300)