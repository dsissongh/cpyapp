import cherrypy
import json
from subprocess import call

users = {'test': 'password'}

#server_config={'server.socket_host': '0.0.0.0'}


class webapp():
	@cherrypy.expose
	def index(self):
		return json.dumps("Test")

	@cherrypy.expose
	def version(self):
		return json.dumps(cherrypy.__version__)

	@cherrypy.expose
	def testing(self):
		return "more testing"

	@cherrypy.expose
	def startt(self):
		call(["/usr/bin/gnome-terminal"])
		return "started"

	def validatepassword(realm, username, password):
		if username in users and users[username] == password:
			return True
		return False


serverconfig = {
	'server.socket_port':8000,

	'/protected/area': {
		'tools.auth_basic.on': True,
		'tools.auth_basic.realm': 'localhost',
		'tools.auth_basic.checkpassword': validatepassword
		}
	}

cherrypy.config.update(serverconfig)

if __name__ == '__main__':

    cherrypy.quickstart(webapp, conf)
