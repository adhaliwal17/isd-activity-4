"""The module defines the ContactListWindow class."""

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QTableWidgetItem
from ui.base.main_window import MainWindow

__author__ = "Amarveer Singh Dhaliwal"
__version__ = "1.0.0"

class ContactListWindow(MainWindow):
    """Defines contact list window."""

    def __init__(self) -> None:
        """Initializes a new instance of contact list window."""

        super().__init__()

        #Widget Initialization
        self.setWindowTitle("Contact Manager")
        self._name_line_edit.setPlaceholderText("Contact Name") 
        self._phone_line_edit.setInputMask("(000) 000-0000;_")
        self._add_button.setDefault(True)
        self._add_button.setEnabled(False)
        self._remove_button.setEnabled(False)

        #UI functionalities
        self._name_line_edit.textChanged.connect(self.__on_input_changed)
        self._phone_line_edit.textChanged.connect(self.__on_input_changed)
        self._add_button.clicked.connect(self.__on_add_contact)
    
    @Slot()
    def __on_input_changed(self) -> None:
        """Enables add button when the input is valid."""

        #counting total string digits in the phone line input
        count = 0
        for char in self._phone_line_edit.text():
             if char.isdigit():
                  count+= 1
             
        if self._name_line_edit.text() != "" \
            and count == 10:
                self._add_button.setEnabled(True)
        else:
             self._add_button.setEnabled(False)

    
    @Slot()
    def __on_add_contact(self) -> None:
         """Adds contacts to the table and resets the input."""
         new_row = self._contact_table.rowCount()
         self._contact_table.insertRow(new_row)
         self._contact_table.setItem(new_row, 0,
                                QTableWidgetItem(self._name_line_edit.text()))
         self._contact_table.setItem(new_row, 1,
                                QTableWidgetItem(self._phone_line_edit.text()))
         self._name_line_edit.clear()
         self._phone_line_edit.clear()
         self._name_line_edit.setFocus()




            
        

    

        

        
        

  



       




