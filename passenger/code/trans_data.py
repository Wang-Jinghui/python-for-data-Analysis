# -*- coding:utf-8 -*-
import pandas as pd
import datetime as dd
filename = '../subset/mvdata.xls'
outfile = '../subset/cleaned_data.xls'
data = pd.read_excel(filename)
def Date(a,b):
    a = dd.datetime.strptime(a,'%Y/%m/%d')
    b = dd.datetime.strptime(b,'%Y/%m/%d')
    m = (b-a).days
    return m
a = data[['FFP_DATE']]
b = data[['LOAD_TIME']].loc[0]['LOAD_TIME']
days = []
for i in range(len(data)):
    aa = a.loc[i]['FFP_DATE']
    day = Date(aa,b)/30.0
    days.append(day)
data = data[['LAST_TO_END','FLIGHT_COUNT','SEG_KM_SUM','avg_discount']]
new_mvd = pd.concat([data,pd.Series(days,index=range(len(days)))],axis=1)
new_mvd.columns = ['R','F','M','C','L']
new_mvd.to_excel(outfile)