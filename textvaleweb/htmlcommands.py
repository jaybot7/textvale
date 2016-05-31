###html command list 

import web
from textvaleweb import outside
from textvaleweb import npc
from textvaleweb import invcmd
from textvaleweb import potionsmenu
from textvaleweb import battlesystem4
from textvaleweb import magiccaster
from textvaleweb import nikaltown
from textvaleweb import shop
from textvaleweb import shops
from textvaleweb import nikalbar
from textvaleweb import conversation
from textvaleweb import questlog

render = web.template.render('templates/', base="layout")

# this is to parse print commands added to a list and convert stuff to html
def htmlsplit(htmllist):
		j2 = -1
		for i in htmllist:
			j2 = j2 + 1
			try:
				htmllist[j2] = i.replace("\n", "<BR><BR>")
			except AttributeError:
					pass

#generic function to go back outside
def outsidedesc2(mapdesc):
	global hero
	mapdesc = mapdesc
	outside.printlist = []
	outside.overworld(hero)
	mapdesc2 = outside.printlist
	htmlsplit(mapdesc2)
	return render.show_room(room=mapdesc, room2=mapdesc2)					

def get_current_shop():
	global currentshop
	if "Arms" in shops.printlist[0]:
		currentshop = shop.ArmsShop("Nikal Arms")
	elif "Items" in shops.printlist[0]:
		currentshop = shop.ItemShop("Nikal Items")
	else:
		pass
	return 
	
def main_commands(hero, printlist, testform):
	global monsterspawn

##########################################bar stuff
########################talkbar choice
	
	if "talkbar_choice" in testform:
		form_tbc = testform.talkbar_choice
		
		# if player exits
		if "x" in form_tbc:
			nikalbar.printlist = []
			nikalbar.localbar(hero)
			mapdesc = nikalbar.printlist
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2="Bar")
		
		elif "q" in form_tbc:
			nikalbar.printlist = []
			questlog.printlist = []
			questlog.listactivequests(hero)
			mapdesc = questlog.printlist
			
			nikalbar.talkabar(hero)
			mapdesc.extend(nikalbar.printlist)
			htmlsplit(mapdesc)
			#return mapdesc
			return render.show_room(room=mapdesc, room2="TalkBar")
		
		elif "1" in form_tbc or "2" in form_tbc or "3" in form_tbc: 
			nikalbar.printlist = []
				
			nikalbar.talkabar_choice(form_tbc, hero)
			mapdesc = nikalbar.printlist
			htmlsplit(mapdesc)
			#return mapdesc
			
			global questionno
			conversation.dialogue(hero, nikalbar.townsfolk, "", "")
			questionno = conversation.questionno 
			global answer
			answer = conversation.answer
			global listnumber
			listnumber = conversation.listnumber
			return render.show_room(room=mapdesc, room2="TalkBar")		
				
		# if all above fails...
		else:
			nikalbar.printlist = []	
			nikalbar.talkabar(hero)
			mapdesc = nikalbar.printlist
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2="TalkBar")	

#####################################talkbar convo loop
	if "barconvo_choice" in testform:
		try:
			form_tbcc = int(testform.barconvo_choice)
			# if only one choice exit no matter what
			if len(conversation.choices) <= 1:
				nikalbar.printlist = []	
				nikalbar.talkabar(hero)
				nikalbar.global_variable_checks(hero)
				mapdesc = nikalbar.printlist
				htmlsplit(mapdesc)
				return render.show_room(room=mapdesc, room2="TalkBar")	 
			else:
				pass
			
			global listnumber
			global questionno
			global answer
			answer = conversation.answer
			townsfolk = nikalbar.townsfolk	
			
			
			conversation.convoloop(hero, townsfolk, questionno, answer, listnumber)
			conversation.printlist = []
			conversation.printlist.append("<h2>\t<==> Nikal Keys Inn - Bar <==></h2>",)
			conversation.printlist.append("<p3>\t--Bar Convo--</p3>\n",)
			conversation.convoloop_answer(hero, townsfolk, questionno, form_tbcc, listnumber)
			
			#hack to make the questions advance correctly
			if questionno <= 11:
				questionno += 20 
			elif questionno > 41:
				questionno += 0 
			else:
				questionno += 10
			
			mapdesc = conversation.printlist
			htmlsplit(mapdesc)
			#return mapdesc
			return render.show_room(room=mapdesc, room2="TalkBar")		
		
		except:
		
		# if all above fails...
		#else:
			nikalbar.printlist = []	
			nikalbar.global_variable_checks(hero)
			nikalbar.talkabar(hero)
			#return nikalbar.printlist
			mapdesc = nikalbar.printlist
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2="TalkBar")				

			
			
########################towntalk choice
	
	if "towntalk_choice" in testform:
		form_ttc = testform.towntalk_choice
		
		# if player exits
		if "x" in form_ttc:
			nikaltown.printlist = []
			nikaltown.townloop(hero)
			mapdesc = nikaltown.printlist
			htmlsplit(mapdesc)
		
			# town desc 		
			return render.show_room(room=mapdesc, room2="")
		
		elif "1" in form_ttc or "2" in form_ttc or "3" in form_ttc or "4" in form_ttc: 
			nikaltown.printlist = []
				
			nikaltown.talkaround_choice(form_ttc, hero)
			mapdesc = nikaltown.printlist
			htmlsplit(mapdesc)
			#return mapdesc
			
			global questionno
			conversation.dialogue(hero, nikaltown.townsfolk, "", "")
			questionno = conversation.questionno 
			global answer
			answer = conversation.answer
			global listnumber
			listnumber = conversation.listnumber
			return render.show_room(room=mapdesc, room2="TownTalk")		
		
		elif "q" in form_ttc:
			nikaltown.printlist = []
			questlog.printlist = []
			questlog.listactivequests(hero)
			mapdesc = questlog.printlist
			
			nikaltown.talkaround(hero)
			mapdesc.extend(nikaltown.printlist)
			htmlsplit(mapdesc)
			#return mapdesc
			return render.show_room(room=mapdesc, room2="TownTalk")
		
		# if all above fails...
		else:
			nikaltown.printlist = []	
			nikaltown.talkaround(hero)
			mapdesc = nikaltown.printlist
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2="TownTalk")		
			
			
#####################################	town talk convo loop
	if "townconvo_choice" in testform:
		try:
			form_ttcc = int(testform.townconvo_choice)
			# if only one choice exit no matter what
			if len(conversation.choices) <= 1:
				nikaltown.printlist = []	
				nikaltown.talkaaround(hero)
				nikaltown.global_variable_checks_talk(hero)
				mapdesc = nikaltown.printlist
				htmlsplit(mapdesc)
				return render.show_room(room=mapdesc, room2="TownTalk")	 
			else:
				pass
			
			global listnumber
			global questionno
			global answer
			answer = conversation.answer
			townsfolk = nikaltown.townsfolk	
			
			
			conversation.convoloop(hero, townsfolk, questionno, answer, listnumber)
			conversation.printlist = []
			conversation.printlist.append("<h2>\t<==> Nikal Town <==></h2>",)
			conversation.printlist.append("<p3>\t--Town Convo--</p3>\n",)
			conversation.convoloop_answer(hero, townsfolk, questionno, form_ttcc, listnumber)
			
			#hack to make the questions advance correctly
			if questionno <= 11:
				questionno += 20 
			elif questionno > 41:
				questionno += 0 
			else:
				questionno += 10
			
			mapdesc = conversation.printlist
			htmlsplit(mapdesc)
			#return mapdesc
			return render.show_room(room=mapdesc, room2="TownTalk")		
		
		except:
		
		# if all above fails...
		#else:
			nikaltown.printlist = []	
			
			nikaltown.talkaround(hero)
			nikaltown.global_variable_checks_talk(hero)
			mapdesc = nikaltown.printlist
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2="TownTalk")	
########################bar choice
	
	if "bar_choice" in testform:
		form_bc = testform.bar_choice
		
		# if player exits
		if "x" in form_bc:
			nikaltown.printlist = []
			nikaltown.townloop(hero)
			mapdesc = nikaltown.printlist
			htmlsplit(mapdesc)
		
			# town desc 		
			return render.show_room(room=mapdesc, room2="")
		
		elif "t" in form_bc:
			nikalbar.printlist = []	
			nikalbar.talkabar(hero)
			mapdesc = nikalbar.printlist
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2="TalkBar")	
		
		elif "b" in form_bc:
			nikalbar.printlist = []
			NikalInn = shop.Inn("Nikal Keys Inn", 10, 3)	
			nikalbar.overnight(NikalInn, hero)
			mapdesc = nikalbar.printlist
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2="Bar")		
				
		# if all above fails...
		else:
			nikalbar.printlist = []
				
			nikalbar.localbar(hero)
			mapdesc = nikalbar.printlist
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2="Bar")		
			
			
###########bar commands
	if "barcom_choice" in testform:
		form_bcom = testform.barcom_choice
		
		# if player exits
		if "x" in form_bcom:
			nikalbar.printlist = []	
			nikalbar.localbar(hero)
			mapdesc = nikalbar.printlist
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2="Bar")
	
		elif "d" in form_bcom:
			nikalbar.printlist = []	
			NikalInn = shop.Inn("Nikal Keys Inn", 10, 3)	
			nikalbar.buybeer(NikalInn, hero)
			mapdesc = nikalbar.printlist
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2="Bar")
		
		elif "b" in form_bcom:
			nikalbar.printlist = []	
			NikalInn = shop.Inn("Nikal Keys Inn", 10, 3)	
			nikalbar.gotobed(NikalInn, hero)
			mapdesc = nikalbar.printlist
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2="Bar")
							
		# if all above fails...
		else:
			nikalbar.printlist = []
			NikalInn = shop.Inn("Nikal Keys Inn", 10, 3)	
			nikalbar.overnight(NikalInn, hero)
			mapdesc = nikalbar.printlist
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2="Bar")

#######beer, yes beer choice
	if "beer_choice" in testform:
		form_beercom = testform.beer_choice
	
		if "y" in form_beercom:
			nikalbar.printlist = []	
			NikalInn = shop.Inn("Nikal Keys Inn", 10, 3)	
			nikalbar.beer_choice(form_beercom, NikalInn, hero)
			mapdesc = nikalbar.printlist
			
			nikalbar.overnight(NikalInn, hero)
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2="Bar")
		
		else:
			nikalbar.printlist = []
			nikalbar.printlist.append("<p8>\t<==> Nikal - Bar <==>\n</p8>",)
			nikalbar.printlist.append("Suit yourself. Anything else I can do for you?",)
			NikalInn = shop.Inn("Nikal Keys Inn", 10, 3)
			mapdesc = nikalbar.printlist
			
			nikalbar.overnight(NikalInn, hero)
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2="NoBeer")

#######bed, no bed choice
	if "bed_choice" in testform:
		form_bedch = testform.bed_choice
	
		if "y" in form_bedch:
			nikalbar.printlist = []	
			NikalInn = shop.Inn("Nikal Keys Inn", 10, 3)	
			nikalbar.gotobed_choice(form_bedch, NikalInn, hero)
			mapdesc = nikalbar.printlist
			
			nikalbar.overnight(NikalInn, hero)
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2="Bar")
		
		else:
			nikalbar.printlist = []
			nikalbar.printlist.append("<p8>\t<==> Nikal - Bar <==>\n</p8>",)
			nikalbar.printlist.append("\nSuit yourself. Anything else I can do for you?",)
			NikalInn = shop.Inn("Nikal Keys Inn", 10, 3)
			mapdesc = nikalbar.printlist
			
			nikalbar.overnight(NikalInn, hero)
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2="NoBed")
			
#########################################town stuff
	####################town choice
	
	if "tchoice" in testform:
		formt = testform.tchoice
		
		# if player exits
		if "x" in formt:
			nikaltown.printlist = []
			outside.printlist = []
			outside.overworld(hero)
			mapdesc = outside.printlist
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2="")			
	
		elif "w" in formt:
			nikaltown.printlist = []
			shops.printlist = []
			NikalArms = shop.ArmsShop("Nikal Arms")
			shops.shopping(NikalArms, hero)
			mapdesc = shops.printlist
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2="Shop")
			
		elif "s" in formt:
			nikaltown.printlist = []
			shops.printlist = []
			NikalItems = shop.ItemShop("Nikal Items")	
			shops.shopping(NikalItems, hero)
			mapdesc = shops.printlist
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2="Shop")
		
		elif "t" in formt:
			nikaltown.printlist = []
				
			nikaltown.talkaround(hero)
			mapdesc = nikaltown.printlist
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2="TownTalk")
		
		elif "b" in formt:
			nikaltown.printlist = []
			nikalbar.printlist = []
				
			nikalbar.localbar(hero)
			mapdesc = nikalbar.printlist
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2="Bar")
		
		# town inv command
		elif "i" in formt:
			nikaltown.printlist = []
			# do item command menu			
			invcmd.printlist = []
			invcmd.invcommand(hero)
			mapdesc = invcmd.printlist
			htmlsplit(mapdesc)

			# show town commands again			
			nikaltown.townloop(hero)
			mapdesc2 = nikaltown.printlist
			htmlsplit(mapdesc2)	
			return render.show_room(room=mapdesc, room2=mapdesc2)
		
		elif "q" in formt:
			nikaltown.printlist = []
			questlog.printlist = []
			questlog.listactivequests(hero)
			mapdesc = questlog.printlist
			
			nikaltown.townloop(hero)
			mapdesc.extend(nikaltown.printlist)
			htmlsplit(mapdesc)
			#return mapdesc
			return render.show_room(room=mapdesc, room2="Nikal")
		
		# town potions
		elif "p" in formt:			
			if "potion" in hero.inventory or "ether" in hero.inventory:
				potionsmenu.printlist = []
				potionsmenu.listpotions(hero, "")
				mapdesc = potionsmenu.printlist
				htmlsplit(mapdesc)	
				return render.show_room(room=mapdesc, room2="Nikal")
		
			else:
				nikaltown.printlist = []
				nikaltown.townloop(hero)
				mapdesc = nikaltown.printlist
				htmlsplit(mapdesc)	
				return render.show_room(room=["No Potions!",
					"<BR><BR>Let's head back..."], room2=mapdesc, ) # that'll work and reset it to the town		
		
		# town magic menu
		if "m" in formt:
			magiccaster.spellslist = []

			# go to magic menu
			if hero.gotspells:
				magiccaster.printlist = []
				magiccaster.magiccast(hero, "")
				mapdesc = magiccaster.printlist
				htmlsplit(mapdesc)	
				return render.show_room(room=mapdesc, room2="Nikal")
		
			else:
				nikaltown.printlist = []
				nikaltown.townloop(hero)
				mapdesc = nikaltown.printlist
				htmlsplit(mapdesc)
				return render.show_room(room=["No Magic!",
				"<BR><BR>Let's head back..."], room2=mapdesc) # that'll work and reset it to the beginning
		
		# if all above fails...
		else:
			nikaltown.printlist = []
			nikaltown.townloop(hero)
			mapdesc = nikaltown.printlist
			htmlsplit(mapdesc)
		
			# town desc 		
			return render.show_room(room=mapdesc, room2="")
	
	###########town sub menus	
	#town magic cast	
	if "tmchoice" in testform:
		formtm = testform.tmchoice
		
		magiccaster.printlist = []
		magiccaster.spellcaster(formtm, hero, "")
		mapdesc = magiccaster.printlist
			
		########## check if no MP
		if "Uh oh... not enough MP!" in mapdesc:
			nikaltown.printlist = []
			nikaltown.townloop(hero)
			mapdesc.extend(nikaltown.printlist)
			htmlsplit(mapdesc)	
			return render.show_room(room=["Nikal"], room2=mapdesc)
		else:
			pass
		htmlsplit(mapdesc)
		
		# town desc map2 
		nikaltown.printlist = []
		nikaltown.townloop(hero)
		mapdesc.extend(nikaltown.printlist)
		htmlsplit(mapdesc)	
		return render.show_room(room=["Nikal"], room2=mapdesc)
		
	# town potions
	if "ptchoice" in testform:
		formpt = testform.ptchoice
		potionsmenu.printlist = []
		potionsmenu.potionchoice(formpt, hero, "")
		mapdesc = potionsmenu.printlist
		htmlsplit(mapdesc)
		
		# town desc map2 
		nikaltown.printlist = []				
		nikaltown.townloop(hero)
		mapdesc2 = nikaltown.printlist
		htmlsplit(mapdesc2)	
		return render.show_room(room=mapdesc, room2=mapdesc2)		
		
	############################outside magic, potions
	#regular magic
	
	if "mchoice" in testform:
		formm = testform.mchoice
		
		magiccaster.printlist = []
		magiccaster.spellcaster(formm, hero, "")
		mapdesc = magiccaster.printlist
			
		########## check if no MP
		if "Uh oh... not enough MP!" in mapdesc:
			return outsidedesc2(mapdesc)
		else:
			pass
		htmlsplit(mapdesc)
		
		# outside desc map2 
		return outsidedesc2(mapdesc)
			
	#regular potions
	if "pchoice" in testform:
		formp = testform.pchoice
		potionsmenu.printlist = []
		potionsmenu.potionchoice(formp, hero, "")
		mapdesc = potionsmenu.printlist
		htmlsplit(mapdesc)
		
		# outside desc map2 ::: use internal function
		return outsidedesc2(mapdesc)
	
	# battle potions
	elif "pbchoice" in testform:
		formpb = testform.pbchoice
		#if cancelled
		if "x" in formpb:
			# battle commands 
			battlesystem4.battlecommandP(hero, monsterspawn)
			mapdesc = battlesystem4.printlist								
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2=None)
			
		else:
			pass
			
		potionsmenu.printlist = []
		potionsmenu.printlist.append("\n\t-%s Actions-\n" % hero.__class__.__name__,)
		potionsmenu.potionchoice(formpb, hero, monsterspawn)
		mapdesc = potionsmenu.printlist
		htmlsplit(mapdesc)
		
		#monstermoves
		battlesystem4.monstercommand(monsterspawn)
		battlesystem4.printlist = []
		if monsterspawn.turn == 0 and hero.flee == False:
			battlesystem4.battlecommandM(monsterspawn, hero)
		elif monsterspawn.turn == 0 and hero.flee == True: 
			hero.flee = False
		else:
			pass	
		
		# battle desc 
		battlesystem4.battlecommandP(hero, monsterspawn)
		mapdesc2 = battlesystem4.printlist								
		htmlsplit(mapdesc2)
		return render.show_room(room=mapdesc, room2=mapdesc2)			
	
	# battle magic
	elif "mbchoice" in testform:
		formmb = testform.mbchoice
			
		#if cancelled
		if "x" in formmb:
			# battle commands :: use internal function
			battlesystem4.battlecommandP(hero, monsterspawn)
			mapdesc = battlesystem4.printlist								
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2=None)				
		else:
			pass
		
		magiccaster.printlist = []
		magiccaster.printlist.append("\n\t-%s Actions-\n" % hero.__class__.__name__,)
		magiccaster.spellcaster(formmb, hero, monsterspawn)
		mapdesc = magiccaster.printlist
			
		########## check if no MP
		if "Uh oh... not enough MP!" in mapdesc:
			#return "no MP"
			battlesystem4.battlecommandP(hero, monsterspawn)
			mapdesc.extend(battlesystem4.printlist)								
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2=None)
		else:
			pass
		#monstermoves built into magic casting			
			
		#check if monster dead
		if monsterspawn.hp < 1:	
			magiccaster.printlist.extend(battlesystem4.printlist)
			mapdesc = magiccaster.printlist
			htmlsplit(mapdesc)						
			# outside desc map 2
			return outsidedesc2(mapdesc)
		else:
			pass
		#check if hero dead
		if hero.hp < 1:
			magiccaster.printlist.extend(battlesystem4.printlist)
			mapdesc = magiccaster.printlist
			htmlsplit(mapdesc)				
			return render.show_room(room=mapdesc, room2=["you dead"])	
		else:
			pass			
		#show battle commands again since no one is dead
		htmlsplit(mapdesc)
		battlesystem4.battlecommandP(hero, monsterspawn)
		mapdesc2 = battlesystem4.printlist
		htmlsplit(mapdesc2)						
		return render.show_room(room=mapdesc, room2=mapdesc2)
		
	#level up decision
	elif "lvlchoice" in testform:
		formlvl = testform.lvlchoice
		if "1" in formlvl or "2" in formlvl or "3" in formlvl or "4" in formlvl: 
			battlesystem4.printlist = []
			battlesystem4.levelupchoice(hero, formlvl)	
			mapdesc = battlesystem4.printlist
			htmlsplit(mapdesc)
		
			# outside desc map2 ::: use internal function
			return outsidedesc2(mapdesc)
		else:
			mapdesc = battlesystem4.printlist
			if "\nThat wasn't a choice. Try again!" in mapdesc[len(mapdesc) - 1]:
				pass
			else:
				mapdesc[len(mapdesc) - 1] = "<p2>\nThat wasn't a choice. Try again! \n1. Strength \n2. Defense \n3. Intelligence \n4. Speed</p2>"
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2=["LevelUp"])		
	
	#######################shop commands	#########################
	elif "s_choice" in testform:
		form_s = testform.s_choice
		
		# if player exits
		if "x" in form_s:
			nikaltown.printlist = []
			nikaltown.townloop(hero)
			mapdesc = nikaltown.printlist
			htmlsplit(mapdesc)
			# town desc 		
			return render.show_room(room=mapdesc, room2="")	
		
		# shop item command
		elif "i" in form_s:
			#we need the current shop to head back
			global currentshop
			get_current_shop()
				
			shops.printlist = []
			# do item command menu			
			invcmd.printlist = []
			invcmd.invcommand(hero)
			mapdesc = invcmd.printlist
			htmlsplit(mapdesc)

			# show shop commands again			
			shops.printlist = []
			shops.shopping(currentshop, hero)
			mapdesc.extend(shops.printlist)
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2=["Shop"])
		
		# shop buy command
		elif "b" in form_s:	
			#we need the current shop for functions
			global currentshop
			get_current_shop()
			
			shops.printlist = []
			shops.shop_choice(form_s, currentshop, hero)
			mapdesc = shops.printlist
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2=["Shop"])
		
		# shop sell command
		elif "s" in form_s:	
			#we need the current shop for functions
			global currentshop
			get_current_shop()
			
			shops.printlist = []
			shops.shop_choice(form_s, currentshop, hero)
			mapdesc = shops.printlist
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2=["Shop"])

		
		# if entered bad input
		else:
			global currentshop
			get_current_shop()
			
			nikaltown.printlist = []
			shops.printlist = []
			shops.shopping(currentshop, hero)
			mapdesc = shops.printlist
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2="Shop")
	
	################shop buy################
	if "sb_choice" in testform:
		global inventorylist
		inventorylist = shops.inventorylist 
		form_sb = testform.sb_choice
		
		#we need the current shop for functions
		global currentshop
		get_current_shop()
		
		shops.printlist = []
		shops.purchase_choice(form_sb, currentshop, hero, inventorylist)
		mapdesc = shops.printlist
		htmlsplit(mapdesc)
		
		# shop buy desc? 
		return render.show_room(room=mapdesc, room2="Shop")	
	
	if "sbconfirm_choice" in testform:
		global itemname
		global itemprice
		itemname = shops.itemname
		itemprice  = shops.itemprice		
		form_sbchoiceconfirm = testform.sbconfirm_choice
		
		#we need the current shop for functions
		global currentshop
		get_current_shop()
			
		shops.printlist = []
		shops.confirm_purchase_choice(form_sbchoiceconfirm, currentshop, hero, itemprice, itemname)
		mapdesc = shops.printlist
		
		
		shops.printlist = []
		shops.shopping(currentshop, hero)
		mapdesc.extend(shops.printlist)
		htmlsplit(mapdesc)
		return render.show_room(room=mapdesc, room2="Shop")	

	################shop selllll################
	if "ss_choice" in testform:
		global inventorylist
		inventorylist = shops.inventorylist 
		form_ss = testform.ss_choice
		
		#we need the current shop for functions
		global currentshop
		get_current_shop()
		
		shops.printlist = []
		shops.sale_choice(form_ss, currentshop, hero, inventorylist)
		mapdesc = shops.printlist
		htmlsplit(mapdesc)
		
		# shop buy desc? 
		return render.show_room(room=mapdesc, room2="Shop")	
	
	if "ssconfirm_choice" in testform:
		global itemname
		global itemprice
		itemname = shops.itemname
		itemprice  = shops.itemprice		
		form_sschoiceconfirm = testform.ssconfirm_choice
		
		#we need the current shop for functions
		global currentshop
		get_current_shop()
			
		shops.printlist = []
		shops.sale_confirm_choice(form_sschoiceconfirm, currentshop, hero, itemprice, itemname)
		mapdesc = shops.printlist
		
		shops.printlist = []
		shops.shopping(currentshop, hero)
		mapdesc.extend(shops.printlist)
		htmlsplit(mapdesc)
		return render.show_room(room=mapdesc, room2="Shop")	
		
	#######################actual battle commands	#########################
	elif "fchoice" in testform:
		formf = testform.fchoice
		
		# if player escaped
		if "x" in formf:
			battlesystem4.printlist = []
			battlesystem4.battlechoice(formf, hero, monsterspawn)
			mapdesc = battlesystem4.printlist
			htmlsplit(mapdesc)
			# outside desc map 2
			return outsidedesc2(mapdesc)			
		
		# battle potion menu
		elif "p" in formf:
			battlesystem4.printlist = []
			
			# go to potion menu
			if "potion" in hero.inventory or "ether" in hero.inventory:
				potionsmenu.printlist = []
				potionsmenu.listpotions(hero, "")
				mapdesc = potionsmenu.printlist
				htmlsplit(mapdesc)	
				return render.show_room(room=mapdesc, room2="Battle")
		
			else:
				battlesystem4.printlist = []
				battlesystem4.battlecommandP(hero, monsterspawn)
				mapdesc = battlesystem4.printlist
				htmlsplit(mapdesc)
				return render.show_room(room=["No Potions!",
					"<BR><BR>Let's head back..."], room2=mapdesc, ) # that'll should work, but fucks up the heros stats... figure it out
		
		# battle magic menu
		elif "m" in formf:
			battlesystem4.printlist = []
			magiccaster.spellslist = []
			
			# go to magic menu
			if hero.gotspells:
				magiccaster.printlist = []
				magiccaster.magiccast(hero, monsterspawn)
				mapdesc = magiccaster.printlist
				htmlsplit(mapdesc)	
				return render.show_room(room=mapdesc, room2="Battle")
		
			else:
				battlesystem4.battlecommandP(hero, monsterspawn)
				mapdesc = battlesystem4.printlist
				htmlsplit(mapdesc)
				return render.show_room(room=["No Magic!",
					"<BR><BR>Let's head back..."], room2=mapdesc, ) # that'll maybe work and reset it to the beginning
		
		# battle item command
		elif "i" in formf:
			battlesystem4.printlist = []
			# do item command menu			
			invcmd.printlist = []
			invcmd.invcommand(hero)
			mapdesc = invcmd.printlist
			htmlsplit(mapdesc)

			# show battle commands again
			battlesystem4.battlecommandP(hero, monsterspawn)
			mapdesc2 = battlesystem4.printlist
			htmlsplit(mapdesc2)						
			return render.show_room(room=mapdesc, room2=mapdesc2)
		
		elif "a" in formf or "b" in formf:
			#monstermoves consolidate this into a function later
			battlesystem4.monstercommand(monsterspawn)
			battlesystem4.printlist = []
			battlesystem4.battlechoice(formf, hero, monsterspawn)
			if monsterspawn.turn == 0 and hero.flee == False:
				battlesystem4.battlecommandM(monsterspawn, hero)
			elif monsterspawn.turn == 0 and hero.flee == True: 
				hero.flee = False
			else:
				pass		
		
			#check if monster dead
			if monsterspawn.hp < 1:
				mapdesc = battlesystem4.printlist
				htmlsplit(mapdesc)
							
				#if levelup happened
				for i in mapdesc:
					try:
						if "LEVEL" in i:
							# not yet battlesystem4.levelupchoice(hero)	
							return render.show_room(room=mapdesc, room2=["LevelUp"])
							
							#return "level up!" #do stuff
						else:
							pass	
					except TypeError:
						pass
					 #go on
					
				# outside desc map 2
				return outsidedesc2(mapdesc)			
			else:
				pass
		
			#check if hero dead
			if hero.hp < 1:
				mapdesc = battlesystem4.printlist
				htmlsplit(mapdesc)				
				return render.show_room(room=mapdesc, room2=["you dead"])	
			else:
				pass
		
			#show battle commands again since no one is dead
			battlesystem4.battlecommandP(hero, monsterspawn)
			mapdesc = battlesystem4.printlist
			htmlsplit(mapdesc)						
			return render.show_room(room=mapdesc, room2=None)

		# if entered bad input
		else:
			battlesystem4.printlist = []
			#return formf
			# battle commands 
			battlesystem4.battlecommandP(hero, monsterspawn)
			mapdesc = battlesystem4.printlist								
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2=None)
		
	##################end battle commands
	
	else:
		pass
		
	##############main overworld choices below
	form = web.input(choice="*")
	
	# inventory
	if form.choice == "i":
		invcmd.printlist = []
		invcmd.invcommand(hero)
		mapdesc = invcmd.printlist
		htmlsplit(mapdesc)

		# outside desc map 2 external function wont work for some reason. dammit
		return outsidedesc2(mapdesc)
	
	# potions
	if form.choice == "p":			
		if "potion" in hero.inventory or "ether" in hero.inventory:
			potionsmenu.printlist = []
			potionsmenu.listpotions(hero, "")
			mapdesc = potionsmenu.printlist
			htmlsplit(mapdesc)	
			return render.show_room(room=mapdesc, room2=None)
		
		else:
			outside.printlist = []
			outside.overworld(hero)
			mapdesc = outside.printlist			
			htmlsplit(mapdesc)
			return render.show_room(room=["No Potions!",
				"<BR><BR>Let's head back..."], room2=mapdesc) # that'll work and reset it to the beginning
	# go to battle		
	if form.choice == "f":			
			battlesystem4.printlist = []				
			monsterspawn = npc.Monster()
			battlesystem4.printlist.append ("A Level %d %s appeared!" % (monsterspawn.xplvl, monsterspawn.name),)
			battlesystem4.battlecommandP(hero, monsterspawn)
			#battlesystem4.newbattle(hero, monsterspawn) bypassing this
			
			mapdesc = battlesystem4.printlist
			htmlsplit(mapdesc)	
			return render.show_room(room=mapdesc, room2=None)			
	
	# go to town		
	if form.choice == "t":			
			nikaltown.printlist = []				
			nikaltown.townloop(hero)
			mapdesc = nikaltown.printlist
			htmlsplit(mapdesc)	
			return render.show_room(room=mapdesc, room2=None)	
	
	# load nothing		
	if form.choice == "=":				
			return render.you_died(arg1="load")
	
	
	# outside magic menu
	if form.choice == "m":
		magiccaster.spellslist = []

		# go to magic menu
		if hero.gotspells:
			magiccaster.printlist = []
			magiccaster.magiccast(hero, "")
			mapdesc = magiccaster.printlist
			htmlsplit(mapdesc)	
			return render.show_room(room=mapdesc, room2=None)
		
		else:
			outside.printlist = []
			outside.overworld(hero)
			mapdesc = outside.printlist			
			htmlsplit(mapdesc)
			return render.show_room(room=["No Magic!",
				"<BR><BR>Let's head back..."], room2=mapdesc) # that'll work and reset it to the beginning
						
	# no good input
	else: # that'll work and reset it to the overworld
		outside.printlist = []
		outside.overworld(hero)
		mapdesc = outside.printlist			
		htmlsplit(mapdesc)				
		return render.show_room(room=mapdesc, room2=None)
		
###the uh, actual game... only runs on first execute
if __name__ == "__main__":
    # this won't be run when imported
	hero = npc.Hero("Duncan")