import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_special=True):
    # Define the character sets
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    number_chars = string.digits if use_numbers else ''
    special_chars = string.punctuation if use_special else ''

    # Combine all the character sets
    all_chars = lowercase_chars + uppercase_chars + number_chars + special_chars

    # Check if there are any characters to choose from
    if not all_chars:
        raise ValueError("At least one character type must be selected")

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    try:
        # Prompt the user for the length of the password
        length = int(input("Enter the desired length of the password: "))
        
        # Validate the length
        if length <= 0:
            raise ValueError("Password length must be a positive integer")
        
        # Prompt the user for complexity options
        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

        # Generate the password
        password = generate_password(length, use_uppercase, use_numbers, use_special)
        
        # Display the generated password
        print(f"Generated Password: {password}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    
    main()
