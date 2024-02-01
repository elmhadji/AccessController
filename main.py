from PySide6.QtWidgets import QApplication ,QMainWindow 
from resources.ui.Main_ui import Ui_MainWindow
from custom_widgets.camera.CameraWidget import CameraWidget
from custom_widgets.dataBase.DataBaseWidget import DataBaseWidget

class MainPage (Ui_MainWindow ,QMainWindow):
	liveTab = None
	playBackTab = None
	eventsTab = None
	dataBaseTab = None
	
	def __init__(self):
		super(MainPage ,self).__init__()
		self.setupUi(self)
		#TODO: we need to lach tha cameras at startup to be able to recognize faces

		self.tabWidget.setTabEnabled(0,False)
		self.liveButton.clicked.connect(self.setLiveTab)
		self.dataBaseButton.clicked.connect(self.setDtataBaseTab)

	def setLiveTab(self):
		if self.liveTab is None:
			self.liveTab = CameraWidget()
			self.tabWidget.addTab(self.liveTab,'Live')
			self.tabWidget.setCurrentIndex(self.tabWidget.count() - 1)

	def setPlayTab(self):
		pass

	def setEventsTab(self):
		pass

	def setDtataBaseTab(self):
		if self.dataBaseTab is None:
			self.dataBaseTab = DataBaseWidget()
			self.tabWidget.addTab(self.dataBaseTab ,'Data Base')
			self.tabWidget.setCurrentIndex(self.tabWidget.count() - 1)
		
		

if __name__=="__main__":
	import sys
	app = QApplication(sys.argv)
	myapp = MainPage()
	myapp.show()
	sys.exit(app.exec())