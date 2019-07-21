import Lib.Word as wd

class Noun(wd.Word):
   
    def __init__(self, text):
        wd.Word.__init__(self, text)
        wd.Word.__grammar  = 'сущ'

    def getPart(self):
        return 'существительное'