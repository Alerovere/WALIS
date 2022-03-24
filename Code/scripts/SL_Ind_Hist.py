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
plt.savefig('Output/Images/jpg/SLI_hist.jpg', dpi=300)