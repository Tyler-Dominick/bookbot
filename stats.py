def count_words(text):
    num_words = len(text.split())
    return num_words

def count_chars(text):
    lowercase = text.lower()
    chars = {}
    for char in lowercase:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(items):
    return items["num"]

def sort_chars(dict):
    list_of_dicts = []
    for char in dict:
        list_of_dicts.append({"char" : f"{char}", "num" : dict[char]})

    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts




