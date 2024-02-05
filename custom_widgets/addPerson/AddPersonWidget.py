from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtGui import QCloseEvent, QPixmap
from PySide6.QtCore import Signal
import face_recognition
from .AddPersonWidget_ui import Ui_AddPersonWidget
from ..dataBase.DataBaseWidget import DataBaseWidget
from databasemanager import DataBaseManager

class AddPersonWidget(Ui_AddPersonWidget, QWidget):
    """
    AddPersonWidget is a custom widget that provides a user interface for adding a new person's
    information to the system. It includes fields for entering the person's name, birthday,
    phone number, email, address, and selecting an image for facial recognition.

    Attributes:
        sendInformation (Signal): Emitted when the widget is closed or when a new person is added.
        dataBaseManager (DataBaseManager): An instance of DataBaseManager for handling database operations.
        imagePath (str): Path to the selected image file for the person being added.
    """

    sendInformation = Signal()
    dataBaseManager = DataBaseManager('peoples.db')
    imagePath = None

    def __init__(self, Widget: DataBaseWidget):
        """
        Initializes the AddPersonWidget with the given parent widget.

        Args:
            Widget (DataBaseWidget): The parent widget that will receive data from this widget.
        """
        super(AddPersonWidget, self).__init__()
        self.setupUi(self)

        # Connect signals to slots
        self.addButton.clicked.connect(self.addPerson)
        self.selectImageButton.clicked.connect(self.selectImage)
        self.cancelButton.clicked.connect(self.closeAddPersonWidget)
        self.sendInformation.connect(Widget.receiveData)

    def closeEvent(self, event):
        """
        Overrides the closeEvent method to emit the sendInformation signal when the widget is closed.

        Args:
            event (QCloseEvent): The close event triggered when the widget is closed.
        """
        self.sendInformation.emit()
        event.accept()

    def selectImage(self):
        """
        Opens a file dialog to select an image for the person being added.
        """
        file_directory = QFileDialog.getOpenFileName(self, 'Select Person Image', filter='Images (*.png *.xpm *.jpg *.jpeg)')
        if file_directory[0] != "":
            self.imagePath = file_directory[0]
            self.personPictureLabel.setPixmap(QPixmap(self.imagePath).scaled(200, 250))

    def addPerson(self):
        """
        Validates the input fields and adds the new person's information to the database.
        """
        #FIXME: Add QDialogue to handle errors
        if self.imagePath is not None and self.nameInput.text() != "":
            # Retrieve input values
            name = self.nameInput.text()
            birthday = self.birthdayInput.date().toString('yyyy-MM-dd')
            phone = self.phoneNumberInput.text()
            email = self.emailInput.text()
            address = self.adresseInput.text()
            image = face_recognition.load_image_file(self.imagePath)
            person_encoding = face_recognition.face_encodings(image)

            # Add the person to the database
            self.dataBaseManager.addPerson(name, birthday, phone, email, address, person_encoding)
            self.sendInformation.emit()
            self.close()

    def closeAddPersonWidget(self):
        """
        Closes the AddPersonWidget and emits the sendInformation signal.
        """
        self.sendInformation.emit()
        self.close()