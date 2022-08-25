def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        index = i-1

        while index >= 0 and key < list[index]:
            list[index + 1] = list[index]
            index -= 1
        list[index + 1] = key
    return list

