# Uses python3
import sys

# def get_number_of_inversions(a, b, left, right):
#     number_of_inversions = 0
#     if right - left <= 1:
#         return number_of_inversions
#     ave = (left + right) // 2
#     number_of_inversions += get_number_of_inversions(a, b, left, ave)
#     number_of_inversions += get_number_of_inversions(a, b, ave, right)
#     #write your code here
#     return number_of_inversions

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *a = list(map(int, input.split()))
#     b = n * [0]
#     print(get_number_of_inversions(a, b, 0, len(a)))


def get_number_of_inversions(numbers):
    number_of_inversions = 0
    if len(numbers) == 1:
        return numbers, number_of_inversions
    m = len(numbers) // 2
    left, left_inv = get_number_of_inversions(numbers[:m])
    right, right_inv = get_number_of_inversions(numbers[m:])
    result, total_inv = merge(left, right, left_inv, right_inv)
    return result, total_inv


def merge(left, right, left_inv, right_inv):
    total_inv = left_inv + right_inv
    result = []
    left_ptr = right_ptr = 0
    while left_ptr < len(left) and right_ptr < len(right):
        if left[left_ptr] <= right[right_ptr]:
            result.append(left[left_ptr])
            left_ptr += 1
        elif right[right_ptr] < left[left_ptr]:
            result.append(right[right_ptr])
            right_ptr += 1
            total_inv += (len(left) - left_ptr)
    if right_ptr < len(right):
        result.extend(right[right_ptr:])
    if left_ptr < len(left):
        result.extend(left[left_ptr:])
    return result, total_inv


_ = input()
numbers = [int(x) for x in input().split()]
print(get_number_of_inversions(numbers)[1])
