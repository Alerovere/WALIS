#Thanks to https://stackoverflow.com/questions/11882393/matplotlib-disregard-outliers-when-plotting
def is_outlier(points, thresh=4):
    """
    Returns a boolean array with True if points are outliers and False 
    otherwise.

    Parameters:
    -----------
        points : An numobservations by numdimensions array of observations
        thresh : The modified z-score to use as a threshold. Observations with
            a modified z-score (based on the median absolute deviation) greater
            than this value will be classified as outliers.

    Returns:
    --------
        mask : A numobservations-length boolean array.

    References:
    ----------
        Boris Iglewicz and David Hoaglin (1993), "Volume 16: How to Detect and
        Handle Outliers", The ASQC Basic References in Quality Control:
        Statistical Techniques, Edward F. Mykytka, Ph.D., Editor. 
    """
    if len(points.shape) == 1:
        points = points[:,None]
    median = np.median(points, axis=0)
    diff = np.sum((points - median)**2, axis=-1)
    diff = np.sqrt(diff)
    med_abs_deviation = np.median(diff)

    modified_z_score = 0.6745 * diff / med_abs_deviation

    return modified_z_score > thresh

# Elevation uncertainty plot
unc_plot = Summary.copy()
unc_plot.drop_duplicates(subset=['WALIS_ID'],inplace=True)
x=unc_plot['Elevation error (m)'].astype(float).dropna()
filtered = x[~is_outlier(x)]

fig, axes = plt.subplots(1, 2,figsize=(15,6))
fig.suptitle('Elevation measurement errors (m)')

sns.kdeplot(data=filtered,fill=True,ax=axes[0])
title_excl='Excluding outliers, avg= '+ "{:.2f}".format(np.mean(filtered))+'m'
axes[0].set(xlabel='Elevation error (m)', ylabel='Density', title=title_excl,xlim=0)

sns.kdeplot(data=x,fill=True,ax=axes[1])
title_incl='Including outliers, avg= '+ "{:.2f}".format(np.mean(x))+'m'
axes[1].set(xlabel='Elevation error (m)', ylabel='Density', title=title_incl,xlim=0)
plt.savefig('Output/Images/svg/Elevation_error.svg', dpi=300)
plt.savefig('Output/Images/jpg/Elevation_error.jpg', dpi=300)