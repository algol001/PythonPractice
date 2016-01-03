
#original
promptHours ='enter hours:\n'
promptRate = 'enter rate:\n'

hours = raw_input(promptHours)
rate = raw_input(promptRate)

Pay = float(hours)* float(rate)

print('Pay:')
print(Pay)

#Ben Edited
promptHours ='enter hours: '
promptRate = 'enter rate: '

hours = float(raw_input(promptHours))
rate = float(raw_input(promptRate))

Pay = hours* rate

print('Pay is %d today' % (Pay))

print('Pay: '+ str(Pay))
#print(Pay)

#Excercise 2.4


width = 17

height = 12.0
print(width/2)
print(width/2.0)
print(height/3)

print(1 + 2 * 5)

#Exercise 2.5
tempCels = float(raw_input('Enter Degrees Celsius\n'))
tempFar = tempCels*1.8 + 32
print(tempFar)
