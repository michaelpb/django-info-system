from django.template.defaultfilters import slugify

import random

user_share_dict_words = None

names = list(filter(bool, '''
Alyse Angelo  
Kellie Kilcrease  
Jacinto Jamal  
Ty Tetzlaff  
Angel Abernethy  
Nicole Nova  
Theo Tinner  
Rosalie Rase  
Moira Manhart  
Kimberlee Kovac  
Adelle Atkin  
Frederic Finamore  
Delorse Dotson  
Tyron Tarbell  
Jeanetta Jeansonne  
Lenard Leddy  
Cecille Cesario  
An Alvear  
Agripina Alberico  
Vance Valenti  
Arden Abraham  
Ossie Ofarrell  
Jennefer Juarez  
Estrella Esterline  
Piedad Pinzon  
Wayne Witmer  
Mariela Mandell  
Chi Clogston  
Lovella Laughter  
Jules Jonas  
Donnie Debellis  
Renetta Raya  
Bobbye Brutus  
Shawnna Sayegh  
Venice Vieyra  
Willis Wooten  
Bessie Bainter  
Johnie Jerome  
Anjelica Alaniz  
Martine Mac  
Lakiesha Lacayo  
Corliss Callaghan  
Shaquana Sheeley  
Heath Heredia  
Verla Villafane  
Shaunte Sutphin  
Susann Stagg  
Joi Jasso  
Evelyne Eyler  
Diana Doctor  
'''.splitlines()))


def _random_words():
    global user_share_dict_words
    if not user_share_dict_words:
        word_file = "/usr/share/dict/words"
        user_share_dict_words = open(word_file).read().splitlines()
    return user_share_dict_words

def get_random_sentence():
    s = get_random_word().capitalize()
    for i in range(random.randint(3, 20)):
        s += ' %s' % get_random_word()
    return s + '.'


def get_random_word():
    return random.choice(_random_words())

def get_random_name():
    return random.choice(names)

