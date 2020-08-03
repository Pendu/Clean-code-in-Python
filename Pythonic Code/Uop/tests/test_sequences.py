import pytest
from unittest import TestCase
from Uop.sequences import Items

class TestSequence(TestCase):
    def test_items(self):
        items = Items(1,2,3,4,5)
        self.assertEqual(items[-1], 5)

# @pytest.fixture()
# def items():
#     return Items(1,2,3,4,5)
#
# def test_items(items):
#
#     assert items[-1] == 5
