###items.py
from random import randint

##items classes
class Item(object):
	#def __init__(self):
	pass	
		
class potion(Item):
	def __init__(self):
		self.name = "Potion"
		self.price = 10
		self.desc = "Heals some HP."
		self.sellprice = 5
		self.useable = True
		self.healhp = True
		self.healamt = randint(10,30)
		self.healmp = False
		
class ether(Item):
	def __init__(self):
		self.name = "Ether"
		self.price = 30
		self.desc = "Heals some MP."
		self.sellprice = 5
		self.useable = True
		self.useable = False
		self.healhp = False
		self.healmp = True
		self.healamt = randint(5,15)
		
class hotdog(Item):
	def __init__(self):
		self.name = "Hotdog"
		self.price = 20
		self.desc = "A tasty, if unhealthy, snack."
		self.sellprice = 10
		self.useable = False		

class sandwich(Item):
	def __init__(self):
		self.name = "Sandwich"
		self.price = 30
		self.desc = "The ingredients are are unknown. It's better that way, really."
		self.sellprice = 15
		self.useable = False

class trashy_novel(Item):
	def __init__(self):
		self.name = "Trashy Novel"
		self.price = 50
		self.desc = "Read it for the articles."
		self.sellprice = 25
		self.useable = False

class boot(Item):
	def __init__(self):
		self.name = "Boot"
		self.price = 5
		self.desc = "Smells of leather. And foot fungus."
		self.sellprice = 1
		self.useable = False		

class banana(Item):
	def __init__(self):
		self.name = "Banana"
		self.price = 7
		self.desc = "Slippery when underfoot."
		self.sellprice = 3
		self.useable = False	
		
class dragon_statue(Item):
	def __init__(self):
		self.name = "Dragon Statue"
		self.price = 100
		self.desc = "A nice Dragon Statue you got from Jimmy."
		self.sellprice = 0
		self.useable = False	
		
class nikal_keys_inn_brew(Item):
	def __init__(self):
		self.name = "Nikal Keys Inn Brew"
		self.price = 3
		self.desc = "A tasty brew from nikal."
		self.sellprice = 0
		self.useable = False	