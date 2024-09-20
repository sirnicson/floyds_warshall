# Recursive Implementation of Floyd-Warshall Algorithm

## Overview

This project implements Floyd-Warshall's algorithm to compute the shortest paths between all pairs of nodes in a graph. The key objective is to implement the algorithm both recursively and iteratively, and then compare their performance. This repository contains:

- Recursive implementation of Floyd-Warshall (recursive_floyd.py)
- Iterative implementation of Floyd-Warshall (iterative_floyd.py)
- Unittests to verify correctness
- Performance tests to compare efficiency

## Project Structure                            

```plaintext
.
├── src
│   ├── recursion
│   │   └── recursive_floyd.py        # Recursive Floyd-Warshall algorithm implementation
│   ├── iterative
│   │   └── iterative_floyd.py        # Iterative Floyd-Warshall algorithm implementation
│   ├── tests
│   │   ├── performance_test.py       # Performance tests comparing recursive and iterative versions
│   │   └── unittests.py              # Unit tests to check correctness of both versions
├── README.md                         # Project documentation
├── requirements.txt                  # Project dependencies for installation


## Key Files:

1. **`recursive_floyd.py`**:
   - Implements the Floyd-Warshall algorithm recursively without using loops. The graph is defined as an adjacency matrix, and the algorithm calculates the shortest path by recursively updating paths between each node.

2. **`iterative_floyd.py`**:
   - Traditional iterative version of Floyd-Warshall with three nested loops to update the shortest paths between all pairs of nodes.

3. **`performance_test.py`**:
   - Compares the performance of both recursive and iterative versions using randomly generated graph data.

4. **`unittests.py`**:
   - Contains unit tests to verify the correctness of the shortest path results from both versions of the algorithm.

## Installation

To set up the project on your local machine:

1. Clone this repository:

   ```bash
   git clone https://github.com/sirnicson/floyds_warshall.git

