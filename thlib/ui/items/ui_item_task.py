# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'items\ui_item_task.ui'
#
# Created: Sat Oct  5 00:17:15 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from thlib.side.Qt import QtWidgets as QtGui
from thlib.side.Qt import QtGui as Qt4Gui
from thlib.side.Qt import QtCore

class Ui_taskItem(object):
    def setupUi(self, taskItem):
        taskItem.setObjectName("taskItem")
        taskItem.resize(108, 20)
        taskItem.setWindowTitle("")
        self.versionlessLayout = QtGui.QGridLayout(taskItem)
        self.versionlessLayout.setContentsMargins(0, 0, 0, 0)
        self.versionlessLayout.setSpacing(0)
        self.versionlessLayout.setObjectName("versionlessLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.versionlessLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.addToolButton = QtGui.QToolButton(taskItem)
        self.addToolButton.setMaximumSize(QtCore.QSize(75, 20))
        self.addToolButton.setIconSize(QtCore.QSize(12, 12))
        self.addToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.addToolButton.setAutoRaise(True)
        self.addToolButton.setArrowType(QtCore.Qt.DownArrow)
        self.addToolButton.setObjectName("addToolButton")
        self.versionlessLayout.addWidget(self.addToolButton, 0, 1, 1, 1)

        self.retranslateUi(taskItem)
        QtCore.QMetaObject.connectSlotsByName(taskItem)

    def retranslateUi(self, taskItem):
        self.addToolButton.setText(u"Add")

