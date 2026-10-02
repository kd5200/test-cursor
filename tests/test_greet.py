import unittest

from src.greet import greet


class GreetTests(unittest.TestCase):
    def test_greets_by_name(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_includes_title(self):
        self.assertEqual(greet("Lovelace", title="Dr."), "Hello, Dr. Lovelace!")

    def test_strips_whitespace(self):
        self.assertEqual(greet("  Grace  "), "Hello, Grace!")

    def test_rejects_blank_name(self):
        with self.assertRaises(ValueError):
            greet("   ")


if __name__ == "__main__":
    unittest.main()
