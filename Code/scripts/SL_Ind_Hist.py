unc_plot = Summary.copy()
unc_plot.drop_duplicates(subset=['WALIS_ID'],inplace=True)
# Make SL index points histograms
plt.figure(figsize=(5, 15))
ax=sns.countplot(y = 'RSL Indicator',
              data = unc_plot,
              order = unc_plot['RSL Indicator'].value_counts(ascending=False).index,
              orient='h',
              palette='viridis')

abs_values = unc_plot['RSL Indicator'].value_counts(ascending=False).values
ax.bar_label(container=ax.containers[0],labels=abs_values,padding=6,bbox=dict(facecolor='white',edgecolor='white'))
ax.set(ylabel='Sea-level indicator type', xlabel='Number of occurrences')
plt.savefig('Output/Images/svg/SLI_hist.svg', dpi=300)
plt.savefig('Output/Images/jpg/SLI_hist.jpg', dpi=300,bbox_inches='tight')

indicators_mod=RSL_Ind
df = {'WALIS RSLind ID': '9999',
      'Name of RSL indicator': 'Single Coral',
      'Description of RSL indicator':'N/A',
      'Description of RWL':'N/A',
      'Description of IR':'N/A',
      'Indicator reference(s)':'N/A',
      'Record created by':'N/A',
      'Record updated by':'N/A',
      'Last Update':'N/A',
      'General type':'Biological'}
indicators_mod = indicators_mod.append(df, ignore_index = True)
df = {'WALIS RSLind ID': '9998',
      'Name of RSL indicator': 'Single Speleothem',
      'Description of RSL indicator':'N/A',
      'Description of RWL':'N/A',
      'Description of IR':'N/A',
      'Indicator reference(s)':'N/A',
      'Record created by':'N/A',
      'Record updated by':'N/A',
      'Last Update':'N/A',
      'General type':'Geomorphological'}
indicators_mod = indicators_mod.append(df, ignore_index = True)

joined=unc_plot.set_index('RSL Indicator').join(indicators_mod.set_index('Name of RSL indicator'),lsuffix='_caller', rsuffix='_other')

# Make SL index points histograms
plt.figure(figsize=(5, 5))
ax=sns.countplot(y = 'General type',
              data = joined,
              order = joined['General type'].value_counts(ascending=False).index,
              orient='h',
              palette='viridis')

abs_values = joined['General type'].value_counts(ascending=False).values
ax.bar_label(container=ax.containers[0],labels=abs_values,padding=6,bbox=dict(facecolor='white',edgecolor='white'))
ax.set(ylabel='Sea-level indicator type', xlabel='Number of occurrences')
plt.savefig('Output/Images/svg/SLI_hist_type.svg', dpi=300)
plt.savefig('Output/Images/jpg/SLI_hist_type.jpg', dpi=300,bbox_inches='tight')