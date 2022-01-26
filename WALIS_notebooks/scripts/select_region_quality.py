quality = Summary.copy()
quality.drop_duplicates(subset=['WALIS_ID'],inplace=True)
#Remove all data with no nation indicated (this deletes RSL datapoints from corals and speleothems)
quality = quality[quality['Region'] != '']
Region1 = widgets.Dropdown(
    options=quality['Region'].unique(),
    description='1st Region:',
    disabled=False)
Region2 = widgets.Dropdown(
    options=quality['Region'].unique(),
    description='2nd Region:',
    disabled=False)
items = [Region1, Region2]
box = Box(children=items)