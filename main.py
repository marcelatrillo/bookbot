
import sys 
from stats import count_words, character_count, sorted_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents


def main():
    print('Usage: python3 main.py <path_to_book>')

    frankenstein = get_book_text(sys.argv[1])
    words = count_words(frankenstein)
    characters =character_count(frankenstein)
    list_letter_count = sorted_list(characters)
    print (f'''============ BOOKBOT ============
    Analyzing book found at {sys.argv[1]}
    ----------- Word Count ----------
    Found {words} total words
    --------- Character Count -------''')
    for i in range(len(list_letter_count)):
        mini_dict= list_letter_count[i]
        print (f'{mini_dict["char"]}: {mini_dict["num"]}')
    print('============= END ===============')


main()