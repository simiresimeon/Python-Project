"""Author: Simire Simeon Obamiegie"""
"""Project: Password strength checker"""
"""Course: CSE111: Programming with Functions"""



# Constants for character types
LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\", "`", "~"]

def word_in_file(word, filename, case_sensitive=False):
    """Checks if a word exists in a specific file with optional case sensitivity."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                clean_line = line.strip()
                if not case_sensitive:
                    if clean_line.lower() == word.lower():
                        return True
                else:
                    if clean_line == word:
                        return True
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    return False

def word_has_character(word, character_list):
    """Returns True if any character in 'word' is in 'character_list'."""
    for char in word:
        if char in character_list:
            return True
    return False

def word_complexity(word):
    """Calculates complexity score (0-4) based on character types."""
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

def password_strength(password, min_length=10, strong_length=16):
    # 1. Dictionary Check
    if word_in_file(password, "wordlist.txt", False):
        message = "Password is a dictionary word and is not secure."
        print(message)
        return 0
        
    # 2. Top Password Check
    if word_in_file(password, "toppasswords.txt", True):
        message = "Password is a commonly used password and is not secure."
        print(message)
        return 0

    # 3. Too Short Check
    if len(password) < min_length:
        message = "Password is too short and is not secure."
        print(message)
        return 1

    # 4. Long Password Check
    if len(password) >= strong_length:
        message = "Password is long, length trumps complexity this is a good password"
        print(message)
        return 5

    # 5. Complexity Calculation 
    complexity = word_complexity(password)
    strength = 1 + complexity
    return strength

def main():
    print("--- Password Strength Checker ---")
    while True:
        user_input = input("\nEnter a password to test (or 'q' to quit): ")
        
        if user_input.lower() == "q":
            break
            
        strength_score = password_strength(user_input)
        # Reports the numeric strength as shown in your test guide
        print(f"Strength: {strength_score}")

if __name__ == "__main__":
    main()