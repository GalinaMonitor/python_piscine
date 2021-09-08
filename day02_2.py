from collections import Counter

class Game(object):

	def __init__(self, matches=10):
		self.matches = matches
		self.registry = Counter()

	def play(self, player1, player2):

		for match in range(self.matches):
			if player1.state == "cooperate" and player2.state == "cooperate":
				self.registry[player1.name] += 2
				self.registry[player2.name] += 2
			if player1.state == "cheat" and player2.state == "cooperate":
				self.registry[player1.name] += 3
				self.registry[player2.name] -= 1
			if player1.state == "cooperate" and player2.state == "cheat":
				self.registry[player1.name] -= 1
				self.registry[player2.name] += 3
			if player1.state == "cheat" and player2.state == "cheat":
				self.registry[player1.name] += 0
				self.registry[player2.name] += 0
			player1.play(player2, match)
			player2.play(player1, match)
		player1.reset()
		player2.reset()

	def top_3(self):
		top_3 = self.registry.most_common(3)
		for player in top_3:
			print('{} {}'.format(player[0], player[1]))


class Player:

	def __init__(self, name="Anonymous"):
		self.name = name

class Cheater(Player):

	def __init__(self):
		self.state = "cheat"
		super().__init__("Cheater")

	def play(self, opponent, match):
		pass

	def reset(self):
		self.state = "cheat"
		super().__init__("Cheater")


class Cooperative(Player):

	def __init__(self):
		self.state = "cooperate"
		super().__init__("Cooperative")

	def play(self, opponent, match):
		pass

	def reset(self):
		self.state = "cooperate"

class Copycat(Player):

	def __init__(self):
		self.state = "cooperate"
		super().__init__("Copycat")

	def play(self, opponent, match):
		self.state = opponent.state

	def reset(self):
		self.state = "cooperate"


class Grudger(Player):

	def __init__(self):
		self.state = "cooperate"
		self.permanent = "cooperate"
		super().__init__("Grudger")

	def play(self, opponent, match):
		if opponent.state == "cheat":
			self.permanent = opponent.state
		self.state = self.permanent

	def reset(self):
		self.state = "cooperate"
		self.permanent = "cooperate"

class Detective(Player):

	def __init__(self):
		self.state = "cooperate"
		self.act_like = "Detective"
		super().__init__("Detective")

	def play(self, opponent, match):

		if self.name == "Detective" and match > 3:
			if self.act_like == "Copycat":
				self.state = opponent.state
		if self.name == "Detective" and match == 0:
			self.state = "cheat"
			if opponent.state == "cheat":
				self.act_like = "Cheater"
		if self.name == "Detective" and match == 1:
			self.state = "cooperate"
			if opponent.state == "cheat":
				self.act_like = "Cheater"
		if self.name == "Detective" and match == 2:
			self.state = "cooperate"
			if opponent.state == "cheat":
				self.act_like = "Cheater"
		if self.name == "Detective" and match == 3:
			if opponent.state == "cheat":
				self.act_like = "Cheater"
			if self.act_like == "Detective":
				self.act_like = "Copycat"
				self.state = opponent.state
			elif self.act_like == "Cheater":
				self.state = "cheat"

	def reset(self):
		self.state = "cooperate"
		self.act_like = "Detective"

if __name__ == '__main__':
	game = Game(100)
	cheater = Cheater()
	cooperative = Cooperative()
	copycat = Copycat()
	grudger = Grudger()
	detective = Detective()
	players = [cheater, cooperative, copycat, grudger, detective]
	for player1 in players:
		for player2 in players:
			if player1.name != player2.name and players.index(player1) > players.index(player2):
				game.play(player1, player2)
	game.top_3()
