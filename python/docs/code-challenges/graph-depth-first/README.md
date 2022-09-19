# Challenge Summary

Write the following method for the Graph class:

- Name: Depth first
- Arguments: Node (Starting point of search)
- Return: A collection of nodes in their pre-order depth-first traversal order
- Program output: Display the collection

## Whiteboard Process
![Code Challenge 38](whiteboardcc38.png)

## Approach & Efficiency

For this challenge, first verified any matches within list and graph. Then checked neighbors and then incremented cost by edge's weight. However, if any of these steps were not verified, it returned false.
The Big O Notation for this challenge is O(N^2) for time and O(N) for space.

## Solution

```python
pip install -r requirements.txt
pytest -k test_graph_depth_first.py
```
