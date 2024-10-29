import re

# find all matches
all_matches = re.findall('100', 'The price is 100 dollars and 100 euros')
print(all_matches)

# replace 100 with 200
replaced_text = re.sub('100', '200', 'The price is 100 dollars')
print(replaced_text)

#
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

