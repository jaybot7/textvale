import web

urls = (
	'/', 'Index', '/bin/'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class Index(object):
	def GET(self):
		return render.hello_form()
		
	def POST(self):
		form = web.input(name="Dude", greet="Hello")
		x = web.input(fucker={})
		filedir = './static/' # change this to the directory you want to store the file in.
		if 'fucker' in x: # to check if the file-object is created
			filepath=x.fucker.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
			filename=filepath.split('/')[-1]  # splits the and chooses the last part (the filename with extension)
			fout = open(filedir +'/'+ "uploaded.jpg",'wb') # creates the file where the uploaded file should be stored
			fout.write(x.fucker.file.read()) # writes the uploaded file to the newly created file.
			fout.close() 

		#defaults dont work after a POST return so....
		if len(form.greet) < 1:
			form.greet = "hey"
		if len(form.name) < 1:
			form.name = "jimmy"
		
		greeting = "%s, %s!" % (form.greet.title(),
					form.name.title())
		return render.index(greeting = greeting)
		#return render.index(0)
		
if __name__ == "__main__":
	app.run()