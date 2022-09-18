# Quick Sort

**Quick Sort** is another sorting algorithm that uses three methods to go through what's called the "divide and conquer" strategy. First, it picks a `pivot` element and partitions an array around the pivot. Partition is particularly important since it will put x at the correct position in relativity to the list and the pivot. Smaller elements than **x** will be put before and greater than after. It should be down in linear time.

## Pseudocode

```python

ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp

```

## Trace

Sample List: [4, 8, 2, 9, 21, 14, 5]

#### Pass 1

> [4   ***8***   2   9   21   14   5]

> [4   2    9   21  14   5  ***8***]

To start, we are given this list of 7 values. For this example, the value **8** will be our pivot and put at the end of the array.

#### Pass 2

> [4   2   *9*  21   14   *5*  ***8***]

> [4   2   *5*  21   14   *9*  ***8***]


Now we are going to go through left_items and right_items. In terms of the pivot, left items start from the left of the list and right from the right. If the left item finds a greater than value and the right a less than value, the two are swapped and so forth.

#### Pass 3

> [4   2   5  21   14   9  ***8***]

> [4   2   5  ***8***   21   14   9]

Now that the greater than and less than values have been organized into two halves in terms of the pivot, 8 is placed back into the middle in terms of a left_item.

#### Pass 4

> [4   2   5  8   21   14   9]

>  [2   4   5   8   9   14   21]

The process is then repeated for the two halves until the list is completely sorted.

## Efficiency

*Time:*
- **O(n^2)**: The worst case for QuickSort is when the algorithm picks a pivot that is either the greatest or smallest element in the list. This essentially doubles the time QuickSort takes since it must go through it multiple times.

*Space:*
- **O(N)**: Not creating any container other than given list.
