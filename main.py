def get_book_text(path):
    with open(path) as f:
       return  f.read()

def count_words(text):
    count = len(text.split())
    return count

def count_chars(text):
    chars = {}
    text_lowered = text.lower()
    for char in text_lowered:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def main():
    path_to_book = "books/frankenstein.txt"
    text = get_book_text(path_to_book)
    word_count = count_words(text)
    chars_count = count_chars(text)
    print (text,"\nTotal word count: ", word_count,"\n", chars_count)

main()