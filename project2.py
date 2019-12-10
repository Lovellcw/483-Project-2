import numpy as np
import math
import scipy.io

def kmeans(k, data):
    centroids = initCentroids(k)
    return findKmeans(centroids, data)

def initCentroids(k):
    centroids = []
    x = 0
    y = 0
    for i in range(k):
        centroids.append([x,y])
        if(i%2==0):
           x = x + 1
        else:
           y = y + 1
    return centroids

def findKmeans(centroids, data):
    print()
    print(centroids)
    dist = []
    buckets = []
    newCentroid = []
    for i in centroids:
        buckets.append([])
    c = 0
    for i in data:
        dist.append([])
        for j in centroids:
            x = abs(i[0] - j[0])
            y = abs(i[1] - j[1])
            dist[c].append([x,y])
        c = c +1
    r = 0
    for row in dist:
        b = 0
        c = 0
        for elem in row:
            if(pythThrm(elem[0],elem[1]) < pythThrm(row[b][0],row[b][1])):
                b = c
            c = c+1
        buckets[b].append(row[b])
        r = r + 1
    c = 0
    for row in buckets:
        if (len(row) > 0):
            avgx = 0
            avgy = 0
            for elem in row:
                avgx = avgx + elem[0]
                avgy = avgy + elem[0]
            avgx = avgx/len(row)
            avgy = avgy/len(row)
            newCentroid.append([avgx,avgy])
        else:
            newCentroid.append(centroids[0])
        c = c + 1

    print (newCentroid)
    if(newCentroid == centroids):
        return newCentroid
    else:
        findKmeans(newCentroid, data)
        
def pythThrm(a, b):
    return math.sqrt(math.pow(a,2) + math.pow(b,2))


mat = scipy.io.loadmat('kmeansdata.mat')
print("Using data:\n")
print(mat['X'])
kmeans(3, mat['X'])