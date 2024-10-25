my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

print("Name is", my_dict['name'])
print("Age is ", my_dict['age'])
print("I live in ", my_dict['city'])

# change record
my_dict['name'] = "John"
my_dict['age'] = 26
my_dict['city'] = "London"

print("Name is", my_dict['name'])
print("Age is ", my_dict['age'])
print("I live in ", my_dict['city'])

# add a key
my_dict['email'] = "john@example.com"
print("Added email ",my_dict)

# pop and delete keys
my_dict.pop('city')
print("With city removed", my_dict)

del my_dict['name']
print("With name deletd ",my_dict)


# print pairs

for x in my_dict:
  print(x,"-",my_dict[x])
  
