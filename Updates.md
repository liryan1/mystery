# To do
1. Google foo.bar
2. design chess game
3. Interpret prefix, postfix, and infix mathematical expressions
4. Given a string and dictionary, return a string split into two words
5. class for 24 game, remove duplicate solutions
6. Read on Shannon information entropy. Construct Huffman tree from a probability distribution
7. generate nth fibonacci number with O(log n) time

## Questions
1. Merkle tree


# Progress and Notes
Some progress updates

## Questions 4/2
1. In recursive functions, python allows function inside. Say if you need the recursive function to pass in additional parameters. How do we deal with this in C++? define a helper function.
2. LRU Cache #include issue - solved.
3. combinatorics questions such as https://leetcode.com/discuss/interview-question/1603439
4. parallel programming/computing
   - linking multiple computational units to speed up

5. distributed systems
   - storage across multiple factories
   - networking
   - backup systems to deal with failure
6. General considerations for OO design


Ads:
- big data solutions, pipelines, concurrency, serving, ranking (ML)

* include conflict example
  a.cpp
    #include a.h
    #include b.h
      #include a.h
  include guard called pre-compile macro: #ifndef

### OO Design
- error handling
  - error code
  - exception
- think about abstraction (interface)
  - which methods?
  - expandable, but don't over design
  - principle: one object achieves one task
- encapsulation: hide private functions and data, provides public information
  - contract between user and provider
  - user can never change private items
  - separate implementation from usage
- polymorphism
  - interface

### Memory leak
- memory leak: objects do not get deleted and overflows memory
  - delete in destructor
  - after owner , destructor is called
  - shared_ptr (ref counting) - if circular pointer, memory leak still happens
  - python has an automatic detector

- resource management
- software design patterns

## February - March 2022
### 2/19
- Trees, Huffman tree, AVL, Red Black

### 3/5
- Floyd–Warshall algorithm
- topological ordering of graph
- check if graph has cycles

### 3/12 Algorithms
- bit vector, powers of 2
- binary search
- two pointer, sliding window
- sorting
  - trade offs between each
- tree algorithms
  - BFS, DFS, Dijkstra, A*, decision tree - finding something
- Dynamic Programming
- graphs
  - with DP
  - find all cycles with length k
  - relationship with matrices
  - ford fulkerson - min cut max flow
  - random walk

### 3/26 Graphs and OO
- Need to review topological sort & Dijkstra
- **need to do rectangle problem**
- Graph(V, E)
  - Adjacency matrix
    - 0 & 1 edges, cost of edge, probability, or counts
  - Node, edge list
- Floyd-Warshall algorithm
  - understand why the simple algorithm works
  - the fundamentals of DP
- Markov process and its relation to the adjacency matrix
- left multiply a state by the adjacency matrix to obtain the new state
- OOP intro
  - encapsulation
  - polymorphism
  - interface
  - dynamic dispatch & RTTI in C++

# Done
- [x] BST implement insertion and deletion - **DataStructures/BST.py**
- [x] Write code to generate tree test cases - **DataStructures/BST.py**
- [x] Update deserialize code to operate while reading file - **serialize_BST.py**
- [x] construct tree from preorder and inorder traversals - **get_other_traversal.py**
- [x] tree traversal using stack & with O(1) space - **Trees/*.py**
- [x] remove_if - **remove_if.cpp**
- [x] two rectangles, check if overlap - **overlapping_rectangles.cpp**
- [x] LRU cache python