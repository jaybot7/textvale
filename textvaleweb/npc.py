## npc.py
##battle NPC stuff
#humanoid class for NPCs		
from random import randint

class Humanoid(object):
	def __init__(self, name):
		self.name = name
		self.shield = False

	turn = 0

class TownsFolk(Humanoid):
		def __init__(self, name):
			self.name = name
			self.defconvo = ["Hello!", 
				"The weather is starting to get warmer lately...\n",
				"Oh, hello good sir!\n", "Sorry, I'm a bit busy now.\n",
				"Could you move out of my way?\n",
				"Nice weather today!\n", "How's it going?\n",]
			self.defconvoq = False
			self.defQ1 = {1 : {"Nice day, isn't it?" : ["Yes", "No"]}, 
			21 : {"Awesome, you think so too!" : ["Okay, bye!"]}, 
			22 : {"What? You're just a grump!" : ["Yup, bye!"]}, }
			#self.defA1 = ["Yes", "No"]
			self.specialA = [0]		

class Seasoned_Adventurer(TownsFolk):
		def __init__(self, name):
			self.name = name
			self.defconvo = ["Hello!"]
			self.defconvoq = True
			self.defQ1 = {1 : {".........." : ["Rufus? Is that you?",
					"Hello?"]}, 
			21 : {"Err... no, you must have me confused with someone else." : [
				"Oh, sorry. My bad.", "Right, couldn't be..."]}, 
			22 : {"Leave me alone." : ["..."]}, 
			31 : {"No worries, I've been getting that a lot lately." : ["Sorry. Bye!"]}, 
			32 : {"I know, I know... ever since the famous Rufus %s" % (
				"went missing, everyone has been looking for him..."): [
				"Poor Rufus!", "Missing? The famous adventurer?"]},
			41 : {"Poor me! I wish people would stop asking me..." : ["I gotta go..."]},
			42 : {"You haven't heard? He went missing during one of his recent %s" % (
				"adventure tours... hasn't been seen or heard from in months!") : [
				"Huh. Interesting..."]}}
			self.specialA = [0]
			
class Worried_Man(TownsFolk):
		def __init__(self, name):
			self.name = name
			self.defconvo = ["Hello!"]
			self.defconvoq = True
			self.defQ1 = {1 : {"Y--yes? Can I help you?" : [
			"You look worried, you okay?", "Sorry, thought you were the waitress!"]}, 
			21 : {"Is it that obvious? Yes, I'm fretting over how to %s" % (
				"get my Dragon back...") : ["Dragon? You have a pet Dragon?! %s" % (
					"That's technically illegal these days..."), "Um, nevermind."]}, 
			22 : {"Nope, not me!" : ["Hehe. Sorry."]}, 
			31 : {"No-no, it's a Dragon Statue! It's been in my family %s" % (
				"for generations... but last night it went missing.\n%s") % (
				"I swear that Jimmy fellow took it..."): [
					"Some guy named Jimmy stole your statue? Got it.", (
					"Oh, definitely not interested. Bye!")]}, 
			32 : {"Oh. Okay." : ["Bye."]},
			41 : {"Yeah, if you can help out, I would totally appreciate it!" : [
				"I'll see what I can do."]},
			42 : {"Oh, okay..." : ["See ya!"]}}
			self.specialA = [41]
			self.specialflag = {"statueknow": 1, "statueknow2": 0}

class Worried_Man2(TownsFolk):
		def __init__(self, name):
			self.name = name
			self.defconvo = ["Hello!"]
			self.defconvoq = True
			self.defQ1 = {1 : {"If you can help out %s" % (
				"with my Dragon Statue, I would appreciate it!") : [
				"I'll see what I can do."]}}
			self.specialA = [0]
	
class Worried_Man3(TownsFolk):
		def __init__(self, name):
			self.name = name
			self.defconvo = ["Hello!"]
			self.defconvoq = True
			self.defQ1 = {1 : {"You're back! did you get the Dragon Statue?" : [
			"I sure did! Take a look.", "Whoops, not yet! Be back later."]}, 
			21 : {"Wow, amazing! Thank you so much!" : [
				"No problem.", "Just be careful from now on!"]}, 
			22 : {"Okay, I'll b-be here waiting..." : ["See you soon."]}, 
			31 : {"I can't thank you enough! I don't have much, but here...%s" % (
				"take this as a reward!") : ["Wow, thanks!"]},
			32 : {"I can't thank you enough! I don't have much, but here...%s" % (
				"take this as a reward!") : ["Wow, thanks!"]}}
			self.specialA = [31, 32]
			self.specialflag = {"statuegave": 1, "statuedone": 0}

class Less_Worried_Man(TownsFolk):
		def __init__(self, name):
			self.name = name
			self.defconvo = ["Thanks again for helping me with my statue!\n"]
			self.defconvoq = False
			self.specialA = [0]
			
class Jimmy_the_Hungry(TownsFolk):
		def __init__(self, name):
			self.name = name
			self.defconvo = ["Hello!"]
			self.defconvoq = True
			self.defQ1 = {1 : {"Why are you bothering me?!" : ["Where is the Dragon?",
					"Yeah, I gotta go..."]}, 
			21 : {"Dragon? Wh-what dragon?" : ["Don't play dumb!!!!", 
					"Um, nevermind?"]}, 
			22 : {"Good, don't bother me!" : ["..."]}, 
			31 : {"Okay, fine! You got me, here it is, take it!" : ["Great, thanks!"]}, 
			32 : {"Yes, indeed, nevermind! Really, some people..." : ["*groan*..."]},}
			self.specialA = [31]
			self.specialflag = {"dragon": 1}

class Jimmy_the_Hungry2(TownsFolk):
		def __init__(self, name):
			self.name = name
			self.defconvo = ["Hello!"]
			self.defconvoq = True
			self.defQ1 = {1 : {"You already got my Dragon... leave me alone." : ["Oh. Right. See ya!"]}}
			self.specialA = [0]
		
			
class Wheelbarrow(TownsFolk):
		def __init__(self, name):
			self.name = name
			self.defconvo = ["......\n\n\tYou have a deep conversation with the Wheelbarrow.", 
				".......\n\n\tYou nod to the Wheelbarrow.",
				"........\n\n\tYou tell the Wheelbarrow a silly story.", 
				"......\n\n\tYou discuss your favorite dessert toppings with the Wheelbarrow.",
				".........\n\n\tYou voice your political concerns to the Wheelbarrow.",
				"........\n\n\tYou ignore the Wheelbarrow in an effort to make it upset.",
				".....\n\n\tYou try to make the Wheelbarrow blush with an inappropriate joke.",]
			self.defconvoq = False
			self.defQ1 = {1 : {"Nice day, isn't it?" : ["Yes", "No"]}, 
			21 : {"Awesome, you think so too!" : ["Okay, bye!"]}, 
			22 : {"What? You're just a grump!" : ["Yup, bye!"]}, }
			#self.defA1 = ["Yes", "No"]
			self.specialA = [0]

class The_Town_Well(TownsFolk):
		def __init__(self, name):
			self.name = name
			self.defconvo = ["......\n\n\tYou peer down the Well in hopes of seeing something other than water.", 
				".......\n\n\tYou almost fall into the Well from sticking your head in too far.",
				"........\n\n\tYou almost flip a coin into the Well, hoping for a wish to come true\n\tthen quickly realize that you don't have anything to wish for.", 
				"......\n\n\tYou discuss your favorite dessert toppings with the Wheelbarrow.",
				".........\n\n\tYou take a sip from the Well.\n\tYou quickly regret it.",
				"........\n\n\tYou try to see your reflection in the water from the Well...\n\tYou can't make it out from the murkiness.\n\tYuck.",
				".....\n\n\tWell, well, well...",]
			self.defconvoq = False
			self.defQ1 = {1 : {"Nice day, isn't it?" : ["Yes", "No"]}, 
			21 : {"Awesome, you think so too!" : ["Okay, bye!"]}, 
			22 : {"What? You're just a grump!" : ["Yup, bye!"]}, }
			#self.defA1 = ["Yes", "No"]
			self.specialA = [0]
			
	#hero class for player		
class Hero(Humanoid):
	def __init__(self, name):
		self.name = name
		self.shield = False #to check for blocking during battle
		self.hp = 30
		self.maxhp = self.hp
		self.mp = 10
		self.maxmp = self.mp
		self.inventory = ["potion", "ether", "potion",  "potion", "shield", "sword", "sandwich", "sandwich"]
		self.gold = 10
		self.xp = 0
		self.xplvl = 1
		self.nextlvl = self.xp + self.xplvl * 10 #change how this works later
		self.flee = False
		#stats
		self.str = 1 #increases damage to attack
		self.defense = 1 #decreases damage received
		self.int = 1 #increase damage to magic
		self.spd = 1 
		# what spells learned : at which xplvl
		self.magicbook = {2: "flame of awesome", 3: "cure", 5: "ice", 7: "spark"}
		self.gotspells = []
		self.globalflags = {}
		self.questbook = []
	pass

#gothon class... could really be monster	
class Monster(Humanoid):
	def __init__(self):
		namepool = ["Gargle", "Spit", "Slimer", "Lizard",
					"Crazy Fox", "Sputtle", "Screaming Toenail", "Moley",
					"Red Buttlebottom", "Phasmagorn", "Fentibottom", "Black Spindle",
					"Bumdoggy", "Crakalaka", "Slugheart", "Fossil Mouth"]
		randname = randint(0, len(namepool) - 1)
		self.name = namepool[randname]
		
		
		#stats
		self.xplvl = randint(1,6)
		self.str = self.xplvl #increases damage to attack
		self.defense = self.xplvl #decreases damage received
		self.int = self.xplvl #increase damage to magic
		self.spd = self.xplvl #decreases odds of missing
		self.hp = self.xplvl * randint(2,4)
		self.maxhp = self.hp
		#self.flee = False
		#after death
		self.dropxp = self.xplvl * randint(1,15)
		self.droploot = ["potion", "boot", "sandwich", "hotdog", "trashy novel"]
		self.dropgold = self.xplvl * randint(1,15)
	command = 0
	pass

class Slimey(Monster): #not using yet, but eventually
	def __init__(self, name):
		self.name = name
		self.shield = False #to check for blocking during battle
		self.hp = randint(1,15)
		self.maxhp = self.hp
		self.inventory = ["potion", "potion", "potion", "shield", "sword", "sandwich", "sandwich"]
		self.dropgold = randint(1,15) #amt that will drop when defeated
		self.dropxp = randint(1,15) #amt that will earn when defeated
		self.xplvl = 1
		self.flee = False
		#stats
		self.str = 0 #increases damage to attack
		self.defense = 0 #decreases damage received
		self.int = 0 #increase damage to magic
		self.spd = 0 
		# what spells learned : at which xplvl
		self.magicbook = {"fire": 3, "cure": 5, "ice": 6, "spark": 8}
	command = 0	
	pass