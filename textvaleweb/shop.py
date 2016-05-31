###shop.py
### just the shop classes

class Shop(object):
	def __init__(self):
		self.name = name

class ArmsShop(Shop):
	def __init__(self, name):
		self.name = name
		self.inventory = ["sword", "shield", "mace",
			"really worn long sword with a long name"]

class ItemShop(Shop):
	def __init__(self, name):
		self.name = name
		self.inventory = ["potion", "hotdog", "sandwich", 
							"trashy novel", "boot", "banana", "ether"]		

class Inn(Shop):
	def __init__(self, name, bed, drink):
		self.name = name
		self.localbeer = "%s Brew" % self.name
		self.inventory = [self.localbeer]
		self.nightlyprice = bed
		self.drinkprice = drink		