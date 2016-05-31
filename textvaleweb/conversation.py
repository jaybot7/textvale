######conversation.py
##### conversation functions for NPCs

from random import randint

import npc
import prompter 
import string
import nikalbar
import web


def dialogue(hero, townsfolk, questionnope, panswer):
	global answer
	answer = panswer
	
	global questionno
	questionno = questionnope
	
	global listnumber
	listnumber = 0
	
	if questionno: # if already been through once
		pass #do nothing
	else: #else assign 1st time through
		questionno = 1
		answer = 0

	#if second time through or more 
	if townsfolk.defconvoq == True:
		if answer >= 1: #it better be on 2nd time!
			
			questionno = (questionno * 10) + answer 
						#if there are more than 9 QA be careful
			
			#print "about to convo loop"
			convoloop(hero, townsfolk, questionno, answer, listnumber)
				
		
		else: # first time through
			convoloop(hero, townsfolk, questionno, answer, listnumber)	
	else: #if no conversation even set on npc, do default
		printlist.append("<p4>\n%s:</p4> %s" % (townsfolk.name, 
			townsfolk.defconvo[randint(0, len(townsfolk.defconvo) - 1)]),)
		
	

def convoloop(hero, townsfolk, questionnope, panswer, plistnumber):
		global listnumber
		listnumber = plistnumber
		
		global answer
		answer = panswer
		
		global questionno
		questionno = questionnope
		
		global choices
		print questionno
		
		
		printlist.append("<p4>\n%s:</p4>" % townsfolk.name,)
		question = (townsfolk.defQ1[questionno].keys())[0]
		printlist.append("%s\n" % question,)
		choices = (townsfolk.defQ1[questionno].values())[0]
		printlist.append("\n<p6>%s's response:</p6>\n" % hero.name,)
		if len(choices) <= 1:
			printlist.append("- %s" % (choices[0]),)
		else:
			
			for i in choices:
				listnumber += 1
				printlist.append("<p2>%d. %s</p2>\n" % (listnumber, i),)
		printlist.append("",)
		###### responses below
		 
		#answer = raw_input(prompter.prompter)
		
		if listnumber <= 1: #if only 1 choice, then automatically exit any key
			#unless the player has reached a special number 
			# specified in the npc tree
			for i in townsfolk.specialA: #range(0, len(townsfolk.specialA)):
				#print i
				#print str (townsfolk.specialA[i])
				if questionno == i: 
					lister = -1
					for i in townsfolk.specialflag.keys():
						lister += 1
						specialkey = townsfolk.specialflag.keys()[lister]
						specialvalue = townsfolk.specialflag.values()[lister]
						hero.globalflags[specialkey] = specialvalue
					

def convoloop_answer(hero, townsfolk, questionnope, panswer, plistnumber):
		global question
		
		global listnumber
		listnumber = plistnumber
		
		global answer
		answer = panswer
		
		global questionno
		questionno = questionnope
		
		#try:
		try:
			int(answer)		
			if answer >= 1: 
				beforeselected = (townsfolk.defQ1[questionno].values())[0]
				print townsfolk.defQ1
				print beforeselected
				answer = int(answer) #convert rawinput to int
				
				while questionno >=11:
					questionno /= 10 #get back to one digit
				#else:
				#	pass
				questionno += 1
				#print "looping now with %d%s" % (questionno, answer)
				try: 
				#	printlist.append("<p3>\n%s:</p3> %s" % (hero.name, beforeselected[answer]),)
				#except:
					printlist.append("<p3>\n%s:</p3> %s" % (hero.name, beforeselected[answer - 1]),)
				except IndexError:
					######### the following is a giant hack for a bug that kind of exists because of the nature
					####### of html and rewriting the input to start half way through the conversation loop
					### hopefully it doesnt fuck anything else up.
					print questionno
					#printlist.append("That key, wasn't something in the list...",)
					print questionno
					questionno *= 10
					questionno -= 10
					questionno += answer
					answerfix = (townsfolk.defQ1[questionno].values())[0]
					questionfix = (townsfolk.defQ1[questionno+10].keys())[0]
					printlist.append("<p3>\n%s:</p3> %s" % (hero.name, answerfix[1]),)					
					printlist.append("<p4>\n%s:</p4>" % townsfolk.name,)
					printlist.append("%s\n" % questionfix,)
					printlist.append("\n<p6>%s's response:</p6>\n" % hero.name,)
					choicesfix = (townsfolk.defQ1[questionno+10].values())[0]			
					printlist.append("- %s" % (choicesfix[0]),)
					
					return 
					
					
				dialogue(hero, townsfolk, questionno, answer)		
				#return go thru the loop again
				
			else:
				printlist.append("Big problem here.",)
				nikalbar.printlist = []	
				nikalbar.global_variable_checks(hero)
				nikalbar.talkabar(hero)
				nikalbar.printlist.append("That wasn't an option",)
				nikalbar.printlist.append("Let's start over and try again...",)
				mapdesc = nikalbar.printlist
				htmlsplit(mapdesc)
				return render.show_room(room=mapdesc, room2="TalkBar")	
				
		#except IndexError:
		#	printlist.append("That index, wasn't something in the list...",)
		#	printlist.append("Let's try that again...",)
			#del questionno
			#del answer
			#dialogue(hero, townsfolk, "", "")
			#return
			
			
		except KeyError:  # if number outside of whats listed
			nikalbar.printlist = []	
			nikalbar.global_variable_checks(hero)
			nikalbar.talkabar(hero)
			nikalbar.printlist.append("That wasn't an option",)
			nikalbar.printlist.append("Let's start over and try again...",)
			mapdesc = nikalbar.printlist
			htmlsplit(mapdesc)
			return render.show_room(room=mapdesc, room2="TalkBar")	
			
			
			#return
			printlist.append("That key, wasn't something in the list...",)
			#print questionno
			#while questionno >=11:
			#		questionno /= 10
			#questionno *= 10
			#questionno += 10
			#questionno += answer
			#print questionno
			#answerfix = (townsfolk.defQ1[questionno].keys())[0]
			#printlist.append("<p3>\n%s:</p3> %s" % (hero.name, answerfix[1]),)
			#dialogue(hero, townsfolk, questionno, answer)	
			#print townsfolk.defQ1.values
			#print townsfolk.defQ1.keys
			#printlist.append("Let's try that again...",)
			#del questionno
			#del answer
			#dialogue(hero, townsfolk, "", "")
			#return
			pass
			
		except ValueError:
			#if number not entered and...	
			printlist.append("That wasn't an option",)
			printlist.append("Let's try again.",)
			#del questionno
			#del answer
			#dialogue(hero, townsfolk, "", "")		
			#return

### an example of how this works:
if __name__ == "__main__":
    # this won't be run when imported			

	hero = npc.Hero("Duncan")

	dude = npc.TownsFolk("Happy Dude")
	dialogue(hero, dude, "", "")

	dude.defconvo = "Sup?"
	dialogue(hero, dude, "", "")

	dude.defconvoq = True
	dialogue(hero, dude, "", "")

	dude2 = npc.Jimmy("Suspicious Guy")
	dialogue(hero, dude2, "", "")


	try:
		if hero.globalflags["dragon"] == 1:
			print "You got the Dragon! Yay!"
			print "And that's how NPC dialogues and global flags work!"

	except KeyError:
		print "You didn't get the Dragon..."