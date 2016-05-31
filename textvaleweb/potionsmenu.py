####potionsmenu.py

import items
import battlesystem4
import prompter 
import invcmd

### for now, healing with potions menu, will most likely
### be expanded for all useable inventory

def listpotions(hero, targetB):
	global printlist
	global inventorylist
	# pull potions from inventory and list the ones that match classes
	# with self.useable, then list them and ask which one they want to use
	# then pass it to heal function
	
	import inspect #to grab all classes into a list
	import string #you'll need this for digits and other things
					# because regex is not something you need	
	
	# this will be quite similar 
	#to grabbing items from the inventory for selling at a shop
	
	# gotta make sure potions aint empty, the reason here is... at the bottom
	if "potion" in hero.inventory or "ether" in hero.inventory: #add elixir later
		
		
		tempitemlist = []
		###grab all names for items class and put them in a list
		for name, obj in inspect.getmembers(items):
				if inspect.isclass(obj):
					tempitemlist.append(obj.__name__)
	
		listnumber = 0
		inventorylist = {}
		printlist.append ("<h2>Potions available!</h2>")
		
		#this will be long and confusing, read the comments!
		
		#grab the inventory, strip to string...		
		invstrip = invcmd.ListStripAnd(hero.inventory)
		
		if "," in invstrip:
			invstrip = invstrip.replace( " and a", "")
			invstrip = invstrip.replace( ", ", ",") #get rid of space after ,
			#stick it in a list....
			invlist = invstrip.split(',')
			
		#....and done!... except if we have multiple items... 
			#...... or names with spaces....
		
		elif "," in invstrip and "X" in invstrip: 
			# this happens when multiples exist and more than two
			invstrip = invstrip.replace( " ", ",")
			invstrip = invstrip.replace( ",X,", " X ")
			invlist = invstrip.split(',')
			
		else: #when two (or less) left, no commas
			invlist = invstrip.split( " and a ")
			
		#need to parse to list, then grab values from classes
		#then copy values for desc and sellprice to 
		multinumber = [] # for multiple stuff
		multiplelist = {} # also for multiple stuff
		
		for i in invlist:
			#first, rip out the multiple items
			if "X" in i:
				fixname = ""
				for character in i:
					if character != "X":
						if character.isspace():
							character = "_"
							fixname = fixname + character
						else:
							fixname = fixname + character
							pass 
					else:
						fixname = fixname + character ##keep trailing X
						fixname = fixname.replace("_X", "") #theres the end!
						fixnumber = i.replace(i[0:len(fixname) + 3], "")
						specialname = fixname.replace(i[0:len(fixname) + 3], "") 
								# make that permanent, but dont fuck up anyone else

				# space between words now a _ , great! lets do you separately!
				if "_" in specialname:
					i = specialname
					multiplelist[specialname] = fixnumber	
				
				# all the normal, one word (but still multiple items) items go ahead
				else:
					j = i.replace(" ", "") # works as long as there is no space in name
					multinumber = j.split('X') #now a nice list of item:amount
					i = multinumber[0]
					multiplelist[i] = multinumber[1]	
			
			elif " " in i: # for single items with a space in its name
							# thats way fucking easier
				i = i.replace(" ", "_")
			
			else:
				pass
		
			# prepare name for comparing to class names
			i = i.lower()
			listnumber += 1 #for listing
		
			#if items
			if i.lower() in tempitemlist:
				if "potion" in i.lower() or "ether" in i.lower(): #add elixir later
					tempinstance = "items.%s" % i #to string
				else:
					listnumber -= 1 # item, but not a potion/ether
					continue
			else:
				# not in item class 
				listnumber -= 1
				continue
				
			# if multiples, parse out how many to a separate dict
			# and keep clean to check against class names
			if "x" in tempinstance:
				multinumber = []
				tempinstance = tempinstance.replace( "x", "")
				from string import digits #################################
				multinumber = tempinstance.split(',')
				tempinstance = tempinstance.translate(None, digits)
				tempinstance = tempinstance.replace( " ", "")
				multiplelist[tempinstance] = multinumber[1]
			else:
				pass
			if " " in tempinstance: # for stuff with spaces
				tempinstance = tempinstance.replace(" ", "_")
			else:
				pass
		
			# get class properties for the current item
			tempinstance = eval(tempinstance)()
			#print list no, item name....
			#we can't print whenever we want with html, so we have to make a list
			
			printlist.append("<p2>%d. %s</p2>: x" % (listnumber, tempinstance.name)) 
			# if multiple, print how many and how much each
			if i.title() in multiplelist:
				printlist.append("%s\n" % multiplelist[i.title()],)
				printlist.append("   %s" % tempinstance.desc,)
			# if not multiple, just print as normal	 
			else:	
				printlist.append("1\n   %s\n" % tempinstance.desc,)
			# make a temp dict with number keys for player selection
			inventorylist[listnumber] = {tempinstance.name: "none"}
	
		#once all that shit is done, finally offer the choice
		printlist.append("\nWhich one ya wanna drink? Enter item number or <p2>(x)</p2> to go back.",)
		
		
		####go to form input here....
def potionchoice(pchoice, hero, targetB):
	if "potion" in hero.inventory or "ether" in hero.inventory:
		global printlist
		global inventorylist
		#drink = raw_input(prompter.prompter)
		drink = pchoice
		 
		# when number of item listed entered	
		try:
			int(drink)
			if drink >= 1: #type(purchase) == int and
				drink = int(drink) #convert raw to int
				listitem = inventorylist[drink] #grab the item from the dict by its number
				itemname = listitem.keys() #convert to list
				itemname = itemname[0] #convert to string
				printlist.append ("<p3>Drinking %s!\n</p3>" % itemname,)
				itemname = itemname.lower()
				heal(hero, targetB, itemname)
				return
				
			else:
				pass
				
		except KeyError: # if number outside of whats listed
			printlist.append("That uh, wasn't something in the list...",)
			printlist.append("Let's head back...",)
			if "Monster" in targetB.__class__.__name__:
				battlesystem4.newbattle(hero, targetB)
			else:
				return
			
		except ValueError:
		#if number not entered and...
			if "x" in drink:
				printlist.append ("Okay, back to the top!",)
				if "Monster" in targetB.__class__.__name__:
					battlesystem4.newbattle(hero, targetB)
				else:
					return
		
			else:
				printlist.append("I'll take that as a no...",)
				printlist.append("Let's go back...",)
				if "Monster" in targetB.__class__.__name__:
					battlesystem4.newbattle(hero, targetB)
				else:
					return
	else:
		# ah, this is why... if the inv become empty during
		# i'm smarter than i look...
		# but fuck, will need to fix this when globals are fixed
		printlist.append("Whoah, no potions to drink!",)
		printlist.append("Let's try again...",)
		if "Monster" in targetB.__class__.__name__:
			battlesystem4.newbattle(hero, targetB)
		else:
			pass
			#return
	 

def heal(targetA, targetB, potionname):
	global printlist
	global inventorylist
	
	if "potion" in targetA.inventory or "ether" in targetA.inventory: #add elixir later
		#print targetA.inventory
		targetA.inventory.remove(potionname)
		#print targetA.inventory
		tempinstance = "items.%s" % potionname
		temppotion = eval(tempinstance)()
		
		#eval(items.temp)()
		#print "%s uses a %s from his inventory!" % (targetA.name, potionname)
		healamt = temppotion.healamt
		if temppotion.healhp == True and temppotion.healmp == False:
			targetA.hp += healamt
			if targetA.hp > targetA.maxhp:
				targetA.hp = targetA.maxhp
			else:
				pass
			printlist.append("<p3>%s healed for %d HP!\n%s's HP is now %d</p3>" % (targetA.name, 
					healamt, targetA.name, targetA.hp),)
			targetA.turn = 1
			return
		if temppotion.healmp == True and temppotion.healhp == False:
			targetA.mp += healamt
			if targetA.mp > targetA.maxmp:
				targetA.mp = targetA.maxmp
			else:
				pass
			printlist.append ("<p3>%s recovered %d MP!\n%s's MP is now %d</p3>" % (targetA.name, 
					healamt, targetA.name, targetA.mp),)
			targetA.turn = 1
			return
		if temppotion.healmp == True and temppotion.healhp == True:
			#when we make an elixir that does both
			pass
	else:
		printlist.append ("%s has no potions in his inventory!" % targetA.name,)
		if "Monster" in targetB.__class__.__name__:
			battlesystem4.newbattle(targetA, targetB)
		else:
			return "wtf"
			pass
			#return