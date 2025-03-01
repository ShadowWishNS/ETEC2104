import cherrypy
import os.path

import random

#we have modules for each page we're displaying 
import page_index
import page_signup
import page_posts
import page_test

class App:
    @cherrypy.expose
    def index(self):
        return page_index.get()
    @cherrypy.expose
    def signup(self):
        return page_signup.get()
    @cherrypy.expose
    def posts(self):
        return page_posts.get()
    @cherrypy.expose
    def test(self):
        return page_test.get()
    
    @cherrypy.expose
    def quote(self):
        d = os.path.dirname(__file__)
        t = mako.template.Template(
            filename=f"{d}"
        )
        q = random.choice(quotes.quotations)
        return t.render(quote=q)
        
#the location where the main.py file is stored: The src folder
srcdir = os.path.abspath(os.path.dirname(__file__))

# issues where localhost will not resolve on my network, ChatGPT told me I can set configs to fix it:
# this indeed fixed my issues
cherrypy.config.update({
    "server.socket_host": "0.0.0.0",  # Binds to all interfaces
    "server.socket_port": 8080,       # Ensures it's running on port 8080
})

app = App()
cherrypy.quickstart(
    app,
    '/',
    {
        "/html": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": f"{srcdir}/../html"
        }
    }
)
