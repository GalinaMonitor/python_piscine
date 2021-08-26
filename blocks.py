import re
import sys

lol = []
list_res_len = 0
count = int(sys.argv[1])
while(count > 0):
	temp = sys.stdin.readline()
	temp = temp.strip('\n')
	lol.append(temp)
	if re.match(r'0{5}[1-9a-zA-Z][0-9a-zA-Z]{26}', lol[list_res_len]) == None:
		lol.remove(lol[list_res_len])
	else:
		list_res_len+=1
	count-=1
for i in range(len(lol)):
	print(lol[i])
