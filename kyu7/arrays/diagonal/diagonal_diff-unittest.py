__author__ = "Shiven"

import unittest
from unittest.mock import patch
from diagonal_diff import diff

class TestDiagonalDiff(unittest.TestCase):

    @patch("builtins.input", lambda: "")
    def test_diagonal_diff_1(self):
        self.assertEqual(diff(), 4)
