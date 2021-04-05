def linearSearch(keyword, list):
    for i in list:
        if i == keyword:
            print('Found: ' + keyword)


array = ['hello', 'there', 'general', 'kenobi']
linearSearch('general', array)