# Challenge Summary

- Write a function called business trip
- Arguments: graph, array of city names
- Return: the cost of the trip (if it’s possible) or null (if not)

Determine whether the trip is possible with direct flights, and how much it would cost.

## Whiteboard Process
![Code Challenge 37](whiteboardcc37.png)

## Approach & Efficiency

For this challenge, utilized lists, queues, and sets. First, enqueued everything into a queue than dequeued and appended to a list.
The Big O Notation for this challenge is O(N) for both time and space.

## Solution

```python
pip install -r requirements.txt
pytest -k test_graph_business_trip.py
```
