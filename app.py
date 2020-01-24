from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QFileDialog
import sys, os
# custom modules
import config, text

# setup main window ui from designer file
uifile = "test.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(uifile)

class Wiki(QMainWindow, Ui_MainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.setWindowTitle('GAMEWIKI')
		self.config = config.GwConfig(self)
		self.config.Load()
		# connect buttons to functions
		self.actionOpen_Project.triggered.connect(self.OpenProjectDialog)
		#self.mainButton.clicked.connect(self.Press)
		# initialize tree
		self.SetProjectPath(self.config.LastProject)
		self.treeView_2.clicked.connect(self.OpenMarkdownFile)
		# set up a var for our last open path
		self.openFilePath = ''
		# set up text processing
		self.text = text.GwParse(self)
		# cannot use below, causes recursion, use key press instead
		#self.textEdit.textChanged.connect(self.HtmlEdited)
		#self.mainButton.clicked.connect(self.HtmlEdited)

	def OpenProjectDialog(self):
		fname = QFileDialog.getExistingDirectory(self, 'Open Project Folder', self.config.LastProject)
		if fname is not '':
			self.OpenProjectPath(fname)

	def OpenProjectPath(self, projectPath):
		self.SetProjectPath(projectPath)
		self.setWindowTitle('GAMEWIKI - ' + projectPath)
		self.config.Save(projectPath)

	def SetProjectPath(self, projectPath):
		self.model = QFileSystemModel()
		self.model.setRootPath(projectPath)
		print('treeview model root path: ', self.model.rootPath())
		self.treeView_2.setModel(self.model)
		self.treeView_2.setRootIndex(self.model.index(projectPath))

	def OpenMarkdownFile(self, signal):
		self.openFilePath=self.model.filePath(signal)

		print('open markdown file: ', self.openFilePath)
		with open(self.openFilePath) as f:
			c = f.read()
			self.text.md = c
			self.text.mh()

	def HtmlEdited(self):
		cur = self.textEdit.textCursor()
		self.textEdit.blockSignals(True)
		self.text.hm()
		self.text.mh()
		self.textEdit.blockSignals(False)
		self.textEdit.setTextCursor(cur)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Wiki()
    window.show()
    sys.exit(app.exec_())