def count_words(text):
    """
    Counts the number of words in a given text.
    
    Parameters:
    text (str): The text to analyze.
    
    Returns:
    int: The number of words in the text.
    """
    return len(text.split())

def count_characters(text):
    """
    Counts the number of times each character appears in the text.
    Converts all characters to lowercase to avoid duplicates.
    
    Parameters:
    text (str): The text to analyze.
    
    Returns:
    dict: A dictionary with characters as keys and their counts as values.
    """
    char_counts = {}
    for char in text.lower():
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_character_counts(char_counts):
    """
    Sorts the character counts dictionary from greatest to least by count.
    Only includes alphabetical characters.
    
    Parameters:
    char_counts (dict): Dictionary of character frequencies.
    
    Returns:
    list: A sorted list of dictionaries with character and count pairs.
    """
    sorted_chars = [
        {"character": char, "count": count} 
        for char, count in char_counts.items() if char.isalpha()
    ]
    sorted_chars.sort(key=lambda x: x["count"], reverse=True)
    return sorted_chars