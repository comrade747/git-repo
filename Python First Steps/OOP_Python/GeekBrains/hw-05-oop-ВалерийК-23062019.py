"""

1. Создайте класс Word. (Вспомните, какое зарезервированное слово используется для создания класса).
2. Добавьте свойства text (класс будет хранить слово) и part (часть речи, которой является слово.
Например, существительное, прилагательное и т.п.). Для добавления свойств воспользуйтесь методом __init__.
3. Создайте экземпляр класса Word, передав в качестве параметров любое слово и указав его часть речи.
4. Создайте класс Sentence. (по аналогии с п. 1).
5. Добавьте свойство content. (по аналогии с п. 2).
Пояснение к дальнейшему коду: content будет хранить список целых чисел, например [0, 1].
Эти номера необходимы для выбора слов из заранее созданного массива, чтобы сформировать предложение.
Пример массива:
words = [["собака", "сущ"],
         ["ела", "глагол"],
         ["колбасу", "сущ"],
         ["вечером", "наречие"]]
Если content == [0, 2], получим предложение вида «Собака колбасу».
6. Создайте из массива (можете взять приведённый выше или придумать свой) список, каждый элемент которого является
экземпляром класса Word. Примечание: список list (назовём его words) — отдельная переменная, не относящаяся к классам
Word и Sentence.
7. Добавьте в класс Sentence метод show, составляющий предложение. Метод должен перебирать числа из свойства content и
подставлять соответствующие слова, которые хранятся в свойстве text экземпляров класса Word. Данные извлекаем из списка
words, который получили на прошлом шаге. При соединении слов в предложение не забудьте добавить пробел между словами.
8. Добавьте в класс Sentence метод show_parts, отображающий, какие части речи входят в предложение.
По аналогии с п. 7 перебирайте в цикле числа из свойства content и сохраняйте результат в отдельный список.
Учтите, что части речи могут повторяться, но список не должен содержать дубликаты.

"""


class Word():
    text = 'same text'
    part = 'существительное, прилагательное и т.п.'

    def __init__(self, text, part):
        self.text = text
        self.part = part


class Sentence():
    content = []

    def __init__(self, content, words):
        self.content = content

    def show(self):
        try:
            return ' '.join([words[i].text if n !=0 else words[i].text.title() for n, i in enumerate(self.content)]) + '.'
        except Exception as err:
            return f"Какая-то ошибка: {err}"

    def show_part(self):
        try:
            return list(set([words[i].part for i in self.content]))
        except Exception as err:
            return f"Какая-то ошибка: {err}"


print()
print("Задание 1,2,3")
w = Word("птица", "существительное")
print(w.text, w.part)

print()
print("Задание 4-7")
word = [["собака", "сущ"],
        ["ела", "глагол"],
        ["колбасу", "сущ"],
        ["вечером", "наречие"]]

words = [Word(x[0], x[1]) for x in word]

s = Sentence([0, 3, 1, 2], words)
print("Наше предложение: ", s.show())

print()
print("Задание 8")
print("Части речи присутсвующие в предложении: ", ' '.join(s.show_part()))
