# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    index1 = 0
    for i in range(1, len(numbers)):
        if numbers[index1] < numbers[i]:
            index1 = i
    if index1 == 0:
        index2 = 1
    else:
        index2 = 0
    for j in range(1, len(numbers)):
        if j != index1 and numbers[index2] < numbers[j]:
            index2 = j
    return numbers[index1] * numbers[index2]


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
