from dataclasses import dataclass
from typing import Union, TypeAlias
from hash_quad import *
import string

MaybeHT: TypeAlias = Union[None, HashTable]     # HashTable or None

@dataclass
class Concordance:

    def __post_init__(self) -> None:
        self.stop_table: MaybeHT = None                     # the hash table for stop words
        self.concordance_table: HashTable = HashTable(191)  # the hash table for concordance

    def load_stop_table(self, filename: str) -> None:
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""

        self.stop_table = HashTable(191)
        try:
            with open(filename, "r") as file:
                for line in file:
                    for word in line.split(): # splits line
                        self.stop_table.insert(word.strip(), None) # strips word and adds into table
        except FileNotFoundError:
            raise FileNotFoundError

    def load_concordance_table(self, filename: str) -> None:
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)

        Process of adding new line numbers for a word (key) in the concordance:
            If word is in table, get current value (list of line numbers), append new line number, insert (key, value)
            If word is not in table, insert (key, value), where value is a Python List with the line number
        If file does not exist, raise FileNotFoundError """

        self.concordance_table = HashTable(191)
        line_num = 1 # line number tracker

        try:
            with open(filename, "r") as file:
                for line in file:
                    new_line = self.process_line(line) # removes punctuation, lower cases
                    split = new_line.split()
                    for word in split:
                        if not self.stop_table.in_table(word): # if word is not in stop word table
                            try:
                                float(word)
                            except ValueError: # if word is not a number
                                if self.concordance_table.get_value(word): # if the line number isn't none
                                    line_numbers = self.concordance_table.get_value(word)
                                    if line_numbers is not None:
                                        if line_num not in line_numbers:
                                            line_numbers += [line_num] # add the line number to the list of line numbers
                                else:
                                    self.concordance_table.insert(word, [line_num]) # if this is a new word, add the line number
                    line_num += 1

        except FileNotFoundError:
            raise FileNotFoundError

        """
        self.concordance_table = HashTable(191)
        line_num = 1

        try:
            with open(filename, "r") as file:
                for line in file:
                    new_line = self.process_line(line)
                    split = new_line.split()
                    for word in split:
                        if not self.stop_table.in_table(word) and not self.is_num(word):
                            if self.concordance_table.get_value(word):
                                line_numbers = self.concordance_table.get_value(word)
                                if line_numbers is not None:
                                    if line_num not in line_numbers:
                                        line_numbers += [line_num]
                            else:
                                self.concordance_table.insert(word, [line_num])
                    line_num += 1  # Increment the line number for the next line

        except FileNotFoundError:
            raise FileNotFoundError
    """

    def process_line(self, line: str) -> None:
        stripped = line.strip()
        word = stripped.lower() # strips and lower cases line
        for char in word:
            if char == "'":
                word = word.replace(char, "")
            if char in string.punctuation:
                word = word.replace(char, " ")
        return word


    def write_concordance(self, filename: str) -> None:
        """ Write the concordance entries to the output file(filename)
        See sample output files for format. """

        lst = []
        with open(filename, "w") as file:
            for word in self.concordance_table.hash_table:
                if word is not None:
                    lst.append((word[0], word[1])) # append word and the list of line numbers
            sort = sorted(lst) # alphabetical order
            for i in range(len(sort)):
                word = sort[i][0]
                line_nums = sort[i][1]
                string = " ".join([str(num) for num in line_nums]) # join into string
                file.write(word + ": " + string)
                if i < len(sort) - 1 and word != sort[i + 1][0]:
                    file.write("\n") # move to next line


        

