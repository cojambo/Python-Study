x = 'oi'
try:
    print(x)

except:
    print('ERROR')


#in this case else is executed if 'try' don't result in a Error, if that happening except is not executed
else:
    print('All Good') 

#Finally is always executed after a error handling, don't matter if try result a error or not
finally:
    print('End of the treatment')