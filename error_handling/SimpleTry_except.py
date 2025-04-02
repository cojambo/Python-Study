#Use try to 'test' a block of commands if an error occurs the program execute the except
try:
    print(x)

#except NameError is for a specific error, Where the variable is not defined
except NameError:
    print('X not defined')

#except with no adicional part, is for errors in general
except:
    print('UNKNOW ERROR')