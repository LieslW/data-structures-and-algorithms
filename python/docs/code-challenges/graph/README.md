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

### Create Tests for Graphs

[] Node can be successfully added to the graph
[] An edge can be successfully added to the graph
[] A collection of all nodes can be properly retrieved from the graph
[] All appropriate neighbors can be retrieved from the graph
[] Neighbors are returned with the weight between nodes included
[] The proper size is returned, representing the number of nodes in the graph
[] A graph with only one node and edge can be properly returned
[] An empty graph properly returns null

## Approach & Efficiency

Took a rigorous testing approach in which I developed the tests for my basic graph functions. First, I understood what the requirements for the tests were then built the tests from there. After building the tests, I used a test driven mindset to build some functions that will pass my tests.
Big O notation for a graphs is [O(1)] for time and [O(N)] for space.


