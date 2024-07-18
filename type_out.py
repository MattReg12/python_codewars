import re

def tokenize(string):
    return re.findall(r'\[\w+\]|[\w ]+', string);

def type_out(string):
    shift = False
    caps_lock = False

    new_str = ''
    tokens = tokenize(string)
    for token in tokens:
        if (token == '[shift]'):
            shift = True
        elif (token == '[unshift]'):
            caps_lock = False
            shift = False
        elif (token == '[holdshift]'):
            caps_lock = True
        elif (shift):
            shift = False
            new_str += token.capitalize()
        elif (caps_lock):
            new_str += token.upper()
        else:
            new_str += token
    return new_str
