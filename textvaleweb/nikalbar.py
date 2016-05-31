####nikalbar.py
###example bar (within a town) and its functions here

from string import digits

import nikaltown
import npc
import shop
import prompter
import conversation
import questlog
#import saveandload
import invcmd

def localbar(hero):
	global printlist
	printlist.append("<h2>\t<==> Nikal Keys Inn - Bar <==></h2>",)
	printlist.append("You walk into the Inn - Bar and notice a few things of interest...\n",)
	printlist.append("Go straight to the <p2>Barkeep</p2> to grab a drink or stay the night? <p2>(b)</p2>\n",)
	printlist.append("Or <p2>Take</p2> a look around? <p2>(t)</p2>\n",)
	printlist.append("Or you can <p2>Exit</p2> the bar. <p2>(x)</p2>\n",)
	
	#choice = raw_input(prompter.prompter)
		
def localbar_choice(choice, hero):

	if "b" in choice :
		NikalInn = shop.Inn("Nikal Keys Inn", 10, 3)	
		overnight(NikalInn, hero)
	elif "t" in choice: 
		talkabar(hero)
	
	elif "x" in choice:
		nikaltown.townloop(hero)
	elif "q" in choice:
		questlog.listactivequests(hero)
		localbar(hero)
		
	elif "save" in choice:
		scene = "nikalbar.localbar"
		saveandload.savegame("saver", hero, "", "", scene)
		localbar(hero)
		
	elif "load" in choice:
		saveandload.loadgame("saver")
	
	else:
		print "Sorry, what was that?"
		#localbar(hero)
		
def talkabar(hero):
	global npcs
	printlist.append("<h2>\t<==> Nikal Keys Inn - Bar <==></h2>",)
	printlist.append("You take a look around the room... You notice:\n",)
	printlist.append("A <p2>waitress</p2>. She looks busy.\n",)
	
	if "statuedone" in hero.globalflags:
		printlist.append("A <p2>slightly less worried man</p2> in the corner. Now enjoying his drink.\n",)
	else:
		printlist.append("A <p2>worried man</p2> in the corner. Hasn't touched his drink.\n",)
	
	printlist.append("A <p2>seasoned adventurer</p2>, nursing his drink. He looks bored.\n",)
	printlist.append("\nWho would you like to talk to? <p2>(x)</p2> to go <p2>back.</p2>\n",)
		
	if "statuedone" in hero.globalflags:
		npcs = ["Less Worried Man", "Busy Waitress", 
				"Seasoned Adventurer"]
	else:
		npcs = ["Worried Man", "Busy Waitress", 
				"Seasoned Adventurer"]

	listitem = 0
	for i in range(0,len(npcs)):
		listitem += 1
		printlist.append("<p2>%d. %s</p2>\n" % (listitem, npcs[i]),)
		
	#choice = raw_input(prompter.prompter)

def global_variable_checks(hero):
	try:
		if hero.globalflags["statueknow"] == 1 and hero.globalflags[
			"statueknow2"] == 0: 
			printlist.append("\nYour <p6>Quest Log</p6> was updated!",)
			printlist.append("Check your <p2>Quest Log</p2> at any time by typing <p2>(q)</p2>.",)
			hero.globalflags["statueknow2"] = 1
			# update quest log here
			
			# self, name, active, finished, desc
			dragon_quest = questlog.Quest("Dragon Quest", True, False, "Find the Worried Man's Dragon Statue")
			#print dragon_quest.questname tempobject, not in the heros list
			
			hero.questbook.append(dragon_quest) #stick the object in the heros questbook list
			
			# hero.questbook.index(dragon_quest) ## index number of the object in the list
			# print hero.questbook[hero.questbook.index(dragon_quest)].questname #that's a fucking mouthful
			# make another tempitem based on the object in the list; as you will need this pattern
			# and values later
			questlistobject = hero.questbook[hero.questbook.index(dragon_quest)]
			questlog.listactivequests(hero)						
			#talkabar(hero)
			
		elif hero.globalflags["statuegave"] == 1 and hero.globalflags[
			"statuedone"] == 0: 
			printlist.append("You gave the <p3>Dragon Statue</p3>.",)
			printlist.append("\nYour <p7>Quest Log</p7> was updated!",)
			hero.globalflags["statuedone"] = 1
			hero.gold += 50
			printlist.append("You received <p6>50 Gold</p6>!\n",)	
			# update quest log here
									
			tempquestlistnames = []
			for i in hero.questbook: #where exactly is the quest in the list
				tempquestlistnames.append(hero.questbook[hero.questbook.index(i)].questname)
				if "Dragon Quest" in tempquestlistnames:
					dragonindex = tempquestlistnames.index("Dragon Quest")	
					try:
						questlistobject = hero.questbook[dragonindex] #here it is!			
						questlistobject.active = False
						questlistobject.finished = True
					except:
						print "uh oh"
						pass
				else:
					pass
			hero.inventory.remove("dragon statue")
			#print hero.inventory
			questlog.listallquests(hero)
			
			#talkabar(hero) 
			
		
	except KeyError:
			#print "You didn't get the Dragon..."
			pass
	
def talkabar_choice(choice, hero):	
	global npcs
	
	global questionno
	questionno = ""
				
	#if "q" in choice:
	#		questlog.listactivequests(hero)
	#		talkabar(hero)
			
	#elif "save" in choice:
	#	scene = "nikalbar.talkabar"
	#	saveandload.savegame("saver", hero, "", "", scene)
	#	localbar(hero)
		
	#elif "load" in choice:
	#	saveandload.loadgame("saver")
	
	#else:
	#	pass	
	try:	
		choice = int(choice)
		if choice >= 1: ## for when an NPC name changes, remember to go 
						##from bottom to top for flag order
			if "statuedone" in hero.globalflags:
				# print hero.globalflags
				npcs[0] = "Less Worried Man"
			elif "statueknow" in hero.globalflags and "dragon statue" in hero.inventory:
				npcs[0] = "Worried Man3"
			elif "statueknow" in hero.globalflags and not "dragon statue" in hero.inventory:
				npcs[0] = "Worried Man2"
			else:
				pass
			makestring = npcs[choice - 1]
			
			try:
				makename = makestring.translate(None, digits) #for diff no. versions
				makestring = "npc.%s" % makestring
				makestring = makestring.replace(" ", "_")
				tempperson = eval(makestring)(makename)
				printlist.append("<h2>\t<==> Nikal Keys Inn - Bar <==></h2>",)
				printlist.append("<p3>\t--Bar Convo--</p3>",)
				#conversation.printlist = []
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
				global_variable_checks(hero)
				
				##########
				#talkabar(hero)		
			
			except AttributeError:
				tempperson = npc.TownsFolk(makename)
				global townsfolk
				townsfolk = tempperson
				printlist.append("<h2>\t<==> Nikal Keys Inn - Bar <==></h2>",)
				printlist.append("<p3>\t--Bar Convo--</p3>",)
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
		printlist.append("Not in the mood for conversation, eh?",)
		printlist.append("Okie dokie, let's head back.",)
		#localbar(hero)
		
def overnight(shop, hero):	
	printlist.append("<h2>\t<==> %s - Bar <==></h2>" % shop.name,)
	printlist.append("<p3>Welcome to the %s!\n" % shop.name,)
	printlist.append("</p3>You here for a brew, or wish to stay the night? Or...\n")
	printlist.append("<p2>Drink (d)\nBed (b)\nExit (x)</p2>\n")
	
	#choice = raw_input(prompter.prompter)

def overnight_choice(choice, shop, hero):

	if "save" in choice:
		scene = "nikalbar.overnight"
		saveandload.savegame("saver", hero, "", shop, scene)
		
	elif "load" in choice:
		saveandload.loadgame("saver")	
		
	elif "d" in choice:
		buybeer(shop, hero)
			
	elif "b" in choice:
		gotobed(shop, hero)
	
	elif "x" in choice:
		localbar(hero)	
		return
	if "quest" in choice:
		questlog.listactivequests(hero)
		talkabar(hero)
		
	else:
		print "Um... not sure I caught that."
		overnight(shop, hero)
			
		
def gotobed(shop, hero):
	printlist.append("<h2>\t<==> %s - Bar <==></h2>" % shop.name,)
	printlist.append("Want a bed, huh?\n",)
	printlist.append("That'll be <p6>%d Gold</p6> for the night, is that OK?\n" % shop.nightlyprice,)
	printlist.append("<p2>Yes! (y)\nNo... (n)\n</p6>",)
	#choice = raw_input(prompter.prompter)
	
def gotobed_choice(choice, shop, hero):	
	printlist.append("<p8>\t<==> %s - Bar <==></p8>\n" % shop.name,)
	if "y" in choice and hero.gold >= shop.nightlyprice:
		printlist.append("One bed, coming up!",)
		hero.gold -= shop.nightlyprice
		printlist.append("You spent <p6>%d Gold</p6>" % shop.nightlyprice,)
		printlist.append("Good night!\n\n",)
		printlist.append("z\n" * 30,)
		printlist.append("Good morning!\n",)
		hero.hp = hero.maxhp
		invcmd.invcommand(hero)
		#overnight(shop, hero)
	elif "y" in choice and hero.gold < shop.nightlyprice:
		printlist.append("One bed, coming uh... Ouch! not enough gold!\nAnything else I can do for you?",)
		#overnight(shop, hero)
	
	elif "save" in choice:
		scene = "nikalbar.overnight"
		saveandload.savegame("saver", hero, "", shop, scene)
		#localbar(hero)
		
	elif "load" in choice:
		#saveandload.loadgame("saver")
		pass
		
	else:
		printlist.append("Suit yourself. Anything else I can do for you?",)
		#overnight(shop, hero)

def buybeer(shop, hero):
	printlist.append("<h2>\t<==> %s - Bar <==></h2>" % shop.name,)
	printlist.append("Thirsty, eh?\nOur local drink is the <p4>%s</p4>.\n" % shop.localbeer,)
	printlist.append("That'll be <p6>%d Gold</p6> for the beverage, is that OK?" % shop.drinkprice,)
	printlist.append("\n<p2>Yes! (y)\nNo... (n)\n</p2>",)
	#choice = raw_input(prompter.prompter)
	
def beer_choice(choice, shop, hero):	
	printlist.append("<p8>\t<==> %s - Bar <==>\n</p8>" % shop.name,)
	if "y" in choice and hero.gold >= shop.drinkprice and not (
			shop.localbeer.lower()) in hero.inventory:
		printlist.append("One brew... <p3>%s</p3>, coming up!\n" % shop.localbeer,)
		hero.gold -= shop.drinkprice
		printlist.append("You spent <p6>%d Gold</p6>\n" % shop.drinkprice,)
		printlist.append("Enjoy the brew!\n",)
		hero.inventory.append(shop.localbeer.lower())
		printlist.append("You got a <p4>%s</p4> and added it to your inventory!\n" % shop.localbeer,)
		# overnight(shop, hero)
	elif "y" in choice and shop.localbeer.lower() in hero.inventory:
		printlist.append("One brew... Oh, looks like you already have one!\n",)
		printlist.append("Sorry, you can only have one drink at a time...\n",)
		printlist.append("Anything else I can do for you?\n",)
		#overnight(shop, hero)
		
	elif "y" in choice and hero.gold < shop.drinkprice:
		printlist.append("One brew... Ouch! not enough gold!\nAnything else I can do for you?\n",)
		#overnight(shop, hero)
	
	elif "save" in choice:
		scene = "nikalbar.overnight"
		saveandload.savegame("saver", hero, "", shop, scene)
		localbar(hero)
		
	elif "load" in choice:
		saveandload.loadgame("saver")
	
	else:
		printlist.append("Suit yourself. Anything else i can do for you?",)
		#overnight(shop, hero)