from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys, os
# custom modules
import GwConfig, GwText, GwData

# setup main window ui from designer file
uifile = "test.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(uifile)

class Wiki(QMainWindow, Ui_MainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.setWindowTitle('GAMEWIKI')
		# set up configuration
		self.config = GwConfig.GwConfig(self)
		self.config.Load()
		self.data = GwData.GwData(self)
		# connect buttons to functions
		self.actionOpen_Project.triggered.connect(self.data.OpenProjectDialog)
		# initialize tree
		self.data.SetProjectPath(self.config.LastProject)
		self.treeView_2.clicked.connect(self.data.OpenMarkdownFile)
		# set up a var for our last open path
		self.openFilePath = ''
		# set up text processing
		self.text = GwText.GwParse(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Wiki()
    window.show()
    sys.exit(app.exec_())