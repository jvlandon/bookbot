from stats import get_word_count
from stats import symbols
from stats import list_out
import sys

if len(sys.argv) != 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    count = get_word_count(text)
    letters = symbols(text)
    out = list_out(letters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for entry in out:
        ch = entry["char"]
        if ch.isalpha():
            print(f"{ch}: {entry['num']}")
    print("============= END ===============")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

main()