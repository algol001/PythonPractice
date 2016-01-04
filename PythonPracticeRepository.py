
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

#chapter 3 example
input = raw_input('enter Far Temp')

try:
	far = float(imp)
	cel = (far-32.0) * 5.0/9.0
	print cel 

except Exception, e:
	print 'please enter a number'
	
#exercise 3.1 * 3.2

try:
	hours = float(raw_input('Enter hours\n'))
	rate = float(raw_input('Enter Rate\n'))

	if hours < 40:
		pay = hours * rate
	elif hours > 40:
		extraHours = hours-40
		pay = 40*rate + extraHours*(rate*1.5)

	print pay

except:
	print('error, enter numeric input')


# exercise 3.3
try:
	score = float(raw_input('Please enter a score between 0.0 and 1.0\n'))

	if score > 1.0 or score < 0.0:
		score = raw_input('Incorrect range.please enter score between 0.0 and 1.0\n')


#not really sure why kept giving me wrong answer when F at the end
	if score >= 0.0 and score<0.6:
		print('F')
	if score >= 0.9:
		print('A')
	elif score >= 0.8:
		print('B')
	elif score >= 0.7:
		print('C')
	elif score >= 0.6:
		print('D')

except:
	print('error: please enter a number\n')


	#fixed this exercise: not sure how
	try:
	score = float(raw_input('Please enter a score between 0.0 and 1.0\n'))

	if score > 1.0 or score < 0.0:
		score = raw_input('Incorrect range.please enter score between 0.0 and 1.0\n')

	
	if score >= 0.9:
		print('A')
	elif score >= 0.8:
		print('B')
	elif score >= 0.7:
		print('C')
	elif score >= 0.6:
		print('D')
	else:
		print('F')

except:
	print('error: please enter a number\n')

	#chapter 4 example 
	import random

for i in range(10):
	x = random.random()
	print x

	

# dealing with random numbers example
import random


for i in range(10):
	x = random.random()
	print x

print(random.randint(5,10))


t = [1,2,3]
print(random.choice(t))

#math example
import math

degrees = 45
radians = degrees/360.0 * 2 * math.pi
print(math.sin(radians))

#function example

def repeat_lyrics():
	print_lyrics()
	print_lyrics()


def print_lyrics():
	print "I'm a lumberjack"
	print "i sleep all night"


repeat_lyrics()

#Exercise 4.6
def computepay(hoursVar, rateVar):
	if hoursVar < 40:
		pay = hoursVar * rateVar
	elif hours > 40:
		extraHours = hoursVar-40
		pay = 40*rateVar + extraHours*(rateVar*1.5)

	return pay

try:
	hours = float(raw_input('Enter hours\n'))
	rate = float(raw_input('Enter Rate\n'))

except:
	print('error, enter numeric input')

pay = computepay(hours, rate)

print(pay)

#Exercise 4.7
def computeGrade(scoreVar):

	if scoreVar >= 0.9:
		print('A')
	elif scoreVar >= 0.8:
		print('B')
	elif scoreVar >= 0.7:
		print('C')
	elif scoreVar >= 0.6:
		print('D')
	else:
		print('F')

try:
	score = float(raw_input('Please enter a score between 0.0 and 1.0\n'))

	if score > 1.0 or score < 0.0:
		score = raw_input('Incorrect range. please enter score between 0.0 and 1.0\n')

except:
	print('error: please enter a number\n')

score = computeGrade(score)
print(score)

