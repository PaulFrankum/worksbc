# create nest dictionary name, age, and email
my_dict = {
  "person" :{
    "name": "Paul Frankum",
    "age": 54,
    "email": "paul_frankum@msn.com"
  },
  "person": {
    "name": "Tony Frankum",
    "age": 52,
    "email": "frankum@gmail"  
},
  "person":{
    "name": "Jane Frankum",
    "age": 79,
    "email": "jane.frankum8@gmail.com"
  }
}

# add unquie id use loop
z=0
new_dict = {}
for x, obj in my_dict.items():
  print(x)

  for y in obj:
    z=z+1
    my_dict.update({"ID": z})
    print(my_dict)


# print(my_dict)  
# for x, obj in my_dict.items():
  # print(x)

#  for y in obj:
# print(y + ':', obj[y])  

# create second dictionary and merge with first
my_dict2 = {
  "person1" :{
    "ID":  2,
    "name": "Jane Smith",
    "age": 45,
    "email": "jane.smith@example.com"
  },
  "person2": {
    "ID": 3,
    "name": "John Doe",
    "age": 25,
    "email": "johndoe@gmail"  
},
  "person3":{
    "ID" : 4,
    "name": "Eric Jones",
    "age": 19,
    "email": "jones@example.com"
  }
}

# my_dict = my_dict + my_dict2
print(my_dict)

# conditional merge say on age above 18

