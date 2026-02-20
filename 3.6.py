import test


def fast_pow(a, b):
    result = 1

    while b > 0:
        if b & 1:
            result *= a
        
        a *= a
        b >>= 1
    
    return result




def main():
    for i in range(30):
        for j in range(10):
            test(fast_pow(i, j), i**j)

if __name__ == '__main__':
    main()