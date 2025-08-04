from stats import get_word_count
from stats import get_chars_count
from stats import get_sorted_chars_list
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    args_count = len(sys.argv)
    if args_count < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]    
    content = get_book_text(filepath)
    word_count = get_word_count(content)
    #print(f"{word_count} words found in the document")
    chars_dict = get_chars_count(content)
    sorted_chars = get_sorted_chars_list(chars_dict)
    #print(chars_dict)
    print(f"{'=' * 12} BOOKBOT {'=' * 12}")
    print(f"Analyzing book found at {filepath}...")
    print(f"{'-' * 11} Word Count {'-' * 10}")
    print(f"Found {word_count} total words")
    print(f"{'-' * 9} Character Count {'-' * 7}")
    #print(sorted_chars)
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")
    


main()