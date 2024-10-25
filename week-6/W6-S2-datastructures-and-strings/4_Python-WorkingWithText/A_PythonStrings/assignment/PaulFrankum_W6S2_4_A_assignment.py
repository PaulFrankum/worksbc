# string single quotes
single_string = 'Paul Frankum'
print(single_string)

# string double quotes so can add Apostrophe in the string
double_string = "Paul's Assignment"
print(double_string)

# string triple quotes can be more than one line and add special charaters like return tabs etc
triple_quotes = """
This is a comment
written in
more than just one line"""
print(triple_quotes)

# Use the `+` operator to concatenate a greeting with a user's name and format it using f-strings
firstname = "Paul"
middlenames = "Matthew"
surname ="Frankum"
fullname = firstname+" "+middlenames+" "+surname # adusing + method and adding space inbetwwen each var
fullname2 = " ".join([firstname, middlenames, surname]) #using join include spaces
print(fullname, " using + method")
print(fullname2, " using join method")

# Demonstrate string slicing to extract specific words or characters from a string.
result = []
namelist = fullname.split(" ")
for x in namelist:
    result.append(x[0].upper())
initals = result[0] + "." + result[1] + "." + result[2] + "." # using + method
initals2 = ".".join([result[0],result[1],result[2]]) # using join instead of +
print(initals, " using + method")  
print(initals2, " using join method")  

#  Prompt the user to input their name, age, and favorite color. Store this information in a dictionary.
print('Enter your name:')
name = input()
print('Enter your age:')
age = input()
print('Enter your favorite colour:')
colour = input()
this_dict = {
    "name": name,
    "age": age,
    "colour": colour
    }
print(this_dict)

# Use string methods to format the dictionary values (e.g., convert the name to uppercase, strip extra spaces from the favorite color) and print the updated dictionary.
this_dict["name"] = this_dict["name"].upper()
this_dict["colour"] = this_dict["colour"].strip() # does front andback of space by deafult can add charater if needed. also lstrip and rstrip do left and right if required

print(this_dict)

