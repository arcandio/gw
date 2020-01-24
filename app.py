from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

uifile = "test.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(uifile)

class Wiki(QMainWindow, Ui_MainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.mainButton.clicked.connect(self.Press)
		self.textEdit.setText("hi")
	def Press (self):
		t = self.textEdit.toPlainText()
		s = "random text"
		print(s)
		self.textEdit.setText(t + s)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Wiki()
    window.show()
    sys.exit(app.exec_())