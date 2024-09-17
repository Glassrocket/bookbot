# declaring variavles for the path of the book and the word count and printing the result
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_dict = get_char_dict(text)
    list_dict = convert_to_list(char_dict)
    print(f"--- Begin report of {book_path} ---\n{word_count} words found in the document\n")
    get_results(list_dict)
    print("--- End report ---")

# Function to count the number of words in the text
def get_word_count(text):
    words = text.split()
    return len(words)

# Function to get the character dictionary from the text and convert it to lowercase
def get_char_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

# Function to get the book text from the file
def get_book_text(path):
    with open(path) as f:
        return f.read()

# Function to convert the dictionary to a list and sort it in descending order filtering out all the non-alphabetic characters
def convert_to_list(dict):
    dict_list = []
    for key, value in dict.items():
        if key.isalpha(): # Filter out non-alphabetic characters
            dict_list.append({"char": key, "count": value})
    dict_list.sort(reverse=True, key=lambda x: x["count"]) # Sort the list in descending order
    return dict_list

# Function to print the results for each character of new list
def get_results(dict):
    for item in dict:
       print(f"The '{item['char']}' characters was found '{item['count']}' times")
        
main()