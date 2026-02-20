import test


def mul_bits(x, y, bits):
    x &= (2 ** bits - 1)
    y &= (2 ** bits - 1)
    return x * y


def mul16k(x, y):
    x0 = x & 0xFF
    x1 = x >> 8
    
    y0 = y & 0xFF
    y1 = y >> 8
    
    z0 = mul_bits(x0, y0, 8)
    z1 = mul_bits(x1, y1, 8)
    z2 = mul_bits(x0 + x1, y0 + y1, 16)
    
    middle = z2 - z1 - z0
    
    return (z1 << 16) + (middle << 8) + z0

def main():
    for i in range(50):
        for j in range(50):
            test(mul16k(i, j), i * j)

if __name__ == "__main__":
    main()