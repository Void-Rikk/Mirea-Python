def fast_mul_gen(y):
    if y == 0:
        print("def f(x):")
        print("    return 0")
        return

    print("def f(x):")
    
    print("    a0 = x")
    
    powers = [1]
    i = 0
    
    while powers[-1] * 2 <= y:
        i += 1
        print(f"    a{i} = a{i-1} + a{i-1}")
        powers.append(powers[-1] * 2)
    
    max_pow = powers[-1]
    
    if max_pow == y:
        print(f"    return a{i}")
        return
    
    diff = max_pow - y
    
    if max_pow >= y:
        print(f"    result = a{i}")
        
        remaining = diff
        for j in reversed(range(len(powers))):
            if powers[j] <= remaining:
                print(f"    result = result - a{j}")
                remaining -= powers[j]
        
        print("    return result")
    
    else:
        print("    result = 0")
        remaining = y
        
        for j in reversed(range(len(powers))):
            if powers[j] <= remaining:
                print(f"    result = result + a{j}")
                remaining -= powers[j]
        
        print("    return result")

def test():
    import builtins

    for y in range(1, 50):
        code_lines = []

        def capture_print(*args):
            code_lines.append(" ".join(map(str, args)))

        old_print = builtins.print
        builtins.print = capture_print

        try:
            fast_mul_gen(y)
        finally:
            builtins.print = old_print

        program = "\n".join(code_lines)

        local_vars = {}
        exec(program, local_vars)

        f = local_vars["f"]

        for x in range(0, 50):
            expected = x * y
            actual = f(x)
            assert actual == expected, (
                f"Ошибка: x={x}, y={y}, got={actual}, expected={expected}\n"
                f"Код:\n{program}"
            )

    print("ALL TESTS PASSED")

if __name__ == "__main__":
    test()