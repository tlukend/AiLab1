import unittest


class MyTestCase(unittest.TestCase):
    def test_algorithm(self):

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
    # # testing if the heuristic works
    # h = HeuristicHamming()
    # n = Node(grid_list[0], 0)
    # print(h.calculate(n, n.state, grid_goal))
