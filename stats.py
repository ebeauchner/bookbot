def get_num_words(book_text):
    book_words = book_text.split()
    num_words = len(book_words)
    return (num_words)

def character_count(book_text):
    lowercase_text = book_text.lower()
    character_dict = {}
    for character in lowercase_text:
        if character not in character_dict:
            character_dict[character] = 0
        character_dict[character] += 1
    return character_dict

def sorted_char_dict(character_dict):
    character_list = []
    for character in character_dict:
        character_list.append((character, character_dict[character]))
    character_list.sort(key=lambda x: x[1], reverse=True)
    return character_list
    