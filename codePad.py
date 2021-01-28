from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QtWidgets.QMainWindow):
    resized = QtCore.pyqtSignal()
    def  __init__(self, parent=None):
        super(Window, self).__init__(parent=parent)
        import MainWindow
        self.ui = MainWindow.Ui_mainWindow(self)
        self.resized.connect(self.ui.windowResized)
        
    def resizeEvent(self, event):
        self.resized.emit()
        return super(Window, self).resizeEvent(event)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
