import os
import base64
import string
import random

# Allowed characters: lowercase ASCII + digits
allowed_chars = string.ascii_lowercase + string.digits

# Function to generate a random salt of length 16
def generate_salt():
    while True:
        # Generate 12 random bytes, then encode as base64, and take 16 characters
        raw_salt = base64.b64encode(os.urandom(12)).decode('utf-8')
        salt = ''.join(c for c in raw_salt if c in allowed_chars)[:16]

        if len(salt) == 16:
            return salt

# Generate 16 distinct salts
unique_salts = set()
while len(unique_salts) < 16:
    unique_salts.add(generate_salt())

# Convert to a sorted list for better readability
salts_list = sorted(unique_salts)

# Save the salts to part3.txt
with open("part3.txt", "w") as f:
    for salt in salts_list:
        f.write(f"{salt}\n")

# Output the results
print("Generated 16 unique salts:")
for salt in salts_list:
    print(salt)

print("Salts saved to part3.txt")
