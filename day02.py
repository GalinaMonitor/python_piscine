class Key:
	passphrase = "zax2rulez"

	def __len__(self):
		return (1337)

	def __getitem__(self, nbr):
		return (3)

	def __gt__(self, nbr):
		if nbr == 9000:
			return 1
		else:
			return 0

	def __str__(self):
		return ("GeneralTsoKeycard")

key = Key()
print("len(key) == 			", len(key))
print("key[404] == 			", key[404])
print("key > 9000 == 			", key > 9000)
print("key.passphrase == 		", key.passphrase)
print("str(key) == 			", str(key))


