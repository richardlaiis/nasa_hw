import hashlib

# The target SHA-256 hash
target_hash = "40c3d69c8a012e181bd63d215d61a1df44e8fe7c182da6d24f26b0fae5348010"

# Path to your password list
wordlist_path = "1M.txt"

# Read password list and try each one
with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        password = line.strip()  # remove newline and spaces
        hashed = hashlib.sha256(password.encode()).hexdigest()
        if hashed == target_hash:
            print(f"The password is: {password}")
            break