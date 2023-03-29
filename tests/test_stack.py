""" тесты с использованием unittest для модуля stack."""
import unittest

from src import stack
from src.stack import Node, Stack

class TestSteck(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.top.data, 3)
        self.assertEqual(stack.top.next_node.data, 2)
        self.assertEqual(stack.top.next_node.next_node.data, 1)

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.top.data, 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.top.data, 1)
        self.assertEqual(stack.pop(), 1)
        self.assertIsNone(stack.top)


if __name__ == '__main__':
    unittest.main()




