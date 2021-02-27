import unittest

from mmr import remove_node


class MyTestCase(unittest.TestCase):

    def test_remove_node(self):
        with self.assertRaises(Exception) as e:
            remove_node("", "", "")

        self.assertTrue(type(e.exception) in [FileNotFoundError])
