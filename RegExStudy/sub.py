import re

text = 'I really like study python, programming is funny'


#replaces one character with another
sub = re.sub(' ','-',text)

print(sub)

