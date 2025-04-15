import re

text = 'I really like study python, programming is funny'


#split the text in a array
split = re.split(' ',text)

print(split)

print('-----')
print(split[1])
print('-----')

for a in split:
    print(a,'\n')
