import sys
from stats import word_count, char_count, book_report

def get_book_test(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        book: str = file.read()
        return book


def main():

    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = args[1]

    book: str = get_book_test(path)
    num_words: int = word_count(book)
    count_chars: dict[str, int] = char_count(book)
    report = book_report(count_chars)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in report:
        print(f"{char}: {count}")
    print("============= END ===============")

if __name__ == "__main__":
    exit(main())
