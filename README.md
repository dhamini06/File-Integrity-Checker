# File Integrity Checker (Cyber Security Mini Project)

## Description
This project is a Python-based File Integrity Checker that detects unauthorized file modifications using cryptographic hashing (SHA-256). It helps ensure data integrity by comparing current file hashes with a stored baseline hash.

## Objective
To monitor files for tampering and detect integrity violations, which is a common requirement in cybersecurity, SOC operations, and digital forensics.

## Technologies Used
- Python
- SHA-256 Hashing
- File Handling
- Cybersecurity Fundamentals

## How It Works
1. The program generates a SHA-256 hash of a selected file.
2. The hash is stored as a baseline.
3. On subsequent executions, the file hash is recalculated.
4. If the hash changes, the program alerts that the file has been modified.

## Usage
1. Run the program:
python integrity_checker.py
2. Enter the file path when prompted.
3. The program will report whether the file is intact or modified.

## Learning Outcome
- Understanding of file integrity concepts
- Practical use of cryptographic hashing
- Basic SOC-style security monitoring

## Author
K Dhamini
