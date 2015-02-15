import itertools
import sys
from collections import Counter

s = 0.5
c = 0.5

tdb1 = {10: {"Beer", "Nuts", "Diaper"},
        20: {"Beer", "Coffee", "Diaper", "Nuts"},
        30: {"Beer", "Diaper", "Eggs"},
        40: {"Beer", "Nuts", "Eggs", "Milk"},
        50: {"Nuts", "Coffee", "Diaper", "Eggs", "Milk"}
        }

items = [] 
for itemsets in tdb1.values():
    for item in itemsets:
        items.append(item)
items = set(items)

def frequentItems(items, tdb, n, s):
    itemsets = set(itertools.combinations(items, n))

    itemTransactions = []
    for i in itemsets:
        for k,v in tdb1.items():
            if set(v).intersection(set(i)) == set(i):
                #print(i)
                #print(k)
                itemTransactions.append(i)

    ret = []
    for k,v in sorted(Counter(itemTransactions).items()):
        if v >= s * len(tdb):
            ret.append([k, v])
    return(dict(ret))

print("All frequent one-itemsets:")
print(frequentItems(items, tdb1, 1, s))

print("All frequent two-itemsets:")
print(frequentItems(items, tdb1, 2, s))

print("All frequent three-itemsets:")
print(frequentItems(items, tdb1, 3, s))

print("All strong association rules:")
f2 = frequentItems(items, tdb1, 2, s)
k2 = [k for k in f2.keys()]
v2 = [v for v in f2.values()]

f1 = frequentItems(items, tdb1, 1, s)
k1 = [k[0] for k in f1.keys()]
v1 = [v    for v in f1.values()]

for i in range(len(k2)):
    i1 = k2[i][0]
    i2 = k2[i][1]
    for j in range(len(k1)):
        if k1[j] == i1:
            confidence = v2[i]/v1[j]
    if v2[i] >= s * len(tdb1) and confidence >= c:
        print("{0:<6} -> {1:<6}: ({2},{3})".format(i1, i2,str(v2[i]),confidence))
    
    i1 = k2[i][1]
    i2 = k2[i][0]
    for j in range(len(k1)):
        if k1[j] == i1:
            confidence = v2[i]/v1[j]
    if v2[i] >= s * len(tdb1) and confidence >= c:
        #print(i1, " -> ", i2, ": (", v2[i], ", ", confidence, ")") 
        print("{0:<6} -> {1:<6}: ({2},{3})".format(i1, i2,str(v2[i]),confidence))


