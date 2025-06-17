def get_num_words(text):
    return len(text.split())

def chars_num(text):
    result = {}
    for char in text.lower():
        # result[char] = result.get(char,0) + 1
        # result[char] = 1 if char not in result else result[char] + 1
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

def sort_on(dict):
    return dict["num"]

def create_report(dict):
    entries = []
    for key in dict:
        entries.append({"char": key, "num": dict[key]})
    entries.sort(reverse=True, key=sort_on)
    return entries

