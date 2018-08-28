randomList = ['Test', 'Random', 'Orange', 'Blue', 'Rabbit', 'Best']
search = input('Search: ')

#Without lambda
woLambdaList = []

for item in randomList:
    if search.lower() in item.lower():
        woLambdaList.append(item)

print('Without lambda: ', woLambdaList)

#With lambda
lambdaList = list(filter(lambda i: search.lower() in i.lower(),randomList))
print('With lambda: ', lambdaList)