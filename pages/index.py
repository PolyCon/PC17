import tornado.web
from handlers import base
import os

class Handler(base.Handler):
    def getGen(self, arguments):
        self.cr()
        with self.tag("html"):
            self.doc.asis(self.g.head("PolyCon 2017", "{0}/logo_300.png".format(self.l)))
            with self.tag("body"):
                imhl = []
                for im in os.listdir("static/slides"):
                    imhl.append("<li><img src='static/slides/{0}'></li>".format(im))
                self.doc.asis(self.hd["general"]["nav"].replace("#", "{0}/logo_300.png".format(self.l)))
                with self.tag("main"):
                    self.doc.asis(self.hd["general"]["prev17i"].replace("#C", "\n".join(imhl)))
        return self.doc.getvalue()