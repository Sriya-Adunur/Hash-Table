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
        If the key is is in the table, the new value replaces the existing value.
        When used with the concordance, value is a Python List of line numbers.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""

    def horner_hash(self, key: str) -> int:
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""

    def in_table(self, key: str) -> bool:
        """ Returns True if key is in an entry of the hash table, False otherwise. Must be O(1)."""

    def get_index(self, key: str) -> Optional[int]:
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None. Must be O(1)."""

    def get_all_keys(self) -> List:
        """ Returns a Python list of all keys in the hash table."""

    def get_value(self, key: str) -> Any:
        """ Returns the value (for concordance, list of line numbers) associated with the key.
        If key is not in hash table, returns None. Must be O(1)."""

    def get_num_items(self) -> int:
        """ Returns the number of entries (words) in the table. Must be O(1)."""

    def get_table_size(self) -> int:
        """ Returns the size of the hash table."""

    def get_load_factor(self) -> float:
        """ Returns the load factor of the hash table (entries / table_size)."""

