"""
This module implements Floyd's Algorithm (Floyd-Warshall) to compute the shortest paths between all pairs of nodes in a graph.
It contains four main functions:
    main -> controls the execution of the script by initializing and running the Floyd-Warshall algorithm
    print_out_graph -> prints out the graph with nodes and distances, replacing unreachable paths with a marker
    recursive_floyd_warshall -> recursively computes shortest paths by considering each node as an intermediate node
    floyd_warshall -> serves as a wrapper function to initialize and invoke the recursive Floyd-Warshall process

The global variables are:
    NO_PATH = Marker for where there is no path (set to the maximum integer value)
    GRAPH = The adjacency matrix representing the graph, where distances are stored
    MAX_LENGTH = The number of nodes in the graph
    MIN_LEVEL = The lowest search level (used in recursive processing, though it's not directly applied in the code)
    NO_PATH_MARKER = Placeholder for unreachable paths used when printing the graph
"""
from sys import maxsize

# Global constants
NO_PATH = maxsize
GRAPH = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(GRAPH[0])
MIN_LEVEL = 0
NO_PATH_MARKER = "No Path"

copy_GRAPH = GRAPH

def main():
    """
    Main function to initialize the Floyd-Warshall algorithm and print the results.
    """
    # Create a copy of the GRAPH matrix to avoid modifying the global matrix directly
    matrix_copy = [row[:] for row in copy_GRAPH]

    # Start the recursive process
    result_matrix = floyd_warshall(matrix_copy)

    # Update the global GRAPH matrix with the result
    global GRAPH
    GRAPH = result_matrix

    # Print the final shortest path distances
    print_out_graph()


def print_out_graph():
    """
    Print out the graph with distances and placeholders for no path.
    """
    for start_node in range(MAX_LENGTH):
        for end_node in range(MAX_LENGTH):
            distance = GRAPH[start_node][end_node]
            if distance == NO_PATH:
                distance = NO_PATH_MARKER

            print(f"Distance from Node {start_node} to Node {end_node} is {distance}")


def recursive_floyd_warshall(matrix, k):
    """
    Recursive implementation of Floyd-Warshall Algorithm.

    :param matrix: The adjacency matrix representing the graph.
    :param k: The current intermediate node being considered.
    """
    n = len(matrix)

    # Base Case: All nodes processed
    if k >= n:
        return

    # Update distances using the current node as an intermediate node
    for i in range(n):
        for j in range(n):
            if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

    # Recursive call to process the next node
    recursive_floyd_warshall(matrix, k + 1)


def floyd_warshall(matrix):
    """
    Wrapper function to initialize and call the recursive Floyd-Warshall function.

    :param matrix: The adjacency matrix representing the graph.
    :return: The shortest path matrix.
    """
    matrix_copy = [row[:] for row in matrix]  # Create a copy of the matrix to avoid modifying the original
    recursive_floyd_warshall(matrix_copy,0)
    return matrix_copy


if __name__ == "__main__":
    main()
