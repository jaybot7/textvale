####overworld.py
 
import shelve # for saving states

import nikaltown
import npc
import shop #classes
import shops #functions
import battlesystem4
import invcmd
import prompter
import saveandload
import potionsmenu
import magiccaster
import questlog
		
START = "Duncan"

#### overworld stuff		
def choices(choice):
	choice = choice
	if "f" in choice:
		monsterspawn = npc.Monster()
		import battlesystem4
		print "A Level %d %s appeared!" % (monsterspawn.xplvl, monsterspawn.name)
		battlesystem4.newbattle(hero, monsterspawn)
		
	#healing
	elif "p" in choice:
			potionsmenu.listpotions(hero, "")
			overworld(hero)
	#check inventory command
	elif "i" in choice:
			return invcmd.invcommand(hero)
			return overworld(hero)			
	# magic	
	elif "m" in choice:
		magiccaster.magiccast(hero, "")	
		overworld(hero)
		
	elif "save" in choice:
		scene = "overworld"
		saveandload.savegame("saver", hero, "", "", scene)
		overworld(hero)
		
	elif "load" in choice:
		saveandload.loadgame("saver")
			
	elif "t" in choice: #go to nikal
		nikaltown.townloop(hero)
		
	elif "q" in choice:
		questlog.listactivequests(hero)
		overworld(hero)
	
	else:
		print "Make a choice:\n\nFight (f)\nHeal (h)\nInventory (i)\nWeapon Shop (w)\n Items Shop (s)"
		overworld(hero)


def overworld(hero):	
	printlist.append ("\n\t<h2><==> Entoque Overworld <==></h2>",) 
	printlist.append ("You are now outside of battle.",)
	printlist.append ("<p3>\n%s: HP - %d/%d | MP - %d/%d </p3>" % (hero.name, 
			hero.hp, hero.maxhp, hero.mp, hero.maxmp),)
	printlist.append ("\nWould you like to fight monsters or... something else?",)
	printlist.append ("<p2>\nFight (f)\nPotions (p)\nInventory (i)",)
	if hero.gotspells:
		printlist.append ("\nMagic (m)\nTravel to Town (t)</p2>",)
	else:
		printlist.append ("\nTravel to Town (t)</p2>",)
	printlist.append ("\nYou can also type <p2>(=) Reset </p2>on this Overworld",)
	printlist.append ("to Clear your game data back to the beginning.",)
	#choice = raw_input(prompter.prompter)
	#choices(choice)
			

			
###the uh, actual game... only runs on first execute
if __name__ == "__main__":
    # this won't be run when imported
	overworld(npc.Hero("Duncan"))