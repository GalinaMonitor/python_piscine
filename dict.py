import typing

def add_ingot(purse) -> typing.Dict[str, int]:
	new_purse = empty(purse)
	new_purse['gold_ingots']+= 1
	return new_purse

def get_ingot(purse) -> typing.Dict[str, int]:
	new_purse = empty(purse)
	if new_purse['gold_ingots'] > 0:
		new_purse['gold_ingots']-= 1
	return new_purse

def empty(purse) -> typing.Dict[str, int]:
	new_purse = {'gold_ingots': 0}
	return new_purse

def split_booty(*args):
	result = set()
	res = []
	temp = 0
	for i in range(len(args)):
		if 'gold_ingots' in args[i]:
			result.add(args[i]['gold_ingots'])
	for i in range(3):
		if len(result) > 0:
			temp = result.pop()
		res.append({'gold_ingots': temp})
	return (res[0], res[1], res[2])

def decorator(func):
	def squeak(purse):
		print('SQUEAK')
		return func(purse)
	return squeak

add_ingot = decorator(add_ingot)
get_ingot = decorator(get_ingot)
empty = decorator(empty)
