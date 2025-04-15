import re

text = 'I really like study python, programming is funny'

search = re.search(input('Search: '),text)
try:
    #calc leng of the 'search'
    st = search.start()
    end = search.end()
    len= end - st

    #Start of the 'Search' on the text
    print(search.start())

    #End of the 'Search' on the text
    print(search.end())

    #Print the leng of the 'search'
    print(len)
except:
    print('None')