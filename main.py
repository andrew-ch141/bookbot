import sys

from stats import get_char_count, get_word_count, sort_char_count


def get_book_text(f_path):
    with open(f_path) as f:
        contents = f.read()
    return contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    num_words = get_word_count(get_book_text(f"{book_path}"))
    sorted_char_count = sort_char_count(get_char_count(get_book_text(f"{book_path}")))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_char_count:
        ch = item["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {item['num']}")
    print("============= END ===============")


main()
