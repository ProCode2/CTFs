from string import ascii_lowercase as lowercase

cipher = input("only the ciphered part?>")

plain = []
for ch in cipher:
    plain.append(lowercase[((ord(ch) - 97) + 11) % 26])

print("picoCTF{%s}" % ''.join(plain))
