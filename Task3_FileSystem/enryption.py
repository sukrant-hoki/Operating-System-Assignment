SHIFT = 3


def encrypt(text):
    result = ""

    for char in text:
        result += chr(ord(char) + SHIFT)

    return result


def decrypt(text):
    result = ""

    for char in text:
        result += chr(ord(char) - SHIFT)

    return result