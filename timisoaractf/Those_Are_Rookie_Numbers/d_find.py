import sys

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

print(modinv(int(sys.argv[2]),int(sys.argv[1])))
# print(modinv(65537, 58900433780152059829684181006276669632563849616305906563893514443102586211160)
# 58900433780152059829684181006276669632563849616305906563893514443102586211160
