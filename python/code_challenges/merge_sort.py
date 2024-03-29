def merge_sort(list):
    n = len(list)

    if n > 1:
        mid = n // 2
        left = list[:mid]
        right = list[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1

        if i == len(left):
            while j < len(right):
                list[k] = right[j]
                k += 1
                j += 1
        else:
            while i < len(left):
                list[k] = left[i]
                k += 1
                i += 1

    return list
