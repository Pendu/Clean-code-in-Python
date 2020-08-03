from unittest import TestCase
import pytest
from Uop.caveats import wrong_user_display, Correct_user_display, BadList, GoodList
import unittest

class TestWrongUserDisplay(TestCase):
    def test_wrong_user_display(self):
        user = wrong_user_display()
        self.assertEqual(user.split()[0], "john")
        self.assertEqual(user.split()[1], "30")


class TestCorrectUserDisplay(TestCase):
    def test_correct_user_display(self):
        user = Correct_user_display()
        self.assertEqual(user.split()[0], "john")
        self.assertEqual(user.split()[1], "30")


class TestBadList(TestCase):
    def test_bad_list(self):
        u = BadList([i for i in range(0, 10)])
        self.assertEqual(u[0], "[even] 0")
        self.assertEqual(u[-1], "[odd] 9")
        self.assertRaises(TypeError, str.join, u)


class TestGoodList(TestCase):
    def test_good_l ist(self):
        u1 = GoodList([i for i in range(0,2)])
        self.assertEqual(u1[0], "[even] 0")
        self.assertEqual(u1[-1], "[odd] 1")
        self.assertEqual("; ".join(u1),"[even] 0; [odd] 1")
