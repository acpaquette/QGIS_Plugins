# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pow.ui'
#
# Created: Wed Aug 27 08:13:16 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_POW(object):
    def setupUi(self, POW):
        POW.setObjectName(_fromUtf8("POW"))
        POW.resize(361, 144)
        self.formLayout = QtGui.QFormLayout(POW)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(POW)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.inputlayers = QtGui.QComboBox(POW)
        self.inputlayers.setObjectName(_fromUtf8("inputlayers"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.inputlayers)
        self.label_2 = QtGui.QLabel(POW)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.edrfieldname = QtGui.QComboBox(POW)
        self.edrfieldname.setObjectName(_fromUtf8("edrfieldname"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.edrfieldname)
        self.label_3 = QtGui.QLabel(POW)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.targetname = QtGui.QComboBox(POW)
        self.targetname.setObjectName(_fromUtf8("targetname"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.targetname)
        self.buttonBox = QtGui.QDialogButtonBox(POW)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.buttonBox)

        self.retranslateUi(POW)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), POW.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), POW.reject)
        QtCore.QMetaObject.connectSlotsByName(POW)

    def retranslateUi(self, POW):
        POW.setWindowTitle(_translate("POW", "POW", None))
        self.label.setText(_translate("POW", "Input Layer", None))
        self.label_2.setText(_translate("POW", "EDR Source Field Location", None))
        self.label_3.setText(_translate("POW", "Target Name", None))

