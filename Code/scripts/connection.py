###### Connect to the WALIS database and prepares the tables for download ######

db=mysql.connector.connect(host='es5.siteground.eu', user='ugvgouyqphgeu', 
                   passwd='WALIS_PUBLIC', db='dbvvfcofpmwxz7',charset='utf8',use_unicode=True,port=3306)

SQLtables=['rsl','countries','regions','MIS_ages','`references`','hrzpostech','rsl_ind',
        'sldatum','vertmeastech','Useries_Corals','aar','luminescence','esr','strat',
		'other_dating','sec_usersusers','Summary_sheets','Dated_samples_RSL','Summary_full']

walis_dict = {1:'rsl', 
              2:'countries', 
              3:'regions', 
              4:'MIS_ages',
              5:'references',
              6:'hrzpos',
              7:'rslind',
              8:'sldatum',
              9:'vrt_meas',
              10:'useries',
              11:'aar',
              12:'luminescence',
              13:'esr',
              14:'strat',
              15:'other',
              16:'user',
              17:'Summary_sheets',
              18:'Dated_samples_RSL',
              19:'Summary_full'}

walis_cols = {1:'rsl', 
              2:'countries', 
              3:'regions', 
              4:'MIS_ages',
              5:'references',
              6:'hrzpos',
              7:'rslind',
              8:'sldatum',
              9:'vrt_meas',
              10:'useries',
              11:'aar',
              12:'luminescence',
              13:'esr',
              14:'strat',
              15:'other',
              16:'user',
              17:'Summary_sheets',
              18:'Dated_samples_RSL',
              19:'Summary_full'}
              
