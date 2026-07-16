from itertools import combinations
list = [-10,2,7,-5,9,36,-45]
print("POSITIVE COMBINATIONS")
for r in range(1,len(list) + 1):
    for combo in combinations(list,r):
        if all(num > 0 for num in combo):
            print(combo)
