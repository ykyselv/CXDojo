import re


def validator(stroka: str):
    regex = r'\(.*\)'
    if stroka:
        if "(" in stroka or ")" in stroka or "[" in stroka or "]" in stroka:
            words = re.split(regex, stroka)

            words_strip = []

            for el in words:
                el_strip = el.strip()
                words_strip.append(el_strip)

            result = ''.join(words_strip)

            return result

        return stroka
    return False
