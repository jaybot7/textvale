from nose.tools import *
from gothonweb.map import *

#test room function...
def test_room():
	#set instance of room with name of goldroom, long description
	gold = Room("GoldRoom",
				"""This room has gold in it you can grab. There's a
				door to the north.""")
	# assert equal--nosetool-tocheckiftrue-- 
	## (this instance name, set to goldroom 
	assert_equal(gold.name, "GoldRoom")
	## do the same with this instance paths, make a dictionary
	assert_equal(gold.paths, {})

# test room paths function	
def test_room_paths():
	#center instance named center, north, south, with desc
	center = Room("Center", "Test room in thge center.")
	north = Room("North", "Test room in the north.")
	south = Room("South", "Test room in the south.")
	
	#add paths function attached to center instance,
	# will update dict with north and south values
	center.add_paths({'north': north, 'south': south})
	
	#assert equal 'go'function on center instance
	# has args north, north
	assert_equal(center.go('north'), north)
	#assert equal 'go' variable on center instance
	# is set to sotuh, south --which should get added to..?
	assert_equal(center.go('south'), south)

#test map function	
def test_map():
	# start/west/down room instance, with desctiptions
	start = Room("Start", "you can go west and down a hole")
	west = Room("Trees", "There are trees here, you can go east")
	down = Room("Dungeon", "Its dark down here, you can go up.")
	
	# add paths variables for start/west/down instances
	#set to dict values
	start.add_paths({'west': west, 'down': down})
	west.add_paths({'east': start})
	down.add_paths({'up': start})
	
	#assert equal that 'go' variable for start has values
	# of west; 
	# the value go.east of start.go west is set to start
	# the value go up of start.go down is start
	assert_equal(start.go('west'), west)
	assert_equal(start.go('west').go('east'), start)
	assert_equal(start.go('down').go('up'), start)
	
def test_gothon_game_map():
	assert_equal(START.go('shoot!'), corridor_death)
	assert_equal(START.go('dodge!'), corridor_death)
	
	room = START.go('tell a joke')
	assert_equal(room, laser_weapon_armory)
	
	assert_equal(room.go('*'), laser_weapon_armory)
	
	room = room.go('0132')
	assert_equal(room, the_bridge)
	
	assert_equal(room.go('throw the bomb'), bridge_death)
	#assert_equal(room.go('*'), bridge_death)
	
	room = room.go('slowly place the bomb')
	assert_equal(room, escape_pod)
	
	assert_equal(room.go('*'), the_end_loser)
	assert_equal(room.go('*'), the_end_loser)
	
	room = room.go('2')
	assert_equal(room, the_end_winner)
	
	room = escape_pod
	room = room.go('*')
	assert_equal(room, the_end_loser)