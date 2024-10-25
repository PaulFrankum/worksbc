set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set3 = set1.union(set2) # join removing copies | & -
print("union ",union_set3)

union_set4 = set1 | set2 # join removing copies | & -
print("union | ",union_set4)

union_set5 = set1 & set2 # only show same values
print("union & ",union_set5)

union_set6 = set1 - set2 # only show unqinue in set 1 
print("union - ",union_set6)

set4 = set1.intersection(set2) # copy the front unqiue values
print("intersection ", set4)

difference_set5 = set1.difference(set2) # show different or what in set one that is not in set 2
print("difference ", difference_set5)

set1.add(6) # add 6 to set1 list
print("add set2 to set1",  set1)

set1.remove(3) # remove 3 from  list
print(set1)
