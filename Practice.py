str = 'X-DSPAM-Confidence: .08475'
colPos=str.find(':')
num = float(str[colPos+1:])
print num
