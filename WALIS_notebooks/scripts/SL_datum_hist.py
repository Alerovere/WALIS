#Vertical datum
unc_plot = Summary.copy()
unc_plot.drop_duplicates(subset=['WALIS_ID'],inplace=True)

# Make SL index points histograms
plt.figure(figsize=(5, 10))
ax=sns.countplot(y = 'Vertical datum',
              data = unc_plot,
              order = unc_plot['Vertical datum'].value_counts(ascending=False).index,
              orient='h',
              palette='viridis')

abs_values = unc_plot['Vertical datum'].value_counts(ascending=False).values
ax.bar_label(container=ax.containers[0],labels=abs_values,padding=6,bbox=dict(facecolor='white',edgecolor='white'))
ax.set(ylabel='Vertical datum', xlabel='Number of occurrences')
plt.savefig('Output/Images/svg/Vrt_datum_hist.svg', dpi=300)
plt.savefig('Output/Images/jpg/Vrt_datum_hist.jpg', dpi=300)