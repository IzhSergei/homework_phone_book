import unittest
from model import PhoneBook, Contact, FileHandler
from exceptions import ContactNotFoundError

class TestPhoneBook(unittest.TestCase):
    def setUp(self):
        """Настройка перед каждым тестом."""
        self.phone_book = PhoneBook()

    def test_add_contact(self):
        """Тест добавления контакта."""
        contact = Contact("Иванов Иван", "1234567890", "друг")
        self.phone_book.add_contact(contact)
        self.assertEqual(len(self.phone_book.get_all_contacts()), 1)

    def test_find_contact(self):
        """Тест поиска контакта."""
        contact1 = Contact("Иванов Иван", "1234567890", "друг")
        contact2 = Contact("Петров Петр", "0987654321", "коллега")
        self.phone_book.add_contact(contact1)
        self.phone_book.add_contact(contact2)
        result = self.phone_book.find_contacts("Иван")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Иванов Иван")

    def test_delete_contact(self):
        """Тест удаления контакта."""
        contact = Contact("Иванов Иван", "1234567890", "друг")
        self.phone_book.add_contact(contact)
        with self.assertRaises(ContactNotFoundError):
            self.phone_book.delete_contact(2)  # Несуществующий ID
        self.phone_book.delete_contact(1)
        self.assertEqual(len(self.phone_book.get_all_contacts()), 0)

    def test_update_contact(self):
        """Тест обновления контакта."""
        contact = Contact("Иванов Иван", "1234567890", "друг")
        self.phone_book.add_contact(contact)
        updated_contact = Contact("Сидоров Сидр", "9998887777", "знакомый")
        self.phone_book.update_contact(1, updated_contact)
        contacts = self.phone_book.get_all_contacts()
        self.assertEqual(contacts[0].name, "Сидоров Сидр")
        self.assertEqual(contacts[0].phone, "9998887777")
        self.assertEqual(contacts[0].comment, "знакомый")

    def test_load_from_file(self):
        """Тест загрузки данных из файла."""
        file_handler = FileHandler()
        phone_book = file_handler.load_from_file("test_phone_book.txt")  # Создайте файл test_phone_book.txt для теста
        contacts = phone_book.get_all_contacts()
        self.assertGreater(len(contacts), 0)

    def test_save_to_file(self):
        """Тест сохранения данных в файл."""
        contact = Contact("Иванов Иван", "1234567890", "друг")
        self.phone_book.add_contact(contact)
        file_handler = FileHandler()
        try:
            file_handler.save_to_file(self.phone_book, "test_save_phone_book.txt")
            with open("test_save_phone_book.txt", "r", encoding="UTF-8") as file:
                data = file.readlines()
                self.assertEqual(len(data), 1)
                self.assertIn("Иванов Иван;1234567890;друг", data[0])
        except Exception as e:
            self.fail(f"Ошибка при сохранении: {e}")

if __name__ == "__main__":
    unittest.main()