def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = word_count(text)
    chars = character_count(text)
    print(f"{words} words found in the document\n\n")
    for key, value in chars.items():
        if "a" <= key <= "z":
            print(f"The '{key}' character was found {value} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    count = len(text.split())
    return count

def character_count(text):
    char_count = {}
    low = text.lower()
    for char in low:
        if not char.isnumeric():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

main()