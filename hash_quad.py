from dataclasses import dataclass
from typing import List, Any, Optional

@dataclass
class HashTable:
    table_size: int                                         # Initial hash table size

    def __post_init__(self) -> None:
        self.hash_table: List = [None]*self.table_size      # Hash table
        self.num_items: int = 0                             # Empty hash table

    def insert(self, key: str, value: Any) -> None:
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is in the table, the new value replaces the existing value.
        When used with the concordance, value is a Python List of line numbers.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""

        hash_value = self.horner_hash(key)
        index = 0
        for i in range(self.table_size):
            index = (hash_value + i ** 2) % self.table_size # quadratic probing
            if self.hash_table[index] is None: # if index is empty
                self.hash_table[index] = (key, value) # add key and value
                self.num_items += 1
                break
            elif self.hash_table[index][0] == key: # if key is already in table
                self.hash_table[index] = (key, value) # new value replaces existing value
                break

        if self.get_load_factor() > 0.5: #resizing
            self.resize()

    def resize(self) -> None:
        self.table_size = self.table_size * 2 + 1
        new_table = HashTable(self.table_size)

        for cell in self.hash_table:
            if cell is not None:
                new_table.insert(cell[0], cell[1]) # inserts key and value into the new table

        self.hash_table = new_table.hash_table
        self.table_size = new_table.table_size
        self.num_items = new_table.num_items


    def horner_hash(self, key: str) -> int:
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""

        h = 0
        n = min(8, len(key))
        for i in range(n):
            h = (31 * h) + ord(key[i])
        return h % self.table_size

    def in_table(self, key: str) -> bool:
        """ Returns True if key is in an entry of the hash table, False otherwise. Must be O(1)."""
        index = self.get_index(key)
        return index is not None

    def get_index(self, key: str) -> Optional[int]:
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None. Must be O(1)."""

        index = self.horner_hash(key)
        j = 0
        for i in range(self.table_size):
            j = (index + i ** 2) % self.table_size # uses quadratic probing to find the index
            if self.hash_table[j] and self.hash_table[j][0] == key:
                return j
        return None


    def get_all_keys(self) -> List:
        """ Returns a Python list of all keys in the hash table."""

        keys = []
        for value in self.hash_table:
            if value is not None:
                keys.append(value[0])
        return keys

    def get_value(self, key: str) -> Any:
        """ Returns the value (for concordance, list of line numbers) associated with the key.
        If key is not in hash table, returns None. Must be O(1)."""
        index = self.get_index(key)
        if index is not None:
            return self.hash_table[index][1]
        return None


    def get_num_items(self) -> int:
        """ Returns the number of entries (words) in the table. Must be O(1)."""
        return self.num_items

    def get_table_size(self) -> int:
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self) -> float:
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.num_items / self.table_size
