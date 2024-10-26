# Function that returns Hello world 
def greet(): 
    return "Hello, World!"
# call function greet and print whats returned
print(greet())

# function that adds 2 numbers
def add(a, b): 
    return a + b
#calls a function that returns 2 numbers added
print(add(3, 5))

#function that returns hello and name if sent if not hell guest
def greet2(name="Guest"): 
    return f"Hello, {name}!"

# greet2 and print reesult which is either hello guest if no nmae sent and hell name if sent
print(greet2())
print(greet2("Paul"))

# use *args and **kwargs
# return first name in list
def print_info(*args):
    return args[0]

print(print_info("jane", "Paul", "Tony"))

# use var lname and reutn with message
def my_function(**kid):
  return "His last name is " + kid["lname"]

print (my_function(fname = "John", lname = "Smith"))