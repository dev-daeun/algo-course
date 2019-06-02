# python3
from random import randint


# create my own input data for stress test.
def create_small_input():
    number_size = randint(2, 10)
    numbers = [randint(1, 50) for _ in range(number_size)]
    return numbers


def create_big_input():
    number_size = randint(2, 1000)
    numbers = [randint(1, 10000) for _ in range(number_size)]
    return numbers


def create_input_with_same_values():
    number_size = randint(2, 999)
    numbers = [randint(1, 1000) for _ in range(number_size)]
    numbers.append(max(numbers))
    numbers.insert(0, max(numbers))
    return numbers


def max_pairwise_product_alternative(numbers):
    biggest = max(numbers)
    numbers.remove(biggest)
    sub_biggest = max(numbers)
    return biggest * sub_biggest


def max_pairwise_product_with_bug(numbers):
    n = len(numbers)
    max_index1 = -1
    for i in range(n):
        if max_index1 == -1 or numbers[i] > numbers[max_index1]:
            max_index1 = i

    max_index2 = -1
    for j in range(n):  # it should compare j and max_index1.
        if numbers[j] != numbers[max_index1] and (max_index2 == -1 or numbers[j] > numbers[max_index2]):
            max_index2 = j

    return numbers[max_index1] * numbers[max_index2]


def stress_test(input_):
    print(f'input: {input_}')

    answer = max_pairwise_product_with_bug(input_)
    alternative_answer = max_pairwise_product_alternative(input_)

    if answer != alternative_answer:
        print(f'results differ. answer: {answer}, alternative_answer: {alternative_answer}')
    else:
        print('OK')


if __name__ == '__main__':
    while True:
        stress_test(create_small_input())
