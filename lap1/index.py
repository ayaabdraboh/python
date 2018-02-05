def index(text, letter):
    result = []
    for idx, char in enumerate(text):
        if char == letter:
            result.append(idx) 
    return result