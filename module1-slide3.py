# #Solve it #1
# print('Solve it 1')
# row = int(input('How many row: '))
# s = ''

# for item in range(row,0,-1):
#     for item2 in range(0,item):
#         s += ' * '
#     s += '\n'

# print(s)

# #Solve it #2
# print('Solve it 2')
# row = int(input('How many row: '))
# s = ''

# for item in range(row,0,-1):
#     for item2 in range(0, item):
#         s += ' * '
#     s += '\n'

# for item in range(2,row+1):
#     for item2 in range(0,item):
#         s += ' * '
#     s += '\n'

# print(s)

# #Solve it #3
# print('Solve it 3')
# s = ''
# row = int(input('How many row: '))
# dotRange = row * 2 - 1
# startPosition = int((dotRange/2) * 3)

# for item in range(1,dotRange + 1,2):
#     s += ' ' * startPosition
#     for item2 in range(0, item):
#         s += ' * '
    
#     startPosition -= 3
#     s += '\n'
# print(s)

# size = int(input('size: '))
# s= ''

# for num in range(size):
#     for num1 in range(0, size-1-num):
#         s += '   '
#     for num2 in range(0, (num*2)+1):
#         s += ' * '
#     s+= '\n'
# print(s)

# #Solve it #4
# print('Solve it 4')
# s = ''
# row = int(input('How many row: '))
# dotRange = row * 2 - 1
# startPosition = 0

# for item in range(dotRange,0,-2):
#     s += ' ' * startPosition
#     for item2 in range(0, item):
#         s += ' * '
    
#     startPosition += 3
#     s += '\n'

# print(s)

# #Solve it #5
# print('Solve it 5')
# s = ''
# dotRange = 10
# startPosition = int((dotRange/2 - 1) * 3)

# for item in range(1,dotRange,2):
#     s += ' ' * startPosition
#     for item2 in range(0, item):
#         s += ' * '
    
#     startPosition -= 3
#     if(item + 1 != dotRange):
#         s += '\n'

# print(s)

# s = ''
# dotRange = 9
# startPosition = 0

# for item in range(dotRange,0,-2):
#     s += ' ' * startPosition
#     for item2 in range(0, item):
#         s += ' * '
    
#     startPosition += 3
#     s += '\n'

# print(s)

#Solve it #6
print('Solve it 6')
row = int(input('How many stars: '))
s = ''
rowTotal = row * 2 - 1
starCountDec = 1
starCountInc = 1
# when decreasing the stars, it will start with 1 star
spaceDec = 1
# when increasing the stars, it will start with 4 stars
spaceInc = (rowTotal - 4)

for item in range(rowTotal):
    # if first or last row, print all stars
    if (item == 0 or item == rowTotal - 1):
        s+= ' * ' * rowTotal
    # otherwise print the stars with the space between
    else:
        if(item + 1 <= row):
            s+= ' * ' * (row - starCountDec) + '   ' * spaceDec + ' * ' * (row - starCountDec)
            # space based on 2 stars difference
            spaceDec += 2
            starCountDec += 1
        else:
            s+= ' * ' * (starCountInc + 1) + '   ' * spaceInc + ' * ' * (starCountInc + 1)
            # space based on 2 stars difference
            spaceInc -= 2
            starCountInc += 1
    print(s)
    s=''
   
# #kotak
# # for item in range(6):
# #     z = ' * ' * 5
# #     print(z)
        
# synchronous
# atas > bawah harus beres dari atas
# function1() { beresin ini dulu }
# function2() {}

# asynchronous
# atas > bawah, jalanin barengan
# function1() { jalan }
# function2() { jalan }


# # lintas shuttle
# # bsd
# # jalan raya serpong no 39
# # wtc matahari serpong