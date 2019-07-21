class Sentence:
    content = tuple()

    def __init__(self, *args):
        self.content = args

    def show(self, words):
        result = ''
        for position in self.content:
            result += words[position].text + ' '
        return result

    def show_parts(self, words):
        result = list()
        for position in self.content:
            if position < len(words): # проверка на превышение индекса массива
                result.append(words[position].getPart())
        return set(result)

