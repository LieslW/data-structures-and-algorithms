# Insertion Sort

**Insertion Sort** is a simple sorting algorithm that sorts the values within the list in comparison to a selected value. The unsorted values are placed at the correct position in comparison to the value and the value is put into the correct place back within the list, then another value is selected. This process is repeated until the list has been sorted.

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

Sample List: [sample list here]

#### Pass 1 through Pass []...

## Efficiency

*Time:*
- Defintion and explanation here
*Space:*
- Definition and explanation here
