import random
import string
import sys

def generate_password(length=16):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def check_strength(password):
    score = 0
    tips = []
    if len(password) >= 8: score += 1
    else: tips.append("8+ characters use karo")
    if any(c.isupper() for c in password): score += 1
    else: tips.append("Capital letter add karo")
    if any(c.islower() for c in password): score += 1
    else: tips.append("Small letter add karo")
    if any(c.isdigit() for c in password): score += 1
    else: tips.append("Number add karo")
    if any(c in "!@#$%^&*" for c in password): score += 1
    else: tips.append("Special character add karo (!@#$)")
    
    levels = {1:"Bahut Kamzor",2:"Kamzor",3:"Theek Hai",4:"Mazboot",5:"Bahut Mazboot"}
    print(f"\nStrength: {levels[score]} ({score}/5)")
    for t in tips:
        print(f"  - {t}")

def wordlist_generator(word, output="wordlist.txt"):
    variations = []
    variations.append(word)
    variations.append(word.capitalize())
    variations.append(word.upper())
    variations.append(word + "123")
    variations.append(word + "2024")
    variations.append(word + "2025")
    variations.append(word + "!")
    variations.append(word + "@123")
    variations.append("123" + word)
    variations.append(word.capitalize() + "!")
    with open(output, 'w') as f:
        f.write('\n'.join(variations))
    print(f"{len(variations)} passwords saved to {output}")

print("=== Password Toolkit ===")
print("1. Password Generate karo")
print("2. Password Strength Check karo")
print("3. Wordlist Generate karo")
choice = input("\nChoice (1/2/3): ")

if choice == "1":
    length = int(input("Length (default 16): ") or 16)
    for i in range(5):
        print(f"  {generate_password(length)}")
elif choice == "2":
    pwd = input("Password enter karo: ")
    check_strength(pwd)
elif choice == "3":
    word = input("Base word enter karo: ")
    wordlist_generator(word)
