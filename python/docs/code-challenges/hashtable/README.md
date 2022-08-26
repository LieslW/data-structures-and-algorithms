# Hash Tables

Hash Tables is another data structure containing Nodes. Contain two main components: `Key` and `Value`. Hashtables have an array structure at the base and are usually quite large. The Key will always reference a value at a certain index, making it time efficient since the algorithm does not need to search through the entire array index.

## Challenge

The challenge today was:

### Create Hashtable Class

Methods:

- **set**
  - Arguments: key, value
  - Returns: nothing
  - Method should hash the key, and set the key and value pair in the table, handling collisions as needed.
  - Should a given key already exist, replace its value from the `value` argument given to this method.
- **get**
  - Arguments: Key
  - Return: Value associated with that key in the table
- **contains**
  - Arguments: key
  - Returns: Boolean, indicating if the key exists in the table already.
- **keys**
  - Returns: collection of keys
- **hash**
  - Arguments: key
  - Returns: Index in the collection for that key

### Create Tests for Hashtable Class

1. Setting a key/value to your hashtable results in the value being in the data structure
2. Retrieving based on a key returns the value stored
3. Successfully returns null for a key that does not exist in the hashtable
4. Successfully returns a list of all unique keys that exist in the hashtable
5. Successfully handle a collision within the hashtable
6. Successfully retrieve a value from a bucket within the hashtable that has a collision
7. Successfully hash a key to an in-range value

## Approach & Efficiency

Took a rigorous testing approach in which I developed the tests for my basic hash functions. First, I understood what the requirements for the tests were then built the tests from there. After building the tests, I used a test driven mindset to build some functions that will pass my tests. Big O notation for a hash table is O(1) for time and O(N) for space.


