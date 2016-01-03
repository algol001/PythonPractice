
try:
	score = float(raw_input('Please enter a score between 0.0 and 1.0\n'))

	if score > 1.0 or score < 0.0:
		score = raw_input('Incorrect range.please enter score between 0.0 and 1.0\n')


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





