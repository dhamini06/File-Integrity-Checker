import hashlib
import os

HASH_FILE = "stored_hash.txt"

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

file_path = input("Enter file path: ")

if not os.path.exists(file_path):
    print("File does not exist.")
    exit()

current_hash = calculate_hash(file_path)

if not os.path.exists(HASH_FILE):
    with open(HASH_FILE, "w") as f:
        f.write(current_hash)
    print("Baseline hash created. File integrity is now being monitored.")

else:
    with open(HASH_FILE, "r") as f:
        stored_hash = f.read()

    if current_hash == stored_hash:
        print("File integrity intact. No modification detected.")
    else:
        print("ALERT! File has been modified or tampered.")
