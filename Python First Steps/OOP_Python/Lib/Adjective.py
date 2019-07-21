import Lib.Word as wd

class Adjective(wd.Word):

    def __init__(self, text):
        wd.Word.__init__(self, text)
        wd.Word.__grammar = 'прил'

    def getPart(self):
        return 'прилагательное'