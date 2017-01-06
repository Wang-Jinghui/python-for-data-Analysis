# -*-coding:utf-8 -*-
# Kmeans 聚类算法
import pandas as pd
from sklearn.cluster import KMeans    #导入kmeans聚类算法
outfile = '../subset/classifision_data.xls'
filename = '../subset/most_value_data.xls'
#filename = '../subset/cleaned_data.xls'   # 标准化前数据
data = pd.read_excel(filename)
k = 5    # 聚类的类别数
iteration = 500
kmodel = KMeans(n_clusters=k,max_iter=iteration)
kmodel.fit(data)    # 训练模型
# 属性值标签 与元数据 组合
r3 = pd.Series(kmodel.labels_,index=range(len(data)))
cluster_data = pd.concat([data,r3],axis=1)
cluster_data.columns = list(data.columns)+[u'聚类类别']
cluster_data.to_excel(outfile)
# 标准化以后的数据 与 聚类类别 组合
r1 = pd.Series(kmodel.labels_).value_counts()     # value_counts() 统计各个类标记的数目

r2 = pd.DataFrame(kmodel.cluster_centers_)
r = pd.concat([r2,r1],axis=1)
r.columns = list(data.columns) + [u'聚类个数']
r.to_excel(outfile)
