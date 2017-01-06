#-*- coding:utf-8 -*-
import pandas as pd
filename = '../subset/classifision_data.xls'
data = pd.read_excel(filename)
r = data[[u'聚类类别']]
data = data[['R','F','M','C','L']]
out_fig = '../figures/'
def fig_plot(data,title): #自定义作图函数
   import matplotlib.pyplot as plt

   plt.rcParams['font.sans-serif'] = ['SimHei']
   plt.rcParams['axes.unicode_minus'] = False
   p = data.plot(kind='kde',lw=2,subplots=True,sharex=False)

   [p[i].set_ylabel(u'密度') for i in range(5)]
   [p[0].set_title(u'聚类类别%s'%title)]
   return plt
for i in range(5):
    fig_plot(data[r[u'聚类类别']==i],i).savefig(u'%s%s.png'%(out_fig,i))
