from PySide6.QtWidgets import QWidget ,QTableWidgetItem ,QPushButton ,QDialog, QMessageBox
from PySide6.QtCore import Slot ,QDate
from .DataBase_ui import Ui_DataBase
from databasemanager import DataBaseManager
import os

class DataBaseWidget(Ui_DataBase ,QWidget):
	dataBaseManager = DataBaseManager()
	addPersonWidgetWindow = None
	
	def __init__(self):
		super(DataBaseWidget ,self).__init__()
		self.setupUi(self)
		
		self.registerIdButton.clicked.connect(lambda : self.showAddPersonWidget())
	
	def showAddPersonWidget(self ,personInfo=None):
		if self.addPersonWidgetWindow is None:
			from ..addPerson.AddPersonWidget import AddPersonWidget
			self.addPersonWidgetWindow = AddPersonWidget(self)
			if personInfo is not None :
				self.addPersonWidgetWindow.fillPersonInfo(personInfo)
			self.addPersonWidgetWindow.show()
		
	def populateTableWithPersonsInfo(self):
		# Get all persons' information from the database
		personsInfo = self.dataBaseManager.getAllPersonsInfo()

		# Clear the existing data from the tableWidget
		self.tableWidget.clearContents()

		# Set the number of rows and columns in the tableWidget
		self.tableWidget.setRowCount(len(personsInfo))
		self.tableWidget.setColumnCount(8) # 6 columns for person info + 2 for actions

		# Populate the tableWidget with the data
		for rowNum, personInfo in enumerate(personsInfo):
			self.tableWidget.setItem(rowNum, 0, QTableWidgetItem(str(personInfo['id'])))
			self.tableWidget.setItem(rowNum, 1, QTableWidgetItem(personInfo['name']))
			self.tableWidget.setItem(rowNum, 2, QTableWidgetItem(personInfo['birthday']))
			self.tableWidget.setItem(rowNum, 3, QTableWidgetItem(str(personInfo['phone'])))
			self.tableWidget.setItem(rowNum, 4, QTableWidgetItem(personInfo['email']))
			self.tableWidget.setItem(rowNum, 5, QTableWidgetItem(personInfo['address']))

			# Create and set the Modify button
			modifyButton = QPushButton("Modify")
			modifyButton.clicked.connect(lambda checked=False , info=personInfo: self.showAddPersonWidget(info))
			self.tableWidget.setCellWidget(rowNum, 6, modifyButton)

			# Create and set the Delete button
			delete_button = QPushButton("Delete")
			delete_button.clicked.connect(lambda checked=False , info = personInfo : self.confirmDeletePerson(info))
			self.tableWidget.setCellWidget(rowNum, 7, delete_button)

		# Hide the 'id' and 'encoding' columns
		self.tableWidget.hideColumn(0) 
		
	def deletePersonImage(self, personName):
		# Define the source folder for person images
		personImageFolder = "person_images"
		# Construct the source file path
		sourcePath = os.path.join(personImageFolder, f"{personName}.jpg")
		# Check if the image file exists
		if os.path.exists(sourcePath):
			# Delete the image file
			os.remove(sourcePath)

	def confirmDeletePerson(self, personInfo):
		dialog = QDialog(self)
		dialog.setWindowTitle("Confirm Deletion")
		# dialog.setWindowModality(WindowModal)

		message = QMessageBox(dialog)
		message.setIcon(QMessageBox.Question)
		message.setText(f"Are you sure you want to delete {personInfo['name']}?")
		message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		message.setDefaultButton(QMessageBox.No)

		result = message.exec_()
		if result == QMessageBox.Yes:
			self.deletePersonImage(personInfo['name'])
			self.dataBaseManager.deletePerson(personInfo['id'])
			self.populateTableWithPersonsInfo()

	@Slot()
	def receiveData (self):
		self.addPersonWidgetWindow = None
		self.populateTableWithPersonsInfo()
