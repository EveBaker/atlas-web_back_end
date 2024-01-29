#!/usr/bin/env python3
""" Unit Test
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """nested map test function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
    
    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_message):
        """test exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """test get_json"""
        class Mocked(Mock):
            """mock json"""
            def json(self):
                """mocked json"""
                return test_payload
            
        with patch('requests.get') as MockClass:
            MockClass.return_value = Mocked()
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
        
class TestMemoize(unittest.TestCase):
    """ Test Class to memoize """

    def test_memoize(self):
        """ Test memoize """
        class TestClass:
            """ Test Class """

            def a_method(self):
                """ A method """
                return 42

            @memoize
            def a_property(self):
                """ Decorator """
                return self.a_method()

        test_class = TestClass()
        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)
            mock.assert_called_once()

    if __name__ == "__main__":
        unittest.main()