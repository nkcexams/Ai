import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data= pd.read_csv('Ecommerce Customers.csv')
X=data.iloc[:,[3,4]].values

wcss=[KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0).fit(X).inertia_ for i in range(1,11)]

plt.plot(range(1,11),wcss)
plt.title('the elbow method')
plt.xlabel('number of clusters')
plt.ylabel('wcss')
plt.show()


kmeans=KMeans(n_clusters=5,init='k-means++',max_iter=300,n_init=10,random_state=0)
Y_kmeans=kmeans.fit_predict(X)

colors = ['red', 'blue', 'green', 'cyan', 'magenta']
labels = ['Careful', 'Standard', 'Target', 'Careless', 'Sensible']

for i,color in enumerate(colors):
    plt.scatter(X[Y_kmeans == i,0],X[Y_kmeans == i,1],s=100,c=color,label=labels[i])
    plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='yellow',label='cecntroids')

plt.title('the number of business customers')
plt.xlabel('annual income(k$)')
plt.ylabel('spending score(1-100)')
plt.legend()
plt.show()
