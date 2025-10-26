"""
Module for managing a simple address book.

Provides classes for contact fields, individual contact records,
and an address book that stores multiple records.
"""

from collections import UserDict


class Field:
    """Base class for contact fields."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Class for contact name."""

    pass


class Phone(Field):
    """Class for phone number."""

    # реалізація класу
    pass


class Record:
    """Class representing a single contact with a name and a list of phones."""

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        pass

    def remove_phone(self, phone):
        pass

    def edit_phone(self, phone):
        pass

    def find_phone(self, phone):
        pass

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """Class representing an address book, where keys are names and values are Record instances."""

    def add_record(self):
        pass

    def find(self):
        pass

    def delete(self):
        pass


book = AddressBook()

john_record = Record("John")
