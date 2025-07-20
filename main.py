import sys

from stats import get_num_words, character_count, sorted_char_dict

def get_book_text(book_location):
    with open(book_location) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    book_location = sys.argv[1]
    book_text = get_book_text(book_location)
    char_dict = character_count(book_text)
    sorted_characters = sorted_char_dict(char_dict)
    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {book_location}\n")
    print("----------- Word Count ----------\n")
    print(f"Found {get_num_words(book_text)} total words\n")
    print("----------- Character Count -----------\n")
    for character, count in sorted_characters:
        if character.isalpha():
            print(f"{character}: {count}")
    print("\n============= END ===============")
    return None

main()