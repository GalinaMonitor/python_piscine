import sys
from collections import Counter

# Class made for game rules
class Game(object):

# Method takes matches as a number of rounds between players,
# Counter used for score
	def __init__(self, matches=10):
		self.matches = matches
		self.registry = Counter()

# Every round game compare states of players and adds an amount of money to each of them.
# In the end of round players update their state, depended on their character
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
			state1 = player1.state
			state2 = player2.state
			player1.play(state2, match)
			player2.play(state1, match)
		player1.reset()
		player2.reset()

	def reset_score(self):
		self.registry.clear()


# Method prints top 3 scorers
	def top_3(self):
		top_3 = self.registry.most_common(5)
		for player in top_3:
			print(player[0], player[1])

# Each child class presents different type of character.
# It affects the change of state
class Player:
	def __init__(self, name="Anonymous"):
		self.name = name

# Always cheats
class Cheater(Player):

	def __init__(self):
		self.state = "cheat"
		super().__init__("Cheater")

	def play(self, opponent_state, match):
		pass

	def reset(self):
		self.state = "cheat"

# Always cooperates
class Cooperative(Player):

	def __init__(self):
		self.state = "cooperate"
		super().__init__("Cooperative")

	def play(self, opponent_state, match):
		pass

	def reset(self):
		self.state = "cooperate"

# Starts with cooperating, but then just repeats whatever the other guy is doing
class Copycat(Player):

	def __init__(self):
		self.state = "cooperate"
		super().__init__("Copycat")

	def play(self, opponent_state, match):
		self.state = opponent_state

	def reset(self):
		self.state = "cooperate"

# Starts with cooperating, but then repeats whatever the other guy is doing,
# but instead of Copycat, forgives one cheat if after goes cooperation
class Copykitten(Player):

	def __init__(self):
		self.state = "cooperate"
		self.let_him_make_mistake = "cooperate"
		super().__init__("Copykitten")

	def play(self, opponent_state, match):
		if self.let_him_make_mistake == opponent_state or opponent_state == 'cooperate':
			self.state = opponent_state
		else:
			self.let_him_make_mistake = opponent_state

	def reset(self):
		self.state = "cooperate"

# Starts by always cooperating, but switches to Cheater
# forever if another guy cheats even once
class Grudger(Player):

	def __init__(self):
		self.state = "cooperate"
		self.permanent = "cooperate"
		super().__init__("Grudger")

	def play(self, opponent_state, match):
		if opponent_state == "cheat":
			self.permanent = opponent_state
		self.state = self.permanent

	def reset(self):
		self.state = "cooperate"
		self.permanent = "cooperate"

# First four times goes with [Cooperate, Cheat, Cooperate, Cooperate],
# and if during these four turns another guy cheats even once - switches
# into a Copycat. Otherwise, switches into Cheater himself
class Detective(Player):

	def __init__(self):
		self.state = "cooperate"
		self.act_like = "Detective"
		super().__init__("Detective")

	def play(self, opponent_state, match):

		if self.name == "Detective" and match > 3:
			if self.act_like == "Copycat":
				self.state = opponent_state
		if self.name == "Detective" and match == 0:
			self.state = "cheat"
			if opponent_state == "cheat":
				self.act_like = "Cheater"
		if self.name == "Detective" and match == 1:
			self.state = "cooperate"
			if opponent_state == "cheat":
				self.act_like = "Cheater"
		if self.name == "Detective" and match == 2:
			self.state = "cooperate"
			if opponent_state == "cheat":
				self.act_like = "Cheater"
		if self.name == "Detective" and match == 3:
			if opponent_state == "cheat":
				self.act_like = "Cheater"
			if self.act_like == "Detective":
				self.act_like = "Copycat"
				self.state = opponent_state
			elif self.act_like == "Cheater":
				self.state = "cheat"

	def reset(self):
		self.state = "cooperate"
		self.act_like = "Detective"

if __name__ == '__main__':
	if len(sys.argv) > 1:
		count = int(sys.argv[1])
	else:
		count = 10
	game = Game(count)
	cheater = Cheater()
	cooperative = Cooperative()
	copycat = Copycat()
	grudger = Grudger()
	detective = Detective()
	copykitten = Copykitten()
	copykitten1 = Copykitten()
	players = [cheater, cooperative, copycat, grudger, detective, copykitten]
	for player1 in players:
		for player2 in players:
			if player1.name != player2.name and players.index(player1) > players.index(player2):
				game.play(player1, player2)

