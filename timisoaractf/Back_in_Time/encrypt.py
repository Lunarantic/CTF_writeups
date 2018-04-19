import random

alpha = "abcdefghijklmnopqrstuvwxyz"
key = ''.join(random.sample(alpha,len(alpha)))
print key
assert(len(alpha) == 26)

plaintext = open("plaintext.txt").read()
ciphertext = ""

sub_dict = {}

for i in range(len(alpha)):
    sub_dict[alpha[i]] = key[i]

for i in range(len(plaintext)):
    if plaintext[i] in alpha:
        ciphertext += sub_dict[plaintext[i]]
    else:
        ciphertext += plaintext[i]

open("ciphertext.txt", "w").write(ciphertext)
