# В связи с тем что я не понял задание от слова совсем.
# за основу я взял просто ссылки которые есть на странице  ru.wikipedia.org/wiki/%D0%94%D0%B5%D1%80%D0%B5%D0%B2%D0%BE
# с помощью регулярки выбрал те ссылки которые имеют внутри себя wikipedia.org, и их отправил в
# visualize_common_words.
# Из-за кодировки не будут отображаться стрницы на иностранных языках.

import re
from requests import get

def get_link(topic):
    link = topic.capitalize()
    return link

def get_topic_page(topic):
    link = get_link(topic)
    html_content = get(link).text
    return html_content


def get_topic_words(topic):
    html_content = get_topic_page(topic)
    words = re.findall("[а-яА-Я\-\']{3,}", html_content)
    return words

def get_common_words(topic):
    words_list = get_topic_words(topic)
    rate = {}
    for word in words_list:
        if word in rate:
            rate[word] += 1
        else:
            rate[word] = 1
    rate_list = list(rate.items())
    rate_list.sort(key = lambda x: -x[1])
    return rate_list

def visualize_common_words(topic):
    words = get_common_words(topic)
    for w in words:
        print(w[0])


def get_arr_links(topic):
    site = get_topic_page(topic)
    link = re.findall(r'(https?://\w{2}\.wiki\w+\.\w+/wiki/\S+[_\S\w]+)[^\S]', site)
    for link_list in link:
        print(link_list)
        print(visualize_common_words(link_list))


get_arr_links('https://ru.wikipedia.org/wiki/%D0%94%D0%B5%D1%80%D0%B5%D0%B2%D0%BE')
