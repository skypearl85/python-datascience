def _7segment(segmentList):
    first = []
    for i in range(len(segmentList)):
        if(segmentList[i] == 1 or segmentList[i] == 4):
            first.append('   ')
        else:
            first.append(' _ ')

    second = []
    for i in range(len(segmentList)):
        if(segmentList[i] == 1 or segmentList[i] == 7):
            second.append('  |')
        elif(segmentList[i] == 2 or segmentList[i] == 3):
            second.append(' _|')
        elif(segmentList[i] == 4 or segmentList[i] == 8 or segmentList[i] == 9):
            second.append('|_|')
        elif(segmentList[i] == 0):
            second.append('| |')
        else:
            second.append('|_ ')

    third = []
    for i in range(len(segmentList)):
        if(segmentList[i] == 2):
            third.append('|_ ')
        elif(segmentList[i] == 3 or segmentList[i] == 5 or segmentList[i] == 9):
            third.append(' _|')
        elif(segmentList[i] == 1 or segmentList[i] == 4 or segmentList[i] == 7):
            third.append('  |')
        else:
            third.append('|_|')

    print(' '.join(first))
    print(' '.join(second))
    print(' '.join(third))

start = True
inputSegment = []
while(start):
    option = input('1.Add number \n2.View number \n3.Quit \nChoice: ')
    if(option == '1'):
        segment = int(input('Insert number: '))
        inputSegment.append(segment)
        print('\n')
    elif(option == '2'):
        _7segment(inputSegment)
        print('\n')
    elif(option == '3'):
        start = False
    else:
        print('Invalid input \n')