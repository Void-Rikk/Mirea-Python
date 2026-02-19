def mul_bits(x, y, bits):
    x &= (2 ** bits - 1)
    y &= (2 ** bits - 1)
    return x * y


def mul16(x, y):
    x0 = x & 0xFF
    x1 = x >> 8
    
    y0 = y & 0xFF
    y1 = y >> 8
    
    p0 = mul_bits(x0, y0, 8)
    p1 = mul_bits(x1, y0, 8)
    p2 = mul_bits(x0, y1, 8)
    p3 = mul_bits(x1, y1, 8)
    
    return (p3 << 16) + ((p1 + p2) << 8) + p0