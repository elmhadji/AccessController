from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot
from .DataBase_ui import Ui_DataBase


class DataBaseWidget(Ui_DataBase ,QWidget):
	addPersonWidgetWindow = None

	def __init__(self):
		super(DataBaseWidget ,self).__init__()
		self.setupUi(self)
		
		self.registerIdButton.clicked.connect(self.showAddPersonWidget)
	
	def showAddPersonWidget(self):
		if self.addPersonWidgetWindow is None:
			from ..addPerson.AddPersonWidget import AddPersonWidget
			self.addPersonWidgetWindow = AddPersonWidget(self)
			self.addPersonWidgetWindow.show()
	
	#TODO: implementation of filters and register batch functionality and modeling
	
	@Slot()
	def receiveData (self):
		self.addPersonWidgetWindow = None

