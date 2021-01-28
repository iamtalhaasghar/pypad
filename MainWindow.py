# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QFontDialog
from PyQt5.QtGui import QFont

class Ui_mainWindow(object):
    
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.setupUi()
        import coding
        self.code = coding.Code()
    
    def setupUi(self):
        
        self.mainWindow.setObjectName("mainWindow")
        self.mainWindow.resize(942, 787)
        self.centralwidget = QtWidgets.QWidget(self.mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(320, 410, 120, 80))
        self.widget.setObjectName("widget")
        self.codeArea = QtWidgets.QTextEdit(self.centralwidget)
        self.codeArea.setGeometry(QtCore.QRect(0, 0, 941, 751))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.codeArea.setFont(font)
        self.codeArea.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.codeArea.setAutoFillBackground(False)
        self.codeArea.setStyleSheet("")
        self.codeArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.codeArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.codeArea.setDocumentTitle("")
        self.codeArea.setOverwriteMode(False)
        self.codeArea.setPlaceholderText("")
        self.codeArea.setObjectName("codeArea")
        self.mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 942, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuDebug = QtWidgets.QMenu(self.menubar)
        self.menuDebug.setObjectName("menuDebug")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.mainWindow)
        self.statusbar.setObjectName("statusbar")
        self.mainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(self.mainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(self.mainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(self.mainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(self.mainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionExit = QtWidgets.QAction(self.mainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionFont = QtWidgets.QAction(self.mainWindow)
        self.actionFont.setObjectName("actionFont")
        self.actionAbout_Us = QtWidgets.QAction(self.mainWindow)
        self.actionAbout_Us.setObjectName("actionAbout_Us")
        self.actionAbout_Codepad = QtWidgets.QAction(self.mainWindow)
        self.actionAbout_Codepad.setObjectName("actionAbout_Codepad")
        self.actionRun = QtWidgets.QAction(self.mainWindow)
        self.actionRun.setObjectName("actionRun")
        self.actionCompile = QtWidgets.QAction(self.mainWindow)
        self.actionCompile.setObjectName("actionCompile")
        self.actionCompileRun = QtWidgets.QAction(self.mainWindow)
        self.actionCompileRun.setObjectName("actionCompileRun")
        self.actionRunCmd = QtWidgets.QAction(self.mainWindow)
        self.actionRunCmd.setObjectName("actionRunCmd")
        
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuDebug.addAction(self.actionRun)
        self.menuDebug.addAction(self.actionCompile)
        self.menuDebug.addAction(self.actionCompileRun)
        self.menuDebug.addSeparator()
        self.menuDebug.addAction(self.actionRunCmd)
        self.menuOptions.addAction(self.actionFont)
        self.menuAbout.addAction(self.actionAbout_Us)
        self.menuAbout.addAction(self.actionAbout_Codepad)
        
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDebug.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.mainWindow)

        self.actionNew.triggered.connect(self.newCodeFile)
        self.actionOpen.triggered.connect(self.openCodeFile)
        self.actionSave_As.triggered.connect(self.saveCodeFileAs)
        self.actionSave.triggered.connect(self.saveCodeFile)
        self.actionExit.triggered.connect(self.mainWindow.close)
        self.codeArea.textChanged.connect(self.giveClueToSaveFile)
        self.actionFont.triggered.connect(self.showFontDialog)
        self.actionRunCmd.triggered.connect(self.openCommandPrompt)
        self.actionCompile.triggered.connect(self.compileProgram)
        self.actionRun.triggered.connect(self.runProgram)
        self.hDifference = self.mainWindow.height() - self.codeArea.height()
        self.wDifference = self.mainWindow.width() - self.codeArea.width()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.mainWindow.setWindowTitle(_translate("mainWindow", "Untitled - CodePad"))
        self.codeArea.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Consolas\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        self.menuDebug.setTitle(_translate("mainWindow","Debug"))
        self.menuOptions.setTitle(_translate("mainWindow", "Options"))
        self.menuAbout.setTitle(_translate("mainWindow", "About"))
        self.actionNew.setText(_translate("mainWindow", "New"))
        self.actionNew.setShortcut(_translate("mainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("mainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("mainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("mainWindow", "Save"))
        self.actionSave.setShortcut(_translate("mainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("mainWindow", "Save As..."))
        self.actionExit.setText(_translate("mainWindow", "Exit"))
        self.actionRun.setText(_translate("mainWindow","Run"))
        self.actionCompile.setText(_translate("mainWindow","Compile"))
        self.actionCompileRun.setText(_translate("mainWindow","Compile and Run"))
        self.actionRunCmd.setText(_translate("mainWindow","Command Prompt"))
        self.actionFont.setText(_translate("mainWindow", "Font"))
        self.actionAbout_Us.setText(_translate("mainWindow", "About Us"))
        self.actionAbout_Codepad.setText(_translate("mainWindow", "About Codepad"))

    def windowResized(self):
        self.codeArea.resize(self.mainWindow.width() - self.wDifference,
                             self.mainWindow.height() - self.hDifference)


    def newCodeFile(self):
        self.codeArea.clear()
        self.mainWindow.setWindowTitle("Untitled - CodePad")
        self.fileExtensionChanged()

    def openCodeFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self.mainWindow,
                "Open Code File", '',
                "Text Files (*.txt);;Python Files (*.py);;" +
                "Java Files (*.java);;C++ Files (*.cpp);;HTML Files (*.html)")
        if(fileName):
            self.changeWindowTitleTo(fileName)
            with open(fileName, 'r') as f:
                s = f.read()
                self.codeArea.setText(s)
            self.fileExtensionChanged()

    def saveCodeFileAs(self):
        fileName, _ = QFileDialog.getSaveFileName(self.mainWindow,
                "Save Code File As",
                '',
                "Text Files (*.txt);;Python Files (*.py);;" +
                "Java Files (*.java);;C++ Files (*.cpp);;HTML Files (*.html);;All Files (*)")
        if(fileName):
            with open(fileName, 'w') as f:
                f.write(self.codeArea.toPlainText())
            self.changeWindowTitleTo(fileName)
            self.fileExtensionChanged()

    def saveCodeFile(self):
        filePath = self.extractFilePath()
        if(len(filePath) != 0):
            with open(filePath,'w') as f:
                f.write(self.codeArea.toPlainText())
                self.changeWindowTitleTo(filePath)
        else:
            self.saveCodeFileAs()
        
        self.fileExtensionChanged()
        
    def changeWindowTitleTo(self, fullPath):
        import os
        self.mainWindow.setWindowTitle('%s - %s [%s]' %
            (os.path.split(fullPath)[1],'CodePad', fullPath))

    def giveClueToSaveFile(self):
        temp = self.mainWindow.windowTitle()
        if(not temp.startswith('*')):
            temp = '* %s *' % temp
            self.mainWindow.setWindowTitle(temp)

    def showFontDialog(self):
        font, ok = QFontDialog.getFont(self.mainWindow)
        if ok:
            self.codeArea.setFont(font)
            print(self.codeArea.toHtml())


    def extractFilePath(self):
        temp = self.mainWindow.windowTitle()
        filePath = str()
        if('[' in temp):
            s = temp.find('[')
            e = temp.find(']')
            filePath = temp[s+1:e]
        return filePath

    def fileExtensionChanged(self):
        path = self.extractFilePath()
        import coding
        if(path.endswith('.txt')):
            self.code = coding.TextFile(path)
        elif(path.endswith('.java')):
            self.code = coding.JavaFile(path)
        else:
            self.code = coding.Code()
        
    # Debugging Operations

    def openCommandPrompt(self):
        self.code.runCmd()

    def compileProgram(self):
        d = self.code.compileCode()
        print(d)
    def runProgram(self):
        self.code.runCode()
