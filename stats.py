def get_num_words():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        words = text.split()
        word_count = len(words)
        print(word_count, "words found in the document")

