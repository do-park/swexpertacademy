
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    while left or right:
        if left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif left:
            result.extend(left)
            break
        elif right:
            result.extend(right)
            break
    return result


arr = [5, 2, 3, 7, 9, 8, 1, 4]
print(merge_sort(arr))