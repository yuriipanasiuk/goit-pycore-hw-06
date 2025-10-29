"""
Module for managing a simple address book.

Provides classes for contact fields, individual contact records,
and an address book that stores multiple records.
"""

from collections import UserDict


class CustomValueError(Exception):
    """Class for handle custom errors"""

    def __init__(self, message="Something went wrong"):
        self.message = message
        super().__init__(self.message)


class Field:
    """Base class for contact fields."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Class for contact name."""

    def __init__(self, value):
        if not value or not value.strip():
            raise CustomValueError("Name cannot be empty")

        super().__init__(value)


class Phone(Field):
    """Class for phone number."""

    def __init__(self, value):
        validate_value = self.validate_number(value)

        super().__init__(validate_value)

    @staticmethod
    def validate_number(phone_number):
        """Validate phone number"""

        only_digits = "".join(filter(str.isdigit, phone_number))

        if len(only_digits) == 10:
            return only_digits

        raise ValueError(f"Number {phone_number} is invalid, should contain 10 digits")


class Record:
    """Class representing a single contact with a name and a list of phones."""

    def __init__(self, name=None):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        """Validate and add phone number to contact book"""

        validated_number = Phone(phone_number)
        self.phones.append(validated_number)

    def find_phone(self, phone_number):
        """Find phone number in contact book"""

        for number in self.phones:
            if number.value == phone_number:
                return number

        raise CustomValueError(f"Number {phone_number} not found")

    def remove_phone(self, phone_number):
        """Remove phone number from contact book"""

        phone = self.find_phone(phone_number)

        self.phones = list(
            filter(lambda number: number.value != phone.value, self.phones)
        )

        print(f"Phone number {phone_number} removed successfully")

    def edit_phone(self, old_phone_number, new_phone_number):
        """Edit phone number in contact book"""

        validated_new_phone = Phone(new_phone_number)
        phone_to_edit = self.find_phone(old_phone_number)
        if phone_to_edit:
            phone_to_edit.value = validated_new_phone.value
            return

        raise CustomValueError(f"Phone number {old_phone_number} not found.")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """Class representing an address book, where keys are names and values are Record instances."""

    def add_record(self, record):
        """Add recort to contact book"""

        self.data[record.name.value] = record

    def find(self, name):
        """Find contact in contact book"""

        return self.data.get(name)

    def delete(self, name):
        """Delete contact from contact book"""

        if name in self.data:
            del self.data[name]


if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
