# def check_redundancy(arr):
#     element_count = {}
#
#     for element in arr:
#         if element in element_count:
#             return -1  # Found a redundant element
#         else:
#             element_count[element] = 1
#
#     return 1  # All elements are unique
#
#
# # Example usage:
# arr1 = [1, 2, 3, 4, 5]
# result1 = check_redundancy(arr1)
# print("Result for arr1:", result1)  # Output: 1 (unique elements)
#
# arr2 = [1, 2, 2, 3, 4, 5]
# result2 = check_redundancy(arr2)
# print("Result for arr2:", result2)  # Output: -1 (redundant element)


def uniqueElementsInArray(inpArray: list) -> int:
    countDict = {}

    for x in inpArray:
        if x in countDict:
            return -1
        else:
            countDict[x] = 1
    return 1


size = int(input())
arr = []

for x in range(size):
    y = int(input())
    arr.append(y)

print(uniqueElementsInArray(arr))


def uniqueElementsInArray(inpArray: list) -> int:
    countDict = {}

    for x in inpArray:
        if x in countDict:
            return -1
        else:
            countDict[x] = 1
    return 1


if __name__ == "__main__":
    # Read the input as a single line and split it into a list of integers
    arr = list(map(int, input().split()))

    result = uniqueElementsInArray(arr)
    print(result)
