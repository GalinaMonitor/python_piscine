import sys

message = sys.argv[1].lower().split(' ')
result = []
for i in range(len(message)):
	result.append(message[i][0])
print (''.join(result))
