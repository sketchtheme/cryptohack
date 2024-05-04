def solve(fav, byte):
    return bytes([byte^b for b in fav])

fav = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
for byte in range(256):
    result = solve(fav, byte)
    if "crypto{" in str(result):
        print(result)
        break