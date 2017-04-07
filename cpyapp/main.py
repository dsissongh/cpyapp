import cherrypy

class webapp():
	@cherrypy.expose
	def index(self):
		return "Test"

	@cherrypy.expose
	def version(self):
		return cherrypy.__version__

if __name__ == '__main__':
    cherrypy.quickstart(webapp())