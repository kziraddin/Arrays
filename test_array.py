import unittest
from array_ops import insertAtEnd, insertAtBeginning, insertAtIndex, removeEnd, removeAtIndex, sortArray

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

    def test_remove_end_success(self):
        arr = [1, 2, 3, 0, 0]
        length = 3
        result = removeEnd(arr, length)
        self.assertTrue(result)
        self.assertEqual(arr[:3], [1, 2, 0])

    def test_remove_end_empty_array(self):
        arr = [0, 0, 0]
        length = 0
        result = removeEnd(arr, length)
        self.assertFalse(result)
        self.assertEqual(arr, [0, 0, 0])

    def test_remove_at_index_success(self):
        arr = [1, 2, 3, 4, 0]
        length = 4
        result = removeAtIndex(arr, 1, length)
        self.assertTrue(result)
        self.assertEqual(arr[:4], [1, 3, 4, 0])

    def test_remove_at_index_invalid_negative(self):
        arr = [1, 2, 3, 4]
        length = 4
        result = removeAtIndex(arr, -1, length)
        self.assertFalse(result)

    def test_remove_at_index_out_of_range(self):
        arr = [1, 2, 3, 4]
        length = 4
        result = removeAtIndex(arr, 4, length)
        self.assertFalse(result)

    def test_sort_array_unsorted(self):
        arr = [5, 2, 9, 1, 5, 6]
        result = sortArray(arr)
        self.assertEqual(result, [1, 2, 5, 5, 6, 9])

    def test_sort_array_already_sorted(self):
        arr = [1, 2, 3, 4]
        result = sortArray(arr)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_sort_array_empty(self):
        arr = []
        result = sortArray(arr)
        self.assertEqual(result, [])

    def test_sort_array_single_element(self):
        arr = [42]
        result = sortArray(arr)
        self.assertEqual(result, [42])
    

if __name__ == '__main__':
    unittest.main()
