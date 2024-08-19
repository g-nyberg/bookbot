def get_book_text(path):
    with open(path) as f:
       return  f.read()

def count_words(text):
    count = len(text.split())
    return count

def main():
    path_to_book = "books/frankenstein.txt"
    text = get_book_text(path_to_book)
    word_count = count_words(text)
    print (text,"\nTotal word count: ", word_count)

main()