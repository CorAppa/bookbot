
import sys

from stats import get_num_words 
from stats import get_num_chars
from stats import get_sorted_list



def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    
    file_to_read = get_book_text(path)
    num_of_words = get_num_words(file_to_read)
    num_chars = get_num_chars(file_to_read)
    sorted_list = get_sorted_list(num_chars)
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + str(path) + "...")
    print("----------- Word Count ----------")
    print("Found " + str(num_of_words) + " total words")
    print("--------- Character Count -------")

    for li in sorted_list:
        print(li["char"] + ": " + str(li["num"]))
    
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

if __name__ == "__main__":
    main()