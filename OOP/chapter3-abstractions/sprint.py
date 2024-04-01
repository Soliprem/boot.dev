class Human:
    def sprint_right(self):
        self.__raise_if_cannot_sprint()
        self.move_right()
        self.move_right()
        self.__use_sprint_stamina()

    def sprint_left(self):
        self.__raise_if_cannot_sprint()
        self.move_left()
        self.move_left()
        self.__use_sprint_stamina()

    def sprint_up(self):
        self.__raise_if_cannot_sprint()
        self.move_up()
        self.move_up()
        self.__use_sprint_stamina()

    def sprint_down(self):
        self.__raise_if_cannot_sprint()
        self.move_down()
        self.move_down()
        self.__use_sprint_stamina()

    def __raise_if_cannot_sprint(self):
        if self.__stamina <= 0:
            raise Exception("not enough stamina to sprint")

    def __use_sprint_stamina(self):
        self.__stamina -= 1

    # don't touch below this line

    def move_right(self):
        self.__pos_x += self.__speed

    def move_left(self):
        self.__pos_x -= self.__speed

    def move_up(self):
        self.__pos_y += self.__speed

    def move_down(self):
        self.__pos_y -= self.__speed

    def get_position(self):
        return self.__pos_x, self.__pos_y

    def __init__(self, pos_x, pos_y, speed, stamina):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed
        self.__stamina = stamina


run_cases = [
    ((0, 0, 5, 3), ["sprint_right"], (10, 0)),
    (
        (0, 0, 20, 3),
        [
            "sprint_left",
            "sprint_left",
            "sprint_left",
        ],
        (-120, 0),
    ),
    ((1, 1, 3, 1), ["sprint_down", "sprint_right"],
     "not enough stamina to sprint"),
]

submit_cases = run_cases + [
    ((3, 5, 5, 1), ["sprint_up"], (3, 15)),
    ((2, 15, 6, 2), ["sprint_down"], (2, 3)),
    (
        (1, 1, 5, 2),
        ["sprint_left", "sprint_up", "sprint_down"],
        "not enough stamina to sprint",
    ),
]


def test(human_args, methods, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    human = Human(*human_args)
    print(
        f" * human: x pos: {human._Human__pos_x}, y pos: {human._Human__pos_y}, speed: {human._Human__speed}, stamina: {human._Human__stamina}"
    )
    print(f" * methods: {methods}")
    print(f"Expected: {expected_output}")
    try:
        for method in methods:
            getattr(human, method)()
        result = human.get_position()
    except Exception as e:
        result = str(e)
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
