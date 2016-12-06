from handlers import base

class Handler(base.Handler):
    def getGen(self, arguments):
        self.cr()
        with self.tag("html"):
            self.doc.asis(self.g.head("PolyCon Test Page", "static/slide_min.png"))
            with self.tag("body"):
                self.doc.asis(self.fmt.gen("test"))
        return self.doc.getvalue()