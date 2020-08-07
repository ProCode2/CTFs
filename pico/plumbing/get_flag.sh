echo "getting the flag"
nc 2019shell1.picoctf.com 13203 > flag.txt
cat flag.txt | grep -oE "picoCTF{.*?}"
