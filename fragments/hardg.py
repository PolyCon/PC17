import os
class grabber:
    def __init__(self):
        hdict = {}
        for folder in os.listdir("fragments/hard"):
            hdict[folder] = {}
            for hpage in os.listdir("fragments/hard/{0}".format(folder)):
                with open("fragments/hard/{0}/{1}".format(folder, hpage), "r") as tmpp:
                    tmpn = hpage.split(".")[0]
                    hdict[folder][tmpn] = tmpp.read()
        self.hdict = hdict