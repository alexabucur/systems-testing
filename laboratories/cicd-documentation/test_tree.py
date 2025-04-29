import unittest
from tree import Tree

class TestTree(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        for val in [3, 4, 0, 8, 2]:
            self.tree.add(val)

    def test_find_existing_node(self):
        node = self.tree.find(4)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 4)

    def test_find_nonexistent_node(self):
        node = self.tree.find(10)
        self.assertIsNone(node)

if __name__ == '__main__':
    unittest.main()
