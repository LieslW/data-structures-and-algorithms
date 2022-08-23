# Insertion Sort

**Insertion Sort** is a simple sorting algorithm that utilizes comparing values together and sorting them. The algorithm does this throughout the list until all have been sorted properly.

## Pseudocode

```python

  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp

```

## Trace

Sample List: [4, 8, 2, 9, 14, 5]

#### Pass 1

> **4**   **8**   2   9   14   5

First two values are compared to each other. Whichever is smaller should be first and greater than second. In this case, the two values are already sorted so the next two values are selected in *Pass 2*.

#### Pass 2

> 4   **8**   **2**   9   14   5
> 4   **2**   **8**   9   14   5

With these next two values, **8** is greater than **2** so 2 is put before **8**. However, as you will see in the next pass, this is not the last step with value **2**.

#### Pass 3

> **4**   **2**   8   9   14   5
> **2**   **4**   8   9   14   5

Value **2** is also compared to value **4** which was originally at the beginning. Since **2** is smaller, it is thus put first.

**These steps thus repeat themselves through the rest of the passes.*

#### Pass 4

> 2   4   **8**   **9**   14   5

Going back to where the algorithm was originally, it compares the next two values. Since they are properly sorted, it had no change.

#### Pass 5

> 2   4   8   **9**   **14**   5

As in pass 4, the next two values are compared and since they are properly sorted, there is no change.

#### Pass 6

> 2   4   8   9   **14**   **5**
> 2   4   8   **9**   **5**   14
> 2   4   **8**   **5**   9   14
> 2   **4**   **5**   8   9   14

Here the algorithm has run into the next two values that do need proper sorting. Once value **5** is put before **14**, it is compared to the other values and put before them until it gets to value **4**. Since **5** is greater than **4**, it is left where it is after the four.

#### Pass 7

> 2   4   5   8   9   14

Now all values have been compared to each the next and sorted in proper order. While the computer doesn't necessarily know it's sorting a list, the end result will always return a sorted list. 

## Efficiency

*Time:*
- Defintion and explanation here
*Space:*
- Definition and explanation here
