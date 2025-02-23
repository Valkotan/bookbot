#title = input("What is the title of the book: ")
#title_lower = title.lower()
#file_path = (f"../bookbot/books/{title_lower}.txt")

def num_words(file_path):
    book_text = ""
    with open(file_path) as b:
        book_text = b.read()
    count = 0
    words = book_text.split()
    for word in words:
        count +=1
    return (f"Found {count} total words")

def num_letters(file_path):
    book_text = ""
    with open(file_path) as b:
        book_text = b.read()
    char_count = {}
    chars = book_text.lower()
    for c in chars:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count


def sort_on(dict_item):
    return list(dict_item.values())[0]

def sort(file_path):
    char_count = num_letters(file_path)
    char_list = []
    for c, count in char_count.items():
        char_list.append({c: count})
    char_list.sort(key=sort_on, reverse=True)
    return char_list
