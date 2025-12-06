from stats import count_words, count_chars, sort_chars
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) >= 2:

        path = sys.argv[1]
        text_string = get_book_text(path)
        print(f"Analyzing book found at {path}...")
        num_words = count_words(text_string)
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        # print(count_chars(get_book_text("books/frankenstein.txt")))
        sorted = sort_chars(count_chars(text_string))
        print("--------- Character Count -------")
        for dict in sorted:
            if dict["char"].isalpha():
                    print(dict["char"] + ":", dict["num"])
        
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()
