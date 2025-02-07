from model import Contact


class View:
    @staticmethod
    def show_menu(menu_items: list):
        print("Основное меню:")
        for i, item in enumerate(menu_items, 1):
            print(f"{i}. {item}")

    @staticmethod
    def show_contacts(contacts: list[Contact]):
        if not contacts:
            print("Телефонная книга пуста")
        else:
            print("=" * 66)
            for i, contact in enumerate(contacts, 1):
                print(f"{i: >2}. {contact}")
            print("=" * 66)

    @staticmethod
    def get_input(prompt: str) -> str:
        return input(prompt)

    @staticmethod
    def show_message(message: str):
        print(message)

    @staticmethod
    def pause():
        input("Нажмите Enter для продолжения...")