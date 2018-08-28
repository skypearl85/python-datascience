start = True
dictionary = {}

def mainMenu():
    print('\n' + '------- MAIN MENU -------')
    menuList = [ '1. View dictionary', '2. Add new dictionary', '3. Filter dictionary', '4. Quit']
    for menu in menuList: 
        print(menu)

    return int(input('Enter an option (1-4): '))

def printDictionary(dict):
    for key in dict.keys():
        if(dict[key]['type'] == 'str'):
            print('| ' + key + ' | ' + '\'' + dict[key]['value'] + '\'')
        else:
            print('| ' + key + ' | ' + dict[key]['value'])

while(start):
    option = mainMenu()
    if(option == 1):
        if(len(dictionary) < 1):
            print('Empty dictionary')
        else:
            print ('| key | value')
            printDictionary(dictionary)
    elif(option == 2):
        newKey = input('Add new key: ')
        newValueType = input('Add value type (int/str): ')
        newValue = input('Add new value: ')
        dictionary[newKey] = {'value': newValue, 'type': newValueType}
        
        print('New dictionary has been added')
    elif(option == 3):
        filterWord = input('Insert filter value: ')
    
        filteredDict = {k:v for (k,v) in dictionary.items() if filterWord in k}
        printDictionary(filteredDict)
    elif(option == 4):
        start = False
