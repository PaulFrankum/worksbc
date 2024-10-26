import re

# Define a pattern

# pattern = r'\d+


#Search for patterns**

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")