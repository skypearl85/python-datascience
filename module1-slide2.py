#Solve it #1
number = input('Please insert a number: ')
if (int(number) % 2 == 0):
    print('Number ' + number + ' is even')
else:
    print('Number ' + number + ' is odd')

#Solve it #2
#BMI = mass(kg) / height(meter) ^ 2
mass = int(input('Enter a mass (in kg): '))
height = int(input('Enter a height (in cm): '))

BMI = mass/((height/100) ** 2)
message = ''

if(BMI < 18.5):
    message = 'underweight'
elif(BMI >= 18.5 and BMI < 25):
    message = 'ideal weight'
elif(BMI >= 25 and BMI < 30):
    message = 'slightly overweight'
elif(BMI >= 30 and BMI < 40):
    message = 'overweight'
else:
    message = 'obesity'

print('BMI is ' + str(BMI) + ', ' + message)
