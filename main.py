# Function opens file to read
def get_book_text(path):
    with open(path) as f:
       return  f.read()

# Function counts words input string and returns count int
def count_words(text):
    count = len(text.split())
    return count

# Function counts Alpha character of a string and returns a dictionary
def count_chars(text):
    chars = {}
    text_lowered = text.lower()
    for char in text_lowered:
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
        else:
            continue
    return chars

# converts the char dictionary to a list of dictionaries for each char that is sorted my highest occurence and returns list of char dictionaries
def convert_char_dict_list_of_dicts(char_dict):
    dicts_list = []
    for ch in char_dict:
        dicts_list.append({"char": ch, "count" : char_dict[ch]})
    dicts_list.sort(key = sort_on, reverse = True)
    return dicts_list

# Function used for .sort() to sort on count value
def sort_on(dict):
    return dict["count"]

# Main generates and prints a report of the book in the console
def main():
    path_to_book = "books/frankenstein.txt"
    text = get_book_text(path_to_book)
    word_count = count_words(text)
    chars_count_dict = count_chars(text)
    char_dicts_list =  convert_char_dict_list_of_dicts(chars_count_dict)
    print (f"Report on {path_to_book}")
    print(f"{word_count} words found in text")
    for item in char_dicts_list:
        print(f"Char : '{item['char']}' appeared '{item['count']}' times")

main()