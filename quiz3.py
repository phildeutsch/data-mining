import itertools

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
            items.append(item)
items = set(items)

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

support
# since the support is always greater than min_support = 3, 
# the number of candidates with and without pruning is the same
6*6+6*5/2

# Q3:
sdb   = {1: ["a", 
        }