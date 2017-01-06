# -*- coding:utf-8 -*-
import  pandas as pd
filename = '../data/air_data.csv'
outfile = '../subset/count.xls'
data = pd.read_csv(filename,encoding='utf-8')
explore = data.describe(percentiles=[],include='all').T   # percentiles 指定计算多少分位数 （1/4位）
explore['null'] = len(data) - explore['count']
explore = explore[['null','max','min']]
explore.columns = [u'空值数',u'最大值',u'最小值']
explore.to_excel(outfile)
