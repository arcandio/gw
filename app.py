from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileSystemModel
import sys, os

uifile = "test.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(uifile)

class Wiki(QMainWindow, Ui_MainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.title = 'GameWiki'
		self.setupUi(self)
		# connect buttons to functions
		self.mainButton.clicked.connect(self.Press)
		self.textEdit.setText("hi")
		# initialize tree
		self.SetProjectPath(os.getcwd())
		self.treeView_2.clicked.connect(self.OpenMarkdownFile)

	def SetProjectPath(self, projectPath):
		self.model = QFileSystemModel()
		self.model.setRootPath(projectPath)
		print(self.model.rootPath())
		self.treeView_2.setModel(self.model)
		self.treeView_2.setRootIndex(self.model.index(projectPath))

	def OpenMarkdownFile(self, signal):
		file_path=self.model.filePath(signal)
		print(file_path)
		with open(file_path) as f:
			c = f.read()
			self.textEdit.setText(c)

	def Press (self):
		s = "random text"
		print(s)
		self.textEdit.setText(t + s)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Wiki()
    window.show()
    sys.exit(app.exec_())