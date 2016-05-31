##shops.py
## actual shop functions

import inspect #to grab all classes into a list
import string #you'll need this for digits and other things

import nikaltown
import items
import arms
import invcmd
import saveandload
import prompter
import questlog

## local load function
def shopbuy(shop, hero):
	global printlist
	printlist.append("<h2>\t<==> %s Shop <==></h2>" % shop.name,)
	printlist.append("<p3>Check out my wares!</p3>",)
	
	listnumber = 0
	global inventorylist
	inventorylist = {}
	
	#take inventory list, make instances from classes and print their values
	for i in shop.inventory:
		listnumber += 1
		if "Item" in shop.name:
			tempinstance = "items.%s" % i #to string
		elif "Arms" in shop.name:
			tempinstance = "arms.%s" % i #to string
		else:
			pass
		if " " in tempinstance: # for stuff with spaces
			tempinstance = tempinstance.replace(" ", "_")
		else:
			pass
		tempinstance = eval(tempinstance)()
		printlist.append("<p2>\n%d. %s:</p2>" % (listnumber, tempinstance.name),)
		printlist.append("<h2>   %d Gold.</h2>   %s" % (tempinstance.price, tempinstance.desc),)
		# make a temp dict with number keys for player selection
		inventorylist[listnumber] = {tempinstance.name: tempinstance.price}
	
	printlist.append("\n<p3>Which one do you want? Enter item number or (x) to go back.</p3>\n",)
	printlist.append("<p6>Current Gold: %d</p6>" % hero.gold,)
	
	###purchase = raw_input(prompter.prompter)
	#purchase_choice()
	
	
def purchase_choice(purchase, shop, hero, inventorylist):
	global itemprice
	global itemname
	
	printlist.append("<h2>\t<==> %s Shop <==></h2>" % shop.name,)
	
	# when number of item listed entered	
	try:
		int(purchase)
		if purchase >= 1: #type(purchase) == int and
			purchase = int(purchase) #convert raw to int
			listitem = inventorylist[purchase] #grab the item from the dict by its number
			itemname = listitem.keys() #convert to list
			itemname = itemname[0] #convert to string
			printlist.append("You wanna buy the <p4>%s</p4>, huh?" % itemname,)
			itemprice = listitem.values() #convert to list
			itemprice = itemprice[0] #convert to int
			printlist.append("That'll be <p4>%d Gold</p4>, is that okay?<p2>\nYes (y) \nor \nNo (n)</p2><p6>\nCurrent Gold: %d</p6>" % (
						itemprice, hero.gold),)
			#confirm = raw_input(prompter.prompter)
			
		else:
			pass
	except ValueError:
		printlist.append("I'll take that as a no...",)
		printlist.append("Was there something else you wanted?\n",)
		shopping(shop, hero)
		
	except IndexError:
		sale = str(sale)
		#if number not entered and...
		purchase = str(purchase)
		if "x" in purchase:
			printlist.append("Okay, back to the top!",)
			#shopping(shop, hero)
		
		elif "i" in purchase:
			invcmd.invcommand(hero)
			#shopbuy(shop, hero)
				
		elif "save" in purchase:
			scene = "shopbuy"
			saveandload.savegame("saver", hero, "", shop, scene)
			
		elif "load" in purchase:
			saveandload.loadgame("saver")
		
		else:
			printlist.append("I'll take that as a no...",)
			printlist.append("Was there something else you wanted?\n",)
			shopping(shop, hero)

def confirm_purchase_choice(confirm, shop, hero, itemprice, itemname):
	try:
	
		printlist.append("<p8>\t<==> %s Shop <==></p8>\n" % shop.name,)
	
		if "y" in confirm:
			if hero.gold >= itemprice:
				printlist.append("You betcha! Gimme a second here while I prep it for ya.\n",)
				hero.gold -= itemprice
				printlist.append("You paid <p6>%d Gold.</p6>\n" % itemprice,)
				printlist.append("You received the <p4>%s!</p4>" % itemname,)
				itemname = itemname.lower()
				hero.inventory.append(itemname)
				invcmd.invcommand(hero)
				printlist.append("\nIs there something else you wanted?\n",)
				#shopbuy(shop, hero)
			else:
				printlist.append("Oh, you seem to be a bit short on Gold...",)
				printlist.append("Is there something else you wanted?\n",)
			#shopbuy(shop, hero)
		else:
			printlist.append("Oh, okay...",)
			printlist.append("Was there something else you wanted?\n",)
			#shopbuy(shop, hero)
	except ValueError:
		printlist.append("I'll take that as a no...",)
		printlist.append("Was there something else you wanted?\n",)
		shopping(shop, hero)
	
	except KeyError:
		purchase = str(purchase)
		#if number not entered and...
		if "x" in purchase:
			printlist.append("Okay, back to the top!",)
			#shopping(shop, hero)
		
		elif "i" in purchase:
			invcmd.invcommand(hero)
			#shopbuy(shop, hero)
				
		elif "save" in purchase:
			scene = "shopbuy"
			saveandload.savegame("saver", hero, "", shop, scene)
			
		elif "load" in purchase:
			saveandload.loadgame("saver")
		
		else:
			printlist.append("I'll take that as a no...",)
			printlist.append("Was there something else you wanted?\n",)
			shopping(shop, hero)
			
def shopsell(shop, hero):
	global inventorylist
	
	# gotta make sure inventory aint empty, the reason here is... at the bottom
	if hero.inventory:
		tempitemlist = []
		###grab all names for items class and put them in a list
		for name, obj in inspect.getmembers(items):
				if inspect.isclass(obj):
					tempitemlist.append(obj.__name__)
	
		temparmslist = []
		### do the same for arms class
		for name, obj in inspect.getmembers(arms):
				if inspect.isclass(obj):
					temparmslist.append(obj.__name__)
	
		listnumber = 0
		inventorylist = {}
		printlist.append("<h2>\t<==> %s Shop <==></h2>" % shop.name,)
		printlist.append("<p3>Sure thing, what would you like to sell?</p3>",)
		
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
		totalcost = 0
		
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
				tempinstance = "items.%s" % i #to string
			
			# and arms
			elif i.lower() in temparmslist:
				tempinstance = "arms.%s" % i #to string
			else:
				#print i
				#if hero.inventory:
				#	tempinstance = "%s" % i
				print "something bad happened"
				#	#in case item not in a class. should be, but just in case
				#	listnumber -= 1
				#	continue
				#else:
				pass
					
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
		
			# get class properties for the current itemS
			tempinstance = eval(tempinstance)()
			
			#calculate total cost to check for non-sellable items
			totalcost += tempinstance.sellprice
			#print totalcost
				
			# if a sellable item, hide it and reduce the list number and skip to next
			if tempinstance.sellprice == 0:
				listnumber -= 1
				continue
			
			printlist.append("<p2>\n%d. %s: x" % (listnumber, 
				tempinstance.name), )
			# if multiple, print how many and how much each
			if i.title() in multiplelist:
				printlist.append("%s</p2>" % multiplelist[i.title()],)
				printlist.append("<h2>   %d Gold each.</h2>   </p2>%s" % (tempinstance.sellprice,
				tempinstance.desc))
			# if not multiple, just print as normal	 
			else:	
				printlist.append("1<h2>   %d Gold.</h2>   </p2>%s" % (tempinstance.sellprice,
					tempinstance.desc))
			# make a temp dict with number keys for player selection
			inventorylist[listnumber] = {tempinstance.name: tempinstance.sellprice}
		
		#once all that shit is done, finally offer the choice... if there are sellable items
		# if no sellable items, skip to no items and head back out
		if totalcost < 1:
				### no sellable items
				printlist.append("<p3>Whoah, your inventory is empty! I'm not in the market for buying air...</p3>",)
				printlist.append("<p3>Let's head back to the top...</p3>",)
				#shopping(shop, hero)
		else:
			pass
				
		printlist.append("<p3>\nWhich one ya wanna sell?\nEnter item number or <p2>(x)</p2> to go back.\n<p6>Current Gold: %d</p6>" % hero.gold,)
		
		#sale = raw_input(prompter.prompter)
		
		#sale_choice(sale, shop, hero, inventorylist)
	
	else:
		# ah, this is why... if the inv become empty WHILE selling
		# i'm smarter than i look...
		printlist.append("<p3>Whoah, your inventory is empty! I'm not in the market for buying air...</p3>",)
		printlist.append("<p3>Let's head back to the top...</p3>",)
		#shopping(shop, hero)	
	
def sale_choice(sale, shop, hero, inventorylist):
		global itemprice
		global itemname
	
		printlist.append("<h2>\t<==> %s Shop <==></h2>" % shop.name,)
	
		# when number of item listed entered	
		try:
			int(sale)
			if sale >= 1: #type(purchase) == int and
				sale = int(sale) #convert raw to int
				listitem = inventorylist[sale] #grab the item from the dict by its number
				itemname = listitem.keys() #convert to list
				itemname = itemname[0] #convert to string
				printlist.append("You wanna sell the <p4>%s</p4>, huh?" % itemname,)
				itemprice = listitem.values() #convert to list
				itemprice = itemprice[0] #convert to int
				printlist.append("That'll be <p4>%d Gold</p4>, is that okay?<p2>\nYes (y) \nor \nNo (n)</p2>\n<p6>Current Gold: %d</p6>" % (
							itemprice, hero.gold),)
				
			else:
				pass
				
				#confirm = raw_input(prompter.prompter)
				#confrim_choice(confirm, shop, h ..",)
			printlist.append("Was there something else you wanted to sell?\n",)
			#shopsell(shop, hero)	
			
		except ValueError:
			printlist.append("I'll take that as a no...",)
			printlist.append("Was there something else you wanted?\n",)
			shopping(shop, hero)
		
		except KeyError:
			sale = str(sale)
			#if number not entered and...
			if "x" in sale:
				printlist.append("Okay, back to the top!",)
				#shopping(shop, hero)
		
			elif "i" in sale:
				invcmd.invcommand(hero)
				#shopsell(shop, hero)
			
			elif "save" in sale:
				scene = "shopsell"
				saveandload.savegame("saver", hero, "", shop, scene)
			
			elif "load" in sale:
				saveandload.loadgame("saver")
		
			else:
				printlist.append("I'll take that as a no...",)
				printlist.append("Was there something else you wanted?\n",)
				shopping(shop, hero)		
				
def sale_confirm_choice(confirm, shop, hero, itemprice, itemname):
			try:	
				printlist.append("<p8>\t<==> %s Shop <==></p8>\n" % shop.name,)
				if "y" in confirm:
					if hero.gold >= 0: #lazy
						printlist.append("You betcha! Gimme a second here while I grab the Gold.",)
						hero.gold += itemprice
						printlist.append("\nYou received <p6>%d Gold.</p6>" % itemprice,)
						printlist.append("\nYou sold the <p4>%s</p4>!" % itemname,)
						itemname = itemname.lower()
						
						hero.inventory.remove(itemname) # or pop()
					
						invcmd.invcommand(hero)
						printlist.append("\nIs there something else you wanted?\n",)
						#shopsell(shop, hero)
					
					else:
						printlist.append("Oh, this is weird... You have negative gold?!",)
						printlist.append("Is there something else you wanted?\n")
						#shopsell(shop, hero)
				else:
					printlist.append("Oh, okay...",)
					printlist.append("Was there something else you wanted?\n",)
					#shopsell(shop, hero)
			
			except IndexError:
				printlist.append("I'll take that as a no...",)
				printlist.append("Was there something else you wanted?\n",)
				shopping(shop, hero)
			
			except ValueError:
			#if number not entered and...
				if "x" in sale:
					printlist.append("Okay, back to the top!",)
					#shopping(shop, hero)
		
				elif "i" in sale:
					invcmd.invcommand(hero)
					#shopsell(shop, hero)
			
				elif "save" in sale:
					scene = "shopsell"
					saveandload.savegame("saver", hero, "", shop, scene)
			
				elif "load" in sale:
					saveandload.loadgame("saver")
		
				else:
					printlist.append("I'll take that as a no...",)
					printlist.append("Was there something else you wanted?\n",)
					shopping(shop, hero)
					
def shopping(shop, hero):	
	printlist.append("<h2>\t<==> %s Shop <==></h2>" % shop.name,)
	printlist.append("Welcome to the <p6>%s</p6> shop!" % shop.name,)
	printlist.append("\nYou wanna Buy or Sell? Or you can exit too...<p2>\nBuy (b)\nSell (s)\nExit (x)</p2>",)

	#choice = raw_input(prompter.prompter)
	#shop_choice(choice, shop, hero)

def shop_choice(choice, shop, hero):
	if "b" in choice:
		shopbuy(shop, hero)
	
	#check inventory - stats command
	elif "i" in choice:
		invcmd.invcommand(hero)
		shopping(shop, hero)
	
	elif "save" in choice:
		scene = "shopping"
		saveandload.savegame("saver", hero, "", shop, scene)
		
	elif "q" in choice:
		questlog.listactivequests(hero)
		shopping(shop, hero) 
			
	elif "load" in choice:
		saveandload.loadgame("saver")	
	elif "s" in choice:
		shopsell(shop, hero)
		
	elif "x" in choice:
		nikaltown.townloop(hero)
		
		#return
	else:
		printlist.append("Um... not sure I caught that.",)
		shopping(shop, hero)