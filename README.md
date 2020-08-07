# Sprint Challenge: Hash Tables

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This challenge allows you to practice the concepts and techniques learned over the past sprint and apply them in a concrete project. This sprint explored hash tables. During this sprint, you studied hash functions, collision resolution, complexity analysis of hash tables, load factor, resizing, and various use cases for hash tables. In your challenge this week, you will demonstrate mastery of these skills by solving five problems related to hash tables.

The sprint challenge is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the sprint challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your TL if you need direction.

_You have **three hours** to complete this challenge. Plan your time accordingly._

## Introduction

This challenge requires you to solve algorithm problems that are amenable to being solved efficiently with a hash table.

### Commits

Commit your code regularly and meaningfully. This practice helps both you (in case you ever need to return to old code for any number of reasons) and your Team Lead as they evaluate your solution.

## Interview Questions

Be prepared to demonstrate your understanding of this week's concepts by answering questions on the following topics. You might prepare by writing down your answers beforehand.

1 Hashing functions

A hash function is a function where the input is any data, and the output is a number.
The requirements for a hash function are:
A hash function must be consistent (deterministic). Every time it receives the same input, it must return the same output. If it’s not deterministic, it is not a hash function.
Different input data should return different numbers. 
A hash function must return numbers that are within a specific range.

The reason the hash function should return different numbers when given different input data is to minimize collisions. When a hash function maps each different input data to a different number, it is called a perfect hash function. In practice, unless we know all the possible data inputs, we can’t create a perfect hash function.
 
2 Collision resolution

 A way of handling collisions, that is, when two or more items should be kept in the same location, especially in a hash table.

3 Performance of basic hash table operations

Performance of basic hash table operations, even when collisions happen (which is unavoidable), if the hashing function is optimal it will spread the data somewhat evenly, chaining more than one value to the same index in some cases, but on average the performance will still be that of constant time O(1). 

4 Load factor

The load factor of a hash table is a simple calculation. You take the number of items stored in the hash table divided by the number of slots.

Hash tables use an array for storage, so the load factor would be the number of occupied slots divided by the length of the array. So, an array of length 10 with three items in it has a load factor of 0.3, and an array of length 20 with twenty items has a load factor of 1. 
As the load factor of a hash table increases, so does the chance of a collision occurring, which in turn reduces the performance of the hash table. It is good practice to constantly monitor the size of the hash table and dynamically resize it when it reaches certain thresholds. 
 
 
5 Automatic resizing

The load factor can also be too small. If the hash table is too large for the data that it is storing, then memory is being wasted. So, in addition to resizing, when the load factor gets too high, you should also resize when the load factor gets too low.
Industry standards normally indicate that when a hash table load factor is greater than 0.7 it is common to double the size of the hash table. On the contrary, when the hash table load factor is 0.2 or below, the hash table size is reduced by a half. 
By doing this operation, the currently stored data in the array must be re inserted into the hash table each time, with the data being reallocated constantly. Each item has to be rehashed. 
Resizing effectively is an expensive operation, so it shouldn’t happen too often. However, when we average it out, hash tables are constant time (O(1)) even with resizing.
 
6 Various use cases for hash tables

Hash tables reduce operation time greatly just by the nature of this data structure. Because of this reason it makes it extremely fast to search for elements within large data sets. 
Another good use would be to find duplicate elements in a data set, as the values are stored in the cache at first pass and can rapidly check from it if the value has already been stored or not. 
Other use cases may implicate very expensive and / or slow functions such as the fibonacci sequence, which can rapidly become extremely exhaustive for a machine to compute once the numbers start becoming larger. Hash tables allow the previous computation to get stored, and the program just has to essentially search for the last two values added to the cache and add them together, without the need of doing the operations from scratch. 


We expect you to be able to answer questions in these areas. Your responses contribute to your Sprint Challenge grade.

## Instructions

### Task 1: Project Set-Up

- [ ] Create a forked copy of this project
- [ ] Add your team lead as a collaborator on Github
- [ ] Clone your OWN version of the repository (Not Lambda's by mistake!)
- [ ] Create a new branch: git checkout -b `<firstName-lastName>`.
- [ ] Implement the project on your newly created `<firstName-lastName>` branch, committing changes regularly
- [ ] Push commits: git push origin `<firstName-lastName>`

### Task 2: Project Requirements

Your finished project must include all of the following requirements:

- [ ] Solve any three of the five problems

For each problem that you choose to solve, complete the following:

- [ ] Navigate into each exercise's directory
- [ ] Read the instructions for the exercise in the README
- [ ] Implement your solution in the `.py` skeleton file
- [ ] Make sure your code passes the tests running the test script with make tests

*Note: For these exercises, we expect you to use Python's built-in `dict` as a hashtable. That said, if you wish, you can attempt to solve using your own hashtable implementation, as well. All solutions should utilize a `dict` or hashtable. You should not use Sets. (Though you can make a `dict` behave like a set if you wish.)*

### Task 3: Stretch Goals

After finishing your required elements, you can push your work further. These goals may or may not be things you have learned in this module, but they build on the material you just studied. Time allowing, stretch your limits, and see if you can deliver on the following optional goals:

- [ ] Solve any four of the five problems
- [ ] Solve all five problems

## Submission format

Follow these steps to complete your project.

- [ ] Submit a Pull-Request to merge <firstName-lastName> Branch into master (student's  Repo). **Please don't merge your own pull request**
- [ ] Add your team lead as a reviewer on the pull-request
- [ ] Your team lead will count the project as complete after receiving your pull-request

