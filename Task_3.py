# Так как в задании не сказано, необходимо ли считать закрывающие теги, то и они подсчитаны

import requests


def tags_count(content_string: str) -> tuple:
    counter_tags = counter_attrtags = 0
    flag_inside_tag = False

    for char in content_string:
        if char == '>':
            flag_inside_tag = False
    # Отслеживаем нахождение внутри тега
        if char == '<':
            flag_inside_tag = True
            counter_tags += 1
            continue
    # Если после тега будет пробел, то тег содержит аттрибуты
        if flag_inside_tag:
            if char == ' ':
                counter_attrtags += 1
                flag_inside_tag = False

    return counter_tags, counter_attrtags


if __name__ == '__main__':
    # Добавляем в гет запрос хедер User-Agent, так как без него сайт не дает смотреть код страницы
    response = requests.get('https://greenatom.ru/', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'})
    tags_count, tags_with_attribute_count = tags_count(response.text)
    print(f"Всего HTML-тегов: {tags_count}")
    print(f"Всего HTML-тегов с аттрибутами: {tags_with_attribute_count}")
