
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m=26):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def encrypt(text, a, b):
    result = ""
    for ch in text:
        if ch.isalpha():
            x = ord(ch.lower()) - ord('a')
            e = (a * x + b) % 26
            result += chr(e + ord('a'))
        else:
            result += ch
    return result

def decrypt(cipher, a, b):
    a_inv = mod_inverse(a)
    if a_inv is None:
        return "Invalid key! 'a' has no modular inverse."
    
    result = ""
    for ch in cipher:
        if ch.isalpha():
            y = ord(ch.lower()) - ord('a')
            d = (a_inv * (y - b)) % 26
            result += chr(d + ord('a'))
        else:
            result += ch
    return result

while True:
    print("\n--- Affine Cipher ---")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        text = input("Enter plaintext: ")
        a = int(input("Enter key a (must be coprime with 26): "))
        b = int(input("Enter key b: "))

        if gcd(a, 26) != 1:
            print("Invalid 'a'. It must be coprime with 26.")
        else:
            print("Encrypted text:", encrypt(text, a, b))

    elif choice == '2':
        cipher = input("Enter ciphertext: ")
        a = int(input("Enter key a: "))
        b = int(input("Enter key b: "))
        print("Decrypted text:", decrypt(cipher, a, b))

    elif choice == '3':
        print("Exiting...")
        break

    else:
        print("Invalid choice!")