import cherrypy
from cherrypy.lib import auth_basic

users = {'test': 'password'}

class myapp():

	@cherrypy.expose
	def test(self):
		return "test"



def validatepassword(realm, username, password):
	if username in users and users[username] == password:
		return True
	return False

conf = {
   '/protected/area': {
       'tools.auth_basic.on': True,
       'tools.auth_basic.realm': 'localhost',
       'tools.auth_basic.checkpassword': validatepassword
    }
}

cherrypy.quickstart(myapp(), '/', config=conf)