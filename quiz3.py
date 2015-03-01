import itertools
import pandas as pd

def pairs(n):
    return(n*n + n*(n-1)/2)

#Q2: 51;51
sdb   = {1: ["a", "bc", "de", "c", "f"],
        2:  ["a", "bd", "bc", "e", "f"],
        3:  ["b", "c", "ad", "e", "b", "f", "c","d"],
        4:  ["a", "b", "cd", "d", "ab", "e"]
        }

# Calculate items in sequence DB
items = [] 
for sequence in sdb.values():
    for transaction in sequence:
        for item in transaction:
            if item not in items:
                items.append(item)

# Calculate support for each item
support = []
for i in items:
    s = 0
    for sequence in sdb.values():
        for transaction in sequence:
            for item in transaction:
                if item == i:
                    s = s + 1
    support.append(s)

itemsup = dict(zip(items, support))
min_sup = 3
length1 = [k for k,v in itemsup.items() if v >=3]

n_pruning = len(length1)
n_nopruning = len(items)

print("Question 2")
print("Without pruning: " + str(pairs(n_nopruning)))
print("With pruning:    " + str(pairs(n_pruning)))

# Q3:
