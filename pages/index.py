import tornado.web
from handlers import base

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
                                self.doc.stag("img", ("height", "400px"), src="static/slide_min.png")
                        with self.tag("div", klass="row"):
                            with self.tag("center"):
                                with self.tag("h2"):
                                    with self.tag("font", ("color", "#583F9A")):
                                        self.text("Coming Soon!")
        return self.doc.getvalue()