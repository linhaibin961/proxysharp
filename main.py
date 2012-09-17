import sys
import time

import PyQt4
from PyQt4 import QtCore, QtGui, QAxContainer

from ui_mainwindow import Ui_MainWindow

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
    
    def execute(self):
        print("execute clicked")
    
    @PyQt4.QtCore.pyqtSignature("")
    def on_Button_clicked(self):
        print("Button clicked")
if __name__ == "__main__":
    a = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(a.exec_())
