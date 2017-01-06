# -*- coding:utf-8 -*-
import pandas as pd
filename = '../subset/data_clean.csv'
outfile = '../subset/mvdata.xls'
data = pd.read_csv(filename,encoding='utf-8')
mostvaluedata = data[['FFP_DATE','LOAD_TIME','FLIGHT_COUNT','avg_discount','SEG_KM_SUM','LAST_TO_END']]
mostvaluedata.to_excel(outfile)