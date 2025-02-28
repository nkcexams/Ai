import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

data=pd.read_csv('Ecommerce Customers.csv')
x=data.iloc[:,[3,4]].values

sch.dendrogram(sch.linkage(x,method='ward'))
plt.title('dendrogram')
plt.xlabel('online business customers')
plt.ylabel('euclidean distance')
plt.show()


hc=AgglomerativeClustering(n_clusters=5, metric='euclidean',linkage='ward')
Y_hc=hc.fit_predict(x)

colors = ['red', 'blue', 'green', 'cyan', 'magenta']
labels = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']

for i,color in enumerate(colors):
    plt.scatter(x[Y_hc == i,0],x[Y_hc == i,1],s=100,c=color,label=labels[i])
plt.title('clusters of online business customers')
plt.xlabel('annual income(k$)')
plt.ylabel('spending score(1-100)')
plt.legend()
plt.show()
