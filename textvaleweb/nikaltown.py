#######nikaltown.py
### an example town map with appropriate functions

import shelve # for saving states
from string import digits

import outside
import npc
import conversation
import shop #classes
import shops #functions
import invcmd
import potionsmenu
import magiccaster
import saveandload
import prompter
import nikalbar
import questlog


def global_variable_checks(hero):
	try:
		if hero.globalflags[
		"statuedone"] == 1 and not "awesome nothing" in hero.inventory: 
			printlist.append("\n\t\t<p4>MESSAGE FROM THE NARRATOR:</p4>\n",)
			printlist.append("Well, you figured out how <p7>Quests</p7> work. Excellent!",)
			printlist.append("Right now, you tripped a global flag in town.\n")
			printlist.append("Not much left to do in here, aside from <p2>buying</p2>,",)
			printlist.append("<p3>selling</p3>, <p4>casting magic</p4> in and out of battles,",)
			printlist.append("Check your <p5>inventory</p5>, <p6>quest log</p6>, <p7>save/load</p7> your game...",)
			printlist.append("<p2>healing HP/MP</p2> with <p3>potions/ether</p3> in and out of battles,\n",)
			printlist.append("And of course <p4>fighting monsters</p4>, getting <p5>XP</p5>, <p6>leveling up</p6>",)
			printlist.append("and choosing your <p7>bonus stats</p7>...\n",)
			printlist.append("Collecting <p2>gold</p2>, talking to <p3>NPCs</p3>, and uh...\n",)
			printlist.append("Whoah, that's a lot actually!\n\n",)
			printlist.append("And of course, you can <p4>talk to Wheelbarrows</p4>.",)
			printlist.append("And just for fun, I'm going to add the <p7>'Awesome Nothing'</p7> to",)
			printlist.append("your inventory now. \nThis keeps the global flag here from",)
			printlist.append("tripping again. Anyway, have fun!",)
			hero.inventory.append("awesome nothing")
							
	except KeyError:
		#print "You didn't get the Dragon..."
		pass

def townloop(hero):
	global printlist
	printlist.append("\n\t<h2><==> Nikal <==></h2>",)
	printlist.append("You are inside of a town.",) 
		#technically, a town could be a class eg town.name, but not right now...
	printlist.append("<p3>\n%s: HP - %d/%d | MP - %d/%d </p3>" % (hero.name, 
			hero.hp, hero.maxhp, hero.mp, hero.maxmp),)
	
	#########do global variable checks here				
	global_variable_checks(hero)
	########################################
	
	
	printlist.append("\nWould you like to talk to people or... something else?\n",)
	printlist.append("<p2>Talk n' Stuff (t)\nWeapon Shop (w)\nItems Shop (s)\nBar - Inn (b)\n",)
	if hero.gotspells:
		printlist.append("Magic (m) \nInventory - Stats (i)\nPotions (p) \nExit (x)",)
	else:
		printlist.append("Inventory - Stats (i)\nPotions (p) \nExit (x)\n</p2>",)	
	
	#choice = raw_input(prompter.prompter)
	#townchoices()

def townchoices(hero, choice):
	global printlist
	# talk and stuff
	if "t" in choice:
		talkaround(hero)		
	#potions
	elif "p" in choice:
			potionsmenu.listpotions(hero, "")
			townloop(hero)
	#check inventory - stats command
	elif "i" in choice:
			invcmd.invcommand(hero)
			townloop(hero)				
	# magic	
	elif "m" in choice:
		magiccaster.magiccast(hero, "")	
		townloop(hero)
		
	elif "w" in choice:
		NikalArms = shop.ArmsShop("Nikal Arms")
		shops.shopping(NikalArms, hero)
		
	elif "save" in choice:
		scene = "nikaltown.townloop"
		saveandload.savegame("saver", hero, "", "", scene)
		townloop(hero)
		
	elif "load" in choice:
		saveandload.loadgame("saver")
			
	elif "s" in choice:
		NikalItems = shop.ItemShop("Nikal Items")	
		shops.shopping(NikalItems, hero)
	
	elif "b" in choice:
		nikalbar.localbar(hero)
	
	elif "x" in choice:
		outside.overworld(hero)
	elif "q" in choice:
		questlog.listactivequests(hero)
		townloop(hero)
		
	else:
		printlist.append("\nTalk n' Stuff (t)\nWeapon Shop (w)\nItems Shop (s)\nBar - Inn (b)",)
		if hero.gotspells:
			printlist.append("Magic (m) \nInventory - Stats (i)\nPotions (p) \nExit (x)",)
		else:
			printlist.append("Inventory - Stats (i)\nPotions (p) \nExit (x)\n",)	
		townloop(hero)
		
		
def talkaround(hero):
	global npcs
	global printlist
	
	printlist.append("\t<h2><==> Nikal <==></h2>",)
	printlist.append("Looking around the town, you see a few things you may",)
	printlist.append("be able to look into...\n",)
	printlist.append("Which would you like to check out? Or <p2>(x)</p2> to go <p2>back</p2>.\n",)
	npcs = ["Woman in Garden", "The Town Well", 
				"Wheelbarrow"]
	tempquestlistnames = []
	
	for i in hero.questbook: # i could just check for a globalflag, 
							 # but hey... i gotta do this sometime
		tempquestlistnames.append(hero.questbook[hero.questbook.index(i)].questname)
	if "Dragon Quest" in tempquestlistnames:
		dragonindex = tempquestlistnames.index("Dragon Quest")	
		try:
			questlistobject = hero.questbook[dragonindex]
			#print questlistobject.questname #questlistobject.active stb
			
			if questlistobject.active == True:
				npcs = ["Woman in Garden", "The Town Well", 
					"Wheelbarrow", "Jimmy the Hungry"]
			else:
				pass
			
		except NameError: 
			printlist.append("still a name error",)
			pass
	
	else:
		pass
	
	listitem = 0
	for i in range(0,len(npcs)):
		listitem += 1
		printlist.append("<p2>%d. %s</p2>\n" % (listitem, npcs[i]),)
	
	printlist.append("",)
	#choice = raw_input(prompter.prompter)
	#talkchoice(hero, npcs, choice)

def global_variable_checks_talk(hero):
	try:
		if hero.globalflags[
		"dragon"] == 1 and not "dragon statue" in hero.inventory: 
			printlist.append("\nYou got the <p6>Dragon Statue</p6> and added it",)
			printlist.append("to your inventory! Yay!",)
			hero.inventory.append("dragon statue")
				
	except KeyError:
			#print "You didn't get the Dragon..."
			pass
	
def talkaround_choice(choice, hero):
	global printlist
	global npcs
	
	global questionno
	questionno = ""
	
	#if "q" in choice:
	#	questlog.listactivequests(hero)
	#	talkaround(hero)	
	
	#check inventory - stats command
	#elif "i" in choice:
	#		invcmd.invcommand(hero)
	#		talkaround(hero)
	
	#elif "save" in choice:
	#	scene = "nikaltown.talkaround"
	#	saveandload.savegame("saver", hero, "", "", scene)
	#	townloop(hero)
		
	#elif "load" in choice:
	#	saveandload.loadgame("saver")
	
	#else:
	#	pass
	try:
		choice = int(choice)
		if choice >= 1: ## for when an NPC name changes
			if "dragon" in hero.globalflags:
				try:
					npcs[3] = "Jimmy the Hungry2"
				except:
					pass
			else:
				pass	
			makestring = npcs[choice - 1]
			
			try:
				makename = makestring.translate(None, digits) #for diff no. versions
				makestring = "npc.%s" % makestring
				makestring = makestring.replace(" ", "_")
				tempperson = eval(makestring)(makename)
				printlist.append("<h2>\t<==> Nikal Town <==></h2>",)
				printlist.append("<p3>\t--Town Convo--</p3>",)
				
				#conversation.dialogue(hero, tempperson, "", "")
				global townsfolk
				townsfolk = tempperson
				#global answer
				#answer = ""
				#(hero, townsfolk, questionno, answer)
				conversation.printlist = []
				conversation.dialogue(hero, tempperson, questionno, "")
				printlist.extend(conversation.printlist)
				
				#########do global variable checks here
				#if 
				#		pass 
				#else:				
				global_variable_checks_talk(hero)
				##########
				#townloop(hero)
			
			
			except AttributeError:
				tempperson = npc.TownsFolk(makename)
				global townsfolk
				townsfolk = tempperson
				printlist.append("<h2>\t<==> Nikal Town <==></h2>",)
				printlist.append("<p3>\t--Town Convo--</p3>",)
				#printlist.append(tempperson.name)
				conversation.printlist = []
				conversation.dialogue(hero, tempperson, "", "")
				printlist.extend(conversation.printlist)
				# talkabar(hero)
					
	
	except ValueError:
		printlist.append("Not in the mood for conversation, eh?",)
		printlist.append("Okie dokie, let's head back.",)
		#localbar(hero)
		
	except IndexError:
		printlist = []	
		talkaround(hero)
		mapdesc = printlist
		#htmlcommands.htmlsplit(mapdesc)
		return 
		
		printlist.append("Not in the mood for conversation, eh?",)
		printlist.append("Okie dokie, let's head back.",)
		#localbar(hero)