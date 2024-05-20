from PySide6.QtCore import Signal, QThread, QDateTime, QTime ,Slot
from PySide6.QtGui import QImage
from databasemanager import DataBaseManager
from .RecognitionThread import RecognitionThread
import os
import cv2

class FrameReadingThread(QThread):
	sendFrame = Signal(cv2.Mat)
	updateFrame = Signal(QImage)
	resetCustomLabel = Signal()

	def __init__(self, captureId:int, captureName:str, parent=None):
		QThread.__init__(self, parent)
		self.captureId = captureId
		self.capture = cv2.VideoCapture(self.captureId)
		self.captureName = str(captureName)
		self.videoWriter = None
		self.status = True
		self.recognitionThread = RecognitionThread(captureName)
		self.sendFrame.connect(self.recognitionThread.setFrame)
		self.lastRecognition = QTime.currentTime()
		self.startTime = QTime.currentTime()
		self.updateFilename()
		self.recognitionThread.start()

	def run(self):
		while self.status:
			ret, frame = self.capture.read()
			if not ret:
				continue
			if self.lastRecognition.secsTo(QTime.currentTime()) >=1 and self.recognitionThread.frame is None:
				self.sendFrame.emit(frame)
				self.lastRecognition = QTime.currentTime()
			if self.startTime.secsTo(QTime.currentTime()) >= 3600000: # 3600000 milliseconds = 1 hour
				self.updateFilename()
			self.videoWriter.write(frame)
			cv2.putText(frame, self.captureName, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
			#TODO Add some sort of icon to know when  recognition is active 
			frameRgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			height, width, channel = frameRgb.shape
			bytesPerLine = channel * width
			qimage = QImage(frameRgb.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
			self.updateFrame.emit(qimage)

	def updateFilename(self):
		dataBaseManager = DataBaseManager()
		recordsFolderPath = dataBaseManager.getRecordsFolderPath()
		videoFolderPath = os.path.join(recordsFolderPath ,'videos')
		if not os.path.isdir(videoFolderPath):
			os.mkdir(videoFolderPath)
		currentTime = QDateTime.currentDateTime().toString("dd_MM_yyyy_HH_mm_ss")
		filename = f"{self.captureName}_{currentTime}.mp4"
		filename = filename.replace(":", "_")
		filename = os.path.join(videoFolderPath ,filename)
		size = (int(self.capture.get(3)), int(self.capture.get(4)))
		fps = int(self.capture.get(cv2.CAP_PROP_FPS))
		if self.videoWriter is not None:
			self.videoWriter.release()
		self.videoWriter = cv2.VideoWriter(filename, cv2.VideoWriter.fourcc(*'mp4v') ,24 ,size, isColor=True)
		self.startTime = QTime.currentTime()

	def endRecognitionThread(self):
		if self.recognitionThread is not None and self.recognitionThread.isRunning():
			self.sendFrame.disconnect(self.recognitionThread.setFrame)
			self.recognitionThread.killThread()
			self.recognitionThread.frame = None
			print('recognition ended')

	def startRecognitionThread(self):
		if self.recognitionThread is not None and not self.recognitionThread.isRunning():
			self.sendFrame.connect(self.recognitionThread.setFrame)
			self.recognitionThread.start()
			print('recognition started')


	def killThread(self):
		self.status = False
		self.sendFrame.disconnect(self.recognitionThread.setFrame)
		self.capture.release()
		if self.videoWriter is not None:
			self.videoWriter.release()
		self.quit()
		self.wait()
		print('frame reading thread complet')

