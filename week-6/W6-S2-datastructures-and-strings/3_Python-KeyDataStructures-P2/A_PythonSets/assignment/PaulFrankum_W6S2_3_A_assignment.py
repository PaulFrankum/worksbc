# create to random sets
import random
set1 = set(random.randint(1, 10) for _ in range(5))
set2 = set(random.randint(5, 15) for _ in range(5))

print("Set 1:", set1) # print set 1
print("Set 2:", set2) # print set 2

# union of set1 and set 2
set3 = set1 & set2
print("Union of Set 1 and Set 2:",  set3) # print set 2

# Intersection of Set 1 and Set 2:

set4 = set1.intersection(set2)
print("Intersection of Set 1 and Set 2:",set4)

# Difference (Set 1 - Set 2): 
set5 = set1.difference(set2)
set6 = set1 - set2

print("Intersection of Set 1 and Set 2:", set5)
print("Set 1 - Set 2:", set6)

# Set 1 after adding 10: {1, 3, 5, 6, 8, 10}
set1.add(10) # add 10 to set1 list
print("add set2 to set1",  set1)

# Set 1 after removing 10: {1, 3, 5, 6, 8}
set1.remove(10) # remove 10 from  list
print(set1)

#Even numbers in Set 1: {6, 8}
set7 = {x for x in set1 if x % 2 == 0}
print("Print Even numbers ", set7)
