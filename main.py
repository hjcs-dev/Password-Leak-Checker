import requests
import hashlib

# Function to check password against Have I Been Pwned
def check_hibp_password(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        hashes = (line.split(':') for line in response.text.splitlines())
        for h, count in hashes:
            if h == suffix:
                return f"Password found {count} times in Have I Been Pwned database."
        return "Password not found in Have I Been Pwned database."
    except requests.RequestException as e:
        return f"Error checking Have I Been Pwned: {str(e)}"

# Function to check email against Have I Been Pwned


def main():
    # Choose the type of check
    choice = input("Choose the type of check (password) : ")
    
    if choice == 'password':
        password = input("Enter the password to check: ")
        result = check_hibp_password(password)
        print(result)
        
        
    else:
        print("Invalid choice. Please enter 'password'")

if __name__ == "__main__":
    main()
