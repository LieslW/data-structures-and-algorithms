# Stacks and Queues

Stacks and Queues are two more of some basic data structures. To put it simply with a metaphor, Stacks act kind of like a stack of plates where you can only take the Node off the `Top`. Queue is like a line for the movie theatres where the one in the `Front` refers to the one behind it.

## Challenge
Write tests to prove some basic functionality of stacks and queues.

1. Can successfully push onto a stack
2. Can successfully push multiple values onto a stack
3. Can successfully pop off the stack
4. Can successfully empty a stack after multiple pops
5. Can successfully peek the next item on the stack
6. Can successfully instantiate an empty stack
7. Calling pop or peek on empty stack raises exception
8. Can successfully enqueue into a queue
9. Can successfully enqueue multiple values into a queue
10. Can successfully dequeue out of a queue the expected value
11. Can successfully peek into a queue, seeing the expected value
12. Can successfully empty a queue after multiple dequeues
13. Can successfully instantiate an empty queue
14. Calling dequeue or peek on empty queue raises exception

[Stack.py](python/data_structures/stack.py)

[Test Stack](python/tests/data_structures/test_stack.py)

[Queue.py](python/data_structures/queue.py)

[Test Queue](python/tests/data_structures/test_queue.py)

## Approach and Efficiency
To solve each feature task, I went slowly through the tests and made sure I understood what exactly was being asked. Then I built the function around that.

Big O Notation for each Feature Task listed above is O(1). It takes the same amount of time no matter how many Nodes within the stack.



