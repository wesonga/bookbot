import sys
from stats import count_words, count_characters, sort_character_counts

def get_book_text(filepath):
    """
    Reads the contents of a file and returns it as a string.
    
    Parameters:
    filepath (str): The path to the file to be read.
    
    Returns:
    str: The contents of the file as a string.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except Exception as e:
        print(f"Error: {e}")
    return ""

def main():
    """
    Main function to read and print the contents of frankenstein.txt.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
   
    num_words = count_words(book_text)
    char_counts = count_characters(book_text)
    sorted_char_counts = sort_character_counts(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_char_counts:
        print(f"{entry['character']}: {entry['count']}")
    print("============= END ===============")

main()