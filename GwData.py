from PyQt5.QtWidgets import QFileSystemModel, QFileDialog

class GwData():
	def __init__(self, app):
		self.app = app

	def OpenProjectDialog(self):
		fname = QFileDialog.getExistingDirectory(self.app, 'Open Project Folder', self.app.config.LastProject)
		if fname is not '':
			self.OpenProjectPath(fname)

	def OpenProjectPath(self, projectPath):
		self.SetProjectPath(projectPath)
		self.app.setWindowTitle('GAMEWIKI - ' + projectPath)
		self.app.config.Save(projectPath)

	def SetProjectPath(self, projectPath):
		self.app.model = QFileSystemModel()
		self.app.model.setRootPath(projectPath)
		print('treeview model root path: ', self.app.model.rootPath())
		self.app.treeView_2.setModel(self.app.model)
		self.app.treeView_2.setRootIndex(self.app.model.index(projectPath))

	def OpenMarkdownFile(self, signal):
		self.openFilePath=self.app.model.filePath(signal)
		print('open markdown file: ', self.openFilePath)
		with open(self.openFilePath) as f:
			c = f.read()
			self.app.text.md = c
			self.app.text.mh()
