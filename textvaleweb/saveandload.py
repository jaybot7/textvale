###saveandload.py
import shelve

import shops
import nikaltown
import nikalbar

import battlesystem4
import outside

###save and load stuff		

def savegame(name, hero, enemy, shop, scene):
	import shops
	#global playerA
	
	print "Saving...\n"
	
	shelfFile = shelve.open(name)
	shelfFile['playerAObject'] = hero #local to catch battle/field diff
	shelfFile['MonsterAObject'] = enemy
	shelfFile['CurrentSceneObject'] = scene
	shelfFile['CurrentShopName'] = shop
	shelfFile.close()
	if "battle" in scene:
		scene = "battlesystem4.newbattle"
		eval(scene)(hero, enemy)
		#return
	elif "shop" in scene:
		scene = "shops.%s" % scene
		eval(scene)(shop, hero)
		
	elif "night" in scene:
		scene = "%s" % scene
		eval(scene)(shop, hero) #because it has a shop argument
	
	elif "bar" in scene:
		scene = "%s" % scene #also weak
		eval(scene)(hero)
	
	elif "town" in scene:
		scene = "%s" % scene #weak... 
		eval(scene)(hero)
	
	else:
		return 
		
def loadgame(name):
	print "Loading...\n"	
	
	shelfFile = shelve.open(name) 
	hero = shelfFile['playerAObject']
	playerA = hero #local to catch battle/field diff
	enemy = shelfFile['MonsterAObject'] 
	scene = shelfFile['CurrentSceneObject'] 
	shop = shelfFile['CurrentShopName']
	shelfFile.close()
	if "battle" in scene:
		scene = "battlesystem4.%s" % scene
		print "A Level %d %s appeared!" % (enemy.xplvl, enemy.name)
		eval(scene)(hero, enemy) # newbattle(hero, monster)
	elif "shop" in scene:
		scene = "shops.%s" % scene
		eval(scene)(shop, hero)
	elif "night" in scene:
		scene = "%s" % scene
		eval(scene)(shop, hero)	
	elif "bar" in scene:
		scene = "%s" % scene
		eval(scene)(hero)
	elif "town" in scene:
		scene = "%s" % scene
		eval(scene)(hero)
	else:
		scene = "outside.%s" % scene
		eval(scene)(hero)#i still cant believe this works.