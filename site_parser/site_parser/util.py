from datetime import datetime
from w3lib.html import replace_entities, remove_tags


def str_to_date(string):
    date_obj = datetime.strptime(string, "%Y-%m-%d")
    return date_obj.date()


def clean_title(title):
    title = replace_entities(title, keep=(), remove_illegal=True, encoding="utf-8").replace(' ', ' ')
    return title


def clean_text(text):
    text = remove_tags(text, encoding='utf-8')
    text = replace_entities(text, keep=(), remove_illegal=True, encoding="utf-8").replace(' ', ' ')
    return text
