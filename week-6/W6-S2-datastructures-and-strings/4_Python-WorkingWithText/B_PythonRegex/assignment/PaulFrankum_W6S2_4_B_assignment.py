import re

# define tel pattern

tel= r'\d{5}\s\d{6}'
text= "This is a test to see if pattern matches with uk tel number 01256 819924"
match = re.search(tel, text)
print(match)
if match:
  print("Successful date match")
else:
  print("No date match")

# define http:// pattern

web_address= r'https?://(?:www\\.)?[ a-zA-Z0-9./]+'
text= "https://www.google.com"
match = re.search(web_address, text)
print(match)
if match:
  print("Successful web address match")
else:
  print("No web address match")

# define date pattern

date = r'(\d{2}+/\d{2}+/\d{4}+)'
text= "My date of birth is 04/07/1970"
match = re.search(date, text)
print(match)
if match:
  print("Successful match date")
else:
  print("No match date")

# re.findall(), re.sub()
pattern = r'£\d'
text = "apples £1, Banana £1, Cheery £1 and Dates £1" 
match =re.findall(pattern, text)
print(match)
match =re.subn("£1", "$1", text)
print(match)

# tokenize a sentence
text = "The quick brown fox jumps over the lazy dog."
sentences = re.split(r'\s', text)
print(sentences)

#re.fullmatch()
match = True
while match:
  telephone = input("Phone Number?")
  if re.fullmatch(tel, telephone):
    match = False
    print(telephone)
  else:
    print("Invalid telephone number")

match = True
while match:
  dob = input("date of birth?")
  if re.fullmatch(date, dob):
    match = False
    print(dob)
  else:
    print("Invalid date of birth number")

match = True

while match:
  web = input("Enter webaddress")
  if re.fullmatch(web_address, web):
    match = False
    print(web)
  else:
    print("Invalid web address")

# re.compile() The re.compile function creates a regular expression object
#  by compiling a regular expression pattern, which can be used as a
#  matching pattern in the re.match, re.search, etc. functions.
#
# The use of this function makes sense mainly when we want to reuse a
#  search pattern throughout our code, since the previous compilation of 
# the search pattern makes the process more efficient. For example, we can
#  start from the following code that performs a search for the same pattern
#  in two different texts:  
text = "My cat, your dog and my cats are playing"
pattern = r'dog[s]?|cat[s]?'
re_obj = re.compile(pattern)
print(re_obj.findall(text))

# output ['cat', 'dog', 'cats']

# re.escape() escape() function takes a pattern as input and returns a
#  string with special characters escaped. String translate tables are  
# created using str. maketrans() and map specific characters to new values.

# Define the pattern string
pattern = 'escape-string-python with re.escape()'
# Use re.escape() to escape special characters in the pattern string
string = re.escape(pattern)
# Print the escaped string
print(string)
# output escape\-string\-python\ with\ re\.escape\(\)