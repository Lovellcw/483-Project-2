import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.io

def kmeans(k, data):
    centroids = initCentroids(k)
    counter = 0
    solution = []
    solution = findKmeans(centroids, data, counter)
    print("\nSolution: ")
    print(solution)
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
    for row in dist:
        b = 0
        c = 0
        for elem in row:
            if(pythThrm(elem[0],elem[1]) < pythThrm(row[b][0],row[b][1])):
                b = c
            c += 1
        buckets[b].append(row[b])
        r +=1
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
        c += 1
    print("\nNew Centroids: " + str(counter))
    print (newCentroid)
    if counter != 10:
        counter += 1
        findKmeans(newCentroid, data, counter)
    print("\nFinal New Centroids: ")
    print (newCentroid)
    return newCentroid

def pythThrm(a, b):
    return math.sqrt(math.pow(a,2) + math.pow(b,2))


mat = scipy.io.loadmat('kmeansdata.mat')
print("Using data:")
print(mat['X'])

#Initial Plot

plt.plot(mat['X'],'bo')
centroids = []
centroids = kmeans(3, mat['X'])

print("\nFinal Centroids:")
print(centroids)
plt.plot(centroids,'rx')

print("\nPlot:")
plt.show()




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


