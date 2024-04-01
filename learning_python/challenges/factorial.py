def factorial(num):
    factorial = 1
    if num == 0:
        return 1
    for i in range(1, num+1):
        factorial = factorial * i
    return factorial


run_cases = [
    (0, 1),
    (4, 24),
]

submit_cases = run_cases + [
    (1, 1),
    (5, 120),
    (7, 5040),
    (9, 362880),
    (13, 6227020800),
    (15, 1307674368000),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input}")
    print(f"Expecting: {expected_output}")
    result = factorial(input)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")
    return f"{passed} passed, {failed} failed"


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
