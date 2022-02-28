# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 17:49:17 2022

@author: Daniel
"""

# app.py
import gui
import generate_path as gen
from PyQt5.QtWidgets import QApplication
import sys


class App:
    def __init__(self):
        self.generator = gen.pathGenerator()
        self.gui = gui.Ui(self.generator)


def main():
    qapp = QApplication(sys.argv)
    app = App()
    qapp.exec_()


if __name__ == '__main__':
    main()
