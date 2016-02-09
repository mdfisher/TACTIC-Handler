# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui_checkin_tree.ui'
#
# Created: Wed Feb 03 15:13:16 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_checkInTree(object):
    def setupUi(self, checkInTree):
        checkInTree.setObjectName("checkInTree")
        checkInTree.resize(681, 711)
        checkInTree.setMinimumSize(QtCore.QSize(400, 250))
        self.verticalLayout_7 = QtGui.QVBoxLayout(checkInTree)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.descriptionSplitter = QtGui.QSplitter(checkInTree)
        self.descriptionSplitter.setOrientation(QtCore.Qt.Vertical)
        self.descriptionSplitter.setObjectName("descriptionSplitter")
        self.commentsSplitter = QtGui.QSplitter(self.descriptionSplitter)
        self.commentsSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.commentsSplitter.setObjectName("commentsSplitter")
        self.layoutWidget = QtGui.QWidget(self.commentsSplitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.searchOptionsSplitter = QtGui.QSplitter(self.layoutWidget)
        self.searchOptionsSplitter.setOrientation(QtCore.Qt.Vertical)
        self.searchOptionsSplitter.setHandleWidth(4)
        self.searchOptionsSplitter.setObjectName("searchOptionsSplitter")
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.searchOptionsSplitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.searchOptionsLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.searchOptionsLayout.setSpacing(0)
        self.searchOptionsLayout.setContentsMargins(0, 0, 0, 0)
        self.searchOptionsLayout.setObjectName("searchOptionsLayout")
        self.resultsGroupBox = QtGui.QGroupBox(self.searchOptionsSplitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultsGroupBox.sizePolicy().hasHeightForWidth())
        self.resultsGroupBox.setSizePolicy(sizePolicy)
        self.resultsGroupBox.setFlat(True)
        self.resultsGroupBox.setObjectName("resultsGroupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.resultsGroupBox)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.resultsTreeWidget = QtGui.QTreeWidget(self.resultsGroupBox)
        self.resultsTreeWidget.setTabKeyNavigation(True)
        self.resultsTreeWidget.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.resultsTreeWidget.setAllColumnsShowFocus(True)
        self.resultsTreeWidget.setHeaderHidden(True)
        self.resultsTreeWidget.setObjectName("resultsTreeWidget")
        self.resultsTreeWidget.headerItem().setText(0, "1")
        self.verticalLayout.addWidget(self.resultsTreeWidget)
        self.gridLayout.addWidget(self.searchOptionsSplitter, 1, 0, 1, 7)
        self.searchLineEdit = QtGui.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.searchLineEdit.setFont(font)
        self.searchLineEdit.setStyleSheet("QLineEdit {\n"
"    color: rgb(192, 192, 192);\n"
"    border: 2px solid darkgray;\n"
"    border-radius: 10px;\n"
"    show-decoration-selected: 1;\n"
"    padding: 0px 8px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(128, 128, 128, 255), stop:1 rgba(64, 64,64, 255));\n"
"    background-position: bottom left;\n"
"    background-image: url(\":/ui_check/gliph/search_16.png\");\n"
"    background-repeat: fixed;\n"
"    selection-background-color: darkgray;\n"
"    padding-left: 15px;\n"
"}\n"
"QLineEdit:hover{\n"
"    color: white;\n"
"    background-image: url(\":/ui_check/gliph/searchHover_16.png\");\n"
"}")
        self.searchLineEdit.setFrame(False)
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.gridLayout.addWidget(self.searchLineEdit, 0, 0, 1, 1)
        self.findOpenedPushButton = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.findOpenedPushButton.sizePolicy().hasHeightForWidth())
        self.findOpenedPushButton.setSizePolicy(sizePolicy)
        self.findOpenedPushButton.setMinimumSize(QtCore.QSize(75, 0))
        self.findOpenedPushButton.setMaximumSize(QtCore.QSize(16777215, 20))
        self.findOpenedPushButton.setObjectName("findOpenedPushButton")
        self.gridLayout.addWidget(self.findOpenedPushButton, 0, 4, 1, 1)
        self.addNewtButton = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addNewtButton.sizePolicy().hasHeightForWidth())
        self.addNewtButton.setSizePolicy(sizePolicy)
        self.addNewtButton.setMinimumSize(QtCore.QSize(75, 0))
        self.addNewtButton.setMaximumSize(QtCore.QSize(16777215, 20))
        self.addNewtButton.setObjectName("addNewtButton")
        self.gridLayout.addWidget(self.addNewtButton, 0, 3, 1, 1)
        self.contextComboBox = QtGui.QComboBox(self.layoutWidget)
        self.contextComboBox.setMinimumSize(QtCore.QSize(80, 0))
        self.contextComboBox.setEditable(True)
        self.contextComboBox.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.contextComboBox.setObjectName("contextComboBox")
        self.gridLayout.addWidget(self.contextComboBox, 0, 2, 1, 1)
        self.refreshToolButton = QtGui.QToolButton(self.layoutWidget)
        self.refreshToolButton.setMaximumSize(QtCore.QSize(16777215, 20))
        self.refreshToolButton.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.refreshToolButton.setAutoRaise(True)
        self.refreshToolButton.setArrowType(QtCore.Qt.RightArrow)
        self.refreshToolButton.setObjectName("refreshToolButton")
        self.gridLayout.addWidget(self.refreshToolButton, 0, 1, 1, 1)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.commentsSplitter)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.playblastGroupBox = QtGui.QGroupBox(self.verticalLayoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playblastGroupBox.sizePolicy().hasHeightForWidth())
        self.playblastGroupBox.setSizePolicy(sizePolicy)
        self.playblastGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.playblastGroupBox.setFlat(True)
        self.playblastGroupBox.setObjectName("playblastGroupBox")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.playblastGroupBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.imagesSplitter = QtGui.QSplitter(self.playblastGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagesSplitter.sizePolicy().hasHeightForWidth())
        self.imagesSplitter.setSizePolicy(sizePolicy)
        self.imagesSplitter.setMinimumSize(QtCore.QSize(0, 376))
        self.imagesSplitter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.imagesSplitter.setOrientation(QtCore.Qt.Vertical)
        self.imagesSplitter.setObjectName("imagesSplitter")
        self.layoutWidget1 = QtGui.QWidget(self.imagesSplitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.iconsLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.iconsLayout.setSpacing(0)
        self.iconsLayout.setContentsMargins(0, 0, 0, 0)
        self.iconsLayout.setObjectName("iconsLayout")
        self.verticalLayoutWidget = QtGui.QWidget(self.imagesSplitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.playblastLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.playblastLayout.setSpacing(0)
        self.playblastLayout.setContentsMargins(0, 0, 0, 0)
        self.playblastLayout.setContentsMargins(0, 0, 0, 0)
        self.playblastLayout.setObjectName("playblastLayout")
        self.verticalLayout_4.addWidget(self.imagesSplitter)
        self.verticalLayout_2.addWidget(self.playblastGroupBox)
        self.dropPlateSplitter = QtGui.QSplitter(self.descriptionSplitter)
        self.dropPlateSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.dropPlateSplitter.setObjectName("dropPlateSplitter")
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.dropPlateSplitter)
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.descriptionLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.descriptionLayout.setContentsMargins(1, 1, 1, 8)
        self.descriptionLayout.setObjectName("descriptionLayout")
        self.commentsGroupBox = QtGui.QGroupBox(self.verticalLayoutWidget_4)
        self.commentsGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.commentsGroupBox.setFlat(True)
        self.commentsGroupBox.setObjectName("commentsGroupBox")
        self.gridLayout_3 = QtGui.QGridLayout(self.commentsGroupBox)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.editorLayout = QtGui.QVBoxLayout()
        self.editorLayout.setSpacing(0)
        self.editorLayout.setObjectName("editorLayout")
        self.gridLayout_3.addLayout(self.editorLayout, 0, 0, 1, 12)
        self.contextLabel = QtGui.QLabel(self.commentsGroupBox)
        self.contextLabel.setMinimumSize(QtCore.QSize(50, 0))
        self.contextLabel.setObjectName("contextLabel")
        self.gridLayout_3.addWidget(self.contextLabel, 3, 10, 1, 1)
        self.descriptionTextEdit = QtGui.QTextEdit(self.commentsGroupBox)
        self.descriptionTextEdit.setObjectName("descriptionTextEdit")
        self.gridLayout_3.addWidget(self.descriptionTextEdit, 1, 0, 1, 12)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 3, 9, 1, 1)
        self.contextLineEdit = QtGui.QLineEdit(self.commentsGroupBox)
        self.contextLineEdit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contextLineEdit.sizePolicy().hasHeightForWidth())
        self.contextLineEdit.setSizePolicy(sizePolicy)
        self.contextLineEdit.setObjectName("contextLineEdit")
        self.gridLayout_3.addWidget(self.contextLineEdit, 3, 11, 1, 1)
        self.saveSelectedCheckBox = QtGui.QCheckBox(self.commentsGroupBox)
        self.saveSelectedCheckBox.setObjectName("saveSelectedCheckBox")
        self.gridLayout_3.addWidget(self.saveSelectedCheckBox, 3, 4, 1, 1)
        self.savePushButton = QtGui.QPushButton(self.commentsGroupBox)
        self.savePushButton.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savePushButton.sizePolicy().hasHeightForWidth())
        self.savePushButton.setSizePolicy(sizePolicy)
        self.savePushButton.setMinimumSize(QtCore.QSize(75, 0))
        self.savePushButton.setChecked(False)
        self.savePushButton.setObjectName("savePushButton")
        self.gridLayout_3.addWidget(self.savePushButton, 3, 2, 1, 1)
        self.updatePushButton = QtGui.QPushButton(self.commentsGroupBox)
        self.updatePushButton.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updatePushButton.sizePolicy().hasHeightForWidth())
        self.updatePushButton.setSizePolicy(sizePolicy)
        self.updatePushButton.setMinimumSize(QtCore.QSize(75, 0))
        self.updatePushButton.setObjectName("updatePushButton")
        self.gridLayout_3.addWidget(self.updatePushButton, 3, 3, 1, 1)
        self.formatTypeComboBox = QtGui.QComboBox(self.commentsGroupBox)
        self.formatTypeComboBox.setObjectName("formatTypeComboBox")
        self.gridLayout_3.addWidget(self.formatTypeComboBox, 3, 0, 1, 2)
        self.descriptionLayout.addWidget(self.commentsGroupBox)
        self.gridLayoutWidget = QtGui.QWidget(self.dropPlateSplitter)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.dropPlateLayout = QtGui.QVBoxLayout(self.gridLayoutWidget)
        self.dropPlateLayout.setSpacing(6)
        self.dropPlateLayout.setContentsMargins(1, 1, 1, 8)
        self.dropPlateLayout.setObjectName("dropPlateLayout")
        self.verticalLayout_7.addWidget(self.descriptionSplitter)

        self.retranslateUi(checkInTree)
        QtCore.QMetaObject.connectSlotsByName(checkInTree)
        checkInTree.setTabOrder(self.searchLineEdit, self.resultsTreeWidget)
        checkInTree.setTabOrder(self.resultsTreeWidget, self.descriptionTextEdit)

    def retranslateUi(self, checkInTree):
        self.resultsGroupBox.setTitle(QtGui.QApplication.translate("checkInTree", "Results:", None, QtGui.QApplication.UnicodeUTF8))
        self.findOpenedPushButton.setText(QtGui.QApplication.translate("checkInTree", "Find Opened", None, QtGui.QApplication.UnicodeUTF8))
        self.addNewtButton.setText(QtGui.QApplication.translate("checkInTree", "Add New", None, QtGui.QApplication.UnicodeUTF8))
        self.playblastGroupBox.setTitle(QtGui.QApplication.translate("checkInTree", "Preview images:", None, QtGui.QApplication.UnicodeUTF8))
        self.commentsGroupBox.setTitle(QtGui.QApplication.translate("checkInTree", "Description:", None, QtGui.QApplication.UnicodeUTF8))
        self.contextLabel.setText(QtGui.QApplication.translate("checkInTree", "Context:", None, QtGui.QApplication.UnicodeUTF8))
        self.descriptionTextEdit.setHtml(QtGui.QApplication.translate("checkInTree", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.saveSelectedCheckBox.setText(QtGui.QApplication.translate("checkInTree", "Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.savePushButton.setText(QtGui.QApplication.translate("checkInTree", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.updatePushButton.setText(QtGui.QApplication.translate("checkInTree", "Update", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
