# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'misc\ui_notes.ui'
#
# Created: Sat Oct  5 00:17:10 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from thlib.side.Qt import QtWidgets as QtGui
from thlib.side.Qt import QtGui as Qt4Gui
from thlib.side.Qt import QtCore

class Ui_notes(object):
    def setupUi(self, notes):
        notes.setObjectName("notes")
        notes.resize(311, 238)
        self.gridLayout_2 = QtGui.QGridLayout(notes)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtGui.QSplitter(notes)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.conversationScrollArea = QtGui.QScrollArea(self.splitter)
        self.conversationScrollArea.setWidgetResizable(True)
        self.conversationScrollArea.setObjectName("conversationScrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 291, 69))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.conversationScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget = QtGui.QWidget(self.splitter)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.replyPushButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.replyPushButton.setMinimumSize(QtCore.QSize(80, 0))
        self.replyPushButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.replyPushButton.setObjectName("replyPushButton")
        self.gridLayout.addWidget(self.replyPushButton, 3, 3, 1, 1)
        self.replyTextEdit = QtGui.QTextEdit(self.gridLayoutWidget)
        self.replyTextEdit.setStyleSheet("")
        self.replyTextEdit.setObjectName("replyTextEdit")
        self.gridLayout.addWidget(self.replyTextEdit, 1, 0, 1, 4)
        self.useFilterCheckBox = QtGui.QCheckBox(self.gridLayoutWidget)
        self.useFilterCheckBox.setObjectName("useFilterCheckBox")
        self.gridLayout.addWidget(self.useFilterCheckBox, 3, 0, 1, 1)
        self.filterUsersPushButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.filterUsersPushButton.setMinimumSize(QtCore.QSize(80, 0))
        self.filterUsersPushButton.setObjectName("filterUsersPushButton")
        self.gridLayout.addWidget(self.filterUsersPushButton, 3, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        self.editorLayout = QtGui.QVBoxLayout()
        self.editorLayout.setSpacing(0)
        self.editorLayout.setContentsMargins(0, 0, 0, 0)
        self.editorLayout.setObjectName("editorLayout")
        self.gridLayout.addLayout(self.editorLayout, 0, 0, 1, 4)
        self.gridLayout_2.addWidget(self.splitter, 2, 0, 1, 3)

        self.retranslateUi(notes)
        QtCore.QMetaObject.connectSlotsByName(notes)

    def retranslateUi(self, notes):
        notes.setWindowTitle(u"Form")
        self.replyPushButton.setText(u"Reply")
        self.useFilterCheckBox.setText(u"Filter by users")
        self.filterUsersPushButton.setText(u"Pick Users")

