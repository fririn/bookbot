from stats import get_num_words,get_num_chars
import sys

def get_book_text(book_path:str):
    with open(book_path) as path:
        book = path.read()
    return book

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)

    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    chardict = get_num_chars(text)
    for char,count in sorted(chardict.items(), key=lambda item: item[1], reverse=True):
        print(f"{char}: {count}")
    print("============= END ===============")
    


main()
        

