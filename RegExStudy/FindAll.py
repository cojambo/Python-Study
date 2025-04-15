import re #RegEx

text = 'I really like study python, programming is funny'

findall = input('Search: ')


#find all the 'search' in the text
find = re.findall(findall,text)

amount = len(find)

print(text)

print(f'Search for "{findall}" in the text')
print(f"Find {amount} of '{findall}' in the text")