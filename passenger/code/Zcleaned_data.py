#-*- coding:utf-8 -*-
# 数据标准化
import pandas as pd
filename = '../subset/cleaned_data.xls'
outfile ='../subset/most_value_data.xls'
data = pd.read_excel(filename)
data = (data - data.mean())/data.std()
data.columns = ['Z'+i for i in data.columns]
data.to_excel(outfile)