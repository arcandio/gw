from appdirs import AppDirs
import os, errno, json

class GwConfig():
	def __init__(self, app):
		self.app = app
		self.appdirs = AppDirs('GameWiki', 'Voidspiral')
		self.dir = self.appdirs.user_config_dir
		self.configFile = self.dir + os.sep + 'gamewiki config.txt'
		self.LastProject = os.getcwd()
		print ('appdir:', self.appdirs.user_config_dir)
	def Load(self):
		if os.path.exists(self.configFile):
			with open(self.configFile, 'r') as cfg:
				c = cfg.read()
				if os.path.exists(c):
					self.LastProject = c
		else:
			print ('nothing to load')
	def Save(self, projectPath):
		print('config last project path:', projectPath)
		# make the directory if it doesn't exist
		try:
			os.makedirs(self.appdirs.user_config_dir)
		except OSError as e:
			if e.errno != errno.EEXIST:
				raise
		# save the config file
		with open(self.configFile, 'w') as cfg:
			cfg.write(projectPath)
