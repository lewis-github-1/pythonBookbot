import sys

def get_num_words():
    with open(sys.argv[1]) as f:
        text = f.read()
        words = text.split()
        word_count = len(words)
        print(f"Found {word_count} total words")

def sort_char_dictionary():
    with open(sys.argv[1]) as f:
        text = f.read()
        text_lower = text.lower()
        text_lower_stripped = text_lower.strip()
        char_dict = {}
        for char in text_lower_stripped:
            if char.isalpha():
                if char in char_dict:
                    char_dict[char] += 1
                else:
                    char_dict[char] = 1
        char_dict_list = []
        for char, count in char_dict.items():            
            char_dict_list.append({"char": char, "num": count})
        
        char_dict_list.sort(key=sort_on, reverse=True)
        return char_dict_list

def sort_on(item):
    return item["num"]