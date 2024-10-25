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

# Use f-strings or other formatting methods to create formatted strings with variables.
age = 54

formatted_string = f"My name is {fullname} and I am {age} years old." 
print(formatted_string)

