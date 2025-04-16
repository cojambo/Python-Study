import os
import time
name = 'Test1'

path = 'C:/Users/erikv/Documents/repositorios GitHub/Python-Study/manipulating files/'

#If to verify file exist
if os.path.exists(path + name):
    print('File exist')
#Create the file
else:
    f = open(path + name,'x')
    f.close()

#slow time to see the created file
time.sleep(5)

#use os command to delete the file
os.remove(path + name)