# Recursive Implementation of Floyd-Warshall Algorithm

## Overview

This project implements Floyd-Warshall's algorithm to compute the shortest paths between all pairs of nodes in a graph. The key objective is to implement the algorithm both **recursively** and **iteratively**, and then compare their performance. This repository contains:

- Recursive implementation of Floyd-Warshall (`recursive_floyd.py`)
- Iterative implementation of Floyd-Warshall (`iterative_floyd.py`)
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
```

## Key Files:

1. **`recursive_floyd.py`**:
   - Implements the Floyd-Warshall algorithm recursively without using loops. The graph is defined as an adjacency matrix and the algorithm calculates the shortest path by recursively updating paths between each node.

2. **`iterative_floyd.py`**:
   - Traditional iterative version of Floyd-Warshall with three nested loops to update the shortest paths between all pairs of nodes.

3. **`performance_test.py`**:
   - Compares the performance of both recursive and iterative versions using randomly generated graph data.

4. **`unittests.py`**:
   - Contains unit tests to verify the correctness of the shortest path results from both versions of the algorithm.

## Installation

To set up the project on your local machine:

Clone this repository: 
```bash
git clone https://github.com/sirnicson/floyds_warshall.git
```

Navigate to the project directory:
```bash
cd floyds_warshall
```

Create a virtual environment and activate it:
```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies:
```bash
pip install -r requirements.txt
```


## Usage

Running the Recursive Floyd-Warshall Algorithm To run the recursive version of Floyd-Warshall, execute:
```bash
python3 -m src.recursion.recursive_floyd
```
Running the Iterative Floyd-Warshall Algorithm To run the iterative version of Floyd-Warshall, execute:
```bash
python3 -m src.iterative.iterative_floyd
```

Running Unit Tests To verify the correctness of both versions, run the unit tests:
```bash
python3 -m src.tests.unittests
```

Running Performance Tests To compare the performance of the recursive and iterative implementations,
run the performance test script:
```bash
python3 -m src.tests.performance_test
```
  
![flow chart](https://github.com/user-attachments/assets/1acd6a97-ec71-48d8-b6f0-a003db26ced9)

## Author
sirnicson


