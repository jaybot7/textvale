import web
from textvaleweb import outside
from textvaleweb import npc
from textvaleweb import invcmd
from textvaleweb import potionsmenu
from textvaleweb import battlesystem4
from textvaleweb import magiccaster
from textvaleweb import htmlcommands

urls = (
	'/game', 'GameEngine',  
	'/', 'Index', 
)

app = web.application(urls, globals())

# little hack so that debug works with sessions
if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store, 
								initializer={'room':None, 'room2':None})
	web.config._session = session
else:
	session = web.config._session
	
render = htmlcommands.render

class Index(object):
	def GET(self):
		# this is used to setup the session with starting values IMPORTANT FOR ALL GLOBAL STUFF
		#, them move onto gameengine with sessions
		global hero
		hero = npc.Hero("Duncan")
		htmlcommands.hero = hero		
		web.seeother("/game")

class GameEngine(object):
	def GET(self):
		global hero
		outside.printlist = []
		outside.overworld(hero)
		mapdesc = outside.printlist
		htmlcommands.htmlsplit(mapdesc)	
		return render.show_room(room=mapdesc, room2=None)
		#else:			
		#	return "The game wants to kill you now, but that's fucking weak." 
	
	def POST(self):
		global hero
		global monsterspawn
		global printlist
		printlist = []
		#this is to test for incoming special values
		testform = web.input(incomingintvalue="")
		
		###all the rest of the commands are in htmlcommands file
		return htmlcommands.main_commands(hero, printlist, testform) 	
	
if __name__ == "__main__":
	app.run()