def main():
    num_words = 0
    character_counter = {}

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = get_number_of_words(file_contents)
        character_counter = get_character_count(file_contents)
    
    print(f"--- Begin report of books/frankenstein.txt ---")

    print(f"{num_words} words found in the document\n")

    for character in character_counter:
        print(f"The '{character}' character was found {character_counter[character]} times")

    print("--- End Report ---")
    

def get_number_of_words(bookText):
    counter = 0
    text_as_list = bookText.split()
    for w in text_as_list:
        counter += 1
    return counter

def get_character_count(bookText):
    character_map = {}
    for c in bookText:
        c = c.lower()
        if c in character_map:
            character_map[c] += 1
        else:
            character_map[c] = 1
    return character_map

main()
