class Frog:
	"""docstring for Frog"""
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

	def interact_with(self,obstacle):
		act = obstacle.action()
		msg = '{} the Frog encounters {} obstacle and {}'.format(self, obstacle, act)
		print(msg)


class Bug:
	"""docstring for Bug"""
	def __str__(self):
		return 'a bug'

	def action(self):
		return 'eats it'

class FrogWorld:
	"""docstring for FrogWorld"""
	def __init__(self, name):
		self.player_name = name

	def __str__(self):
		return '\n\n\t------ Frog World -------'

	def make_character(self):
		return Frog(self.player_name)

	def make_obstacle(self):
		return Bug()


class Wizard:
	"""docstring for Wizard"""
	def __init__(self, name):
		self.name = name
		
	def __str__(self):
		return self.name

	def interact_with(self, obstacle):
		act = obstacle.action()
		msg = '{}, the Wizard battles against {} obstacle and {}'.format(self, obstacle, act)
		print(msg)


class Ork:
	"""docstring for Ork"""
	def __str__(self):
		return 'an evil ork'

	def action(self):
		return 'kills it'
		

class WizardWorld:
	"""docstring for WizardWorld"""
	def __init__(self, name):
		print(self)
		self.player_name = name

	def __str__(self):
		return '\n\n\t------ Wizard World -------'

	def make_character(self):
		return Wizard(self.player_name)

	def make_obstacle(self):
		return Ork()		


class GameEnviroment:
	"""docstring for GameEnviroment"""
	def __init__(self, factory):
		self.hero = factory.make_character()
		self.obstacle = factory.make_obstacle()

	def play(self):
		self.hero.interact_with(self.obstacle)


# Scripting
def validate_age(name):
	try:
		age = input('Welcome {}. How old are you?'.format(name))
		age = int(age)
	except ValueError as e:
		print('Age {} is invalid, please try again'.format(age))
		return (False, age)

	return (True, age)


def main():
	name = input('Hello. Whats your name?')
	valid_input = False

	while not valid_input:
		valid_input, age = validate_age(name)

	game = FrogWorld if age < 18 else WizardWorld

	enviroment = GameEnviroment(game(name))
	enviroment.play()

if __name__ == '__main__':
	main()