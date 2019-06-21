import unittest
from name_function import get_formatted_name
class NamesTestCase(unittest.TestCase):
    """测试 name_function.py"""
    def test_first_last_name(self):
        """能够正确地处理像 Janis Joplin 这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    def test_first_last_middle_name(self):
             """能够正确地处理像 Wolfgang Amadeus Mozart 这样的姓名吗？"""
             formatted_name = get_formatted_name(
                 'wolfgang', 'mozart', 'amadeus')
             self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
unittest.main()