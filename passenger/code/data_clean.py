# -*- coding:utf-8 -*-
import pandas as pd
filename = '../data/air_data.csv'
savefile = '../subset/data_clean.xls'

data = pd.read_csv(filename,encoding='utf-8')

data = data[data['SUM_YR_1'].notnull()&data['SUM_YR_2'].notnull()]

index1 = data['SUM_YR_1'] !=0
index2 = data['SUM_YR_2'] !=0

# 筛选掉 折扣不为零且飞行里程大于零的数据
index3 = (data['SEG_KM_SUM']==0)&(data['avg_discount']==0)
data = data[index1 | index2 | index3]

data.to_excel(savefile)
