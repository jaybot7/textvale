#arms.py

##weapons classes
class Arms(object):
	#def __init__(self):
	pass	

class sword(Arms):
	def __init__(self):
		self.name = "Sword"
		self.price = 10
		self.desc = "Standard Hero issue. Quite blunt."
		self.sellprice = 5
		self.equipped = True
		self.attack = 1
		self.defense = 0
		
class mace(Arms):
	def __init__(self):
		self.name = "Mace"
		self.price = 30
		self.desc = "Spikey ball and chain. Menacing."
		self.sellprice = 15
		self.equipped = False	
		self.attack = 3
		self.defense = 0
	
class shield(Arms):
	def __init__(self):
		self.name = "Shield"
		self.price = 20
		self.desc = "Probably made of plastic. For show, really."
		self.sellprice = 10
		self.equipped = True
		self.attack = 0
		self.defense = 1

class really_worn_long_sword_with_a_long_name(Arms):
	def __init__(self):
		self.name = "Really Worn Long Sword With A Long Name"
		self.price = 12
		self.desc = "Read it all night long!"
		self.sellprice = 6
		self.useable = False