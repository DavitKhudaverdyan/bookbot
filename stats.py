 
def get_word_count(text):
    words = text.split()
    return len(words)

def get_chars_count(text):
    chars = {}
    for char in text:
        lower_char = char.lower()
        if lower_char not in chars:
            chars[lower_char] = 0
        chars[lower_char] += 1
    return chars

def get_sorted_chars_list(chars_dict):
    result = []
    for char, count in chars_dict.items():
        result.append({"char": char, "count": count})

    result.sort(key = lambda item: item["count"], reverse=True)

    return result

