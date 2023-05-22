import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_01a(self) -> None:
        ht = HashTable(7)
        self.assertEqual(ht.get_table_size(), 7)

    def test_01b(self) -> None:
        ht = HashTable(7)
        self.assertEqual(ht.get_num_items(), 0)

    def test_01c(self) -> None:
        ht = HashTable(7)
        self.assertAlmostEqual(ht.get_load_factor(), 0)

    def test_01d(self) -> None:
        ht = HashTable(7)
        self.assertEqual(ht.get_all_keys(), [])

    def test_01e(self) -> None:
        ht = HashTable(7)
        self.assertEqual(ht.in_table("cat"), False)

    def test_01f(self) -> None:
        ht = HashTable(7)
        self.assertEqual(ht.get_value("cat"), None)

    def test_01g(self) -> None:
        ht = HashTable(7)
        self.assertEqual(ht.get_index("cat"), None)

    def test_01h(self) -> None:
        ht = HashTable(7)
        self.assertEqual(ht.horner_hash("cat"), 3)

    def test_02a(self) -> None:
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.get_table_size(), 7)

    def test_02b(self) -> None:
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.get_num_items(), 1)

    def test_02c(self) -> None:
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)

    def test_02d(self) -> None:
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_02e(self) -> None:
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.in_table("cat"), True)

    def test_02f(self) -> None:
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.get_value("cat"), [5])

    def test_02g(self) -> None:
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.get_index("cat"), 3)

    def test_03(self) -> None:
        ht = HashTable(7)
        ht.insert("cat", [5])
        ht.insert("cat", [5, 17])
        self.assertEqual(ht.get_value("cat"), [5, 17])

    def test_04(self) -> None:
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.get_index("cat"), 3)

        ht.insert("dog", [8])
        self.assertEqual(ht.get_num_items(), 2)
        self.assertEqual(ht.get_index("dog"), 6)
        self.assertAlmostEqual(ht.get_load_factor(), 2 / 7)

        ht.insert("mouse", [10])
        self.assertEqual(ht.get_num_items(), 3)
        self.assertEqual(ht.get_index("mouse"), 4)
        self.assertAlmostEqual(ht.get_load_factor(), 3 / 7)

        ht.insert("elephant", [12]) # hash table should be resized
        self.assertEqual(ht.get_num_items(), 4)
        self.assertEqual(ht.get_table_size(), 15)
        self.assertAlmostEqual(ht.get_load_factor(), 4 / 15)
        self.assertEqual(ht.get_index("cat"), 12)
        self.assertEqual(ht.get_index("dog"), 14)
        self.assertEqual(ht.get_index("mouse"), 13)
        self.assertEqual(ht.get_index("elephant"), 9)
        keys = ht.get_all_keys()
        keys.sort()
        self.assertEqual(keys, ["cat", "dog", "elephant", "mouse"])

if __name__ == '__main__':
   unittest.main()
