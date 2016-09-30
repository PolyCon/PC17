from bs4 import BeautifulSoup
import tornado.web
from yattag import Doc
from fragments import gen

class Handler(tornado.web.RequestHandler):
    def cr(self):
        self.g = gen.general()
        self.doc, self.tag, self.text = Doc().tagtext()
    def clean(self, htmli):
        return BeautifulSoup(htmli, "html.parser").prettify()
    def getGen(self):
        return "<html><body><h1>Hello world!</h1></body></html>"
    def get(self):
        self.write(self.clean(self.getGen()))
    def postGen(self):
        return "<html><body><h1>Hello world!</h1></body></html>"
    def post(self):
        self.write(self.clean(self.postGen()))