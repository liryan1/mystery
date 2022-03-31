# To do
2. Interpret prefix, postfix, and infix mathematical expressions
3. Given a string and dictionary, return a string split into two words
4. class for 24 game, remove duplicate solutions
7. Read on Shannon information entropy. Construct Huffman tree from a probability distribution
8. generate nth fibonacci number with O(log n) time

# System Design Questions
* You have a server that can handle 10 requests per second. How would you handle a situation when 20 requests come?

# Questions
1. In recursive functions, python allows function inside. Say if you need the recursive function to pass in additional parameters. How do we deal with this in C++?
2. LRU Cache #include issue
3. distributed systems, parallel programming
4. General considerations for OO design
5. 

# Progress and Notes
Some progress updates

## 2/19
- Trees, Huffman tree, AVL, Red Black

## 3/5
- Floyd–Warshall algorithm
- topological ordering of graph
- check if graph has cycles

## 3/12 Algorithms
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

## 3/26 Graphs and OO
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