def vowelnum(text):
    vowels = ['a', 'e', 'o', 'i', 'u', 'A', 'E', 'O', 'U', 'I']
    for char in text:
        if char in vowels:
            text = text.replace(char,'')
    return text