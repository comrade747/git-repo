class Word:
    text = ''
    __grammar = ''

    def __init__(self, text):
        self.text = text

    def getPart(self):
        return 'undefined'