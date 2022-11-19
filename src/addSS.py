import random
import numpy as np

BASE = 10;

PRECISION_INTEGRAL = 8
PRECISION_FRACTIONAL = 8
Q = 293973345475167247070445277780365744413

PRECISION = PRECISION_INTEGRAL + PRECISION_FRACTIONAL

assert(Q > BASE ** PRECISION)

def encode(rational):
    upscaled = int(rational * BASE**PRECISION_FRACTIONAL)
    field_element = upscaled % Q
    return field_element

def decode(field_element):
    upscaled = field_element if field_element <= Q/2 else field_element - Q
    rational = upscaled / BASE**PRECISION_FRACTIONAL
    return rational

def encrypt(secret):
    first = random.randrange(Q)
    second = random.randrange(Q)
    third = (secret - first - second) % Q
    return [first, second, third]

def decrypt(sharing):
    return sum(sharing) % Q

def add(a, b):
    c = list()
    for i in range(len(a)):
        c.append((a[i] + b[i]) % Q)
    return tuple(c)

if __name__ == '__main__':
    x = 500.123456789
    y = 100.123456789
    encode_x = encode(x)
    encode_y = encode(y)
    print(x, " encode as encode_x: ",encode_x)
    print(y, " encode as encode_y: ",encode_y)
    enc_x = encrypt(encode_x)
    enc_y = encrypt(encode_y)
    print("enc_x: ", enc_x)
    print("enc_y: ", enc_y)
    enc_z = add(enc_x, enc_y)
    print("enc_z: ", enc_z)
    encode_z = decrypt(enc_z)
    print("encode_z: ",encode_z)
    z = decode(encode_z)
    print("z: ",z)
    print("明文下运算：",x+y)