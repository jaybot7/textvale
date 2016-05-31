#make a class room

class Room(object):
	#when it makes an instance attach a name (arg1)
	# and a desccription (arg2)
	# and make a dict with name path
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}

# function go, with self and direciton args		
	def go(self, direction):
		#return values from the dict which match self(direction)
		return self.paths.get(direction, None)

# function to add paths with self and path args	
	def add_paths(self, paths):
		# update adds dict values from another dict (like extend)
		#the self.paths dict with the received paths variable
		self.paths.update(paths)
	
	
central_corridor = Room("Central Corridor",
"""
The Gothons of planet percal #25 have invade youre ship and other 
bad shit. im not going to typoe this all out.
Some fucker is blocking you. what  do you wanna do?
shoot! dodge! or tell a joke
""")

laser_weapon_armory = Room("Laser Weapon Armory",
"""
you leartned insults and jokes, you tell one to the fucker
he dies laughing
You move to the amorry and need to enter a code
its 3 digits
don't worry it won't kill you to try
""")

the_bridge = Room("The Bridge",
"""
you got it, it opens. you go to the brideg and need to set a bomb
throw the bomb or slowly place the bomb
""")

escape_pod = Room("Escape Pod",
"""
you place the bomb without dyuing and go to the escape pods
there aRE 5 pods. which one do you take?
1 2 3 4 or 5
""")

the_end_winner = Room("The End",
"""
Right Pod,
You win!
""")

the_end_loser = Room("The End",
"""
Wrong pod,
You lose!
""")

escape_pod.add_paths({
	'2': the_end_winner,
	'*': the_end_loser
})

generic_death = Room("death", "You died.")

bridge_death = Room("death", "You died on the bridge.")

armory_death = Room("death", "You died in the armory.")

corridor_death = Room("death", "You died in the corridor.")

the_bridge.add_paths({
	'throw the bomb': bridge_death,
	'slowly place the bomb': escape_pod,
	'*': the_bridge
})

laser_weapon_armory.add_paths({
	'0132': the_bridge,
	'*': laser_weapon_armory
})

central_corridor.add_paths({
	'shoot!': corridor_death,
	'dodge!': corridor_death,
	'tell a joke': laser_weapon_armory,
	'*': central_corridor
})

START = central_corridor

def loop(currentroom):
	print currentroom.description
	if "death" in currentroom.name or "End" in currentroom.name:
		exit(0)
	else:
		pass
	choice = raw_input("> ")
	#print choice
	if choice in currentroom.paths:
		room = currentroom.go(choice)
		#print room.name
		loop(room)
	else:
		print "nope"
		loop(currentroom)
	
#loop(START)