from handlers import base
from tools import sheets
import collections

class Handler(base.Handler):
    def getGen(self, arguments):
        self.cr()
        survey = arguments["survey"][0].decode()
        with self.tag("html"):
            self.doc.asis(self.g.head("PolyCon {0} Survey".format(survey), "static/slide_min.png"))
            with self.tag("body", ("style", "background-image:url('static/xp.jpg')")):
                with self.tag("div", klass="container"):
                    with self.tag("div", ("id", "rcorners"), klass="card white darken-1"):
                        with self.tag("div", ("id", "tbardt")):
                            with self.tag("div", klass="row"):
                                with self.tag("div", klass="col s1"):
                                    self.text("")
                                with self.tag("h3", klass="xp col s7"):
                                    self.text("polycon_improvement.exe")
                                with self.tag("div", klass="col s2"):
                                    self.text("")
                                with self.tag("div", ("style","background-color:red"), ("id","optb"),klass="col s1"):
                                    with self.tag("h4", klass="xp"):
                                        with self.tag("center"):
                                            self.text("X")
                                with self.tag("div", klass="col s1"):
                                    self.text("")
                        self.doc.asis("<br>")
                        self.doc.asis("<br>")
                        self.doc.asis("<br>")
                        self.doc.asis(self.fmt.gen(survey).replace("waves-effect waves-light btn","bxp"))
                        self.doc.asis("<br>")
        return self.doc.getvalue()
    def postGen(self, arguments):
        self.cr()
        tmpl = []
        od = collections.OrderedDict(sorted(arguments.items()))
        for keys, vals in od.items():
            tmpl.append(vals[0].decode())
        self.s.addRow(self.s.ss, "Improvement", tmpl)
    def post(self):
        self.postGen(self.request.arguments)
        self.redirect("message?message=Thank you!")