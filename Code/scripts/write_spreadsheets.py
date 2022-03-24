filename=os.path.join(path,'Output','Data','xls','WALIS_spreadsheet.xlsx')
print('Your file will be created in {} '.format(path+'/Output/Data/'))

###### Prepare messages for the readme ######
# First cell
date_string = date.strftime("%d %m %Y")
msg1='This file was exported from WALIS on '+date_string
# Second cell
msg2= ("The data in this file were compiled in WALIS, the World Atlas of Last Interglacial Shorelines. " 
"WALIS is a product of the ERC project WARMCOASTS (ERC-StG-802414). "
"Bugs and suggestions for improvements can be sent to arovere@marum.de")
# Third cell
if not Summary.empty:
    bit1=(" - Summary RSL datapoints: RSL datapoints from stratigraphic records, U-Series from corals and U-Series from speleothems. Rows with common RSL ID (but different ages available) are highlighted with alternating gray and white colors. \n")
else:
    bit1=("")

if not useries_corals_RSL.empty:
    bit2=(" - RSL from single coral: RSL datapoints from dated corals, for which paleo water depth is estimated \n")
else:
    bit2=("")

if not useries_speleo_RSL.empty:
    bit3=(" - RSL from single speleothem: RSL datapoints from dated speleothems, for which paleo RSL is estimated \n")
else:
    bit3=("")
    
if not RSL_Datapoints.empty:
    bit4=(" - RSL proxies: RSL indicators from stratigraphic information, with grouped age details \n")
else:
    bit4=("")

if not RSL_Ind.empty:
    bit5=(" - RSL indicators: list of types of RSL indicators used in the 'RSL proxies' sheet  \n")
else:
    bit5=("")

if not vrt_meas.empty:
    bit6=(" - Elevation measurement techniques: list of elevation survey methods used both in the 'RSL proxies' sheet and in the elevation fields of dated samples \n")
else:
    bit6=("")

if not hrz_meas.empty:
    bit7=(" - Geographic positioning: list of geographic positioning methods used in the 'RSL proxies' sheet \n")
else:
    bit7=("")

if not sl_datum.empty:
    bit8=(" - Sea level datums: list of datums used both in the 'RSL proxies' sheet and in the datums fields of dated samples \n")
else:
    bit8=("")
if not useries_corals.empty:
    bit9=(" - U-Series (corals): list of all the coral samples dated with U-Series. This sheet contains all U-Series coral ages created by the user or falling within the region of interest, all U-Series coral ages reported in the 'RSL proxies' sheet and all the U-Series coral ages used as age banchmarks to AAR ages contained in the 'RSL proxies tab' \n")
else:
    bit9=("")

if not useries_moll.empty:
    bit10=(" - U-Series (mollusks): list of all the mollusks (or algae) samples dated with U-Series. This sheet contains all U-Series mollusk/algal ages created by the user or falling within the region of interest, all U-Series mollusk/algal ages reported in the 'RSL proxies' sheet and all the U-Series mollusk/algal ages used as age banchmarks to AAR ages contained in the 'RSL proxies tab' \n")
else:
    bit10=("")

if not useries_oolite.empty:
    bit10a=(" - U-Series (mollusks): list of all the mollusks (or algae) samples dated with U-Series. This sheet contains all U-Series mollusk/algal ages created by the user or falling within the region of interest, all U-Series mollusk/algal ages reported in the 'RSL proxies' sheet and all the U-Series mollusk/algal ages used as age banchmarks to AAR ages contained in the 'RSL proxies tab' \n")
else:
    bit10a=("")


if not useries_speleo.empty:
    bit11=(" - U-Series (speleothems): list of all the speleothem samples dated with U-Series. This sheet contains all U-Series speleothem ages created by the user or falling within the region of interest, all U-Series speleothem ages reported in the 'RSL proxies' sheet and all the U-Series speleothem ages used as age banchmarks to AAR ages contained in the 'RSL proxies tab' \n")
else:
    bit11=("")

if not aar.empty:
    bit12=(" - Amino Acid Racemization: list of all the samples dated with AAR. This sheet contains all AAR ages created by the user or falling within the region of interest and all AAR ages reported in the 'RSL proxies' sheet. \n")
else:
    bit12=("")

if not esr.empty:
    bit13=(" - Electron Spin Resonance: list of all the samples dated with ESR. This sheet contains all ESR ages created by the user or falling within the region of interest, all ESR ages reported in the 'RSL proxies' sheet and all the ESR ages used as age banchmarks to AAR ages contained in the 'RSL proxies tab' \n")
else:
    bit13=("")

if not lum.empty:
    bit14=(" - Luminescence: list of all the samples dated with luminescence. This sheet contains all luminescence ages created by the user or falling within the region of interest, all luminescence ages reported in the 'RSL proxies' sheet and all the luminescence ages used as age banchmarks to AAR ages contained in the 'RSL proxies tab' \n")
else:
    bit14=(" ")

if not strat.empty:
    bit15=(" - Chronostratigraphy: list of all the chronostratigraphic age constraints. This sheet contains all constraints created by the user or falling within the region of interest, all chronostratigraphic constraints reported in the 'RSL proxies' sheet and all the chronostratigraphic constraints ages used as age banchmarks to AAR ages contained in the 'RSL proxies tab' \n")
else:
    bit15=("")

if not other.empty:
    bit16=(" - Other age constraints: list of all the other age constraints. This sheet contains all constraints created by the user or falling within the region of interest and all other age constraints reported in the 'RSL proxies' sheet \n")
else:
    bit16=("")

bit17=(" - References: list of all references contained in the culled database. \n")

msg3= ("The sheets in this file contain the following information (if available): \n"+bit1+bit2+bit3+bit4+bit5+bit6+bit7+bit8+bit9+bit10+bit10a+bit11+bit12+bit13+bit14+bit15+bit16+bit17)

#Fourth cell
msg4= ("Information on each field can be found at: https://walis-help.readthedocs.io/en/latest/ \n"
"Information on WALIS (Including data download) can be found at: https://warmcoasts.eu/world-atlas.html \n")

#Fifth cell
people=str(user_contrib_df['index'].values.tolist()).replace("'", '').replace("[", '').replace("]", '')
msg5=("Suggested acknowledgments: The data used in this study were [extracted from / compiled in] WALIS, a sea-level database interface developed by the ERC Starting Grant WARMCOASTS (ERC-StG-802414), in collaboration with PALSEA (PAGES / INQUA) working group. The database structure was designed by A. Rovere, D. Ryan, T. Lorscheid, A. Dutton, P. Chutcharavan, D. Brill, N. Jankowski, D. Mueller, M. Bartz, E. Gowan and K. Cohen. The data points used in this study were contributed to WALIS by: "+people+" (in order of numbers of records inserted).")

#Create and give format to xls file
writer = pd.ExcelWriter(filename, engine='xlsxwriter',options={'strings_to_numbers': True,'strings_to_formulas': False})
workbook=writer.book
wrap = workbook.add_format({'text_wrap': True, 'valign':'vcenter','align':'center'})
wrap2 = workbook.add_format({'text_wrap': True, 'valign':'vcenter','align':'left'})
header_format = workbook.add_format({'bold': True,'text_wrap': True,'valign': 'vcenter','align':'center','fg_color':'#C0C0C0','border': 1})

###### Write the readme in the first sheet ######
column_names = ['WALIS spreadsheet']
df = pd.DataFrame(columns = column_names)
df.to_excel(writer, sheet_name='README',index=False)
worksheet = writer.sheets['README']
worksheet.write('A2', msg1)
worksheet.write('A4', msg2)
worksheet.write('A6', msg3)
worksheet.write_string('A8', msg4)
worksheet.write_string('A9', msg5)
worksheet.set_column('A:A',180,wrap2)

###### Summary sheets ######
Summary=Summary.sort_values(by=['Nation','WALIS_ID'])
#Create Summary sheet 
if not Summary.empty:
    filename_csv=os.path.join(path,'Output','Data','csv','Summary.csv')
    Summary.to_csv(filename_csv,index = False,encoding='utf-8-sig')
    Summary.to_excel(writer, sheet_name='Summary of RSL datapoints',index=False)
    worksheet = writer.sheets['Summary of RSL datapoints']
    worksheet.set_column('A:XFD',20,wrap)
    worksheet.set_column('ZZ:ZZ',0,wrap)
    worksheet.set_column('AB:AB', 30,wrap)
    for row in range(1, 10000):
        worksheet.set_row(row, 50)
    worksheet.freeze_panes(1, 4)
    # Write the column headers with the defined format.
    for col_num, value in enumerate(Summary.columns.values):
        worksheet.write(0, col_num, value, header_format)
    index = Summary.index
    number_of_rows = len(index)
    worksheet.write('AF2', 0)
    for k in range(3, number_of_rows+2):
        i=k-1
        k=str(k)
        i=str(i)
        cell='ZZ'+k
        formula='=MOD(IF(A'+k+'=A'+i+',0,1)+ZZ'+i+',2)'
        worksheet.write_formula(cell,formula)
    format1 = workbook.add_format({'bg_color': '#D3D3D3'})
    worksheet.conditional_format("$A$1:$ZZ$%d" % (number_of_rows+1),{"type": "formula","criteria": '=INDIRECT("ZZ"&ROW())=0',"format": format1})

###### RSL datapoints from U-Series ######
#RSL from corals
useries_corals_RSL = useries_corals_RSL.sort_values(by=['Analysis ID'])
if not useries_corals_RSL.empty:
    filename_csv=os.path.join(path,'Output','Data','csv','RSL_from_single_coral.csv')
    useries_corals_RSL.to_csv(filename_csv,index = False,encoding='utf-8-sig')
    useries_corals_RSL.to_excel(writer, sheet_name='RSL from single coral',index=False)
    #Define fields for corals
    worksheet = writer.sheets['RSL from single coral']
    worksheet.set_column('A:ZZ',20,wrap)
    for row in range(1, 5000):
        worksheet.set_row(row, 45)
    worksheet.freeze_panes(1, 1)
    # Write the column headers with the defined format.
    for col_num, value in enumerate(useries_corals_RSL.columns.values):
        worksheet.write(0, col_num, value, header_format)      
        
###### RSL datapoints from Speleothems ######
useries_speleo_RSL = useries_speleo_RSL.sort_values(by=['Analysis ID'])
if not useries_speleo_RSL.empty:
    filename_csv=os.path.join(path,'Output','Data','csv','RSL_from_single_speleothem.csv')
    useries_corals_RSL.to_csv(filename_csv,index = False,encoding='utf-8-sig')
    useries_speleo_RSL.to_excel(writer, sheet_name='RSL from single speleothem',index=False)
    #Define fields for corals
    worksheet = writer.sheets['RSL from single speleothem']
    worksheet.set_column('A:ZZ',20,wrap)
    for row in range(1, 5000):
        worksheet.set_row(row, 45)
    worksheet.freeze_panes(1, 1)
    # Write the column headers with the defined format.
    for col_num, value in enumerate(useries_speleo_RSL.columns.values):
        worksheet.write(0, col_num, value, header_format)

###### RSL datapoints ######
if not RSL_Datapoints.empty:
    RSL_Datapoints.sort_values(by=['Nation','Region'],inplace=True)
    filename_csv=os.path.join(path,'Output','Data','csv','RSL_proxies.csv')
    RSL_Datapoints.to_csv(filename_csv,index = False,encoding='utf-8-sig')
    RSL_Datapoints.to_excel(writer, sheet_name='RSL proxies',index=False)
    worksheet = writer.sheets['RSL proxies']
    worksheet.set_column('A:XFD',20,wrap)
    for row in range(1, 10000):
        worksheet.set_row(row, 50)
    worksheet.freeze_panes(1, 1)
	# Add a header format.
    header_format = workbook.add_format({'bold': True,'text_wrap': True,'valign': 'vcenter','align':'center',
										 'fg_color':'#C0C0C0','border': 1})
	# Write the column headers with the defined format.
    for col_num, value in enumerate(RSL_Datapoints.columns.values):
        worksheet.write(0, col_num, value, header_format)
    
###### RSL indicators ######
if not RSL_Ind.empty:
    filename_csv=os.path.join(path,'Output','Data','csv','RSL_indicators.csv')
    RSL_Ind.to_csv(filename_csv,index = False,encoding='utf-8-sig')
    RSL_Ind=RSL_Ind.sort_values(by=['Name of RSL indicator'])
    RSL_Ind.to_excel(writer, sheet_name='RSL indicators',index=False)
    worksheet = writer.sheets['RSL indicators']
    worksheet.set_column('A:K',50,wrap)
    for row in range(1, 5000):
        worksheet.set_row(row, 80)
    worksheet.freeze_panes(1, 1)
	# Write the column headers with the defined format.
    for col_num, value in enumerate(RSL_Ind.columns.values):
        worksheet.write(0, col_num, value, header_format)
    
###### Elevation measurement techniques ######
if not vrt_meas.empty:
    vrt_meas=vrt_meas.sort_values(by=['Measurement technique'])
    vrt_meas.reset_index(inplace=True,drop=True)
    filename_csv=os.path.join(path,'Output','Data','csv','Elevation_measurement.csv')
    vrt_meas.to_csv(filename_csv,index = False,encoding='utf-8-sig')
    vrt_meas.to_excel(writer, sheet_name='Elevation measurement',index=False)
    worksheet = writer.sheets['Elevation measurement']
    worksheet.set_column('A:G',50,wrap)
    for row in range(1, 5000):
        worksheet.set_row(row, 80)
    worksheet.freeze_panes(1, 1)
    # Write the column headers with the defined format.
    for col_num, value in enumerate(vrt_meas.columns.values):
        worksheet.write(0, col_num, value, header_format)
    
###### Geographic positioning techniques ######
if not hrz_meas.empty:
    hrz_meas=hrz_meas.sort_values(by=['Measurement technique'])
    filename_csv=os.path.join(path,'Output','Data','csv','Geographic_positioning.csv')
    hrz_meas.to_csv(filename_csv,index = False,encoding='utf-8-sig')    
    hrz_meas.to_excel(writer,sheet_name='Geographic positioning',index=False)
    worksheet = writer.sheets['Geographic positioning']
    worksheet.set_column('A:G',50,wrap)
    for row in range(1, 5000):
        worksheet.set_row(row, 80)
    worksheet.freeze_panes(1, 1)
# Write the column headers with the defined format.
    for col_num, value in enumerate(hrz_meas.columns.values):
        worksheet.write(0, col_num, value, header_format)
    
###### Sea level datum ######
if not sl_datum.empty:
    sl_datum=sl_datum.sort_values(by=['Datum name'])
    filename_csv=os.path.join(path,'Output','Data','csv','Sea_level_datums.csv')
    sl_datum.to_csv(filename_csv,index = False,encoding='utf-8-sig')    
    sl_datum.to_excel(writer,sheet_name='Sea level datums',index=False)
    worksheet = writer.sheets['Sea level datums']
    worksheet.set_column('A:H',50,wrap)
    for row in range(1, 5000):
        worksheet.set_row(row, 80)
    worksheet.freeze_panes(1, 1)
    # Write the column headers with the defined format.
    for col_num, value in enumerate(sl_datum.columns.values):
        worksheet.write(0, col_num, value, header_format)
    
###### U-Series ######
#Corals
useries_corals=useries_corals.sort_values(by=['Analysis ID'])
if not useries_corals.empty:
    filename_csv=os.path.join(path,'Output','Data','csv','USeries_corals.csv')
    useries_corals.to_csv(filename_csv,index = False,encoding='utf-8-sig')    
    useries_corals.to_excel(writer, sheet_name='U-Series (corals)',index=False)
    #Define fields for corals
    worksheet = writer.sheets['U-Series (corals)']
    worksheet.set_column('A:ZZ',20,wrap)
    for row in range(1, 5000):
        worksheet.set_row(row, 45)
    worksheet.freeze_panes(1, 1)
    # Write the column headers with the defined format.
    for col_num, value in enumerate(useries_corals.columns.values):
        worksheet.write(0, col_num, value, header_format)

#Mollusks
useries_moll = useries_moll.sort_values(by=['Analysis ID'])
if not useries_moll.empty:
    filename_csv=os.path.join(path,'Output','Data','csv','USeries_mollusks.csv')
    useries_moll.to_csv(filename_csv,index = False,encoding='utf-8-sig')    
    useries_moll.to_excel(writer,sheet_name='U-Series (mollusks)',index=False)
    #Define fields for mollusks
    worksheet = writer.sheets['U-Series (mollusks)']
    worksheet.set_column('A:ZZ',20,wrap)
    for row in range(1, 5000):
        worksheet.set_row(row, 45)
    worksheet.freeze_panes(1, 1)
    # Write the column headers with the defined format.
    for col_num, value in enumerate(useries_moll.columns.values):
        worksheet.write(0, col_num, value, header_format)

#Speleothem
useries_speleo = useries_speleo.sort_values(by=['Analysis ID'])
if not useries_speleo.empty:
    filename_csv=os.path.join(path,'Output','Data','csv','USeries_speleo.csv')
    useries_speleo.to_csv(filename_csv,index = False,encoding='utf-8-sig')    
    useries_speleo.to_excel(writer,sheet_name='U-Series (speleothems)',index=False)
    #Define fields for mollusks
    worksheet = writer.sheets['U-Series (speleothems)']
    worksheet.set_column('A:ZZ',20,wrap)
    for row in range(1, 5000):
        worksheet.set_row(row, 45)
    worksheet.freeze_panes(1, 1)
    # Write the column headers with the defined format.
    for col_num, value in enumerate(useries_speleo.columns.values):
        worksheet.write(0, col_num, value, header_format)

#Oolites
useries_oolite = useries_oolite.sort_values(by=['Analysis ID'])
if not useries_oolite.empty:
    filename_csv=os.path.join(path,'Output','Data','csv','USeries_oolite.csv')
    useries_oolite.to_csv(filename_csv,index = False,encoding='utf-8-sig')    
    useries_oolite.to_excel(writer,sheet_name='U-Series (Oolites)',index=False)
    #Define fields for mollusks
    worksheet = writer.sheets['U-Series (Oolites)']
    worksheet.set_column('A:ZZ',20,wrap)
    for row in range(1, 5000):
        worksheet.set_row(row, 45)
    worksheet.freeze_panes(1, 1)
    # Write the column headers with the defined format.
    for col_num, value in enumerate(useries_oolite.columns.values):
        worksheet.write(0, col_num, value, header_format)
        
###### AAR ######
aar=aar.sort_values(by=['Analysis ID'])
if not aar.empty:
    filename_csv=os.path.join(path,'Output','Data','csv','Amino_Acid_Racemization.csv')
    aar.to_csv(filename_csv,index = False,encoding='utf-8-sig')    
    aar.to_excel(writer, sheet_name='Amino Acid Racemization',index=False)
    # Write the column headers with the defined format.
    worksheet = writer.sheets['Amino Acid Racemization']
    worksheet.set_column('A:ZZ',20,wrap)
    for row in range(1, 5000):
        worksheet.set_row(row, 45)
    worksheet.freeze_panes(1, 1)
    for col_num, value in enumerate(aar.columns.values):
        worksheet.write(0, col_num, value, header_format)

###### ESR ######
esr=esr.sort_values(by=['Analysis ID'])
if not esr.empty:
    filename_csv=os.path.join(path,'Output','Data','csv','Electron_Spin_Resonance.csv')
    esr.to_csv(filename_csv,index = False,encoding='utf-8-sig')    
    esr.to_excel(writer, sheet_name='Electron Spin Resonance',index=False)
    # Write the column headers with the defined format.
    worksheet = writer.sheets['Electron Spin Resonance']
    worksheet.set_column('A:ZZ',20,wrap)
    for row in range(1, 5000):
        worksheet.set_row(row, 45)
    worksheet.freeze_panes(1, 1)
    for col_num, value in enumerate(esr.columns.values):
        worksheet.write(0, col_num, value, header_format)
        
###### LUM ######
lum=lum.sort_values(by=['Analysis ID'])
if not lum.empty:
    filename_csv=os.path.join(path,'Output','Data','csv','Luminescence.csv')
    lum.to_csv(filename_csv,index = False,encoding='utf-8-sig')    
    lum.to_excel(writer, sheet_name='Luminescence',index=False)
    # Write the column headers with the defined format.
    worksheet = writer.sheets['Luminescence']
    worksheet.set_column('A:ZZ',20,wrap)
    for row in range(1, 5000):
        worksheet.set_row(row, 45)
    worksheet.freeze_panes(1, 1)
    for col_num, value in enumerate(lum.columns.values):
        worksheet.write(0, col_num, value, header_format)

###### Stratigraphic constraints ######
strat=strat.sort_values(by=['Chronostratigraphy ID'])
if not strat.empty:
    filename_csv=os.path.join(path,'Output','Data','csv','Chronostratigrapy.csv')
    strat.to_csv(filename_csv,index = False,encoding='utf-8-sig')    
    strat.to_excel(writer, sheet_name='Chronostratigraphy',index=False)
    # Write the column headers with the defined format.
    worksheet = writer.sheets['Chronostratigraphy']
    worksheet.set_column('A:ZZ',20,wrap)
    for row in range(1, 5000):
        worksheet.set_row(row, 45)
    worksheet.freeze_panes(1, 1)
    for col_num, value in enumerate(strat.columns.values):
        worksheet.write(0, col_num, value, header_format)

###### Other constraints ######
other=other.sort_values(by=['WALIS Other chronology ID'])
if not other.empty:
    filename_csv=os.path.join(path,'Output','Data','csv','Other_age_constraints.csv')
    other.to_csv(filename_csv,index = False,encoding='utf-8-sig')    
    other.to_excel(writer, sheet_name='Other age constraints',index=False)
    # Write the column headers with the defined format.
    worksheet = writer.sheets['Other age constraints']
    worksheet.set_column('A:ZZ',20,wrap)
    for row in range(1, 5000):
        worksheet.set_row(row, 45)
    worksheet.freeze_panes(1, 1)
    for col_num, value in enumerate(other.columns.values):
        worksheet.write(0, col_num, value, header_format)        

###### References_query ######
References_query.drop(columns=['Abstract'],inplace=True)
References_query=References_query.sort_values(by=['Reference'])
if not References_query.empty:
    filename_csv=os.path.join(path,'Output','Data','csv','References.csv')
    References_query.to_csv(filename_csv,index = False,encoding='utf-8-sig')    
    References_query.to_excel(writer, sheet_name='References',index=False)
    # Write the column headers with the defined format.
    worksheet = writer.sheets['References']
    worksheet.set_column('A:A', 15,wrap)
    worksheet.set_column('B:B', 35,wrap)
    worksheet.set_column('C:C', 150,wrap)
    worksheet.set_column('D:D', 30,wrap)
    worksheet.set_column('E:E', 10,wrap)
    worksheet.set_column('F:ZZ', 30,wrap)
    worksheet.freeze_panes(1, 1)
    for col_num, value in enumerate(References_query.columns.values):
        worksheet.write(0, col_num, value, header_format)
writer.save()