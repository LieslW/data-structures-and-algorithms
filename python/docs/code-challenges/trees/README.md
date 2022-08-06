# Trees

Trees are another set of data structure containing Nodes and are very similar to linked lists except they can contain multiple children. They can also more efficiently filter through data.

## Challenge

The challenge today was:

### Binary Tree

1. Create a Binary Tree class
- Define a method for each of the depth first traversals:
  - pre order
  - in order
  - post order which returns an array of the values, ordered appropriately.

### Binary Search Tree
2. Create a Binary Search Tree class
- This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
- Add
  - Arguments: value
  - Return: nothing
  - Adds a new node with that value in the correct location in the binary search tree.
- Contains
  - Argument: value
  - Returns: boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency

Took a rigorious testing approach in which I developed the functions around the pre-existing tests. First, I understood what the test required then built the function, values, and functionality from there. Big O notation for a binary tree is O(N) while the notation for a binary search tree is O(log(n)).


