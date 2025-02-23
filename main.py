import sys
from stats import num_words
from stats import sort




def main(file_path):
    # Print header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(num_words(file_path))
    print("--------- Character Count -------")
    sorted_chars = sort(file_path)
    for char_dict in sorted_chars:
        for char, count in char_dict.items():
            if char.isalpha():  # only print alphabetic characters
                print(f"{char}: {count}")
    print("============= END ===============")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
