import test


def fast_mul(a, b):
    result = 0
    
    while b > 0:
        if b & 1:
            result += a

        a <<= 1
        b >>= 1
    
    return result


def main():
    for i in range(50):
        for j in range(50):
            test(fast_mul(i, j), i * j)

if __name__ == '__main__':
    main()