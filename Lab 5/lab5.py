def mul02(byte):
    if byte & 0x80:
        result = (byte << 1) ^ 0x1B
    else:
        result = byte << 1
    return result & 0xFF


def mul03(byte):
    return mul02(byte) ^ byte


byte1 = 0xD4
byte2 = 0xBF


result1 = mul02(byte1)
result2 = mul03(byte2)


print(f"{hex(byte1)} * 02 = {hex(result1)}")
print(f"{hex(byte2)} * 03 = {hex(result2)}")


