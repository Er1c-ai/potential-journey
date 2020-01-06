import unittest
import operator
import argparse
from sort_this import SortingData


class TestSortingMethods(unittest.TestCase):

    def setUp(self):
        self.sort = SortingData()
        self.data = [['Product', ' Color', ' Amount'], ['Vans', ' Blue', ' 10.00'], ['Nike', ' Red', ' 20.00'],
                    ['Nike', ' Green', ' 10.00'], ['New Balance', ' White', ' 50.00'], ['Adidas', ' Blue', ' 30.00']]

    def test_not_equal_sorting_ascending(self):
        new_output = self.sort.sort_by_ascending_amount(self.data)
        self.assertNotEqual(list(self.data), new_output)

    def test_equal_sorting_ascending(self):
        new_output = self.sort.sort_by_ascending_amount(self.data)
        self.assertTrue(list(self.data), new_output)

    def test_not_equal_sorting_ascending_product_color_amount(self):
        new_output = self.sort.sort_by_ascending_product_color_amount(self.data)
        self.assertNotEqual(list(self.data), new_output)

    def test_equal_sorting_ascending_product_color_amount(self):
        new_output = self.sort.sort_by_ascending_product_color_amount(self.data)
        self.assertTrue(list(self.data), new_output)

    def test_not_equal_sorting_descending_product_color_amount(self):
        new_output = self.sort.sort_by_descending_product_color_amount(self.data)
        self.assertNotEqual(list(self.data), new_output)

    def test_equal_sorting_descending_product_color_amount(self):
        new_output = self.sort.sort_by_descending_product_color_amount(self.data)
        self.assertTrue(list(self.data), new_output)

    def test_none_should_fail(self):
        self.assertRaises(TypeError, self.sort.sort_by_ascending_amount(self.data), None)

    def test_non_string_should_fail(self):
        self.assertRaises(TypeError, self.sort.sort_by_descending_product_color_amount(self.data), 234)

    def test_assert_is_instance_ascending(self):
        self.assertIsInstance(self.sort.sort_by_ascending_amount(self.data), list)

    def test_assert_is_instance_ascending_product_color_amount(self):
        self.assertIsInstance(self.sort.sort_by_ascending_product_color_amount(self.data), list)

    def test_assert_is_instance_descending_product_color_amount(self):
        self.assertIsInstance(self.sort.sort_by_descending_product_color_amount(self.data), list)

if __name__ == "__main__":
    unittest.main()

