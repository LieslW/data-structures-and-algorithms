# Quick Sort

**Quick Sort** is another sorting algorithm that uses three methods to go through what's called the "divide and conquer" strategy. 

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

Sample List: [4, 8, 2, 21, 9, 14, 5]

#### Pass 1

> **[4   8   2   21   9   14   5]**

> [4    8   2   21]   [9  14   5]

To start, we are given this list of 7 values. It's going to be divided in half and divided in half more later on.

#### Pass 2

> **[4    8   2   21]   [9  14   5]**

> [4    8]    [2  21]

>[4] [8]

So far, the list has only had one pass through the first method which splits the list in halves. Here we see the first half being split until it can't split further.

#### Pass 3

> [4] [8]

> [4  8]

Method 1 will focus on very first half before it moves to the rest of the list. Here we see the first two original values, `4` and `8`, being merged back together in sorted order.

#### Pass 4

> [2  21]

> [2]  [21]

> [2  21]

Like `4` and `8` above, the next two original values are divided until no further then put back together in a sorted order.

#### Pass 5

> [4  8]   [2  21]

> [2  4  8  21]

Still focusing on the original first half, we have two sorted halves. These are merged together in a sorted order, marking the end of sorting the first half.

#### Pass 6

> **[9  14  5]**

>[9  14]

>[9] [14]

> [9 14]

> [5  9  14]

Going back to the original second half, we repeat the process. In this case we have an outlier, value `5`. Since `5` doesn't need to be sorted by itself, it is simply added in the final list with `9` and `14`.

#### Pass 7

> [2  4  8  21]  [5  9  14]

> [2  4  5  8  9  14]

Now that we have our two sorted halves of our original list, they are finally merged together to make one sorted list.

## Efficiency

*Time:*
- **O(logN)**: In all cases, merge sort always divides the list into two halves and takes linear time to merge the two halves.

*Space:*
- **O(N)**: Needs N space since the elements are copied within a temporary list
