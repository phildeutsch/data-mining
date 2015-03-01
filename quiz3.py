import itertools

def pairs(n):
    return(n*n + n*(n-1)/2)
    
def calc_supports(sdb):
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
            thissequence = 0
            for transaction in sequence:
                for item in transaction:
                    if item == i and thissequence == 0:
                        s = s + 1
                        thissequence = 1

        support.append(s)

    itemsup = dict(zip(items, support))
    return(itemsup)


#Q2:
sdb   = {1: ["a", "bc", "de", "c", "f"],
        2:  ["a", "bd", "bc", "e", "f"],
        3:  ["b", "c", "ad", "e", "b", "f", "c","d"],
        4:  ["a", "b", "cd", "d", "ab", "e"]
        }

min_sup = 3
itemsup = calc_supports(sdb)
length1_p  = [k for k,v in itemsup.items() if v >=min_sup]
length1_np = [k for k,v in itemsup.items() if v >=0]

n_pruning = len(length1_p)
n_nopruning = len(length1_np)

print("Question 2")
print("Without pruning: " + str(pairs(n_nopruning)))
print("With pruning:    " + str(pairs(n_pruning)))


itemsup = calc_supports(sdb)
length1 = [k for k,v in itemsup.items() if v >=min_sup]
        