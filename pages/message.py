from handlers import base

class Handler(base.Handler):
    def getGen(self, arguments):
        self.cr()
        with self.tag("html"):
            self.doc.asis(self.g.head("PolyCon", "<img src='{0}/logo_300.png'/>".format(self.l)))
            with self.tag("body"):
                with self.tag("div", klass="container"):
                    with self.tag("div", klass="row"):
                        with self.tag("center"):
                            self.doc.asis("<img src='{0}/logo_300.png'/>".format(self.l))
                            with self.tag("h3"):
                                self.text(arguments["message"][0].decode())
        return self.doc.getvalue()