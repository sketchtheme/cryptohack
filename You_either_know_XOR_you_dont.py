key = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
print(key)
# KEY1 = b"\x0e\x0b!?&\x04\x1eH\x0b&!\x7f'4"
# KEY2 = b".\x17]\x0e\x07\n<[\x10>%&!\x7f'4"
# KEY3 = b".\x17]\x0e\x07~&4Q\x15\x01\x04"
# print("".join(chr(i) for i in KEY1))
# print("".join(chr(i) for i in KEY2))
# print("".join(chr(i) for i in KEY3))
KEY = b"\x0e\x0b!?&\x04\x1eH\x0b&!\x7f'4.\x17]\x0e\x07\n<[\x10>%&!\x7f'4.\x17]\x0e\x07~&4Q\x15\x01\x04"


def xor_with_key(message, key):
    key = key * (len(message) // len(key)) + key[:len(message) % len(key)]
    return bytes([char ^ key_char for char, key_char in zip(message, key)])
print(xor_with_key(KEY, b'crypto{'))
print(xor_with_key(KEY, b'myXORke+y_Q'))
