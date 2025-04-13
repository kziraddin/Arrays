import unittest
from array_ops import insertAtEnd, insertAtBeginning, insertAtIndex

class TestArrayOperations(unittest.TestCase):
    def test_insert_at_end_success(self):
        arr = [0, 0, 0]
        length = 0
        capacity = 3
        success = insertAtEnd(arr, 10, length, capacity)
        self.assertTrue(success)
        self.assertEqual(arr[0], 10)

    def test_insert_at_end_full_array(self):
        arr = [1, 2, 3]
        length = 3
        capacity = 3
        success = insertAtEnd(arr, 4, length, capacity)
        self.assertFalse(success)
        self.assertEqual(arr, [1, 2, 3])

    def test_insert_at_beginning_success(self):
        arr = [0, 0, 0]
        length = 2
        arr[0] = 1
        arr[1] = 2
        capacity = 3
        success = insertAtBeginning(arr, 5, length, capacity)
        self.assertTrue(success)
        self.assertEqual(arr, [5, 1, 2])

    def test_insert_at_index_middle(self):
        arr = [1, 2, 0]
        length = 2
        capacity = 3
        success = insertAtIndex(arr, 5, 1, length, capacity)
        self.assertTrue(success)
        self.assertEqual(arr, [1, 5, 2])

    def test_insert_at_index_invalid_negative(self):
        arr = [0, 0, 0]
        length = 0
        capacity = 3
        success = insertAtIndex(arr, 7, -1, length, capacity)
        self.assertFalse(success)

    def test_insert_at_index_out_of_capacity(self):
        arr = [0, 0, 0]
        length = 3
        capacity = 3
        success = insertAtIndex(arr, 9, 1, length, capacity)
        self.assertFalse(success)

    def test_insert_at_index_edge(self):
        arr = [0, 0, 0]
        length = 1
        arr[0] = 8
        capacity = 3
        success = insertAtIndex(arr, 4, 1, length, capacity)
        self.assertTrue(success)
        self.assertEqual(arr, [8, 4, 0])

if __name__ == '__main__':
    unittest.main()
