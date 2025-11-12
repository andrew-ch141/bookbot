def get_word_count(book_text):
    word_count = 0
    for word in book_text.split():
        word_count += 1
    return word_count


def get_char_count(book_text):
    char_count = {}
    for char in book_text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_on(items):
    return items["num"]


def sort_char_count(unsorted_char_count):
    sorted_char = []
    for char, count in unsorted_char_count.items():
        sorted_char.append({"char": char, "num": count})
    sorted_char.sort(reverse=True, key=sort_on)
    return sorted_char
