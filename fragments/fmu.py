import os
class form:
    def __init__(self, yto, color="black"):
        self.yat = yto
    def gen(self, formn):
        doc, tag, text = self.yat
        curp = 1
        with tag("form", ("id", formn), ("method", "POST")):
            with open("fragments/fmu/{0}.fmf".format(formn), "r") as formf:
                with tag("div", klass="container"):
                    with tag("div", klass="row"):
                        doc.asis("<div id='page{0}'>".format(str(curp)))
                        for line in formf:
                            line = line.replace("\n", "")
                            if line[0] == "#":
                                hn = line.count("#")
                                line = line.replace("#","")
                                with tag("h"+str(hn)):
                                    doc.asis(line)
                            elif line[:2] == "rb":
                                line = line[3:]
                                lines = line.split(",")
                                group = lines[0]
                                lines = lines[1:]
                                doc.asis("<input type='hidden' id='{0}' name='{0}'/>".format(group))
                                for line in lines:
                                    with tag("p"):
                                        doc.asis("""<input type='radio' id='{1}' onclick='document.getElementById("{0}").value = "{1}";'/>""".format(group, line))
                                        with tag("label", ("for", line)):
                                            doc.asis(line)
                            elif line[:2] == "rf":
                                lines = line[3:].split(",")
                                rang = lines[0]
                                with tag("div", klass="row"):
                                    with tag("div", klass="col s1"):
                                        text(lines[1])
                                    with tag("div", klass="col s9"):
                                        with tag("p", klass="range-field"):
                                            doc.asis("<input type='range' id='come_back' name='come_back' min='0' max='{0}'/>".format(str(rang)))
                                    with tag("div", klass="col s1"):
                                        text(lines[2])
                            elif line[0] == "c":
                                line = line[3:]
                                lines = line.split(",")
                                group = lines[0]
                                lines = lines[1:]
                                doc.asis("<input type='hidden' id='{0}' name='{0}'/>".format(group))
                                for line in lines:
                                    with tag("p"):
                                        doc.asis("""<input type='checkbox' id='{0}' onclick='document.getElementById("{1}").value += "{0},";'/>""".format(line, group))
                                        with tag("label", ("for", line)):
                                            doc.asis(line)
                            elif line[1] == "l":
                                lt = line[:2]
                                line = line[3:]
                                lines = line.split(",")
                                with tag(lt):
                                    for line in lines:
                                        with tag("li"):
                                            doc.asis(line)
                            elif line[0] == "t":
                                line = line[2:]
                                lines = line.split(",")
                                for line in lines:
                                    with tag("div", klass="input-field col s12"):
                                        doc.asis("<input id='{0}' name='{0}' type='text' class='validate'>".format(line))
                                        with tag("label", ("for", line)):
                                            doc.asis(line)
                            elif line == "npb":
                                if curp > 1:
                                    with tag("div", ("onClick", "previous('{0}', '{1}')".format(str(curp - 1), str(curp))), klass="waves-effect waves-light btn"):
                                        text("Previous")
                                with tag("div", ("onClick", "next('{0}', '{1}')".format(str(curp), str(curp + 1))), klass="waves-effect waves-light btn"):
                                    text("Next")
                                doc.asis("</div>")
                                curp += 1
                                doc.asis("<div id='page{0}' style='display:none'>".format(str(curp)))
                            elif line == "sub":
                                with tag("button", ("type", "submit"), ("name", "action"), ("onClick","next('{0}','{1}')".format(str(curp), str(curp+1))), klass="btn waves-effect waves-light"):
                                    text("Submit")
                                doc.asis("</div>")
                                doc.asis("<div id='page{0}' style='display:none'>".format(str(curp+1)))
                                with tag("div", klass="spinner"):
                                    for it in range(1,6):
                                        with tag("div", klass="rect"+str(it)):
                                            doc.asis("")
                            else:
                                print(line)
                        doc.asis("</div>")
        return doc.getvalue()