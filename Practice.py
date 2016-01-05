
count = 0
total = 0
largest = None
smallest = None
import re


while True:
	enteredValue = raw_input("enter a number\n")

	if re.search('done',enteredValue, re.IGNORECASE):
		break
	else:
		try: 
			enteredValueFloat = float(enteredValue)
			#total += enteredValueFloat

			if smallest is None or smallest < enteredValueFloat:
				smallest = enteredValueFloat

			if largest is None or largest > enteredValueFloat:
				largest = enteredValueFloat

			count += 1

		except ValueError as e: #this catches value errors  - to catch multiple types of errors can layer one after another
			print('Error:')
			print e

print 'count: ', count
print 'smallest: ', smallest
print 'largest: ', largest