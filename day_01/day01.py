import typing

def decorator(func):
	def squeak(purse):
		print('SQUEAK')
		return func(purse)
	return squeak

@decorator
def add_ingot(purse) -> typing.Dict[str, int]:
	new_purse = purse.copy()
	new_purse['gold_ingots']+= 1
	return new_purse

@decorator
def get_ingot(purse) -> typing.Dict[str, int]:
	new_purse = purse.copy()
	if new_purse['gold_ingots'] > 0:
		new_purse['gold_ingots']-= 1
	return new_purse

@decorator
def empty(purse) -> typing.Dict[str, int]:
	new_purse = {'gold_ingots': 0}
	return new_purse

def split_booty(*args):
	result = 0
	res = []
	temp = 0
	for i in range(len(args)):
		if 'gold_ingots' in args[i]:
			result += args[i]['gold_ingots']
	print(result)
	for i in range(3):
		temp = int(result / (3 - i))
		result-= temp
		res.append({'gold_ingots': temp})
	return (res[0], res[1], res[2])



if __name__ == "__main__":
	purse = {}
	print("\nTest - empty+get+add+get 		= ", get_ingot(add_ingot(add_ingot(add_ingot(get_ingot(empty(purse)))))))
	print("\nTest - split_booty (1 2 3 3 4)		= ", split_booty({'gold_ingots': 1}, {'gold_ingots': 2}, {'gold_ingots': 3}, {'gold_ingots': 3}, {'gold_ingots': 4}))
	print("\nTest - split_booty (1) 			= ", split_booty({'gold_ingots': 1}))
	print("\nTest - split_booty (4 3) 		= ", split_booty({'gold_ingots': 4}, {'gold_ingots': 3}))
