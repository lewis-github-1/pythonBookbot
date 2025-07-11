from stats import get_num_words
from stats import sort_char_dictionary

import sys

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("========== BOOKBOT ==========")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("---------- Word count ----------")
    get_num_words()
    
    print("---------- Character Count ----------")
    dict_list = sort_char_dictionary()
    for char_dict in dict_list:
        char = char_dict["char"]
        count = char_dict["num"]

        if char.isalpha():
            print(f"{char}: {count}")




if __name__ == "__main__":
    main()

