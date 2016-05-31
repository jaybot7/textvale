###battlesystemX.py
#most of the work goes in here

from random import randint
import shelve # for saving states

import npc
import items
import invcmd
import saveandload
import magiccaster
import prompter			
import potionsmenu
import questlog

####battle stuff

# start of new battle	
def newbattle(targetA, targetB):
	if 0 == 0:
	#while targetA.hp >= 1 and targetB.hp >= 1 and targetA.flee == False:
		monstercommand(targetB)
		#battlecommandP(targetA, targetB)
		#if targetB.turn == 0 and targetA.flee == False:
		#	battlecommandM(targetB, targetA)
		#elif targetB.turn == 0 and targetA.flee == True: 
		#	targetA.flee = False
			#return
		#else:
		#	pass		
	#if targetA.flee == True:
	#	pass
		#return # back to monster turn (disable it!), then return to overworld
	#else:
	#	pass
	if targetA.hp <= 0:
		printlist.append("%s died. How sad..." % targetA.name,)
		#exit(0) dont kill the server
		
	elif targetB.hp <= 0 and "Hero" in targetB.__class__.__name__: 
					#this can happen during a monster flip a/b, I know...
		printlist.append("%s died. How sad..." % targetB.name,)
		#exit(0) dont kill the server
		
	else:
		battlevictory(targetA, targetB)
		#return	


#set blocking flag for monster or hero		
def block(targetA):
	targetA.shield = True
	printlist.append("\n\t-%s Actions-" % targetA.__class__.__name__,)
	if "Hero" in targetA.__class__.__name__:
		printlist.append("<p3>",)
	else:
		printlist.append("<p4>",)
	
	printlist.append("\n%s is blocking." % targetA.name,)
	if "Hero" in targetA.__class__.__name__:
		printlist.append("</p3>",)
	else:
		printlist.append("</p4>",)
	
	targetA.turn = 1
	return
	
# hit or miss, turn over
def hitormiss(targetA, targetB): 
	printlist.append("\n\t-%s Actions-" % targetA.__class__.__name__,)
	if "Hero" in targetA.__class__.__name__:
		printlist.append("<p3>",)
	else:
		printlist.append("<p4>",)
	
	hit = randint(0,3)
	chance = randint(1,10) * int(round(float((targetA.spd) / targetA.xplvl)) * 1.5)
	chance = int(chance)
	
	if chance < 4: # change this to increase odds of hitting
		printlist.append("\n%s missed!" % targetA.name,)
		targetA.turn = 1
		if "Hero" in targetA.__class__.__name__:
			printlist.append("</p3>",)
		else:
			printlist.append("</p4>",)
		#return
	
	elif chance >= 4: # this too
		printlist.append("\n'%s' hits '%s'!" % (
				targetA.name, targetB.name),)	
		
		# if target b is blocking
		if targetB.shield == True:
		# if damage amount more than 2, reduce the damage
			if hit >= 2:
				reduce = int((hit * 0.5)) # so it doesnt float
				reduce = int(reduce)
				newhit = int(hit - reduce) 
				newhit = int(newhit) #something is not int-ing, clean this up later
				#printlist.append(newhit,)
				printlist.append("...but the %s blocks, only losing %d HP!" % (
				targetB.__class__.__name__, newhit),)
				targetB.hp -= newhit 
				targetB.shield = False
				if "Hero" in targetA.__class__.__name__:
					printlist.append("</p3>",)
				else:
					printlist.append("</p4>",)
				
				if int(targetB.hp) >= 1:
					targetA.turn = 1
					return
				elif int(targetB.hp) <= 0:
					#print targetB.name, targetB.hp
					targetA.turn = 1
					if "Hero" in targetB.__class__.__name__:
						printlist.append("%s died. How sad..." % targetB.name,)
						#exit(0) #ooh what happens here? nice! it kills the server entirely hahahah
						
					else:
						battlevictory(targetA, targetB)
				else:
					printlist.append("whoah nellie!",)
					
			else: #just do the normal attack since damage is not reduced
				targetB.shield = False
				newerhit =  hit * targetA.str / targetB.defense 
				if newerhit < 1:
					newerhit = 1
				if hit == 3 and newerhit > 1:
					printlist.append("<p5>\n\nCritical!</p5>",)
				printlist.append("The %s loses %r HP!" % (targetB.__class__.__name__, newerhit),)
				targetB.hp -= newerhit 
				targetA.turn = 1
				if "Hero" in targetA.__class__.__name__:
					printlist.append("</p3>",)
				else:
					printlist.append("</p4>",)
				
				
				if int(targetB.hp) >= 1:
					return
				elif int(targetB.hp) <= 0:
					#print "noooooooooooooooooo"
					targetA.turn = 1
					if "Hero" in targetB.__class__.__name__:
						#print "yessssssssss"
						printlist.append("%s died. How sad..." % targetB.name,)
						#exit(0) dont kill the server!
						
					else:
						#print "arrrrrrrrrrrrgjhhHH"
						battlevictory(targetA, targetB)
				else:
					printlist.append("wtf happened here?",)
		else:	
			newerhit =  hit * targetA.str / targetB.defense
			if newerhit < 1:
				newerhit = 1
			if hit == 3 and newerhit > 1:
				printlist.append("<p5>\nCritical!</p5>",)
			printlist.append("The %s loses %r HP!" % (targetB.__class__.__name__, newerhit),)
			targetB.hp -= newerhit
			targetA.turn = 1
			
			if "Hero" in targetA.__class__.__name__:
				printlist.append("</p3>",)
			else:
				printlist.append("</p4>",)
			
			if int(targetB.hp) >= 1:
				return
			elif int(targetB.hp) <= 0:
					targetA.turn = 1
					if "Hero" in targetB.__class__.__name__:
						printlist.append("%s died. How sad..." % targetB.name,)
						#exit(0) dont kill the server!
						
					else:
						battlevictory(targetA, targetB)
			else:
				printlist.append("wtf happened here?",)

	else:
		printlist.append("uh oh",)		
	return

# monster commands will be set (block or not) 
# before going to player commands	
def monstercommand(monster):
	monster.turn = 0
	command = randint(1,2)
	if command == 1:
		monster.shield = True
	else:
		monster.shield = False
		#return
		
#battle commands loop
def battlecommandP(targetA, targetB):
	printlist.append("\n\t<h2><==> Battle Menu <==></h2>",) 
	
	
	#while True: #targetA.hp >= 1 and targetB.hp >= 1:
	targetA.turn = 0
	printlist.append("<p3>%s's HP: %d/%d | MP - %d/%d </p3>" % (targetA.name,
			targetA.hp, targetA.maxhp, targetA.mp, targetA.maxmp),)
	printlist.append("<---------------------------\n--------------------------> <p4>%s's HP: %d/%d</p4>\n" % (targetB.name, targetB.hp, targetB.maxhp),)
	printlist.append("Your command?\n<p2>Attack (a) \nBlock (b) \nPotions (p)",)
	if targetA.gotspells:
		printlist.append("\nMagic (m)\nInventory (i)\nFlee (x)</p2>",)
	else:
		printlist.append("\nInventory (i)\nFlee (x)</p2>",)
		 
		#battlechoice(targetA, targetB)
		
def battlechoice(formf, targetA, targetB):
		choice = formf #raw_input(prompter.prompter)
		# heal command
		if "p" in choice:
			potionsmenu.printlist = []
			potionsmenu.listpotions(targetA, targetB)
			#return
		#block command	
		elif "b" in choice:
			block(targetA)
			#return
		# magic	
		elif "m" in choice:
			magiccaster.magiccast(targetA, targetB)	
			
		#check inventory command
		elif "i" in choice:
			invcmd.printlist = []
			invcmd.invcommand(targetA)	
		#flee
		elif "x" in choice:
			printlist.append("%s runs away!!!" % targetA.name,)
			targetA.flee = True
			import outside
			targetA.flee = False #just in case... which it is
			outside.overworld(targetA)
		#save
		elif "save" in choice:
			scene = "newbattle"
			saveandload.savegame("saver", targetA, targetB, "", scene)
			battlecommandP(targetA, targetB)
		#load
		elif "load" in choice:
			saveandload.loadgame("saver")		
		# attack command
		elif "a" in choice:
			#print "hit or miss going"
			hitormiss(targetA, targetB)
			#return 
		
		elif "q" in choice:
			questlog.listactivequests(targetA)
			newbattle(targetA, targetB) #uh, i think
		
		else:
			printlist.append("Make a choice:\nAttack (a) \nBlock (b) \nHeal(h)\nInventory (i)",)

# monster commands
def battlecommandM(monster, player):
	#while True: #targetA.hp >= 1 and targetB.hp >= 1:
	if 0 == 0:
		if monster.hp >= 1:
			hitormiss(monster, player)
			# print "you will never see this"
			monster.turn = 1
			return monster.turn 
		else:
			monster.turn = 1
			return monster.turn
			

# after winning battle	
def battlevictory(targetA, targetB):
	printlist.append("<p2>\n\t\t-Battle WON!-</p2>",)
	printlist.append("\n%s died. %s is VICTORIOUS! Yay!\n" % (targetB.name, targetA.name),)
	lootG = targetB.dropgold
	printlist.append("You received <h2>%d Gold!</h2>" % lootG,)
	targetA.gold += lootG
	randloot = randint(0,4)
	looter = targetB.droploot[randloot].title()
	printlist.append("You also found a <p3>%s </p3>and added it to your inventory!\n" % looter,)
	looter = looter.lower()
	targetA.inventory.append(looter)
	
	gotXP = targetB.dropxp
	printlist.append("You earned <p6>%d Experience Points!</p6>" % gotXP,)
	targetA.xp += gotXP
	if targetA.xp >= targetA.nextlvl:
		levelup(targetA)
		pass
	else:
			pass
	
	#invcmd.invcommand(targetA)	
	import outside
	#return
	outside.overworld(targetA)		

	
# level up function, called after getting XP at end of battle			
def levelup(targetA):
	printlist.append("<h2>\n\t==LEVEL UP!==\n</h2>",)
	
	targetA.xplvl += 1
	targetA.maxhp = targetA.maxhp + (targetA.xplvl / 1.5 )
	targetA.hp = targetA.maxhp #heal that
	targetA.maxmp = targetA.maxmp + (targetA.xplvl / 1.5 )
	targetA.mp = targetA.maxmp #heal that
	printlist.append("%s gained a new level!" % targetA.name,)
	printlist.append("%s is now <p5>level %d</p5>" % (targetA.name, targetA.xplvl),)
	targetA.str += 1
	targetA.defense += 1
	targetA.int += 1
	targetA.spd += 1
	printlist.append("%s's stats increased!\n" % (targetA.name),)
	printlist.append("<p3>%s's stats:\nStrength: %d\nDefense: %d\nIntelligence: %d\nSpeed: %d</p3>" % (
			targetA.name, targetA.str, targetA.defense, targetA.int,
			targetA.spd),)
	printlist.append("\nYou get one bonus point to spend. \nWhich stat would you like to increase?",)
	printlist.append("<p2>\n1. Strength \n2. Defense \n3. Intelligence \n4. Speed</p2>",)
	#levelupchoice()
	
	#while True:
def levelupchoice(targetA, choice):
	
	if "1" in choice:
		targetA.str += 1
	elif "2" in choice:
		targetA.defense += 1
	elif "3" in choice:
		targetA.int += 1
	elif "4" in choice:
		targetA.spd += 1

	else:
		pass
		#printlist.append("That wasn't a choice. Try again!")
		
	# new spells learned here
	if targetA.xplvl in targetA.magicbook.keys():
		printlist.append("<p6>\n\t==NEW SPELL!==\n</p6>",)
		newspell = targetA.magicbook[targetA.xplvl]
		targetA.gotspells.append(newspell)

		printlist.append("%s learned the new spell, <p4>%s!\n</p4>" % (targetA.name, newspell.title()),)
		
	#kludgy, but works for now, and almost looks nice
	targetA.nextlvl = (targetA.xp + randint(1,9)) + targetA.xplvl * 50
	return