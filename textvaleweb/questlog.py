###questlog.py

### quest classes and list active quests function
		
class QuestBook(object):
	def __init__(self, name):
		self.name = name
		
	
class Quest(QuestBook):
	def __init__(self, name, active, finished, desc):
		self.questname = name
		self.active = active #if currently doing it or if its closed?
		self.finished = finished #if done and done
		self.desc = desc #description of the quest

def listactivequests(hero):
	global printlist
	if hero.questbook:
		for i in hero.questbook:
			if i.active == True: 
			# questlistobject.finished of course == False too
				printlist.append("\n<p3>Active Quests:</p3>",)
				printlist.append("\n\t* <p2>%s -</p2>%s.\n" % (i.questname, i.desc),)
				#return
			else:
				printlist.append("\n<p7>No Active Quests.</p7>\n",)
	else:
		printlist.append("\nNo quests.\n",)
		#will also need ot cover no active quests here eventually too
		#return
		
	return	

def listallquests(hero):
	global printlist
	if hero.questbook:
		for i in hero.questbook:
			if i.active == True: 
			# questlistobject.finished of course == False too
				printlist.append("\nActive Quests:",)
				printlist.append("\n\t* %s - %s.\n" % (i.questname, i.desc),)
				#return
			else:
				printlist.append("\nNo Active Quests.\n",)
			
			if i.finished == True:
				printlist.append("\nFinished Quests:",)
				printlist.append("\n\t* %s - %s.\n" % (i.questname, i.desc),)
				#return
			else:
				printlist.append("\nNo Finished Quests.\n",)
			
	else:
		printlist.append("\nNo quests.\n",)
		#will also need ot cover no active quests here eventually too
		#return
		
	#return	

	
"""
		if questlistobject.active == True: #of course it is *now*, but for later
		# questlistobject.finished of course == False too
							print "Active Quests:"
							print "%s - %s." % (questlistobject.questname, questlistobject.desc)
							
							
							hero.questbook
							"""					