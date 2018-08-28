# #Recursive function
# def power(x, y):
#     if(y == 1):
#         return x
#     else:
#         y -= 1
#         return x * power(x , y)
# print(power(2,4))

# #Default parameter
# def multiple(num = 2, num2 = 5):
#     return num * num2
# print(multiple(num2 = 10))

#Solve it #1
x = [40, 100, 1, 5, 25, 10]

def sort(sortList, sortType):
    for i in range(len(sortList)):
        j = i + 1
        for j in range(len(sortList)):
            if(sortType == 'ascending'):
                if(sortList[i] < sortList[j]):
                    temporary = sortList[i]
                    sortList[i] = sortList[j]
                    sortList[j] = temporary
            if(sortType == 'descending'):
                if(sortList[j] < sortList[i]):
                    temporary = sortList[i]
                    sortList[i] = sortList[j]
                    sortList[j] = temporary
    return sortList

print('Ascending order: ' + str(sort(x, 'ascending')))
print('Descending order: '+ str(sort(x, 'descending')))

#Solve it #2
y = [40, 100, 1, 5, 25, 10]

def max(maxList):
    for i in range(len(maxList)):
        max = maxList[i]
        j = i + 1
        for j in range(len(maxList)):
            if(max < maxList[j]):
                max = maxList[j]
    return max

def min(minList):
    for i in range(len(minList)):
        min = minList[i]
        j = i + 1
        for j in range(len(minList)):
            if(min > minList[j]):
                min = minList[j]
    return min

print('The highest element in the list is: ', str(max(y)))
print('The lowest element in the list is: ', str(min(y)))