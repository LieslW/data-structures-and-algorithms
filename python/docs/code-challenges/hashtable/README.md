# Hash Tables

Hash Tables is another data structure containing Nodes. Contain two main components: `Key` and `Value`. Hashtables have an array structure at the base and are usually quite large. The Key will always reference a value at a certain index, making it time efficient since the algorithm does not need to search through the entire array index.

## Challenge

The challenge today was:

### Create Hashtable Class

Methods:

- set
  - Arguments: key, value
  - Returns: nothing
  - Method should hash the key, and set the key and value pair in the table, handling collisions as needed.
  - Should a given key already exist, replace its value from the `value` argument given to this method.
- get
  - Arguments: Key
  - Return: Value associated with that key in the table
- contains
  - Arguments: key
  - Returns: Boolean, indicating if the key exists in the table already.
- keys
  - Returns: collection of keys
- hash
  - Arguments: key
  - Returns: Index in the collection for that key

## Approach & Efficiency

Took a rigorous testing approach in which I developed the functions around the pre-existing tests. First, I understood what the test required then built the function, values, and functionality from there. Big O notation for a hash table is O(1) for time and O(N) for space.


