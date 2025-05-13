import unittest
from solution import Solution

class TestCanFinish(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_simple_case(self):
        self.assertTrue(self.solution.canFinish(2, [[1, 0]]))

    def test_cycle_case(self):
        self.assertFalse(self.solution.canFinish(2, [[1, 0], [0, 1]]))

    def test_larger_dag(self):
        self.assertTrue(self.solution.canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]]))

    def test_complex_cycle(self):
        self.assertFalse(self.solution.canFinish(3, [[1, 0], [2, 1], [0, 2]]))

    def test_no_prerequisites(self):
        self.assertTrue(self.solution.canFinish(3, []))

    def test_single_course(self):
        self.assertTrue(self.solution.canFinish(1, []))

if __name__ == "__main__":
    unittest.main()