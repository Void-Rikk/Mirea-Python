def main(x):
    step1 = x + x
    step2 = step1 + step1
    step3 = step2 + step2
    step4 = step3 - (x - step3)

    return step4