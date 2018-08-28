# def fizzBuzz(number):
#     for i in range(number + 1):
#         if(i % 3 == 0 and i % 5 == 0):
#             print('FizzBuzz')
#         elif(i % 5 == 0):
#             print('Buzz')
#         elif(i % 3 == 0):
#             print('Fizz')
#         else:
#             print(i)
# fizzBuzz(20)

# def fibonancci(number):
#     fiboList = [1,1]
#     for i in range(number - 2):
#         if(i < (number - 2)):
#             fiboList.append(fiboList[i] + fiboList[i+1])
#     print(fiboList)
#     print('fibonacci 12 is '+ str(fiboList.pop()))
# fibonancci(12)

# def reverse(rList):
#     for i in range(int(len(rList) / 2)):
#         temporary = rList[i]
#         rList[i] = rList[len(rList) - (i+1)]
#         rList[len(rList) - (i+1)] = temporary
#     print(rList)
# reverse([1,2,3,4,5,6,7,8,9,10,11])

# import math
# sample = [1,1,2,2]
# def mean(listNo):
#     sum = 0
#     for no in listNo:
#         sum += no
#     print('Mean: ' + str(int(sum/(len(listNo)))))

# def median(listNo):
#     for i in range(len(listNo)):
#         j = i + 1
#         for j in range(len(listNo)):
#             if(listNo[i] < listNo[j]):
#                 temporary = listNo[i]
#                 listNo[i] = listNo[j]
#                 listNo[j] = temporary

#     if(len(listNo) % 2 == 0):
#         medianIndex = int(len(listNo) / 2)
#         median = int((listNo[medianIndex] + listNo[medianIndex - 1]) / 2)
#         print('Median: ' + str(median))
#     else:
#         medianIndex = math.floor(len(listNo) /2)
#         print('Median: ' + str(listNo[medianIndex]))

def mode(listNo):
    uniqueList = list(set(listNo))
    countList = []
    maxCount = 0
    mode = []

    dictNo = {}
    for i in range(len(listNo)):
        dictNo[listNo[i]] = dictNo.get(listNo[i], 0) + 1

    for item in dictNo:
        countList.append(dictNo[item])
        
    for i in range(len(countList)):
        if(countList[i] >= maxCount):
            maxCount = countList[i]
    
    for item in dictNo:
        condition = len(uniqueList) != len(countList)

        if(dictNo[item] == maxCount and condition):
            mode.append(item)
            
    print('Mode: ' + str(mode))

mean(sample)
median(sample)
mode(sample)

# def modefinder(thelist):
#     countpermodes =max(map(thelist.count,thelist))
#     set_countpermodes =set(filter(lambda a: thelist.count(a) ==countpermodes, thelist))
    
#     if set(thelist) - set_countpermodes != set():
#         print(countpermodes) 
#     else:
#         print("There is no mode.") 


# nomode = [1,2,3,4,5,6,7]
# withmodes = [1,2,2,2,3,4,5,6,6,6]
# modefinder(nomode)
# modefinder(withmodes)