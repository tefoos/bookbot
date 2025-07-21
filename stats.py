from typing import TypedDict

class CharCount(TypedDict):
    char: str
    count: int


def get_words_count(book: str) -> int:
    words = book.split()
    return len(words)

def word_count_formatted(char_dict: dict[str, int]) -> CharCount:
     formatted_list: list[CharCount] = []
     for char in char_dict:
        formatted_list.append({'char': char, 'count': char_dict[char]})
     formatted_list.sort(reverse=True, key=sort_on)
     return formatted_list


def get_chars_count(book: str) -> dict[str, int]:
    char_dict = dict()
    for char in book.lower():
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    return char_dict

def sort_on(items):
    return items["count"]
