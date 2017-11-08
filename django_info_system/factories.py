from django.template.defaultfilters import slugify

import random

user_share_dict_words = None

def _random_words():
    global user_share_dict_words
    if not user_share_dict_words:
        word_file = "/usr/share/dict/words"
        user_share_dict_words = open(word_file).read().splitlines()

def get_random_word():
    return random.choice(_random_words())

