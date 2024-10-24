with open("/Users/ericbeauchner/workspace/github.com/ebeauchner/bookbot/books/frankenstein.txt") as f:
    file_contents = f.read()
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
print(f"{words_list_length} words found in the document\n")
for item in ordered_count:
    print(f"The '{item}' character was found {letter_count[item]} times")
print("--- End report ---")