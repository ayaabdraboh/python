def dictions(names):
    names.sort()
    result = {}
    for name in names:
        if name[0] in result:
            result[name[0]].append(name)
        else:
            result[name[0]] = [name]
           
    return result