shutil.rmtree('Output')

path = os.getcwd()
Output = 'Output'
Output_path=os.path.join(path,Output)
os.mkdir(Output_path)
Data = 'Data'
Data_path=os.path.join(Output_path,Data)
os.mkdir(Data_path)
xls = 'xls'
xls_dir=os.path.join(Data_path,xls)
os.mkdir(xls_dir)
csv = 'csv'
csv_dir=os.path.join(Data_path,csv)
os.mkdir(csv_dir)
json = 'json'
json_dir=os.path.join(Data_path,json)
os.mkdir(json_dir)
Images = 'Images'
Images_path=os.path.join(Output_path,Images)
os.mkdir(Images_path)
jpg = 'jpg'
jpg_path=os.path.join(Output_path,Images,jpg)
os.mkdir(jpg_path)
svg = 'svg'
svg_path=os.path.join(Output_path,Images,svg)
os.mkdir(svg_path)
html = 'html'
html_path=os.path.join(Output_path,html)
os.mkdir(html_path)
DB_Structure = 'DB_Structure'
DB_Structure_path=os.path.join(Output_path,DB_Structure)
os.mkdir(DB_Structure_path)
Holocene = 'Holocene'
Holocene_path=os.path.join(Output_path,Holocene)
os.mkdir(Holocene_path)

# Make CSV files with table column descriptions
for i in range(len(SQLtables)): 
    #fn_str=DB_Structure_path+'\\'+str(SQLtables[i])+'.csv'
    fn_str=os.path.join(DB_Structure_path,str(SQLtables[i])+'.csv')
    walis_cols[i].drop(columns=['Default','Extra','Privileges']).to_csv(fn_str,index = False)