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

