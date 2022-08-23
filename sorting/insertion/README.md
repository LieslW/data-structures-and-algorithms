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

## Efficiency

*Time:*
- Defintion and explanation here
*Space:*
- Definition and explanation here
