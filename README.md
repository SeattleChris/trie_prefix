# trie_prefix

We're going to make our own Contacts application! The application must perform two types of operations:

1) add name, where `name` is a string denoting a contact name. This must store `name` as a new contact in the application.
2) find partial, where `partial` is a string denoting a partial name to search the application for. It must count the number of contacts starting with `partial` and print the count on a new line.

Given `n` sequential add and find operations, perform each operation in order.

## Function Description

The `contacts` function has the following parameters:

* string queries[n]: the operations to perform

Returns

* int[]: the results of each find operation

Additional data structure code is not provided for this problem.

## Constraints

* 1<= n <= 10^5
* 1 <= length of `name` <= 21
* 1 <= length of `partial` <= 21
* `name` and `partial` contain lowercase English letters only.
* The input does not have any duplicate `name` for the `add` operation.

## Input Format

* The first line contains a single integer, `n`, the number of operations to perform (the size of `queries[]`).
* Each of the following `n` lines contains a string, `queries[i]`.
* Each of `queries[i]` is a string with an operation (either 'add' or 'find') as the first word (space separated) and the second word as the text for that operation.
