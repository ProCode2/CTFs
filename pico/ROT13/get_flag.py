from string import ascii_lowercase as lowercase
from string import ascii_uppercase as uppercase

cipher = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"

flag = []
for ch in cipher:
    if ch in lowercase:
        flag.append(lowercase[(((ord(ch) - 97) + 13) % 26)])
    elif ch in uppercase:
        flag.append(uppercase[(((ord(ch) - 65) + 13) % 26)])
    else:
        flag.append(ch)


print(''.join(flag))
