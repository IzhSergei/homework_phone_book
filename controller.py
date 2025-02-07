from model import PhoneBook, FileHandler, Contact
from view import View
from exceptions import FileLoadError, FileSaveError, ContactNotFoundError

class Controller:
    def __init__(self):
        self.phone_book = PhoneBook()

    def load_phone_book(self, filename: str):
        try:
            self.phone_book = FileHandler.load_from_file(filename)
            View.show_message("Телефонная книга успешно открыта")
        except FileLoadError as e:
            View.show_message(str(e))

    def save_phone_book(self, filename: str):
        try:
            FileHandler.save_to_file(self.phone_book, filename)
            View.show_message("Телефонная книга успешно сохранена")
        except FileSaveError as e:
            View.show_message(str(e))

    def show_contacts(self):
        View.show_contacts(self.phone_book.get_all_contacts())

    def add_contact(self):
        name = View.get_input("Введите имя: ")
        phone = View.get_input("Введите телефон: ")
        comment = View.get_input("Введите комментарий: ")
        contact = Contact(name, phone, comment)
        self.phone_book.add_contact(contact)
        View.show_message("Контакт успешно добавлен")

    def find_contact(self):
        keyword = View.get_input("Введите слово для поиска: ")
        contacts = self.phone_book.find_contacts(keyword)
        if not contacts:
            View.show_message("Контакты не найдены")
        else:
            View.show_contacts(contacts)

    def delete_contact(self):
        contact_id = View.get_input("Введите ID контакта для удаления: ")
        if not contact_id.isdigit():
            View.show_message("ID должен быть числом")
            return
        try:
            self.phone_book.delete_contact(int(contact_id))
            View.show_message("Контакт успешно удален")
        except ContactNotFoundError as e:
            View.show_message(str(e))

    def update_contact(self):
        contact_id = View.get_input("Введите ID контакта для изменения: ")
        if not contact_id.isdigit():
            View.show_message("ID должен быть числом")
            return
        try:
            name = View.get_input("Введите новое имя: ")
            phone = View.get_input("Введите новый телефон: ")
            comment = View.get_input("Введите новый комментарий: ")
            updated_contact = Contact(name, phone, comment)
            self.phone_book.update_contact(int(contact_id), updated_contact)
            View.show_message("Контакт успешно обновлен")
        except ContactNotFoundError as e:
            View.show_message(str(e))

    def run(self):
        menu = [
            "Открыть файл",
            "Сохранить файл",
            "Показать все контакты",
            "Создать контакт",
            "Найти контакт",
            "Изменить контакт",
            "Удалить контакт",
            "Выход"
        ]
        while True:
            View.show_menu(menu)
            choice = View.get_input("Выберите пункт меню: ")
            if choice == "1":
                self.load_phone_book("phone_book.txt")
            elif choice == "2":
                self.save_phone_book("phone_book.txt")
            elif choice == "3":
                self.show_contacts()
            elif choice == "4":
                self.add_contact()
            elif choice == "5":
                self.find_contact()
            elif choice == "6":
                self.update_contact()
            elif choice == "7":
                self.delete_contact()
            elif choice == "8":
                break
            else:
                View.show_message("Некорректный выбор")
            View.pause()
        View.show_message("Работа программы завершена")