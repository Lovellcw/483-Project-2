import numpy as np
import pandas as pd
import math

def getList(df):
    results = df[df.columns[len(df.columns)-1]].tolist()
    EM = EntropyMatrix(results)
    ig = []
    n = []
    for i in range(0, len(df.columns)-1):
        print(df.columns[i])
        ig.append((IG(df.columns[i], df[df.columns[i]].tolist(), results, EM),df.columns[i]))
    ig = sorted(ig, key=lambda tup: tup[0], reverse = True);
    for i in ig:
        print ("IG(" + i[1] + ",x): " + str(i[0]) + "\n")
    return ig
def IG(setName, Set, result, EM):
    v = [Set[0]]
    c = [0]
    E = []
    P = []
    r = []
    ig = 0
    total = len(result)
    for i in Set:
        count = 0
        found = False
        for j in v:
            if i == j:
                c[count] = c[count] + 1
                found = True
            count = count + 1
        if not found:
            v.append(i)
            c.append(1)
    count = 0
    for i in v:
        print ("\nE(" + setName + "("+ i + "))\n")
        E.append(Entropy(setName, Set, result, i))
        P.append(Probability(c[count], total))
        r.append(c[count]/total)
        print ("P("+ setName + "("+ i + ")) = " + P[count] + "\n")
        count = count+1
    S = "IG("+setName+",x) = E(S)"
    count = 0
    for i in v:
        S = S + "-P(" + setName + "("+ i + "))*E(" + setName + "("+ i + "))"
        count = count + 1
    print (S)
    S = "IG("+setName+",x) = "  + str(EM)
    count = 0
    for i in E:
        S = S + "-(" + P[count] + ")*(" + str(i)+ ")"
        count = count + 1
    print (S)
    S = "IG("+setName+",x) = " + str(EM)
    count = 0
    for i in E:
        S = S + "-(" + str(r[count]) + ")*(" + str(i)+ ")"
        count = count + 1
    print (S)
    ig = EM
    count = 0
    for i in E:
        ig = ig - r[count]*i
        count = count + 1
    print ("IG("+setName+",x) = " + str(ig) + "\n")
    return ig
        
def EntropyMatrix(result):
    v = [result[0]]
    c = [0]
    P = []
    r = []
    R = []
    total = len(result)
    for i in result:
        count = 0
        found = False
        for j in v:
            if i == j:
                c[count] = c[count] + 1
                found = True
            count = count + 1
        if not found:
            v.append(i)
            c.append(1)
    count = 1;
    for i in v:
        print ("Value " + str(count) + ": ", i, "\nCount: ", c[count-1], "\n")
        count = count + 1
    
    print ("Total: ", total, "\n")
    for i in c:
        P.append(Probability(i, total))
        r.append(i/total)

    count = 0
    for i in P:
        print ("P("+v[count]+") = " + i)
        count = count + 1

    S = "\nE(S) = "
    for i in v:
        S = S + "-P(" + i + ")*Log2(P(" + i + "))"
    print (S)
        
    S = "E(S) = "
    for i in P:
        S = S + "-(" + i + ")*Log2(" + i + ")"

    print (S)
    for i in r:
        if(i == 0):
            R.append(0)
        else:
            R.append(math.log(i,2))

    S = "E(S) = "
    count = 0
    for i in r:
        S = S + "-(" + str(i) + ")*(" + str(R[count]) + ")"
        count = count + 1
    print(S)
    
    E = 0
    count = 0
    for i in r:
        E =  E +(-1)*((i*R[count]))
        count = count + 1
    
    print ("E(S) = " + str(E) + "\n")
    return E

def Entropy(setName, Set, result, value):
    v = [result[0]]
    c = [0]
    P = []
    r = []
    R = []
    total = 0
    counti = 0
    for i in Set:
        if i == value:
            total = total + 1
            countj = 0
            found = False
            for j in v:
                if result[counti] == j:
                    c[countj] = c[countj] + 1
                    found = True
                countj = countj + 1
            if not found:
                v.append(result[counti])
                c.append(1)
        counti = counti + 1
    count = 1;
    for i in v:
        print ("Value " + str(count) + ": ", i, "\nCount: ", c[count-1], "\n")
        count = count + 1
    
    print ("Total: ", total, "\n")
    for i in c:
        P.append(Probability(i, total))
        r.append(i/total)

    count = 0
    for i in P:
        print ("P("+v[count]+") = " + i)
        count = count + 1

    S = "\nE(" + setName + "("+ value + ")) = "
    for i in v:
        S = S + "-P(" + i + ")*Log2(P(" + i + "))"
    print (S)
        
    S = "E(" + setName + "("+ value + ")) = "
    for i in P:
        S = S + "-(" + i + ")*Log2(" + i + ")"

    print (S)
    for i in r:
        if(i == 0):
            R.append(0)
        else:
            R.append(math.log(i,2))

    S = "E(" + setName + "("+ value + ")) = "
    count = 0
    for i in r:
        S = S + "-(" + str(i) + ")*(" + str(R[count]) + ")"
        count = count + 1
    print(S)
    
    E = 0
    count = 0
    for i in r:
        E =  E +(-1)*((i*R[count]))
        count = count + 1
    
    print ("E(" + setName + "("+ value + ")) = "+ str(E) + "\n")
    return E
    
def Probability(v1, v2):
    ratio = str(v1) + "/" + str(v2)
    return ratio

titles = {'HAS a JOB', 'HAS an INSURANCE', 'VOTES', 'ACTION'}
d = {'HAS a JOB' : pd.Series(['yes', 'yes', 'yes', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'no']),
     'HAS an INSURANCE' : pd.Series(['yes', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no']),
     'VOTES' : pd.Series(['yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'no', 'yes', 'no']),
     'ACTION' : pd.Series(['leave-alone', 'leave-alone', 'force-into', 'leave-alone', 'force-into', 'leave-alone', 'leave-alone', 'force-into', 'leave-alone', 'force-into'])}

df = pd.DataFrame(d)

print("Starting with this data set\n", df)
getList(df)

d = {'Day' : pd.Series(['D1','D2','D3','D4','D5','D6','D7','D8','D9','D10','D11','D12','D13','D14']),
     'Outlook' : pd.Series(['Sunny','Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain']),
     'Humidity' : pd.Series(['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High']),
     'Wind' : pd.Series(['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong']),
     'Play' : pd.Series(['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No'])}

df = pd.DataFrame(d)
print("Starting with this data set\n", df)
getList(df)
