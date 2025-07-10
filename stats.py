def get_num_words():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        words = text.split()
        word_count = len(words)
        print(word_count, "words found in the document")

def get_num_characters():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        text_lower = text.lower()
        text_lower_stripped = text_lower.strip()
        char_dict = {}
        for char in text_lower_stripped:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        print(char_dict)




        