from yattag import Doc

class general:
    def __init__(self):
        self.doc, self.tag, self.text = Doc().tagtext()
    def cr(self):
        self.doc, self.tag, self.text = Doc().tagtext()
    def head(self, title, icon=None):
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