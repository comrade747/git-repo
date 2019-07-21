import Lib.Word as wd

class Adverb(wd.Word):

    def __init__(self, text):
        wd.Word.__init__(self, text)
        wd.Word.__grammar = 'нар'

    def getPart(self):
        return 'наречие'