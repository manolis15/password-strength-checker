import string
import math
import os
#this is to define the greek letters without intonation
GREEK_LOWER = "αβγδεζηθικλμνξοπρστυφχψω"
GREEK_UPPER = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
ALLOWED_CHARS = (
    string.ascii_letters+    # a-z, A-Z
    string.digits+           # 0-9
    string.punctuation+      # !@#$%^&*...
    GREEK_LOWER+             # greek
    GREEK_UPPER             # Capital greek
)
def load_common_passwords(filename="common_passwords.txt"):
    #this is to find the common_passwords file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        print(f"\n[WARNING] file not found at: {file_path}")
        print("Ensure that the file is named accordingly.")
        return set()
def calculate_time_to_crack(password):
    pool_size = 0
    #checking for english letters(upper and lower) in the password
    if any(char in string.ascii_lowercase for char in password): pool_size += 26
    if any(char in string.ascii_uppercase for char in password): pool_size += 26
    #checking for greek letters(upper and lower) in the password
    if any(char in GREEK_LOWER for char in password): pool_size += 24
    if any(char in GREEK_UPPER for char in password): pool_size += 24
    #checking for digits and punctuations in the password
    if any(char in string.digits for char in password): pool_size += 10
    if any(char in string.punctuation for char in password): pool_size += 32
    #calculation of all possible combinations
    combinations = pool_size ** len(password)
    #hypothetical estimate of how many passwords can be guessed in a second
    guesses_per_second = 10000000000 
    seconds = combinations / guesses_per_second
    return seconds
def format_time(seconds):
    if seconds < 60: return "a few seconds"
    if seconds < 3600: return f"{seconds/60:.1f} minutes"
    if seconds < 86400: return f"{seconds/3600:.1f} hours"
    if seconds < 31536000: return f"{seconds/86400:.1f} days"
    if seconds < 3153600000: return f"{seconds/31536000:.1f} years"
    return "Centuries!"
def check_password_strength(password, common_passwords):
    for char in password:
        if char not in ALLOWED_CHARS:
            print("This character is not supported sorry!")
            print("\nΕxiting...")
            return -1,'',0
    if password in common_passwords:
        return 1, "Too weak(found in the common passwords txt)", "instantenous"
    score = 0
    length = len(password)
    #grade based on length
    if length < 5:
        return 2, "Too small", "instantenous"
    elif length >= 8: score += 2
    elif length >= 12: score += 3
    elif length >= 16: score += 4
    #check lower,upper,digit,punctuation
    has_lower = any(c in string.ascii_lowercase or c in GREEK_LOWER for c in password)
    has_upper = any(c in string.ascii_uppercase or c in GREEK_UPPER for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    #check if it has greek or english
    has_greek = any(c in GREEK_LOWER or c in GREEK_UPPER for c in password)
    has_english = any(c in string.ascii_letters for c in password)
    #grade based on the checks
    if has_upper: score += 1
    if has_lower: score += 1
    if has_digit: score += 1
    if has_special: score += 2
    #Containing a variety of combinations
    if has_upper and has_lower and has_digit and has_special:
        score += 1   
    #being mixed language
    if has_greek and has_english:
        score += 2
    if score > 10: score = 10
    #calling the functions
    seconds_to_crack = calculate_time_to_crack(password)
    time_display = format_time(seconds_to_crack)
    return score, "OK" if score > 5 else "Weak", time_display
#main
if __name__ == "__main__":
    print("--- Password Strength Checker  ---")
    common_pass = load_common_passwords()
    
    while True:
        user_pass = input("\nGive a password! (or 'q' to exit): ")
        if user_pass.lower() == 'q':
            break
        final_score, message, time_est = check_password_strength(user_pass, common_pass)
        if final_score!=-1:
            print(f"Score: {final_score}/10")
            if final_score < 10 and message != "OK":
                print(f"Comment: {message}")
            print(f"Estimated time of breach: {time_est}")