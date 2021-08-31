import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from sklearn.cluster import KMeans

img=cv2.imread('fff.png')
# plt.imshow(img)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# plt.imshow(img)
img=img.reshape((img.shape[1]*img.shape[0],3))
kmeans=KMeans(n_clusters=5)
s=kmeans.fit(img)
# print(s)
labels=kmeans.labels_
labels=list(labels)
# print(labels)
centroid=kmeans.cluster_centers_
print(centroid)
percent=[]
for i in range(len(centroid)):
  j=labels.count(i)
  j=j/(len(labels))
  percent.append(j)
plt.pie(percent,colors=np.array(centroid/255),labels=np.arange(len(centroid)))
plt.show()