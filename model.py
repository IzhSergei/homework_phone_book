from exceptions import FileLoadError, FileSaveError, ContactNotFoundError

class Contact:
    def __init__(self, name: str, phone: str, comment: str):
        self.name = name
        self.phone = phone
        self.comment = comment

    def to_string(self) -> str:
        return f"{self.name};{self.phone};{self.comment}"

    def __str__(self):
        return f"{self.name:<20} {self.phone:<20} {self.comment:<20}"

class PhoneBook:
    def __init__(self):
        self.contacts: dict[int, Contact] = {}
        self.next_id: int = 1

    def add_contact(self, contact: Contact):
        self.contacts[self.next_id] = contact
        self.next_id += 1

    def find_contacts(self, keyword: str) -> list[Contact]:
        result = []
        for contact in self.contacts.values():
            if keyword.lower() in contact.name.lower() or keyword in contact.phone:
                result.append(contact)
        return result

    def delete_contact(self, contact_id: int):
        if contact_id not in self.contacts:
            raise ContactNotFoundError(contact_id)
        del self.contacts[contact_id]

    def update_contact(self, contact_id: int, updated_contact: Contact):
        if contact_id not in self.contacts:
            raise ContactNotFoundError(contact_id)
        self.contacts[contact_id] = updated_contact

    def get_all_contacts(self) -> list[Contact]:
        return list(self.contacts.values())

class FileHandler:
    @staticmethod
    def load_from_file(filename: str) -> PhoneBook:
        phone_book = PhoneBook()
        try:
            with open(filename, 'r', encoding='UTF-8') as file:
                for line in file:
                    data = line.strip().split(';')
                    if len(data) == 3:
                        contact = Contact(data[0], data[1], data[2])
                        phone_book.add_contact(contact)
        except FileNotFoundError:
            raise FileLoadError(filename)
        return phone_book

    @staticmethod
    def save_to_file(phone_book: PhoneBook, filename: str):
        try:
            with open(filename, 'w', encoding='UTF-8') as file:
                for contact in phone_book.get_all_contacts():
                    file.write(contact.to_string() + '\n')
        except Exception as e:
            raise FileSaveError(filename) from e