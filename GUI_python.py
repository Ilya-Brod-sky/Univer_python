#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import sys
import PyQt5.QtWidgets as qw
import requests
from PyQt5.QtCore import pyqtSlot

class MainWindow(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(400, 300)
        self.move(100, 100)
        self.setWindowTitle('PERSONAL HELPER!!!')

        self.callBtn = qw.QPushButton('Call computer goddess', self)
        self.callBtn.move(50, 50)
        self.callBtn.clicked.connect(self.call_goddess)

        self.donothBtn = qw.QPushButton('do nothing for 10 secundes\n (click only if you are exhausted)', self)
        self.donothBtn.move(50, 100)
        self.donothBtn.clicked.connect(self.do_nothing)

        self.goNetBtn = qw.QPushButton('Download Yandex', self)
        self.goNetBtn.move(50, 150)
        self.goNetBtn.clicked.connect(self.dwnld_Yand)

        self.quitBtn = qw.QPushButton('Quit', self)
        self.quitBtn.move(50, 200)
        self.quitBtn.clicked.connect(self.close)

    @pyqtSlot(bool)
    def call_goddess(self, evt):
        print('Please wait, we are trying to connect')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('..')
        time.sleep(1)
        print('...')
        time.sleep(0.5)
        print("Unforunately, comp-goddess is bizy and not able to meet you now. But she gives you her blessing!!!")

    @pyqtSlot(bool)
    def dwnld_Yand(self, evt):
        r = requests.get('https://yandex.ru')
        print("Got", 'https://yandex.ru', "of", len(r.content), "bytes")


    @pyqtSlot(bool)
    def do_nothing(self, evt):
        time.sleep(10)

if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    w = MainWindow()
    w.show()

    sys.exit(app.exec_())