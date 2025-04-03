import sys
from stats import word_count, char_count, book_report

# from pathlib import Path
# BOOK: Path = Path("./books/frankenstein.txt")

# def word_count(text: str) -> int:
#     delims: str = "\n\t "
#     inside: bool = True
#     count: int = 1
#     for char in text.strip():
#         if char in delims and inside:
#             inside = False
#             count += 1
#         elif char in delims and not inside:
#             continue
#         else:
#             inside = True
#     return count
#
#
# def char_count(text: str) -> dict[str, int]:
#
#     count: dict[str, int] = {}
#
#     for char in text.lower():
#         if char not in count.keys():
#             count[char] = 1
#         else:
#             count[char] += 1
#
#     return count
#
#
# def book_report(chars: dict[str, int]) -> list[tuple[str, int]]:
#
#     _filter = lambda _filter: _filter[0].isalpha()
#     char_filtered = filter(_filter, chars.items())
#
#     _sort = lambda _sort: _sort[1]
#     char_sorted = sorted(char_filtered, key=_sort, reverse=True)
#
#     return char_sorted

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

    # with open(BOOK, "r", encoding="utf-8") as file:
    #     book: str = file.read()
    #     words: int = word_count(book)
    #     report = book_report(char_count(book))
    #
    # print("--- Begin report of books/frankenstein.txt ---")
    # print(words, "words found in the document\n")
    #
    # for char, count in report:
    #     print(f"The '{char}' character was found {count} times")
    #
    # print("--- End report ---")

if __name__ == "__main__":
    exit(main())
