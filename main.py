from PySide6.QtWidgets import QApplication ,QMainWindow  
from resources.ui.Main_ui import Ui_MainWindow
from custom_widgets.camera.Camera import CameraWidget
from custom_widgets.dataBase.DataBase import DataBaseWidget
from custom_widgets.setting.Setting import Setting


class MainPage (Ui_MainWindow ,QMainWindow):
	liveTab = None
	playBackTab = None
	settingTab = None
	dataBaseTab = None
	def __init__(self):
		super(MainPage ,self).__init__()
		self.setupUi(self)
		#TODO: we need to lach tha cameras at startup to be able to recognize faces

		self.tabWidget.setTabEnabled(0,False)
		self.liveButton.clicked.connect(self.setLiveTab)
		self.dataBaseButton.clicked.connect(self.setDtataBaseTab)
		self.settingbutton.clicked.connect(self.setSettingTab)



	def closeEvent(self, event):
		if self.liveTab is not None:
			self.liveTab.closeEvent(event)
		if self.dataBaseTab is not None and self.dataBaseTab.PersonDetailsWidgetWindow is not None:
			self.dataBaseTab.PersonDetailsWidgetWindow.close()
		event.accept()

	def setLiveTab(self):
		if self.liveTab is None:
			self.liveTab = CameraWidget()
			self.tabWidget.addTab(self.liveTab,'Live')
			self.tabWidget.setCurrentIndex(self.tabWidget.count() - 1)

	def setPlayTab(self):
		pass

	def setSettingTab(self):
		if self.settingTab is None:
			self.settingTab = Setting()
			self.tabWidget.addTab(self.settingTab,'Setting')
			self.tabWidget.setCurrentIndex(self.tabWidget.count() - 1)
		

	def setDtataBaseTab(self):
		if self.dataBaseTab is None:
			self.dataBaseTab = DataBaseWidget()
			self.dataBaseTab.populateTableWithPersonsInfo()
			self.tabWidget.addTab(self.dataBaseTab ,'Data Base')
			self.tabWidget.setCurrentIndex(self.tabWidget.count() - 1)

	def onTabChange(self ,index):
		current_tab_name = self.tabWidget.tabText(index)
		if current_tab_name == "Data Base": 
			self.dataBaseTab.populateTableWithPersonsInfo()	

if __name__=="__main__":
	import sys
	app = QApplication(sys.argv)
	myapp = MainPage()
	myapp.show()
	sys.exit(app.exec())