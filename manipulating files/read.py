name = 'Test1'

f = open('C:/Users/erikv/Documents/repositorios GitHub/Python-Study/manipulating files/' + name,'r')

#r - Read
#a - Append
#w - Write
#x - Create
#t - text
#b - binary

#read all the file
print(f.read())


#read read line for line
for l in f:
    print(l)

#read 1 line
#print(f.readline())

f.close()