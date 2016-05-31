###invcmd.py
## i just needed a better place to put these common functions
import npc

#check inventory, pretty much anywhere

def invcommand(targetA):
	global printlist
	printlist = []
	if targetA.inventory:
		printlist.append ("<p3>%s's inventory contains:</p3>\n%s" % (targetA.name, ListStripAnd(targetA.inventory)),)
	else:
		printlist.append ("\n%s's inventory is empty!" % (targetA.name),)
	printlist.append("<h2>Total Gold: %d</h2>" % targetA.gold,)
	printlist.append("<p6>%s is a Level %d %s</p6>" % (targetA.name, targetA.xplvl, 
			targetA.__class__.__name__),)
	printlist.append("\n%s's current stats:\n<p7>Strength: %d\nDefense: %d\nIntelligence: %d\nSpeed: %d</p7>" % (
			targetA.name, targetA.str, targetA.defense, targetA.int,
			targetA.spd),)
	printlist.append("\nCurrent Experience Points: <p6>%d XP</p6>" % targetA.xp,)
	printlist.append("\nNext level at <p5>%d XP</p5>" % targetA.nextlvl,)
	return
	
def ListCombine(listname):
	# so you dont fuck up the actual inventory, copy it to a new list
	newlist =[]; newlist.extend(listname)
	# so you don't fuck up the copy during loops
	newerlist =[]; newerlist.extend(listname)

	for i in newlist:
		while newerlist.count(i) > 1:
			#print "found more than 1 %r" % i
			itemname = i
			multiple = newerlist.count(i)
			newerlist.append("%s x %d" % (itemname, multiple))
			while multiple > 0:
				newerlist.remove(itemname)
				multiple -= 1
	return newerlist
	
#list strip to make list more readable as inventory		
def ListStripAnd(listname):
	newlist = ListCombine(listname)			
		
	liststripA = ""
	indextotal = len(newlist) - 1
	
	if indextotal > 1:
		for i in range(0, indextotal):
			liststripA += newlist[i] + ", "
		liststripB = newlist[indextotal]
		liststripAB = "%sand a %s" % (liststripA.title(), liststripB.title())
		# added title() above to make it more readable without affecting a, and
		return liststripAB
	elif indextotal == 1:
		for i in range(0, indextotal):
			liststripA += newlist[i] + " "
		liststripB = newlist[indextotal]
		liststripAB = "%sand a %s" % (liststripA.title(), liststripB.title())
		return liststripAB
	elif indextotal == 0:
		for i in range(0, indextotal):
			liststripA += newlist[i] + " "
		liststripB = newlist[indextotal]
		liststripAB = "%s" % (liststripB)
		return liststripAB.title()
	else:
		liststripAB = "%s" % (listname)
		return liststripAB