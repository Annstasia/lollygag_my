from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
import json
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.choose_subject = QtWidgets.QComboBox(self.centralwidget)
        self.choose_subject.setGeometry(QtCore.QRect(20, 10, 191, 41))
        self.choose_subject.setObjectName("choose_subject")
        self.display = QtWidgets.QLCDNumber(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(230, 10, 191, 41))
        self.display.setObjectName("display")
        self.num_2 = QtWidgets.QPushButton(self.centralwidget)
        self.num_2.setGeometry(QtCore.QRect(230, 120, 51, 51))
        self.num_2.setObjectName("num_2")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.num_2)
        self.num_1 = QtWidgets.QPushButton(self.centralwidget)
        self.num_1.setGeometry(QtCore.QRect(300, 120, 51, 51))
        self.num_1.setObjectName("num_1")
        self.buttonGroup.addButton(self.num_1)
        self.num_0 = QtWidgets.QPushButton(self.centralwidget)
        self.num_0.setGeometry(QtCore.QRect(370, 120, 51, 51))
        self.num_0.setObjectName("num_0")
        self.buttonGroup.addButton(self.num_0)
        self.num_4 = QtWidgets.QPushButton(self.centralwidget)
        self.num_4.setGeometry(QtCore.QRect(300, 60, 51, 51))
        self.num_4.setObjectName("num_4")
        self.buttonGroup.addButton(self.num_4)
        self.num_3 = QtWidgets.QPushButton(self.centralwidget)
        self.num_3.setGeometry(QtCore.QRect(370, 60, 51, 51))
        self.num_3.setObjectName("num_3")
        self.buttonGroup.addButton(self.num_3)
        self.num_5 = QtWidgets.QPushButton(self.centralwidget)
        self.num_5.setGeometry(QtCore.QRect(230, 60, 51, 51))
        self.num_5.setObjectName("num_5")
        self.buttonGroup.addButton(self.num_5)
        self.delete_all = QtWidgets.QPushButton(self.centralwidget)
        self.delete_all.setGeometry(QtCore.QRect(20, 480, 181, 50))
        self.delete_all.setObjectName('delete_all')
        self.settings = QtWidgets.QPushButton(self.centralwidget)
        self.settings.setGeometry(QtCore.QRect(240, 480, 181, 50))
        self.settings.setObjectName('settings')

        self.save_weight = QtWidgets.QPushButton(self.centralwidget)
        self.save_weight.setGeometry(QtCore.QRect(20, 240, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_weight.setFont(font)
        self.save_weight.setObjectName("save_weight")
        self.add_button = QtWidgets.QRadioButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(230, 180, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.remove_button = QtWidgets.QRadioButton(self.centralwidget)
        self.remove_button.setGeometry(QtCore.QRect(340, 180, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.remove_button.setFont(font)
        self.remove_button.setObjectName("remove_button")
        self.save_marks = QtWidgets.QPushButton(self.centralwidget)
        self.save_marks.setGeometry(QtCore.QRect(230, 240, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_marks.setFont(font)
        self.save_marks.setObjectName("save_marks")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 300, 401, 141))
        self.textBrowser.setObjectName("textBrowser")
        self.spinBox_k = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_k.setGeometry(QtCore.QRect(90, 60, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.spinBox_k.setFont(font)
        self.spinBox_k.setObjectName("spinBox_k")
        self.spinBox_f = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_f.setGeometry(QtCore.QRect(90, 120, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.spinBox_f.setFont(font)
        self.spinBox_f.setObjectName("spinBox_f")
        self.spinBox_t = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_t.setGeometry(QtCore.QRect(90, 180, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.spinBox_t.setFont(font)
        self.spinBox_t.setObjectName("spinBox_t")
        self.pushButton_k = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_k.setGeometry(QtCore.QRect(20, 60, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_k.setFont(font)
        self.pushButton_k.setObjectName("pushButton_k")
        self.pushButton_f = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_f.setGeometry(QtCore.QRect(20, 120, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_f.setFont(font)
        self.pushButton_f.setObjectName("pushButton_f")
        self.pushButton_t = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_t.setGeometry(QtCore.QRect(20, 180, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_t.setFont(font)
        self.pushButton_t.setObjectName("pushButton_t")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 441, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.num_2.setText(_translate("MainWindow", "2"))
        self.num_1.setText(_translate("MainWindow", "1"))
        self.num_0.setText(_translate("MainWindow", "0"))
        self.num_4.setText(_translate("MainWindow", "4"))
        self.num_3.setText(_translate("MainWindow", "3"))
        self.num_5.setText(_translate("MainWindow", "5"))
        self.delete_all.setText(_translate("MainWindow", "Сброс"))
        self.settings.setText(_translate("MainWindow", "Настройки"))
        self.save_weight.setText(_translate("MainWindow", "Сохранить вес"))
        self.add_button.setText(_translate("MainWindow", "Добавить"))
        self.remove_button.setText(_translate("MainWindow", "Убрать"))
        self.save_marks.setText(_translate("MainWindow", "Сохранить оценки"))
        self.pushButton_k.setText(_translate("MainWindow", "К"))
        self.pushButton_f.setText(_translate("MainWindow", "Ф"))
        self.pushButton_t.setText(_translate("MainWindow", "Т"))

class Setting_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(441, 483)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 10, 201, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(120, 70, 201, 41))
        self.comboBox.setObjectName("comboBox")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(80, 220, 41, 41))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(140, 220, 41, 41))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(200, 220, 41, 41))
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_4.setGeometry(QtCore.QRect(260, 220, 41, 41))
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_5 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_5.setGeometry(QtCore.QRect(320, 220, 41, 41))
        self.spinBox_5.setObjectName("spinBox_5")
        self.spinBox_6 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_6.setGeometry(QtCore.QRect(320, 280, 41, 41))
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_7 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_7.setGeometry(QtCore.QRect(200, 280, 41, 41))
        self.spinBox_7.setObjectName("spinBox_7")
        self.spinBox_8 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_8.setGeometry(QtCore.QRect(80, 280, 41, 41))
        self.spinBox_8.setObjectName("spinBox_8")
        self.spinBox_9 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_9.setGeometry(QtCore.QRect(140, 280, 41, 41))
        self.spinBox_9.setObjectName("spinBox_9")
        self.spinBox_10 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_10.setGeometry(QtCore.QRect(260, 280, 41, 41))
        self.spinBox_10.setObjectName("spinBox_10")
        self.spinBox_11 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_11.setGeometry(QtCore.QRect(320, 350, 41, 41))
        self.spinBox_11.setObjectName("spinBox_11")
        self.spinBox_12 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_12.setGeometry(QtCore.QRect(200, 350, 41, 41))
        self.spinBox_12.setObjectName("spinBox_12")
        self.spinBox_13 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_13.setGeometry(QtCore.QRect(80, 350, 41, 41))
        self.spinBox_13.setObjectName("spinBox_13")
        self.spinBox_14 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_14.setGeometry(QtCore.QRect(140, 350, 41, 41))
        self.spinBox_14.setObjectName("spinBox_14")
        self.spinBox_15 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_15.setGeometry(QtCore.QRect(260, 350, 41, 41))
        self.spinBox_15.setObjectName("spinBox_15")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 220, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: white;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 280, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: white;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 350, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: white;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 160, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: white;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(140, 160, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: white;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 160, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: white;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(260, 160, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: white;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(320, 160, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: white;")
        self.label_10.setObjectName("label_10")
        self.spinBox_16 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_16.setGeometry(QtCore.QRect(380, 220, 41, 41))
        self.spinBox_16.setObjectName("spinBox_16")
        self.spinBox_17 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_17.setGeometry(QtCore.QRect(380, 350, 41, 41))
        self.spinBox_17.setObjectName("spinBox_17")
        self.spinBox_18 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_18.setGeometry(QtCore.QRect(380, 280, 41, 41))
        self.spinBox_18.setObjectName("spinBox_18")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(380, 160, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: white;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 10, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: white;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 70, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: white;")
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 10, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: white;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 70, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: white;")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 441, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "К"))
        self.label_4.setText(_translate("MainWindow", "Ф"))
        self.label_5.setText(_translate("MainWindow", "Т"))
        self.label_6.setText(_translate("MainWindow", "5"))
        self.label_7.setText(_translate("MainWindow", "4"))
        self.label_8.setText(_translate("MainWindow", "3"))
        self.label_9.setText(_translate("MainWindow", "2"))
        self.label_10.setText(_translate("MainWindow", "1"))
        self.label_11.setText(_translate("MainWindow", "0"))
        self.label_12.setText(_translate("MainWindow", "добавить"))
        self.label_13.setText(_translate("MainWindow", "удалить"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.pushButton_2.setText(_translate("MainWindow", "-"))

class SettingWidget(QMainWindow, Setting_Window):
    def __init__(self, mark_dict, weight_dict):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add)
        self.mark_dict = mark_dict
        self.weight_dict = weight_dict
    def add(self):
        name = self.lineEdit.text()
        if bool(name):
            self.mark_dict[name] = {'new', {'k': [], 'f': [], 't': []},
                                    'saved': {'k': [], 'f': [], 't': []}}
            self.weight_dict[name] = [70, 20, 10]
    # Удаление, просмотр кол-ва + редактирование, возврат


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        try:

            super().__init__()
            self.setupUi(self)

            # Добавление словаря оценок
            try:
                with open('marks.json', mode='r', encoding='utf-8') as file:
                    self.mark_dict = json.loads(file.read())
            except:
                self.mark_dict = {
                    'Алгебра': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}},
                    'Биология': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}},
                    'География': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}},
                    'Геометрия': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}},
                    'Иностранный язык': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}},
                    'Информатика': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}},
                    'История': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}},
                    'Литература': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}},
                    'Обществознание': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}},
                    'Русский язык': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}},
                    'Физика': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}},
                    'Физическая культура': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}},
                    'Химия': {'saved': {'k': [], 'f': [], 't': []}, 'new': {'k': [], 'f': [], 't': []}}}

            # Добавление веса оценок
            try:
                with open('weight.json', mode='r', encoding='utf-8') as file:
                    self.weight_dict = json.loads(file.read())
            except Exception as e:
                self.weight_dict = {'Алгебра': [60, 25, 15],
                                    'Биология': [70, 5, 25],
                                    'География': [70, 10, 20],
                                    'Геометрия': [60, 25, 15],
                                    'Иностранный язык': [50, 30, 20],
                                    'Информатика': [60, 20, 20],
                                    'История': [40, 20, 40],
                                    'Литература': [40, 20, 40],
                                    'Обществознание': [60, 20, 20],
                                    'Русский язык': [40, 20, 40],
                                    'Физика': [70, 20, 10],
                                    'Физическая культура': [34, 33, 33],
                                    'Химия': [70, 20, 10]}

            # self.num_1.clicked.connect(self.run)
            # ввод чисел
            [i.clicked.connect(self.read_and_count_marks) for i in
             self.buttonGroup.buttons()]
            # установка значения "добавить" по умолчанию
            self.add_button.setChecked(True)
            # подключение к, ф, т
            self.pushButton_k.clicked.connect(self.k_pusher)
            self.pushButton_f.clicked.connect(self.f_pusher)
            self.pushButton_t.clicked.connect(self.t_pusher)
            # Сброс
            self.delete_all.clicked.connect(self.delete_all_func)
            # Настройки
            self.settings.clicked.connect(self.settings_func)
            # для дальнейшего исправления добавленных предметов
            self.subjects = ['Алгебра',
                             'Биология',
                             'География',
                             'Геометрия',
                             'Иностранный язык',
                             'Информатика',
                             'История',
                             'Литература',
                             'Обществознание',
                             'Русский язык',
                             'Физика',
                             'Физическая культура',
                             'Химия']
            # combobox
            self.choose_subject.addItems(self.subjects)
            self.choose_subject.activated[str].connect(self.onActivated)
            # сохранить вес
            self.save_weight.clicked.connect(self.save_weight_funk)
            self.save_marks.clicked.connect(self.save_marks_func)
            self.subject = self.subjects[0]
            self.spinBox_k.setValue(self.weight_dict[self.subject][0])
            self.spinBox_f.setValue(self.weight_dict[self.subject][1])
            self.spinBox_t.setValue(self.weight_dict[self.subject][2])
            self.set_text(self.mark_dict[self.subject])
            # Автоматически стоит ввод формирующих оценок
            self.pushButton_f.setStyleSheet('QPushButton {background-color: #87CEEB; color: blue;}')
            self.mark_flag = 2
            self.pushButton_k.setStyleSheet('QPushButton {background-color: white; color: black;}')
            self.pushButton_t.setStyleSheet('QPushButton {background-color: white; color: black;}')



        except Exception as e:
            print('init', e)



    # функция ввода, показа и подсчета оценок
    def read_and_count_marks(self):
        try:
            if self.mark_flag == 1:
                m_type = 'k'
            elif self.mark_flag == 2:
                m_type = 'f'
            else:
                m_type = 't'
            marks = self.mark_dict[self.subject]
            # Добавить/Убрать
            if self.add_button.isChecked():
                marks['new'][m_type].append(int(self.sender().text()))
            if self.remove_button.isChecked():
                if int(self.sender().text()) in marks['new'][m_type]:
                    marks['new'][m_type].remove(int(self.sender().text()))
                elif int(self.sender().text()) in marks['save'][m_type]:
                    marks['saved'][m_type].remove(int(self.sender().text()))
            # Вывод
            k = ((sum(marks['new']['k']) / len(marks['new']['k']) if len(marks['new']['k']) != 0 else 0) +
                 (sum(marks['saved']['k']) / len(marks['saved']['k']) if len(marks['saved']['k']) != 0 else 0)) *\
                  self.weight_dict[self.subject][0] / 100
            f = ((sum(marks['new']['f']) / len(marks['new']['f']) if len(marks['new']['f']) != 0 else 0) +
                 (sum(marks['saved']['f']) / len(marks['saved']['f']) if len(marks['saved']['f']) != 0 else 0)) *\
                  self.weight_dict[self.subject][1] / 100
            t = ((sum(marks['new']['t']) / len(marks['new']['t']) if len(marks['new']['t']) != 0 else 0) +
                 (sum(marks['saved']['t']) / len(marks['saved']['t']) if len(marks['saved']['t']) != 0 else 0)) *\
                  self.weight_dict[self.subject][2] / 100
            self.display.display(round(k + f + t, 2))
            self.set_text(self, marks)
        except Exception as e:
            print('read_and_count', e)

    # Вывод всех оценок
    def set_text(self, marks):
        self.textBrowser.setPlainText('''Констатирующая.\nsaved:{}.\nnew{}.\n
                                                  Формирующая.\nsaved: {}.\nnew{}: .\n
                                                  Творческая.\nsaved: {}.\nnew{}: .\n'''.format(
            ' '.join(map(str, marks['saved']['k'])), ' '.join(map(str, marks['new']['k'])),
            ' '.join(map(str, marks['saved']['f'])), ' '.join(map(str, marks['new']['f'])),
            ' '.join(map(str, marks['saved']['t'])), ' '.join(map(str, marks['new']['t']))))


    # подсчет после нажатия, radiobutton через pushputton, так красивее, вместо проверки кнопки провека флага
    def k_pusher(self):
        try:

            if self.pushButton_k.sender():
                self.pushButton_k.setStyleSheet('QPushButton {background-color: #F08080; color: #800000;}')
                self.mark_flag = 1
                self.pushButton_f.setStyleSheet('QPushButton {background-color: white; color: black;}')
                self.pushButton_t.setStyleSheet('QPushButton {background-color: white; color: black;}')
        except Exception as e:
            print('k_pusher', e)

    def f_pusher(self):
        try:
            if self.pushButton_f.sender():
                self.pushButton_f.setStyleSheet('QPushButton {background-color: #87CEEB; color: blue;}')
                self.mark_flag = 2
                self.pushButton_k.setStyleSheet('QPushButton {background-color: white; color: black;}')
                self.pushButton_t.setStyleSheet('QPushButton {background-color: white; color: black;}')
        except Exception as e:
            print('f_pusher', e)

    def t_pusher(self):
        try:
            if self.pushButton_t.sender():
                self.pushButton_t.setStyleSheet('QPushButton {background-color: #98FB98; color: #008000;}')
                self.mark_flag = 3
                self.pushButton_k.setStyleSheet('QPushButton {background-color: white; color: black;}')
                self.pushButton_f.setStyleSheet('QPushButton {background-color: white; color: black;}')
        except Exception as e:
            print('t_pusher', e)

    # кобмобокс
    def onActivated(self, text):
        try:
            self.subject = text
            self.spinBox_k.setValue(self.weight_dict[self.subject][0])
            self.spinBox_f.setValue(self.weight_dict[self.subject][1])
            self.spinBox_t.setValue(self.weight_dict[self.subject][2])
            marks = self.mark_dict[self.subject]
            self.set_text(marks)
        except Exception as e:
            print('onActivated', e)

    # сохранить вес
    def save_weight_funk(self):
        try:
            k = self.spinBox_k.value()
            f = self.spinBox_f.value()
            t = self.spinBox_t.value()
            assert k + f + t == 100
            self.weight_dict[self.subject] = [k, f, t]


        except AssertionError:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Неверный вес оценок. Вес каждой оценки задается в процентах. '
                        'Суммарный вес всех оценок должен быть равен 100')
            msg.setWindowTitle('Error')
            msg.show()
        except Exception as e:
            print('sav_weight', e)

    def save_marks_func(self):
        self.mark_dict[self.subject]['saved']['k'] += self.mark_dict[self.subject]['new']['k']
        self.mark_dict[self.subject]['saved']['f'] += self.mark_dict[self.subject]['new']['f']
        self.mark_dict[self.subject]['saved']['t'] += self.mark_dict[self.subject]['new']['t']
        self.mark_dict[self.subject]['new']['k'] = []
        self.mark_dict[self.subject]['new']['f'] = []
        self.mark_dict[self.subject]['new']['t'] = []
        self.set_text(self.mark_dict[self.subject])

    def delete_all_func(self):
        for i in self.mark_dict:
            for j in self.mark_dict[i]:
                for q in self.mark_dict[i][j]:
                    self.mark_dict[i][j][q] = []
        self.set_text(self.mark_dict[self.subject])

    # Открытие нового окна настроек
    def settings_func(self):
        self.sw = SettingWidget()


    # Отслеживание закрытия
    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, 'Информация', "Вы уверены, что хотите уйти?",
             QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            with open('weight.json', mode='w', encoding='utf-8') as file:
                file.write(json.dumps(self.weight_dict))
            with open('marks.json', mode='w', encoding='utf-8') as file:
                self.mark_dict[self.subject]['new']['k'] = []
                self.mark_dict[self.subject]['new']['f'] = []
                self.mark_dict[self.subject]['new']['t'] = []
                file.write(json.dumps(self.mark_dict))
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())