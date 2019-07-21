import Lib.Word as wd

class Verb(wd.Word):

    def __init__(self, text):
        wd.Word.__init__(self, text)
        wd.Word.__grammar = 'гл'

    def getPart(self):
        return 'глагол'