unc_plot = Summary.copy()
unc_plot.drop_duplicates(subset=['WALIS_ID'],inplace=True)

# Make SL index points histograms
plt.figure(figsize=(5, 10))
ax=sns.countplot(y = 'Elevation measurement technique',
              data = unc_plot,
              order = unc_plot['Elevation measurement technique'].value_counts(ascending=False).index,
              orient='h',
              palette='viridis')

abs_values = unc_plot['Elevation measurement technique'].value_counts(ascending=False).values
ax.bar_label(container=ax.containers[0],labels=abs_values,padding=6,bbox=dict(facecolor='white',edgecolor='white'))
ax.set(ylabel='Elevation measurement method', xlabel='Number of occurrences')
plt.savefig('Output/Images/svg/Vrt_meas_hist.svg', dpi=300)
plt.savefig('Output/Images/jpg/Vrt_meas_hist.jpg', dpi=300,bbox_inches='tight')

joined=unc_plot.set_index('Elevation measurement technique').join(vrt_meas.set_index('Measurement technique'),lsuffix='_caller', rsuffix='_other')

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
plt.savefig('Output/Images/svg/Vrt_meas_hist_type.svg', dpi=300)
plt.savefig('Output/Images/jpg/Vrt_meas_hist_type.jpg', dpi=300,bbox_inches='tight')