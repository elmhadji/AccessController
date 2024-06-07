from PySide6.QtWidgets import QWidget ,QListWidgetItem ,QMessageBox
from PySide6.QtCore import Slot ,QUrl 
from PySide6.QtGui import QPixmap ,Qt
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtMultimedia import QMediaPlayer
from .records_ui import  Ui_Records
from ..videoCardInfo.videoCardInfo import VideoCardInfo
from ..pictureCardInfo.pictureCardInfo import PictureCardInfo
from databasemanager import DataBaseManager
import os

class Records(Ui_Records ,QWidget):
	def __init__(self):
		super(Records ,self).__init__()
		self.setupUi(self)
		self.toggleSideBarButton.setChecked(True)
		self.initializeVideoPlayer()
		self.fillListWidgetWithVideos()
		self.toggleSideBarButton.clicked.connect(self.toggleSideBar)
		self.videoRadioButton.toggled.connect(self.setVideoPlayer)
		self.pictureRadioButton.toggled.connect(self.setPictureViewer)
		self.deleteAllButton.clicked.connect(self.deleteAll)
		
	def setPosition(self, position):
		self.player.setPosition(position)

	def updateSlider(self, position):
		self.slider.setValue(position)

	def updateCurrentTimeLabel(self, position):
		self.currentTimeVideo.setText(self.getFormatTime(position))
		self.totalTimeVideo.setText(self.getFormatTime(self.player.duration()))
	
	def durationChanged(self, duration):
		self.slider.setRange(0, duration)
		self.totalTimeVideo.setText(self.getFormatTime(duration))

	def getFormatTime(self ,ms):
		seconds = ms // 1000
		minutes = seconds // 60
		hours = minutes // 60
		return f"{hours:02d}:{minutes % 60:02d}:{seconds % 60:02d}"

	def initializeVideoPlayer(self):
		self.titleLabel.setText('Videos')
		self.player = QMediaPlayer()
		self.videoWidget = QVideoWidget()
		self.player.setVideoOutput(self.videoWidget)
		self.videoWidgetFramLayout.addWidget(self.videoWidget)
		self.listWidget.itemClicked.connect(lambda item :self.itemSelected(item))
		self.slider.setRange(0, 0)
		self.slider.sliderMoved.connect(self.setPosition)
		# Connect the player's positionChanged signal to update_slider
		self.player.positionChanged.connect(self.updateSlider)
		self.player.durationChanged.connect(self.durationChanged)
		self.player.positionChanged.connect(self.updateCurrentTimeLabel)

	def setVideoPlayer(self):
		self.titleLabel.setText('Videos')
		self.clearVideoViewer()
		self.clearPictureViewer()
		self.stackedWidget.setCurrentIndex(0)
		self.fillListWidgetWithVideos()

	def setPictureViewer(self):
		self.titleLabel.setText('Pictures')
		self.clearVideoViewer()
		self.clearPictureViewer()
		self.stackedWidget.setCurrentIndex(1)
		self.fillListWidgetWithPictures()

	@Slot()
	def fillListWidgetWithVideos(self):
		self.listWidget.clear()
		dataBaseManager = DataBaseManager()
		recordsFolderPath = dataBaseManager.getRecordsFolderPath()
		videoFolderPath = os.path.join(recordsFolderPath ,'videos')
		if not os.path.isdir(videoFolderPath):
			os.mkdir(videoFolderPath)
		videoFiles = [f for f in os.listdir(videoFolderPath) if f.endswith(('.mp4', '.avi', '.mkv'))]
		for videoFile in videoFiles:
			videoCardInfo = VideoCardInfo()
			videoCardInfo.refreshVideoList.connect(self.refreshVideoViewer)
			videoCardInfo.setupCard({
					"videoFolderPath":videoFolderPath,
					"videoFile":videoFile,
				})
			listWidgetItem = QListWidgetItem(self.listWidget)
			listWidgetItem.setSizeHint(videoCardInfo.sizeHint())
			self.listWidget.addItem(listWidgetItem)
			self.listWidget.setItemWidget(listWidgetItem, videoCardInfo)


	def fillListWidgetWithPictures(self):
		self.listWidget.clear()
		dataBaseManager = DataBaseManager()
		recordsFolderPath = dataBaseManager.getRecordsFolderPath()
		picturesFolderPath = os.path.join(recordsFolderPath ,'pictures')
		if not os.path.isdir(picturesFolderPath):
			os.mkdir(picturesFolderPath)
		pictureFiles = [f for f in os.listdir(picturesFolderPath) if f.endswith(('.jpg', '.jpeg'))]
		for pictureFile in pictureFiles:
			pictureCardInfo = PictureCardInfo()
			pictureCardInfo.refreshPicturesList.connect(self.refreshPictureViewer)
			pictureCardInfo.setupCard({
					"pictureFolderPath":picturesFolderPath,
					"pictureFile":pictureFile,
				})
			listWidgetItem = QListWidgetItem(self.listWidget)
			listWidgetItem.setSizeHint(pictureCardInfo.sizeHint())
			self.listWidget.addItem(listWidgetItem)
			self.listWidget.setItemWidget(listWidgetItem, pictureCardInfo)

	def refreshVideoViewer (self):
		self.clearVideoViewer()
		self.fillListWidgetWithVideos()

	def refreshPictureViewer (self):
		self.clearPictureViewer()
		self.fillListWidgetWithPictures()

	def clearVideoViewer (self):
		#TODO: Think how store the current item nam in the viewer
		#TODO: Compare between selected item to delete and current item in the viewer
		if self.player.isPlaying():
			self.player.pause()
		self.player.setSource(QUrl())
		self.player.play()
		self.currentTimeVideo.setText("00:00:00")
		self.totalTimeVideo.setText("00:00:00")
	
	def clearPictureViewer (self):
		#TODO: Think how store the current item nam in the viewer
		#TODO: Compare between selected item to delete and current item in the viewer
		size = self.pictureViewer.size()
		self.pictureViewer.setPixmap(
				QPixmap('resources/images/blackImage.jpg').scaled(size ,Qt.AspectRatioMode.KeepAspectRatio)
			)

	def toggleSideBar(self):
		if self.videoRadioButton.isChecked():
			self.fillListWidgetWithVideos()
		elif self.pictureRadioButton.isChecked():
			self.fillListWidgetWithPictures()
		
	def itemSelected(self ,item:QListWidgetItem):
		itemWidget = self.listWidget.itemWidget(item)
		if isinstance(itemWidget ,VideoCardInfo):
			videoCardInfo:VideoCardInfo = self.listWidget.itemWidget(item)

			print(f"QUrl(videoCardInfo.videoFilePath) {QUrl(videoCardInfo.videoFilePath)}")
			print(f"videoCardInfo.videoFilePath {videoCardInfo.videoFilePath}")
			self.player.setSource(QUrl(videoCardInfo.videoFilePath))
			self.player.play()
		elif isinstance(itemWidget ,PictureCardInfo):
			pictureCardInfo:PictureCardInfo = self.listWidget.itemWidget(item)
			self.pictureViewer.setPixmap(QPixmap(pictureCardInfo.pictureFilePath))

	def deleteAll(self):
		reply = QMessageBox.question(self, 'Confirm Delete',
										f"Are you sure you want to delete All Items ?", QMessageBox.Yes |
										QMessageBox.No, QMessageBox.No)
		if reply != QMessageBox.Yes:
			return
		
		if self.videoRadioButton.isChecked():
			# delte all file video
			dataBaseManager = DataBaseManager()
			recordsFolderPath = dataBaseManager.getRecordsFolderPath()
			videoFolderPath = os.path.join(recordsFolderPath, 'videos')
			for filename in os.listdir(videoFolderPath):
				if filename.endswith(('.mp4', '.avi', '.mkv')):
					os.remove(os.path.join(videoFolderPath, filename))
			#TODO: cleare the video viewer
			# Clear the list widget
			self.listWidget.clear()
			# Refill the list widget with videos
			self.fillListWidgetWithVideos()
		elif self.pictureRadioButton.isChecked():
			 # Delete all picture files
			dataBaseManager = DataBaseManager()
			recordsFolderPath = dataBaseManager.getRecordsFolderPath()
			picturesFolderPath = os.path.join(recordsFolderPath, 'pictures')
			for filename in os.listdir(picturesFolderPath):
				if filename.endswith(('.jpg', '.jpeg', '.png')):
					os.remove(os.path.join(picturesFolderPath, filename))
			#TODO: cleare the picture viewer
			# Clear the list widget
			self.listWidget.clear()
			# Refill the list widget with pictures
			self.fillListWidgetWithPictures()