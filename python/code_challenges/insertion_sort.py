class InsertionSort():

    def insertion_sort(self, list):
        for i in range(1, len(list)):
            key = list[i]
            move_value = i-1
            while move_value >= 0 and key < list[move_value]:
                list[move_value + 1] = list[move_value]
                move_value -= 1
            list[move_value + 1] = key

# InsertionSort(int[]
# arr)
#
# FOR
# i = 1
# to
# arr.length
#
# int
# j < -- i - 1
# int
# temp < -- arr[i]
#
# WHILE
# j >= 0
# AND
# temp < arr[j]
# arr[j + 1] < -- arr[j]
# j < -- j - 1
#
# arr[j + 1] < -- temp
