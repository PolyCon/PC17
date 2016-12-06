import tornado.web
from handlers import base

class Handler(base.Handler):
    def getGen(self, arguments):
        self.cr()
        with self.tag("html"):
            self.doc.asis(self.g.head("PolyCon 2017", "{0}/logo_300.png".format(self.l)))
            with self.tag("body"):
                self.doc.asis(self.hd["general"]["nav"].replace("#", "{0}/logo_300.png".format(self.l)))
                with self.tag("main"):
                    self.doc.asis(self.hd["general"]["faq"])
        return self.doc.getvalue()