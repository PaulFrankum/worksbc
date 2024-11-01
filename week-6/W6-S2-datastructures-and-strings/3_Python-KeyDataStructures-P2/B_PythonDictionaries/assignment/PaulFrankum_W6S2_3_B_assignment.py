# create nest dictionary name, age, and email
my_dict = {
  "person1" :{
    "name": "Paul Frankum",
    "age": 54,
    "email": "paul_frankum@msn.com"
  },
  "person2": {
    "name": "Tony Frankum",
    "age": 52,
    "email": "frankum@gmail"  
},
  "person3":{
    "name": "Jane Frankum",
    "age": 79,
    "email": "jane.frankum8@gmail.com"
  }
}

# add unquie id use loop
z=0
for k, v in my_dict.items():
    z=z+1
    my_dict[k]["id"] = z
print("Id added",my_dict)

# create second dictionary and merge with first
my_dict2 = {
  "person3" :{
    "name": "Jane Smith",
    "age": 45,
    "email": "jane.smith@example.com",
    "ID":  4
  },
  "person5": {
    "name": "John Doe",
    "age": 25,
    "email": "johndoe@gmail",
    "ID": 5
  
},
  "person6":{
    "name": "Eric Jones",
    "age": 19,
    "email": "jones@example.com",
    "ID" : 6
  }
}
# my_dict = my_dict + my_dict2
import copy
import itertools

def merge_dicts(a, b, complete):
    new_dict = copy.deepcopy(a)
    if complete:
        for key, value in b.items():
            new_dict.setdefault(key, []).extend(value)
    else:
        for key, value in b.items():
            if key in new_dict:
                # rename first key
                counter = itertools.count(1)
                while True:
                    new_key = f'{key}_{next(counter)}'
                    if new_key not in new_dict:
                        new_dict[new_key] = new_dict.pop(key)
                        break
                # create second key
                while True:
                    new_key = f'{key}_{next(counter)}'
                    if new_key not in new_dict:
                        new_dict[new_key] = value
                        break
            else:
                new_dict[key] = value
    return new_dict

full_dict = my_dict | my_dict2 # overwrite conflicts
print(full_dict)

full_dict2 = {**my_dict, **my_dict2} # overwrite conflicts
print(full_dict2)

new_dicts = merge_dicts(my_dict, my_dict2, False) # changes unquie name
print("merged and new ID created", new_dicts)

my_dict3 = my_dict
my_dict3.update(my_dict2) # overwrite conflict
print(my_dict3) 

# conditional merge say on age above 50
my_dict = {
  "person1" :{
    "name": "Paul Frankum",
    "age": 54,
    "email": "paul_frankum@msn.com"
  },
  "person2": {
    "name": "Tony Frankum",
    "age": 25,
    "email": "frankum@gmail"  
},
  "person3":{
    "name": "Jane Frankum",
    "age": 79,
    "email": "jane.frankum8@gmail.com"
  }
}

my_dict2 = {
  "person4" :{
    "name": "Jane Smith",
    "age": 45,
    "email": "jane.smith@example.com",
  },
  "person5": {
    "name": "John Doe",
    "age": 52,
    "email": "johndoe@gmail", 
},
  "person6":{
    "name": "Eric Jones",
    "age": 19,
    "email": "jones@example.com",
  }
}

age_dict = {}
full_dict = my_dict | my_dict2
for obj in my_dict:
  x = my_dict[obj]
  if x["age"] < 50:
    full_dict.pop(obj)
for obj in my_dict2:
  x = my_dict2[obj]
  if x["age"] < 50:
    full_dict.pop(obj)

print("Merged everyone over 50", full_dict)      