class PhoneBookException(Exception):
    """Базовое исключение для телефонного справочника."""
    pass

class FileLoadError(PhoneBookException):
    """Исключение при загрузке файла."""
    def __init__(self, filename):
        self.filename = filename
        super().__init__(f"Ошибка при загрузке файла: {filename}")

class FileSaveError(PhoneBookException):
    """Исключение при сохранении файла."""
    def __init__(self, filename):
        self.filename = filename
        super().__init__(f"Ошибка при сохранении файла: {filename}")

class ContactNotFoundError(PhoneBookException):
    """Исключение, возникающее, если контакт не найден."""
    def __init__(self, contact_id):
        self.contact_id = contact_id
        super().__init__(f"Контакт с ID {contact_id} не найден")
