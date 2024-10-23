# initialize tuples
person_info = ("John", "Doe", 30, "New York")
coordinates = (40.7128, 74.0060)

#Access and unpack elements
# first_name, last_name, age, city = person_info into variables
first_name = person_info[0]
last_name = person_info[1]
age = person_info[2]
city = person_info[3]
print(first_name, " ",last_name, " is ",age," and from ",city)

#Slice the tuple
#Get the first two elements from the `person_info` tuple
name = slice(2)
print("The Person Full Name is ",person_info[name])

#Concatenate and repeat tuples
#Concatenate two tuples to form a new tuple.
person_info2 = ("Jane", "Smith", 22, "Deane")
person_info_all = person_info + person_info2 + person_info
print(person_info, " first person info in tuples")
print(person_info2, " second person info in tuples")
print(person_info_all, " first second and first repeated of person info merge into one big tuples")

#Use tuple methods
#Demonstrate the use of `count()` and `index()`
x = person_info_all.count("Doe")
print(" Doe appear ",x ," times in the tuples")
y = person_info_all.index("Doe")
print(" Doe appear in first time in postion",y ," in the tuples")

#Real-world application: Return multiple values
#Create a function that returns a tuple of values, such as calculating the sum, difference, and product of two numbers
calculate_operations = (10, 5)
a = calculate_operations[0]
b = calculate_operations[1]
def calculate_answer(a, b):
    return (a + b, a - b, a * b, a / b)
print(calculate_answer(a, b)," the answer are the number Added, minus, multiplied , divide")
