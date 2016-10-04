import tornado.web
from handlers import base
import requests
from bs4 import BeautifulSoup

class Handler(base.Handler):
    def getGen(self):
        self.cr()
        with self.tag("html"):
            self.doc.asis(self.g.head("PolyCon 2017", "static/slide_min.png"))
            with self.tag("body"):
                with self.tag("main"):
                    with self.tag("div", klass="container"):
                        with self.tag("div", klass="row"):
                            with self.tag("center"):
                                soup = BeautifulSoup(requests.get("https://docs.google.com/forms/d/e/1FAIpQLSfTI1Rs4inaRiuqdvlyHdrsydSMOYiEPwaWreaRwLkMwp5aEw/viewform?key=pqbhTz7PIHum_4qKEdbUWVg").text)
                                self.doc.asis(str(soup.find("form")))
        return self.doc.getvalue()