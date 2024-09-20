# src/tests/performance_test.py

"""
This module contains a simple performance test which
compares the recursive version of Floyd's algorithm with the
iterative version.
"""

import sys
sys.path.append('..')

from src.recursion.recursive_floyd import GRAPH
from src.recursion.recursive_floyd import recursive_floyd_warshall
from src.iterative.iterative_floyd import iterative_floyd
from time import process_time


def performance_test(function_handle, *args):
    """
    A function that performs a simple performance test.
    function_handle -> The function which is being tested.
    *args -> Arguments to pass to the function being tested.
    """

    # Measure start time
    start_time = process_time()

    # Execute the function
    function_handle(*args)

    # Measure end time
    end_time = process_time()

    # Calculate elapsed time
    elapsed_time = end_time - start_time

    # Print the elapsed time
    print(f"Elapsed time: {elapsed_time:.6f} seconds")


# Print and test the recursive Floyd-Warshall implementation
print("Recursion Test Time")
performance_test(recursive_floyd_warshall, GRAPH, 0)  # Pass the graph and starting node 'k'

# Print and test the iterative Floyd-Warshall implementation
print("Iterative Test Time")
performance_test(iterative_floyd)  # Pass the graph for the iterative version
