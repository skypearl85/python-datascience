import math
#Solve it #1
x = 4
y = 3
z = 2

w = ((x + y * z) / (x * y)) ** z
print(w)

#Solve it #2
number = input('Please enter any number: ')
result = (int(number) ** 2)
print('to the power of 2 = ' + str(result))

#Solve it #3
total = 485
year = int(total / 360)
month = int((total % 360) / 30)
week = int((total % 360) / 30) % 4
day = int((total % 360) % 30)

# year = math.floor(total / 360)
# month = math.floor((total % 360) / 30)
# week = math.floor(((total % 360) % 30) / 7)
# day = math.floor(((total % 360) % 30) % 7)

print('485 days equals to ' + str(year) + ' year(s) ' + str(month) + ' month(s) ' + str(week) + ' week(s) ' + str(day) + ' day(s) ')

#Solve it #4
# total = 49
# totalRatio = 14
# individual = total/totalRatio
# andi = 4 * individual
# budi = 10 * individual

andi = int(4/14 * 49 + 2)
budi = int(10/14 * 49 + 2)
print('In next 2 years, Andi will be ' + str(andi) + ' years old and Budi will be ' + str(budi) + ' years old')

# #Solve it #5
# string = "Hello World"
# count = 0
# for s in string:
#     if s == 'o':
#         count += 1

# print('The amount of letter o from the word ' + string + ' is ' + str(count))

#Solve it #6
# A = 60
# B = 40
# distance = 120
# 60t = 120 - (40t)

start = 9
distance = 120
speedTotal = 100/3600
totalInSecond = distance / speedTotal
hour = math.floor(totalInSecond / 3600)
minute = math.floor((totalInSecond % 3600) / 60)
second = math.floor((totalInSecond % 3600) % 60)

# hour = math.floor(120/100)
# minute = math.floor(120/100 * 60 - 60)
timeCollide = 9 + hour
print('Time they collide is ' + str(timeCollide) + '.' +  str(minute) + '.' + str(second))