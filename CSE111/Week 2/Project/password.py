# Constants defined List
LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\", "`", "~"]

def word_in_file(word, filename, case_sensitive=False):
    """Checks if a word exists in a specific file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                clean_line = line.strip()
                # If case_sensitive is False, convert both to lower for comparison
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
    #return word complexity
    return complexity

def password_strength(password, min_length=10, strong_length=16):
    """Evaluates the password and prints the specific status message."""
    
    # 1. Checks Dictionary (Case Insensitive)
    if word_in_file(password, "dictionary.txt", False):
        print("Password is a dictionary word and is not secure.")
        return 0
        
    # 2. Checks Common Passwords (Case Sensitive)
    if word_in_file(password, "passwords.txt", True):
        print("Password is a commonly used password and is not secure.")
        return 0

    # 3. Checks Minimum Length
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    # 4. Checks Strong Length
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    # 5. Complexity Score 
    complexity = word_complexity(password)
    strength = 1 + complexity
    print(f"Password complexity is {complexity}. Strength score: {strength}")
    return strength

def main():
    """Main input loop for the user."""
    print("--- Password Strength Checker ---")
    while True:
        user_input = input("\nEnter a password to test (or 'q' to quit): ")
        
        if user_input.lower() == "q":
            print("Goodbye!")
            break
            
        # Call the strength function
        result = password_strength(user_input)
        print(f"Final Strength Rating: {result}")

if __name__ == "__main__":
    main()