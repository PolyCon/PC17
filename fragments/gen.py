from yattag import Doc

class general:
    def __init__(self):
        self.doc, self.tag, self.text = Doc().tagtext()
    def cr(self):
        self.doc, self.tag, self.text = Doc().tagtext()
    def head(self, title, icon=None):
        self.cr()
        with self.tag("head"):
            with self.tag("title"):
                self.text(title)
            if icon != None:
                self.doc.asis("<link rel='icon' type='image/png' href='{0}'/>".format(icon))
            with open("estatic/css.txt", "r") as css:
                cssl = css.read().split("\n")
                for stylesheet in cssl:
                    self.doc.asis("<link rel='stylesheet' href='{0}'>".format(stylesheet))
            with open("estatic/js.txt", "r") as js:
                jsl = js.read().split("\n")
                for script in jsl:
                    self.doc.asis("<script src='{0}'></script>".format(script))
        tmpf = self.doc.getvalue()
        self.cr()
        return tmpf
    def rbg(self, vals, name):
        self.cr()
        for val in vals:
            with self.tag("p"):
                if len(val) == 2:
                    self.doc.asis("<input name='{0}' type='radio' id='{1}' />".format(name, val[1]))
                elif len(val) == 3:
                    self.doc.asis("<input name='{0}' type='radio' id='{1}' onclick='{2}'/>".format(name, val[1], val[2]))
                with self.tag("label", ("for", val[1])):
                    self.doc.asis(val[0])
        tmpf = self.doc.getvalue()
        self.cr()
        return tmpf