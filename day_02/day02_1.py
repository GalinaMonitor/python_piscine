class Key:
	passphrase = "zax2rulez"

	def __len__(self):
		return (1337)

	def __getitem__(self, nbr):
		return (3)

	def __gt__(self, nbr):
		if nbr <= 9000:
			return 1
		else:
			return 0

	def __str__(self):
		return ("GeneralTsoKeycard")

key = Key()

assert len(key) == 1336
assert key[404] == 3
assert key > 9000
assert key.passphrase == "zax2rulez"
assert str(key) == "GeneralTsoKeycard"
