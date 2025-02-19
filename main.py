
path_to_file = "books/frankenstein.txt"

def main(path_to_file):
    with open(path_to_file) as f:
        book_content = f.read()
        return book_content

def count_words(path_to_file):
    book = main(path_to_file)   
    split_book = book.split()
    count = len(split_book)
    
    return count

def character_count(path_to_file):
    book = main(path_to_file)
    lowered_case_book = book.lower()
    character_obj = {}

    for char in lowered_case_book:
        if char in character_obj:
            character_obj[char] +=  1
        else:
            character_obj[char] = 1

    return character_obj


characters = character_count(path_to_file)
words = count_words(path_to_file)
del characters["#"]
del characters[" "]
del characters["."]

updated_characters = characters

def generate_report(path, updated_characters, total_words):
    print(f"--- Begin report of {path} ---")
    print(f"{total_words} words found in the document\n")

    for char in updated_characters:
        print(f"The '{char}' character was found {updated_characters[char]} times")

    print(f"--- End report ---")

generate_report(path_to_file, characters, words)
