from collections import Counter

class Game(object):

	def __init__(self, matches=10):
		self.matches = matches
		self.registry = Counter()

	# def play(self, player1, player2):
	# 	# simulate number of matches
	# 	# equal to self.matches

	def top3(self):
		Counter.most_common([3])

