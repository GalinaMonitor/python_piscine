import sys

message = sys.argv[1]
message = message.lower()
message = message.split(' ')
result = []
for i in range(len(message)):
	result.append(message[i][0])
print (''.join(result))
