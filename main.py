from stats import get_num_words

def get_book_text():
    with open("books/frankenstein.txt") as f:
        print(f.read())


def main():
    get_book_text()
    get_num_words()




if __name__ == "__main__":
    main()