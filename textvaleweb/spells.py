###spells.py

##spell classes
class Spell(object):
	#def __init__(self):
	pass	
		
class flame_of_awesome(Spell):
	def __init__(self):
		self.name = "Flame Of Awesome"
		self.atk = 5
		self.desc = "Burn your enemies with the power of a large pack of matches!"
		self.element = "fire"
		self.mpcost = 3

class ice_of_doom(Spell):
	def __init__(self):
		self.name = "Ice of Doom"
		self.atk = 7
		self.desc = "Freeze your enemies with the power of a popsicle!"
		self.element = "ice"
		self.mpcost = 6

class spark_of_righteousness(Spell):
	def __init__(self):
		self.name = "Spark Of Righteousness"
		self.atk = 11
		self.desc = "Electrocute your enemies with the power of a 9V Battery!"
		self.element = "lit"
		self.mpcost = 10
		
class cure(Spell):
	def __init__(self):
		self.name = "Cure"
		self.healamt = 15
		self.desc = "Cure some HP for MP. Good deal."
		self.element = "healing"
		self.mpcost = 5