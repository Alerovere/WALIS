# Make literature histograms
unc_plot = Summary.copy()
unc_plot.drop_duplicates(subset=['WALIS_ID'],inplace=True)
x=References_query['Year'].astype(int).dropna()
ref_plot=sns.histplot(x,fill=True)
ref_plot.set(xlabel='Publication year', ylabel='Number of studies')
plt.savefig('Output/Images/References_stats.svg', dpi=300)
plt.close()

# Make SL index points histograms
plt.figure()
indplot=sns.countplot(x = 'RSL Indicator',
              data = unc_plot,
              order = unc_plot['RSL Indicator'].value_counts().index,
              palette='viridis')
plt.xticks(rotation=90)

indplot.set(xlabel='', ylabel='Number of index points')
plt.savefig('Output/Images/Indicators_stats.svg', dpi=300)
plt.close()

# Make SL elevation, datums and geographic positioning histograms
fig, axes = plt.subplots(1, 3,figsize=(14,5))

vrtplot=sns.countplot(x = 'Elevation measurement technique',
              data = unc_plot,
              order = unc_plot['Elevation measurement technique'].value_counts().index,
              palette='viridis',
              ax=axes[0])
vrtplot.set(xlabel='', ylabel='Number of index points',title='Elevation measurement technique')
axes[0].tick_params(labelrotation=90)

dtmplot=sns.countplot(x = 'Vertical datum',
              data = unc_plot,
              order = unc_plot['Vertical datum'].value_counts().index,
              palette='viridis',
              ax=axes[1])
dtmplot.set(xlabel='', ylabel='Number of index points',title='Sea level datum')
axes[1].tick_params(labelrotation=90)

geoplot=sns.countplot(x = 'Horizontal Positioning Technique',
              data = RSL_Datapoints,
              order = RSL_Datapoints['Horizontal Positioning Technique'].value_counts().index,
              palette='viridis',
              ax=axes[2])
geoplot.set(xlabel='', ylabel='Number of index points',title='Horizontal positioning')
axes[2].tick_params(labelrotation=90)

plt.savefig('Output/Images/Geo_Stats.svg', dpi=300)