import hashlib
import re

def identify_hash(h):
    length = len(h)
    if length == 32: return "MD5"
    elif length == 40: return "SHA1"
    elif length == 64: return "SHA256"
    elif length == 128: return "SHA512"
    else: return "Unknown"

def crack_hash(target, wordlist_file):
    try:
        with open(wordlist_file, 'r') as f:
            words = f.read().splitlines()
    except:
        print("Wordlist file nahi mili!")
        return

    hash_type = identify_hash(target)
    print(f"Hash type: {hash_type}")
    print(f"Trying {len(words)} passwords...")

    for word in words:
        for algo in ['md5','sha1','sha256','sha512']:
            h = hashlib.new(algo, word.encode()).hexdigest()
            if h == target:
                print(f"\n[+] MILA! Password: {word} ({algo})")
                return
    print("\n[-] Nahi mila wordlist mein.")

def make_hash(text):
    print(f"\nMD5:    {hashlib.md5(text.encode()).hexdigest()}")
    print(f"SHA1:   {hashlib.sha1(text.encode()).hexdigest()}")
    print(f"SHA256: {hashlib.sha256(text.encode()).hexdigest()}")

print("=== Hash Toolkit ===")
print("1. Hash Identify karo")
print("2. Hash Crack karo")
print("3. Hash Banao")
choice = input("\nChoice (1/2/3): ")

if choice == "1":
    h = input("Hash enter karo: ")
    print(f"Type: {identify_hash(h)}")
elif choice == "2":
    h = input("Hash enter karo: ")
    w = input("Wordlist path (default: wordlist.txt): ") or "wordlist.txt"
    crack_hash(h, w)
elif choice == "3":
    text = input("Text enter karo: ")
    make_hash(text)
