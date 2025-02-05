import hashlib
import itertools
import string

# Given values
password = "comp2108"
target_hash = "9f02b0fd48e9211a5a33ae3321b942896e4ebb0cb267fdfff53fa58cf8c56f24"

# Characters allowed in the salt (lowercase ASCII)
characters = string.ascii_lowercase

# Function to brute-force the salt
def find_salt():
    for salt in itertools.product(characters, repeat=8):  # Generate all 8-char lowercase salts
        salt = ''.join(salt)
        combined = password + salt
        sha256_hash = hashlib.sha256(combined.encode()).hexdigest()

        if sha256_hash == target_hash:
            return salt  # Found the correct salt

# Start brute-force search
salt = find_salt()

# Save the salt to part2.txt
with open("part2.txt", "w") as f:
    f.write(f"Salt: {salt}\n")

# Output the result
if salt:
    print(f"Salt found: {salt}")
    print("Saved to part2.txt")
else:
    print("No valid salt found.")
