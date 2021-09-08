import re
import sys

result = ''
temp = ''
i = 0
while (i < 3):
	temp = sys.stdin.readline()
	temp = temp.rstrip('\n')
	if len(temp) % 5 != 0 and len(temp) / 5 == 1:
		print('Error')
		exit()
	result += ''.join(temp)
	i+= 1
if len(result) != 15:
	print('Error')
	exit()
if re.fullmatch(r'\*[^\*]{3}\*{3}[^\*]\*{3}[^\*]\*[^\*]\*', result) != None:
	print('True')
else:
	print('False')
