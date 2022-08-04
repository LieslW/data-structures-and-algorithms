# Challenge Summary
Validate whether or not brackets within a string are balanced or not via a function named "validate brackets". Depending on their balance, return True or False.

## Whiteboard Process
![WhiteBoard: Class 13](python/docs/code-challenges/stack-queue-brackets/whiteboard.png)

## Approach & Efficiency
I decided the best approach would to check if all the pairs of brackets would cancel each other first. Then any leftovers would get pushed into a stack. If there are brackets pushed to the stack, that would result in the function returning False.

## Solution
<!-- Show how to run your code, and examples of it in action -->
