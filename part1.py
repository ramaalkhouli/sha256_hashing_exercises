import hashlib
import random
import string

# Constants for matching criteria
first = "c0ffee"

# Get student number input
student_number = input("Enter your student number: ")
last_two_digits = student_number[-2:]  # Extract last 2 digits

# Function to generate a random password
def generate_password():
    length = random.randint(8, 16)
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choices(characters, k=length))

# Function to find a valid hash
def find_valid_hash(student_number):
    while True:
        password = generate_password(random.randint(8, 16))  # Random length
        combined = password + student_number
        sha256_hash = hashlib.sha256(combined.encode()).hexdigest()

        # Check if the hash starts with "c0ffee" and has the last 2 digits of student number in the 7th and 8th position
        if sha256_hash.startswith(first) and sha256_hash[6:8] == last_two_digits:
            return password, sha256_hash

# Generate the valid hash
password, valid_hash = find_valid_hash(student_number)

# Save the password to part1.txt
with open("part1.txt", "w") as f:
    f.write(f"Password: {password}\nSHA256 Hash: {valid_hash}")

# Output the results
print("Valid hash found!")
print(f"Password: {password}")
print(f"SHA256 Hash: {valid_hash}")
print("Saved to part1.txt")
