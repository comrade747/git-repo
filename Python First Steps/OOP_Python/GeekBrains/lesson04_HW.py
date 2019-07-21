from requests import get
import re


class WikiTopic(object):
    wiki = "https://ru.wikipedia.org"

    def __init__(self, topic_name: str):
        self.topic_name = topic_name.capitalize()

    def __str__(self):
        pass

    def get_topic(self):
        link = f"{self.wiki}/wiki/{self.topic_name}"
        print(f"Link is {link}")
        return get(link).text

    @staticmethod
    def get_words(html):
        pattern = re.compile("[а-яА-я\-\']{3,}")
        rus_words = pattern.findall(html)
        return rus_words

    @staticmethod
    def get_common_words(words_list):
        rate = {}
        for word in words_list:
            if word in rate:
                rate[word] += 1
            else:
                rate[word] = 1
        ret = list(rate.items())
        ret.sort(key=lambda x: -x[1])
        return ret

    def get_links(self):
        html = self.get_topic()
        pattern = re.compile(r'href="([^"#]+)"')
        links = pattern.findall(html)
        return [i for i in links if i[0:2] == "/w" and i[3:7] != "load"]

    @staticmethod
    def write_to_file(html_content):
        with open("new.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        return True

    def adjacent_pages_words(self):
        ret = []
        buf_size = 0

        def __get_adjacent_html(local_link):
            link = f"{self.wiki}{local_link}"
            return get(link).text
        links = self.get_links()
        length = len(links)
        do = 0
        print(f"We have {length} adjacent pages")
        for i in links:
            html = __get_adjacent_html(i)
            words_list = self.get_words(html)
            ret.append(self.get_common_words(words_list))
            do += 1
            buf_size += len(i) #
            print(f"Do {do} of {length}, buf size {buf_size}")
        return ret


def main():
    g = WikiTopic("Аэроватт")  # Пример короткой статьи
    adj_list = g.adjacent_pages_words()
    for i, j in enumerate(adj_list):
        print(f"Страница №{i} --> {j}j")


if __name__ == '__main__':
    main()
