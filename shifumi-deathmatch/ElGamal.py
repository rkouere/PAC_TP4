class ElgamalError(Exception):
    """Launched when something bad happen during the use of the Elgamal class.
    """

    def __init__(self, value):
    """Create a new ElgamalError with a specific message."""
self.value = value


class Elgamal:
    """This class handle the signature, the encrytion and decryption using the
    ElGamal encryption system."""

    __X_NOT_SET = "The private part of the key (x) is not set."
    __R_NOT_CORRECT = "The r ({0}) value must be including beetween 0 and p"
    __S_NOT_CORRECT = "The s ({0}) value must be including beetween 0 and q"

    def __init__(self, p, g, h, x = None):
    """Create a new class Elgamal. Depends on the actions you want to
perform, you do not have to set the x value. You have to set x, only
if you want to perform decryption and generate signature."""
self.__p = p
self.__g = g
self.__x = x
self.__h = h

def decrypt(self, a, m):
"""Decrypt a encrypted message m. This method does not check if the
result are consistent."""
if self.__x == None:
    raise ElgamalError(self.__X_NOT_SET)
h = pow(a, x, p)
h_inv = modinv(h, p)
decipher_text = (b * h_inv) % p
return decipher_text

def encrypt(self, m):
"""Encrypt the message m. m must be an interger. If not, an TypeError
will be raise. Return a tuple like this one : (g^y, encrypted message).
"""
if not type(m) is int:
    raise TypeError()
y = random.randint(1, self.__p -1)
enc_m = m * pow(self.__h, y, self.__p)
return (pow(self.__g, y, self.__p), enc_m)

def sign(self, m):
"""Generate a signature for the message m. Return the result as a
tuple (r = g^k, s). If m is not a int, raise an TypeError exception"""
q = self.__p - 1
k = random.randint(1, q - 1)
while gcd(k , q) != 1:
    k = random.randint(1, q - 1)

r = pow(g, k, self.__p)
s = (modinv(k, q) * (m - self.__x * r)) % q
return (r, s)

def check_signature(self, r, s, m):
"""Take the signature elgamal and the message and check if the signature
is correct. Return True if the signature is correct. False, otherwise.
"""
q = self.__p - 1
if not 0 < r < self.__p:
    raise ElgamalError(self.__R_NOT_CORRECT.format(r))
if not 0 < s < q:
    raise ElgamalError(self.__S_NOT_CORRECT.format(s))

g_m = pow(self.__g, m, self.__p)

return g_m == (pow(self.__h, r, self.__p) * pow(r, s, self.__p)) % self.__p
