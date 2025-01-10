import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import fcluster

points=np.array([
    [1,2],
    [2,3],
    [3,4],
    [5,6],
    [8,8],
    [8,9],
    [25,30]
])
linked=linkage(points,method='ward')
plt.figure(figsize=(8,5))
dendrogram(linked,labels=list(range(1,len(points)+1)))
plt.title("Dendrogram for Hierarchical Clustering")
plt.xlabel("Data points")
plt.ylabel("Distance")
plt.show()

clusters=fcluster(linked,t=10,criterion='distance')
print("Cluster assignments:",clusters)

plt.figure(figsize=(8,5))
for i,cluster in enumerate(clusters):
    plt.scatter(points[i,0],points[i,1],label=f"Cluster {cluster}")
for i,txt in enumerate(range(1,len(points)+1)):
    plt.annotate(txt,(points[i,0]+0.2,points[i,1]+0.2))
plt.title("Clusters")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
