def fast_pow(a, b):
    result = 1

    while b > 0:
        if b & 1:
            result *= a
        
        a *= a
        b >>= 1
    
    return result




def main():
    assert fast_pow(3, 3) == 27
    assert fast_pow(2, 4) == 16
    assert fast_pow(2, 0) == 1

if __name__ == '__main__':
    main()