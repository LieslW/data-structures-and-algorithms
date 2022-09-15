# Graphs

**Graphs** are a non-linear data structure and collection of `vertices` (***nodes***) potentially connected by line segments named `edges`.


## Challenge

Implement your own `Graph`. It should be represented as an adjacency list.

### Methods
1. add node
   - Arguments: value
   - Returns: The added node
- Add a node to the graph
2. add edge
   - Arguments: 2 nodes to be connected by the edge, weight (optional)
   - Returns: nothing
   - Adds a new edge between two nodes in the graph
   - If specified, assign a weight to the edge
   - Both nodes should already be in the Graph
3. get nodes
   - Arguments: none
   - Returns all the nodes in the graph as a collection (set, list, or similar)
4. get neighbors
   - Arguments: node
   - Returns a collection of edges connected to the given node
   - Include the weight of the connection in the returned collection
5. size
   - Arguments: none
   - Returns the total number of nodes in the graph

### Pass Tests for Graphs

[X] Node can be successfully added to the graph
[X] An edge can be successfully added to the graph
[X] A collection of all nodes can be properly retrieved from the graph
[X] All appropriate neighbors can be retrieved from the graph
[X] Neighbors are returned with the weight between nodes included
[X] The proper size is returned, representing the number of nodes in the graph
[X] A graph with only one node and edge can be properly returned

## Approach & Efficiency

Took a rigorous testing approach in which I practiced TDD and built my graph functions around understanding the tests.
Big O notation for a graphs is O(N) for time and O(N) for space.


