# Merge Sort

**Merge Sort** is another sorting algorithm that uses two methods to go through what's called the "divide and conquer" strategy. In the method, the list is divided into equal halves until it can't be divided any further. Then it combines them back together in a sorted manner. The second method takes the two sorted lists and merges them together to end up with the original list, but now in sorted order.

## Pseudocode

```python

  ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left

```

## Trace

Sample List: [4, 8, 2, 21, 9, 14, 5]

#### Pass 1 (Method 1)

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
- **[Enter notation]**:

*Space:*
- **[Enter notation]**:
