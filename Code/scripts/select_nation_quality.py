quality = Summary.copy()
quality.drop_duplicates(subset=['WALIS_ID'],inplace=True)
#Remove all data with no quality score (this deletes RSL datapoints from corals and speleothems)
noqual_data=len(quality[quality['Quality of RSL information'] == ''])
quality = quality[quality['Quality of RSL information'] != '']
Nation1 = widgets.Dropdown(
    options=quality['Nation'].unique(),
    description='1st Nation:',
    disabled=False)
Nation2 = widgets.Dropdown(
    options=quality['Nation'].unique(),
    description='2nd Nation:',
    disabled=False)
items = [Nation1, Nation2]
box = Box(children=items)