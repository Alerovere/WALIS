plt.figure()
ax = References_query['Year'].hist()
ax.set_xlabel('Year of publication')
ax.set_ylabel('Number of papers')
ax.set_title('References in WALIS by year')
plt.tight_layout()
plt.savefig('Output/Images/svg/References.svg', dpi=300)
plt.savefig('Output/Images/jpg/References.jpg', dpi=300)