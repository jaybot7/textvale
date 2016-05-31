###magiccaster.py
##this is too fucking long to stay in the battlecommand file
from random import randint

import spells
import invcmd
import battlesystem4
import prompter

def magiccast(hero, targetB):
	global printlist
	global spellslist
	global spellselements
	import inspect #to grab all classes into a list
	import string #you'll need this for digits and other things
					# because regex is not something you need	
	
	# this will be quite similar 
	#to grabbing items from the inventory for selling at a shop
	
	# gotta make sure spells aint empty, the reason here is... at the bottom
	if hero.gotspells:
		tempitemlist = []
		###grab all names for spells class and put them in a list
		for name, obj in inspect.getmembers(spells):
				if inspect.isclass(obj):
					tempitemlist.append(obj.__name__)
		
		#print tempitemlist
		listnumber = 0
		spellslist = {}
		spellselements = {}
		printlist.append("<h2>Magic Spells...</h2>",)
		
		#this will be long and confusing, read the comments
		#grab the inventory, strip to string...		
		spestrip = invcmd.ListStripAnd(hero.gotspells)
		
		if "," in spestrip:
			spestrip = spestrip.replace( " and a", "")
			spestrip = spestrip.replace( ", ", ",") #get rid fo space after ,
			#stick it in a list....
			spelist = spestrip.split(',')
			
		#....and done!... except if we have multiple items... 
			#...... or names with spaces....
		
		elif "," in spestrip and "X" in spestrip: 
			# this happens when multiples exist and more than two
			spestrip = spestrip.replace( " ", ",")
			spestrip = spestrip.replace( ",X,", " X ")
			spelist = spestrip.split(',')
			
		else: #when two (or less) left, no commas
			spelist = spestrip.split( " and a ")
			
		#need to parse to list, then grab values from classes
		#then copy values for desc and sellprice to 
		multinumber = [] # for multiple stuff
		multiplelist = {} # also for multiple stuff
		
		for i in spelist:
			
			if " " in i: # for single items with a space in its name
							# thats way fucking easier
				i = i.replace(" ", "_")
			
			else:
				pass
		
			# prepare name for comparing to class names
			i = i.lower()
			listnumber += 1 #for listing
		
			#if items
			if i.lower() in tempitemlist:
				tempinstance = "spells.%s" % i #to string
			
			else:
				printlist.append(i,)
				tempinstance = "%s" % i
				printlist.append("something bad happened",)

			# if multiples, parse out how many to a separate dict
			# and keep clean to check against class names
			
			if " " in tempinstance: # for stuff with spaces
				tempinstance = tempinstance.replace(" ", "_")
			else:
				pass
		
			# get class properties for the current item
			tempinstance = eval(tempinstance)()
			
			#check if we're on the overworld or during a battle
			if "Monster" in targetB.__class__.__name__:
				#print list no, item name....
				printlist.append("<p2>\n%d. %s</p2> -" % (listnumber, 
					tempinstance.name),)

				printlist.append("%d MP\n   <p6>%s</p6>" % (tempinstance.mpcost,
						tempinstance.desc),)
				# make a temp dict with number keys for player selection
				spellslist[listnumber] = {tempinstance.name: tempinstance.mpcost}
			
				#also, we need its element later, grab it now before you forget
				spellselements[listnumber] = {tempinstance.name: tempinstance.element}
			
			else:
				if "healing" in tempinstance.element:
					#print list no, item name....
					printlist.append("<p2>\n%d. %s </p2>-" % (listnumber, 
						tempinstance.name),)

					printlist.append("%d MP\n   <p6>%s</p6>" % (tempinstance.mpcost,
							tempinstance.desc),)
					# make a temp dict with number keys for player selection
					spellslist[listnumber] = {tempinstance.name: tempinstance.mpcost}
			
					#also, we need its element later, grab it now before you forget
					spellselements[listnumber] = {tempinstance.name: tempinstance.element}
				else:
					listnumber -= 1 
					# not a healing spell, so we skip it on overworld
					continue
			
		#once all that shit is done, finally offer the choice
		
		if listnumber <= 0:
			#no healing spells available, go back
			printlist.append("Whoah, your have no healing spells! Nothing to cast...",)
			printlist.append("Let's head back to the top...",)
			#return
		else:
			pass #im not indenting everything below
			
		printlist.append("\nWhich one ya wanna use?",)
		printlist.append("Enter item number or <p2>(x)</p2> to go back.\n<p3>Current MP: %d/%d</p3>" % (
					hero.mp, hero.maxmp),)
		
		#spellchoice(spellcast)
		
def spellcaster(spellchoice, hero, targetB):
		spellcast = spellchoice
			
		# when number of item listed entered	
		try:
			int(spellcast)
			if spellcast >= 1: #type(purchase) == int and
				spellcast = int(spellcast) #convert rawinput to int
				listitem = spellslist[spellcast] #grab the item from the dict by its number
				listelement = spellselements[spellcast]
				
				spellname = listitem.keys() #convert to list
				elementname = listelement.keys()
				
				spellname = spellname[0] #convert to string
				elementname = elementname[0]
								
				printlist.append("<p3>Casting %s!</p3>" % spellname,)
				spellprice = listitem.values() #convert to list #because cast looks like cost
				elementvalue = listelement.values()
				
				spellprice = spellprice[0] #convert to int
				elementvalue = elementvalue[0]
				
				if hero.mp >= spellprice: #make sure they have enough mp
					hero.mp -= spellprice
					
					
					############### healing	
					if "healing" in elementvalue:
						#print "we be healing!"
						elementname = elementname.replace(" ", "_")
						elementname = "spells.%s" % elementname.lower()
						tempinstance2 = eval(elementname)() #shoudlve done this earlier
						
						curepoints = randint(2,3) * (tempinstance2.healamt)
						hero.hp += curepoints
						if hero.hp > hero.maxhp:
							hero.hp = hero.maxhp
						else:
							pass
						printlist.append("<p3>%s heals for %d HP!\nHP is now %d</p3>" % (
								hero.name, curepoints, hero.hp),)
				
						if "Monster" in targetB.__class__.__name__:
							battlesystem4.hitormiss(targetB, hero) 
						else:
							#return
							pass
						####################

					elif "fire" in elementvalue:
						#print "we be attacking with fire element"
						elementname = elementname.replace(" ", "_") #those pesky spaces...
						elementname = "spells.%s" % elementname.lower()
						tempinstance2 = eval(elementname)() #shoudlve done this earlier
						
						hit = randint(1,3)	
						newerhit =  hit * tempinstance2.atk  
						if newerhit < 1:
							newerhit = 1
						if hit == 3 and newerhit > 1:
							printlist.append("<p5>\nWhoah!</p5>",)
						printlist.append("<p3>The %s loses %r HP!</p3>" % (targetB.__class__.__name__, newerhit),)
						targetB.hp -= newerhit 
						hero.turn = 1
						if targetB.hp >= 1:
							#return
							battlesystem4.hitormiss(targetB, hero)
						elif targetB.hp <= 0:
							pass
							battlesystem4.newbattle(hero, targetB)
						else:
							printlist.append("wtf happened here?",)
							
					else:
						printlist.append("we fucked up.",)
						
						# then heal or attack for the specified amoutn times randint
						
						#change hero turn to 1 and return to battlecommand 
						
					hero.turn = 1
					#return
					
				else:
					printlist.append("Uh oh... not enough MP!",)
					printlist.append("Let's head back then...",)
					#return
			else:
				printlist.append("Oh, okay...",)
				printlist.append("Was there something else you do?",)
				#return
			
		except KeyError: # if number outside of whats listed
			printlist.append("That uh, wasn't something in the list...",)
			printlist.append("Was there something else you wanna do?",)
			#return
			
		except ValueError:
		#if number not entered and...
			if "x" in spellcast:
				printlist.append("Okay, back to the top!",)
				#return
		
			elif "save" in spellcast:
				scene = "newbattle"
				saveandload.savegame("saver", hero, "", shop, scene)
			
			elif "load" in spellcast:
				saveandload.loadgame("saver")
		
			else:
				printlist.append("I'll take that as a no...",)
				printlist.append("Was there something else you wanted to do?\n",)
				#return
		#else:
			# ah, this is why... if the hero has no spells yet...
			# i'm smarter than i look...
		#	printlist.append("Whoah, your have no spells! Nothing to cast...",)
		#	printlist.append("Let's head back to the top...",)
			#return