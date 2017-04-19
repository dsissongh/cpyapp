import cherrypy
import json

#import MySQLdb
#from md5 import md5

class RootServer:
    @cherrypy.expose
    def index(self):
        return json.dumps("Public")

class SecureServer:
    @cherrypy.expose
    def index(self):
        return "This is a secure section"


def encrypt_pw(pw):
    return pw

if __name__ == '__main__':
    users = {'test': 'password'}

    conf = {'/secure': {'tools.basic_auth.on': True,
                        'tools.basic_auth.realm': 'Some site2',
                        'tools.basic_auth.users': users,
                        'tools.basic_auth.encrypt': encrypt_pw}}
    root = RootServer()
    root.secure = SecureServer()
    cherrypy.quickstart(root, '/', config=conf)