def test_exp(exp_to_test: str, target: int):
    if eval(exp_to_test) == target:
        print(exp_to_test, '= 200')


def find_expressions(digits: list[int], target: int, current_exp: str = "", iter_count: int = 0):
    if iter_count == len(digits) - 1:
        test_exp(current_exp, target)
        return

    next_digit = str(digits[iter_count + 1])

    # Без операции
    find_expressions(digits, target, current_exp + next_digit, iter_count + 1)

    # Сложение
    find_expressions(digits, target, current_exp + "+" + next_digit, iter_count + 1)

    # Вычитание
    find_expressions(digits, target, current_exp + "-" + next_digit, iter_count + 1)


d = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

find_expressions(d, 200, str(d[0]))
