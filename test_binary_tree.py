"""Запуск из папки проекта: python -m unittest -v"""
import random
import unittest

from binary_tree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    def assert_tree(self, tree, values):
        """Проверяем содержимое, размер, отсутствие циклов и границы всех узлов."""
        seen = set()
        stack = [(tree.root, None, None)]
        while stack:
            node, lower, upper = stack.pop()
            if node is None:
                continue
            self.assertNotIn(id(node), seen, "Цикл или общий дочерний узел")
            seen.add(id(node))
            if lower is not None:
                self.assertGreater(node.value, lower)
            if upper is not None:
                self.assertLessEqual(node.value, upper)
            stack.append((node.left, lower, node.value))
            stack.append((node.right, node.value, upper))
        self.assertEqual(len(seen), len(values))
        self.assertEqual(len(tree), len(values))
        self.assertEqual(tree.inorder(), sorted(values))

    def test_empty_tree(self):
        tree = BinarySearchTree()
        self.assertIsNone(tree.root)
        self.assertIsNone(tree.search(10))
        self.assertNotIn(10, tree)
        self.assertFalse(tree.delete(10))
        for traversal in (tree.inorder, tree.preorder, tree.postorder):
            self.assertEqual(traversal(), [])
        self.assert_tree(tree, [])

    def test_insert_first_node(self):
        tree = BinarySearchTree()
        self.assertIsNone(tree.insert(10))
        self.assertEqual(tree.root.value, 10)
        self.assert_tree(tree, [10])

    def test_insert_left_and_right(self):
        tree = BinarySearchTree([10, 5, 15])
        self.assertEqual(tree.root.left.value, 5)
        self.assertEqual(tree.root.right.value, 15)
        self.assert_tree(tree, [10, 5, 15])

    def test_search_existing_and_missing(self):
        values = [12, 6, 17, 3, 7, 15, 31, 9]
        tree = BinarySearchTree(values)
        for value in values:
            self.assertEqual(tree.search(value).value, value)
            self.assertIn(value, tree)
        self.assertIsNone(tree.search(100))
        self.assertNotIn(100, tree)

    def test_duplicates_go_left(self):
        tree = BinarySearchTree([5, 5, 5])
        self.assertEqual(tree.root.left.left.value, 5)
        self.assert_tree(tree, [5, 5, 5])

    def test_delete_missing_does_not_change_tree(self):
        tree = BinarySearchTree([5, 2, 8])
        before = tree.preorder()
        self.assertFalse(tree.delete(99))
        self.assertEqual(tree.preorder(), before)
        self.assert_tree(tree, [5, 2, 8])

    def test_delete_leaf(self):
        tree = BinarySearchTree([10, 5, 15])
        self.assertTrue(tree.delete(5))
        self.assertIsNone(tree.root.left)
        self.assert_tree(tree, [10, 15])

    def test_delete_node_with_left_child(self):
        tree = BinarySearchTree([10, 5, 3])
        self.assertTrue(tree.delete(5))
        self.assertEqual(tree.root.left.value, 3)
        self.assert_tree(tree, [10, 3])

    def test_delete_node_with_right_child(self):
        tree = BinarySearchTree([10, 15, 17])
        self.assertTrue(tree.delete(15))
        self.assertEqual(tree.root.right.value, 17)
        self.assert_tree(tree, [10, 17])

    def test_delete_only_root(self):
        tree = BinarySearchTree([10])
        self.assertTrue(tree.delete(10))
        self.assertIsNone(tree.root)
        self.assert_tree(tree, [])

    def test_delete_root_with_one_child(self):
        for child in (5, 15):
            with self.subTest(child=child):
                tree = BinarySearchTree([10, child])
                self.assertTrue(tree.delete(10))
                self.assertEqual(tree.root.value, child)
                self.assert_tree(tree, [child])

    def test_delete_root_with_two_children(self):
        tree = BinarySearchTree([10, 5, 15])
        self.assertTrue(tree.delete(10))
        self.assert_tree(tree, [5, 15])

    def test_delete_internal_node_with_two_children(self):
        values = [20, 10, 30, 5, 15, 12, 17]
        tree = BinarySearchTree(values)
        self.assertTrue(tree.delete(10))
        values.remove(10)
        self.assert_tree(tree, values)

    def test_predecessor_has_left_child(self):
        values = [20, 10, 30, 15, 13]
        tree = BinarySearchTree(values)
        self.assertTrue(tree.delete(20))
        values.remove(20)
        self.assert_tree(tree, values)

    def test_delete_with_duplicate_replacement_candidates(self):
        # Минимум справа повторяется: важно не нарушить строгое > справа.
        values = [10, 5, 15, 12, 12, 5, 4]
        tree = BinarySearchTree(values)
        for value in [10, 12, 5]:
            self.assertTrue(tree.delete(value))
            values.remove(value)
            self.assert_tree(tree, values)

    def test_delete_one_duplicate_at_a_time(self):
        tree = BinarySearchTree([5, 5, 5])
        for remaining in (2, 1, 0):
            self.assertTrue(tree.delete(5))
            self.assert_tree(tree, [5] * remaining)
        self.assertFalse(tree.delete(5))

    def test_minimum_and_maximum(self):
        tree = BinarySearchTree([3, -7, 0, 12, 3])
        self.assertEqual(tree.minimum(), -7)
        self.assertEqual(tree.maximum(), 12)
        tree.delete(-7)
        tree.delete(12)
        self.assertEqual(tree.minimum(), 0)
        self.assertEqual(tree.maximum(), 3)

    def test_empty_minimum_and_maximum_raise(self):
        tree = BinarySearchTree()
        with self.assertRaises(ValueError):
            tree.minimum()
        with self.assertRaises(ValueError):
            tree.maximum()

    def test_all_traversals(self):
        tree = BinarySearchTree([12, 6, 17, 3, 7, 15, 31, 9])
        self.assertEqual(tree.inorder(), [3, 6, 7, 9, 12, 15, 17, 31])
        self.assertEqual(tree.preorder(), [12, 6, 3, 7, 9, 17, 15, 31])
        self.assertEqual(tree.postorder(), [3, 9, 7, 6, 15, 31, 17, 12])

    def test_strings(self):
        tree = BinarySearchTree(["b", "a", "c", "b"])
        self.assertTrue(tree.delete("b"))
        self.assert_tree(tree, ["a", "b", "c"])

    def test_degenerate_tree_without_recursion_limit(self):
        for values in (list(range(1500)), list(range(1499, -1, -1))):
            with self.subTest(first=values[0]):
                tree = BinarySearchTree(values)
                self.assert_tree(tree, values)
                self.assertEqual(tree.preorder(), values)
                self.assertEqual(tree.postorder(), values[::-1])
                self.assertIn(values[-1], tree)
                self.assertTrue(tree.delete(values[-1]))
                self.assert_tree(tree, values[:-1])

    def test_random_operations_against_list(self):
        # Независимая модель: обычный список хранит ожидаемые значения.
        rng = random.Random(42)
        tree = BinarySearchTree()
        expected = []
        for step in range(500):
            value = rng.randint(-20, 20)
            with self.subTest(step=step, value=value):
                if rng.random() < 0.55:
                    tree.insert(value)
                    expected.append(value)
                else:
                    existed = value in expected
                    self.assertEqual(tree.delete(value), existed)
                    if existed:
                        expected.remove(value)
                self.assertEqual(value in tree, value in expected)
                self.assert_tree(tree, expected)
        for value in expected.copy():
            self.assertTrue(tree.delete(value))
            expected.remove(value)
            self.assert_tree(tree, expected)
        tree.insert(99)
        self.assert_tree(tree, [99])


if __name__ == "__main__":
    unittest.main(verbosity=2)
