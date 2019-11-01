import unittest
from DynamicArray import *


class TestDynamicArray(unittest.TestCase):
    global my_array
    my_array = DynamicArray()

    def test_append(self):
        my_array.append(1)
        self.assertEqual(my_array[0], 1)
        my_array.append(2)
        self.assertEqual(my_array[1], 2)
        my_array.append(9)
        self.assertEqual(my_array[2], 9)
        my_array.append(4)
        self.assertEqual(my_array[3], 4)
        my_array.append(5)
        self.assertEqual(my_array[4], 5)

    def test_pop(self):
        my_array.pop()
        self.assertFalse(5 in my_array)

    def test_delete(self):
        my_array.delete(2)
        self.assertFalse(9 in my_array)
        self.assertTrue(1 in my_array)
        self.assertTrue(4 in my_array)
        self.assertEqual(my_array[2], 4)


if __name__ == '__main__':
    unittest.main()
