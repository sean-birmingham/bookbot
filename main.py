import sys
from stats import get_num_words, count_chars, sort_chars

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    text = get_book_text(file_path)

    word_count = get_num_words(text)
    print(f"Found {word_count} total words")

    char_counts = count_chars(text)
    sorted_char_list = sort_chars(char_counts)

    for entry in sorted_char_list:
        print(f"{entry['char']}: {entry['num']}")


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()