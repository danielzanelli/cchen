# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\eliminarFiltro.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EliminarFiltro(object):
    def setupUi(self, EliminarFiltro):
        EliminarFiltro.setObjectName("EliminarFiltro")
        EliminarFiltro.resize(373, 346)
        self.cancelar = QtWidgets.QPushButton(EliminarFiltro)
        self.cancelar.setGeometry(QtCore.QRect(222, 300, 121, 29))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cancelar.setFont(font)
        self.cancelar.setObjectName("cancelar")
        self.eliminar = QtWidgets.QPushButton(EliminarFiltro)
        self.eliminar.setGeometry(QtCore.QRect(30, 300, 111, 29))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.eliminar.setFont(font)
        self.eliminar.setObjectName("eliminar")
        self.label_91 = QtWidgets.QLabel(EliminarFiltro)
        self.label_91.setGeometry(QtCore.QRect(10, 40, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_91.setFont(font)
        self.label_91.setAlignment(QtCore.Qt.AlignCenter)
        self.label_91.setWordWrap(True)
        self.label_91.setObjectName("label_91")
        self.label = QtWidgets.QLabel(EliminarFiltro)
        self.label.setGeometry(QtCore.QRect(30, 180, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(EliminarFiltro)
        self.label_3.setGeometry(QtCore.QRect(30, 240, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(EliminarFiltro)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.valor = QtWidgets.QLabel(EliminarFiltro)
        self.valor.setGeometry(QtCore.QRect(150, 240, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.valor.setFont(font)
        self.valor.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.valor.setText("")
        self.valor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.valor.setObjectName("valor")
        self.condicion = QtWidgets.QLabel(EliminarFiltro)
        self.condicion.setGeometry(QtCore.QRect(150, 180, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.condicion.setFont(font)
        self.condicion.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.condicion.setText("")
        self.condicion.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.condicion.setObjectName("condicion")
        self.parametro = QtWidgets.QLabel(EliminarFiltro)
        self.parametro.setGeometry(QtCore.QRect(150, 120, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.parametro.setFont(font)
        self.parametro.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.parametro.setText("")
        self.parametro.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.parametro.setObjectName("parametro")

        self.retranslateUi(EliminarFiltro)
        QtCore.QMetaObject.connectSlotsByName(EliminarFiltro)

    def retranslateUi(self, EliminarFiltro):
        _translate = QtCore.QCoreApplication.translate
        EliminarFiltro.setWindowTitle(_translate("EliminarFiltro", "Dialog"))
        self.cancelar.setText(_translate("EliminarFiltro", "Cancelar"))
        self.eliminar.setText(_translate("EliminarFiltro", "Eliminar"))
        self.label_91.setText(_translate("EliminarFiltro", "¿Estas seguro que quieres eliminar este filtro?"))
        self.label.setText(_translate("EliminarFiltro", "Condicion"))
        self.label_3.setText(_translate("EliminarFiltro", "Valor"))
        self.label_2.setText(_translate("EliminarFiltro", "Parametro"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EliminarFiltro = QtWidgets.QDialog()
    ui = Ui_EliminarFiltro()
    ui.setupUi(EliminarFiltro)
    EliminarFiltro.show()
    sys.exit(app.exec_())