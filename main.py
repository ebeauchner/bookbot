import sys
from stats import get_word_count

if len(sys.argv) != 2:
    print("Usage: python main.py <path_to_book>")
    sys.exit(0)

with open(sys.argv[1]) as f:
    file_contents = f.read()

num_words = get_word_count(file_contents)
words_list = file_contents.split()
words_list_length = len(words_list)
file_contents_lower = file_contents.lower()
letter_count = {}

#lowercase ascii: 97-122
for character in file_contents_lower:
    if character in letter_count:
        letter_count[character] += 1
    elif ord(character) >= 97 and ord(character) <= 122:
        letter_count[character] = 1
ordered_count = dict(sorted(letter_count.items(), reverse=True, key=lambda item: item[1]))


print("--- Begin report of books/frankenstein.txt ---")
print(f"{num_words} words found in the document\n")
for item in ordered_count:
    print(f"{item}: {letter_count[item]}")
print("--- End report ---")