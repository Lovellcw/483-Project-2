#Lovell Willmore 890341399
#Steven Alvarez 890191927

import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.io

def kmeans(k, data):
    centroids = initCentroids(k)
    counter = 0
    solution = []
    solution = findKmeans(centroids, data, counter)
    return solution

def initCentroids(k):
    centroids = []
    centroids.append([3,3])
    centroids.append([6,2])
    centroids.append([8,5])
    return centroids

def findKmeans(centroids, data, counter):
    print("\nCentroids: " + str(counter))
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
        c += 1
    r = 0
    for i in dist:
        b = 0
        c = 0
        for j in dist[r]:
            if(pythThrm(j[0],j[1]) < pythThrm(dist[r][b][0],dist[r][b][1])):
                b = c
            c += 1
        buckets[b].append(data[r])
        r +=1
    c = 0
    for row in buckets:
        if (len(row) > 0):
            avgx = 0
            avgy = 0
            for elem in row:
                avgx = avgx + elem[0]
                avgy = avgy + elem[1]
            avgx = avgx/len(row)
            avgy = avgy/len(row)
            newCentroid.append([avgx,avgy])
        else:
            newCentroid.append([4,4])
        c += 1
    print("\nNew Centroids: " + str(counter))
    print (newCentroid)
    if (newCentroid != centroids and counter < 20):
        counter += 1
        findKmeans(newCentroid, data, counter)
    else:
        

        #print("\nFirst Bucket: ")
        #print(buckets[0])
        plt.plot(*zip(*buckets[0]),'bo')

        #print("\Second Bucket: ")
        #print(buckets[1])
        plt.plot(*zip(*buckets[1]),'go')

        #print("\Third Bucket: ")
        #print(buckets[2])
        plt.plot(*zip(*buckets[2]),'mo')

        #print("\nFinal New Centroids: ")
        #print (newCentroid)
        plt.plot((newCentroid[0][0]), (newCentroid[0][1]),'bx')
        plt.plot((newCentroid[1][0]), (newCentroid[1][1]),'gx')
        plt.plot((newCentroid[2][0]), (newCentroid[2][1]),'mx')
        #print("\nPlot:")
        plt.show()
        return newCentroid


def pythThrm(a, b):
    return math.sqrt(math.pow(a,2) + math.pow(b,2))


mat = scipy.io.loadmat('kmeansdata.mat')
print("Using data:")
print(mat)

#Initial Plot

#plt.plot(mat['X'],'bo')
kmeans(3, mat['X'])





#plt.legend.set_label('Initial Distribution')


#colors = list("rgbcmyk")

#for i in mat.values():
#	x = i.keys()
#	y = i.values()
#	plt.scatter(x,y,colors=colors.pop())

#plt.legend(mat.keys())
#plt.show()
#mat = sorted(mat.items())
#x, y = zip(*mat)
#plt.scatter(mat['X'])
#plt.show()


#print(len(mat))


