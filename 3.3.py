import test


def m15(x):
    step1 = x + x
    step2 = step1 + step1
    step3 = step2 + step2
    step4 = step3 - (x - step3)

    return step4

def main():
    for i in range(100):
        test(m15(i), i * 15)

if __name__ == "__main__":
    main()