# import json module
import json
# create json string
json_string = '{"name": "Alice", "age": 25, "city": "New York"}'
# convert string to json object
data = json.loads(json_string)
#print values
print(data['name'])
print(data['age'])
print(data['city'])
# change age
data['age'] = 26
# print again to show change
print(data['name'])
print(data['age'])
print(data['city'])
#change json back to string
json_data = json.dumps(data)
print(json_data)

