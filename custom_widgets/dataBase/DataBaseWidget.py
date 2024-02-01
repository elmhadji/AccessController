from PySide6.QtWidgets import QWidget
from .DataBase_ui import Ui_DataBase


class DataBaseWidget(Ui_DataBase ,QWidget):
	add_person_widget_window = None

	def __init__(self):
		super(DataBaseWidget ,self).__init__()
		self.setupUi(self)
		

