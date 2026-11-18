"""The module defines the ContactListWindow class."""

from ui.base.main_window import MainWindow
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QLineEdit, QPushButton)

__author__ = "Amarveer Singh Dhaliwal"
__version__ = "1.0.0"

class ContactListWindow(MainWindow):
    """Defines contact list window."""

    def __init__(self) -> None:
        """Initializes a new instance of contact list window."""

        super().__init__()

        self.setWindowTitle("Contact Manager")
        self._name_line_edit.setPlaceholderText("Contact Name") 
        self._phone_line_edit.setInputMask("(000) 000-0000;_")
        self._add_button.setDefault(True)
        self._add_button.setEnabled(False)
        self._remove_button.setEnabled(False)



       




