from data_structures.hashtable import Hashtable
import re


def hashtable_repeated_word(word):
    regex_string = re.compile('[^a-zA-Z ]')
    words_strip = regex_string.sub('', word)
    words = words_strip.lower().split()

    dict = set()
    for word in words:
        if word in dict:
            return word
        else:
            dict.add(word)

