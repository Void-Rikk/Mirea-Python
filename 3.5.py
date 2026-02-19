def fast_mul(a, b):
    result = 0
    
    while b > 0:
        if b & 1:
            result += a

        a <<= 1
        b >>= 1
    
    return result


def main():
    assert fast_mul(3, 5) == 15
    assert fast_mul(5, 5) == 25
    assert fast_mul(-2, 5) == -10
    assert fast_mul(0, 5) == 0

if __name__ == '__main__':
    main()