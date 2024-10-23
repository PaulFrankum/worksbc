# Start writing code with comments form here

# alist of cars
cars = ["Audi", "BMW", "Chevrolet", "Daewoo", "Esel"]

# count the number of times a striong appears in list
print(cars.count("BMW"), " counts the number of times BMW appers in list")

# Chevrolet has changed to Chrysele 
cars[2] = "Chryseler"
print(cars, " Chevrolet has changed to Chryseler")

# pop removes with no number removes last from list with number removes that one strting from 0
cars.pop(1)
print(cars," removes second car from list")
cars.pop()
print(cars," removes the last car from list")

# insert add to list
cars.insert(1, "BMW")
print(cars," adds to second in list")
cars.insert(-1, "Esel")
print(cars," adds to 2nd to end of list")

# added Ford to the end
car = ("Ford","GMC")
cars.extend(car)
print(cars, " Added 2nd listd to the List")

# reverse order
cars.reverse()
print (cars, "list backwards")

# sort 
cars.sort()
print (cars, "sort in Alphabetical order")

# index
x = cars.index("Esel")
print (" Esel", x, "in the list (starting from 0)")

# clear empty the list
cars.clear()
print(cars, "Clears the list")

