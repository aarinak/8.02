from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt,  QCoreApplication
from PyQt5.QtGui import QIcon


class Ui_weather_form(object):
    def setupUi(self, weather_form):
        weather_form.setWindowFlags(Qt.FramelessWindowHint)
        weather_form.setWindowTitle('Погода')
        weather_form.setObjectName("weather_form")
        weather_form.resize(371, 440)
        weather_form.setTabletTracking(True)
        weather_form.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("https://freepngimg.com/png/23523-weather-file"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        weather_form.setWindowIcon(icon)
        weather_form.setWindowOpacity(1.0)
        weather_form.setLayoutDirection(QtCore.Qt.LeftToRight)
        weather_form.setStyleSheet("QWidget {\n"
"    background-color:#80ffa0;\n"
"}")
        self.inputCity = QtWidgets.QLineEdit(weather_form)
        self.inputCity.setGeometry(QtCore.QRect(50, 30, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Sport-Express Inline")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.inputCity.setFont(font)
        self.inputCity.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.inputCity.setAcceptDrops(False)
        self.inputCity.setStyleSheet("QLineEdit {\n"
"    background-color: /*#d8ff75*/#fff4d2;\n"
"    /*border: 1px solid rgb(0, 85, 255);*/\n"
"    border-radius: 3px;\n"
"    color: #727173;\n"
"    font: 16pt \"Gotham Pro\";\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #727173;\n"
"}")
        self.inputCity.setInputMethodHints(QtCore.Qt.ImhNone)
        self.inputCity.setInputMask("")
        self.inputCity.setFrame(True)
        self.inputCity.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inputCity.setDragEnabled(False)
        self.inputCity.setReadOnly(False)
        self.inputCity.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.inputCity.setClearButtonEnabled(False)
        self.inputCity.setObjectName("inputCity")
        self.buttonGet = QtWidgets.QPushButton(weather_form)
        self.buttonGet.setGeometry(QtCore.QRect(130, 80, 111, 31))
        self.buttonGet.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.buttonGet.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.buttonGet.setAutoFillBackground(False)
        self.buttonGet.setStyleSheet("QPushButton {\n"
"    background-color: /*#d8ff75*/#fff4d2;\n"
"    border-radius: 3px;\n"
"    color: #727173;\n"
"    font: 12pt \"Gotham Pro\";\n"
"    padding-left: 6px;\n"
"    padding-right: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 1px solid #727173;\n"
"}")
        self.buttonGet.setInputMethodHints(QtCore.Qt.ImhNone)
        self.buttonGet.setCheckable(False)
        self.buttonGet.setAutoRepeat(False)
        self.buttonGet.setAutoExclusive(False)
        self.buttonGet.setAutoRepeatDelay(304)
        self.buttonGet.setObjectName("buttonGet")
        self.text_weather_in_city = QtWidgets.QLabel(weather_form)
        self.text_weather_in_city.setGeometry(QtCore.QRect(10, 120, 351, 21))
        self.text_weather_in_city.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    font: 12pt \"Sport-Express Inline\";\n"
"}\n"
"")
        self.text_weather_in_city.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_weather_in_city.setFrameShadow(QtWidgets.QFrame.Plain)
        self.text_weather_in_city.setTextFormat(QtCore.Qt.AutoText)
        self.text_weather_in_city.setScaledContents(False)
        self.text_weather_in_city.setAlignment(QtCore.Qt.AlignCenter)
        self.text_weather_in_city.setWordWrap(False)
        self.text_weather_in_city.setObjectName("text_weather_in_city")
        self.text_temp = QtWidgets.QLabel(weather_form)
        self.text_temp.setGeometry(QtCore.QRect(10, 190, 351, 51))
        self.text_temp.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    font: 44pt \"Sport-Express Inline\";\n"
"}\n"
"")