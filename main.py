from stats import get_num_words
from stats import get_num_characters

def get_book_text():
    with open("books/frankenstein.txt") as f:
        print(f.read())


def main():
    get_book_text()
    get_num_words()
    get_num_characters()




if __name__ == "__main__":
    main()




    