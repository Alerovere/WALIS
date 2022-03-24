sel_display = widgets.Select(
    options=['Highlight','Single points'],
    description='Style',
    rows=1,
    disabled=False)
choice=widgets.RadioButtons(
    options=['yes', 'no'],
    value='yes', # Defaults to 'yes'
    layout={'width': 'max-content'}, # If the items' names are long
    description='Global map?',
    disabled=False)

select = ['RSL datapoints']
if not useries_corals.empty:
 select.append('U-series (corals)')
if not useries_oolite.empty:
 select.append('U-series (oolites)')
if not useries_speleo.empty:
 select.append('U-series (speleothems)')
if not useries_moll.empty:
 select.append('U-series (mollusks)')
if not aar.empty:
 select.append('AAR')
if not lum.empty:
 select.append('Luminescence')
if not esr.empty:
 select.append('ESR')
map_strat=RSL_Datapoints.replace('',np.nan).dropna(axis=0,subset=['Stratigraphic context/age IDs']).drop_duplicates(subset=['WALIS RSL ID'])
if not map_strat.empty:
 select.append('Stratigraphy')
map_other=RSL_Datapoints.replace('',np.nan).dropna(axis=0,subset=['Other age constraints IDs']).drop_duplicates(subset=['WALIS RSL ID'])
if not map_other.empty:
 select.append('Other dating')

sel=widgets.Dropdown(
    options=select,
    rows=10,
    description='Map choice',
    disabled=False)

display(sel_display,choice,sel)