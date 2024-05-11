KEY = bytes.fromhex("your cipher")
print(key)

def xor_with_key(message, key):
    key = key * (len(message) // len(key)) + key[:len(message) % len(key)]
    return bytes([char ^ key_char for char, key_char in zip(message, key)])
print(xor_with_key(KEY, b'crypto{'))
print(xor_with_key(KEY, b'myXORkey'))
