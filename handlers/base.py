from bs4 import BeautifulSoup
import tornado.web
from yattag import Doc
from fragments import gen, hardg, fmu
from tools import sheets

class Handler(tornado.web.RequestHandler):
    def cr(self):
        self.g = gen.general()
        self.doc, self.tag, self.text = Doc().tagtext()
        self.hg = hardg.grabber()
        self.hd = self.hg.hdict
        self.fmt = fmu.form(Doc().tagtext())
        self.s = sheets.st()
        self.l = "https://s3.amazonaws.com/polycon"
    def clean(self, htmli):
        return BeautifulSoup(htmli, "html.parser").prettify()
    def getGen(self, arguments):
        return "<html><body><h1>Hello world!</h1></body></html>"
    def get(self):
        self.write(self.clean(self.getGen(self.request.arguments)))
    def postGen(self, arguments):
        return "<html><body><h1>Hello world!</h1></body></html>"
    def post(self):
        self.write(self.clean(self.postGen(self.request.arguments)))