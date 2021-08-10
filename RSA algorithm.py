import random
def isPrime(n):

    if n < 2:
        return False

    # low prime numbers to save time
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
                 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839,
                 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
                 991, 997]

    # if in lowPrimes
    if n in lowPrimes:
        return True

    # if low primes divide into n
    for prime in lowPrimes:
        if n % prime == 0:
            return False

    # find number c such that c * 2 ^ r = n - 1
    c = n - 1  # c even bc n not divisible by 2
    while c % 2 == 0:
        c /= 2  # make c odd

    return True


def generateKeys(keysize=1024):
    e = d = N = 0

    # get prime nums, p & q
    p = int(input("Enter a prime number for p: "))
    q = int(input("Enter a prime number for q: "))
    # RSA Modulus
    N = p * q
    # totient
    z = (p - 1) * (q - 1)

    # choose e
    # e is coprime with z & 1 < e <= z
    while True:
        e = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
        if (isCoPrime(e, z)):
            break

    # choose d
    # d is mod inv of e with respect to phiN, e * d (mod phiN) = 1
    d = modularInv(e, z)

    return e, d, N


def isCoPrime(p, q):

    return gcd(p, q) == 1


def gcd(p, q):
    """
        euclidean algorithm
    """

    while q:
        p, q = q, p % q
    return p


def egcd(a, b):
    s = 0;
    old_s = 1
    t = 1;
    old_t = 0
    r = b;
    old_r = a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    # return gcd, x, y
    return old_r, old_s, old_t


def modularInv(a, b):
    gcd, x, y = egcd(a, b)

    if x < 0:
        x += b

    return x


def encrypt(e, N, msg):
    cipher = ""

    for c in msg:
        m = ord(c)
        cipher += str(pow(m, e, N)) + " "

    return cipher


def decrypt(d, N, cipher):
    msg = ""

    parts = cipher.split()
    for part in parts:
        if part:
            c = int(part)
            msg += chr(pow(c, d, N))

    return msg


def main():
    print("RSA Algorithm")

    keysize = 32

    e, d, N = generateKeys(keysize)

    msg = "SUZANNE"

    enc = encrypt(e, N, msg)
    dec = decrypt(d, N, enc)

    print(f"Message: {msg}")
    print(f"e: {e}")
    print(f"d: {d}")
    print(f"N: {N}")
    print(f"encrypt message: {enc}")
    print(f"decrypt message: {dec}")


main()
#p=53,q=59