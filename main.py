from stats import get_words_count, get_chars_count, word_count_formatted, CharCount
import sys

def get_book_text(path: str) -> str:
    with open(path) as f:
        file_content = f.read()
    return file_content

def print_char_count(formatted_list: CharCount):
    for char_count in formatted_list:
        char = char_count['char']
        if (char.isalpha()):
            count = char_count['count']
            print(f'{char}: {count}')

def print_report(formatted_list: CharCount, num_words: int):
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    print_char_count(formatted_list)
    print('============= END ===============')

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    content = get_book_text(sys.argv[1])
    char_count = get_chars_count(content)
    formatted_list = word_count_formatted(char_count)
    num_words = get_words_count(content)
    print_report(formatted_list, num_words)


main()
