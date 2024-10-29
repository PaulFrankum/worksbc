import re

#**Basic Function**:
def greet(): return "Hello John!"

print(greet())

#**Function with Parameters**
def create_message(name, age): return "Hello " + name + " is " + age + " old."

print(create_message("John Smith", "25"))

#**Function with Default Arguments**
def greet2(name = "guest"): return "Hello "+name+"!"

print("no name passed " + greet2())
print("name passed " + greet2("Jane Smith"))

#**Regular Expression Function**
def validate_email(email): 
    email_address= r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    match = re.search(email_address, email)
    if match:
        return email + " Is a valid Email Address"
    else:
        return email + " Is not a valid Email Address"

print(validate_email("paul_frankum@msn.com"))
print(validate_email("paul_frankummsncom"))

# **Function Handling a Dictionary**
# def process_user_info(user_data)
    
# return answer

