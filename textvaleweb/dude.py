######conversation.py

##### conversation functions for NPCs

import npc
import prompter 
import string

def conversation(hero, townsfolk, questionno, answer):
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
	
			convoloop(hero, townsfolk, questionno, answer, listnumber)				
		
		else: # first time through
			convoloop(hero, townsfolk, questionno, answer, listnumber)	
	else: #if no conversation even set on npc, do default
		print townsfolk.defconvo
		
	

def convoloop(hero, townsfolk, questionno, answer, listnumber):
	
		print "\n%s:" % townsfolk.name,
		question = (townsfolk.defQ1[questionno].keys())[0]
		print "%s\n" % question
		choices = (townsfolk.defQ1[questionno].values())[0]
		print "%s's response:" % hero.name
		if len(choices) <= 1:
			print "- %s" % (choices[0])
		else:
			
			for i in choices:
				listnumber += 1
				print "%d. %s" % (listnumber, i)
			
		###### responses below
		 
		answer = raw_input(prompter.prompter)		
		
		if listnumber <= 1: #if only 1 choice, then automatically exit any key
			#unless the player has reached a special number 
			# specified in the npc tree
			if questionno == townsfolk.specialA:
				specialkey = townsfolk.specialflag.keys()[0]
				specialvalue = townsfolk.specialflag.values()[0]
				hero.globalflags[specialkey] = specialvalue
				return
			#nothing special to do
			return #get outta here!
		
		#try:
		try:
			int(answer)		
			if answer >= 1: 
				beforeselected = (townsfolk.defQ1[questionno].values())[0]
				
				answer = int(answer) #convert rawinput to int
				
				if questionno >=11:
					questionno /= 10 #get back to one digit
				else:
					pass
				questionno += 1
				#print "looping now with %d%s" % (questionno, answer)
				print "\n%s: %s" % (hero.name, beforeselected[answer - 1])
				
				conversation(hero, townsfolk, questionno, answer)		
				return
				
			else:
				print "Big problem here."
				
		except KeyError: # if number outside of whats listed
			print "That uh, wasn't something in the list..."
			print "Let's try that again..."
			del questionno
			del answer
			conversation(hero, townsfolk, "", "")
			return
			
		except ValueError:
			#if number not entered and...	
			print "That wasn't an option"
			print "Let's try again."
			del questionno
			del answer
			conversation(hero, townsfolk, "", "")		
			return

### an example of how this works:
if __name__ == "__main__":
    # this won't be run when imported			

	hero = npc.Hero("Duncan")

	dude = npc.TownsFolk("Happy Dude")
	conversation(hero, dude, "", "")

	dude.defconvo = "Sup?"
	conversation(hero, dude, "", "")

	dude.defconvoq = True
	conversation(hero, dude, "", "")

	dude2 = npc.Jimmy("Suspicious Guy")
	conversation(hero, dude2, "", "")


	try:
		if hero.globalflags["dragon"] == 1:
			print "You got the Dragon! Yay!"
			print "And that's how NPC dialogues and global flags work!"

	except KeyError:
		print "You didn't get the Dragon..."