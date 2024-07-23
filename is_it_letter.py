import re

def is_it_letter(s):
    return True if re.fullmatch(r'[a-z]', s, re.IGNORECASE) else False
