import unittest
from src.recursion.recursive_floyd import floyd_warshall

class TestFloydWarshall(unittest.TestCase):
    def setUp(self):
        """
        Set up the initial graph for testing.
        """
        self.graph = [
            [0, 3, float('inf'), 7],
            [float('inf'), 0, 1, 2],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        self.expected_result = [
            [0, 3, 4, 5],
            [float('inf'), 0, 1, 2],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0]
        ]

    def test_floyd_warshall(self):
        """
        Test the Floyd-Warshall algorithm implementation on a standard graph.
        """
        result = floyd_warshall(self.graph)
        for i in range(len(self.expected_result)):
            for j in range(len(self.expected_result[i])):
                self.assertEqual(result[i][j], self.expected_result[i][j])

    def test_empty_graph(self):
        """
        Test the Floyd-Warshall algorithm with an empty graph.
        """
        empty_graph = []
        result = floyd_warshall(empty_graph)
        self.assertEqual(result, [])

    def test_single_node_graph(self):
        """
        Test the Floyd-Warshall algorithm with a single-node graph.
        """
        single_node_graph = [[0]]
        result = floyd_warshall(single_node_graph)
        self.assertEqual(result, [[0]])

    def test_disconnected_graph(self):
        """
        Test the Floyd-Warshall algorithm with a graph that has multiple disconnected components.
        """
        disconnected_graph = [
            [0, float('inf'), float('inf')],
            [float('inf'), 0, float('inf')],
            [float('inf'), float('inf'), 0]
        ]
        expected_result = [
            [0, float('inf'), float('inf')],
            [float('inf'), 0, float('inf')],
            [float('inf'), float('inf'), 0]
        ]
        result = floyd_warshall(disconnected_graph)
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
