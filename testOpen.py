import random
# Moduł przeglądarki internetowej zapewnia interfejs
# wysokiego poziomu, który umożliwia wyświetlanie użytkownikom dokumentów internetowych.
# https://docs.python.org/3/library/webbrowser.html
import webbrowser
# biblioteka konwersji tekstu na mowę w języku Python.
# https://pypi.org/project/pyttsx3/
import pyttsx3
# Moduł sys w Pythonie zapewnia różne funkcje i zmienne,
# które są używane do manipulowania różnymi częściami środowiska wykonawczego Pythona.
# https://docs.python.org/3/library/sys.html
import sys
# wieloplatformowy moduł do automatyzacji GUI w języku Python dla ludzi.
# Służy do programowego sterowania myszą i klawiaturą.
# https://pypi.org/project/PyAutoGUI/
import pyautogui
# Googlesearch to biblioteka Pythona do wyszukiwania w Google.
# https://pypi.org/project/googlesearch-python/
from googlesearch import search
# Wrapper do OpenWeatherMap https://pypi.org/project/pyowm/ (
import pyowm
from pyowm.utils.config import get_default_config
# Pakiet tkinter („interfejs Tk”) jest standardowym interfejsem
# Pythona do zestawu narzędzi Tk GUI.
# https://docs.python.org/3/library/tkinter.html
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
# Pillow to fork PIL. PIL to biblioteka obrazowania języka Python autorstwa Fredrika Lundha i współautorów.
# https://pypi.org/project/Pillow/
from PIL import ImageTk, Image
# Ten moduł zapewnia różne funkcje związane z czasem.
# https://docs.python.org/3/library/time.html
import time
from nose.tools import *
from unittest import mock
from unittest.mock import patch
from mock import patch
import io
import pytest
import unittest

def open_from_file():

        try:

            openFile = input("Jaki plik mam otworzyć?\n")

            file = open(openFile + ".txt", "r")
            print(file.read())
            webbrowser.open(openFile + ".txt")

            print("Plik otwarto")
            return ("ok")

        except Exception as e:

            print(e)
            return ("Błąd")

def wyjscie():
    sys.exit()

class Test(unittest.TestCase):

    def testOpenFileExists(self):

        mock.builtins.input = lambda _: "TEST_PLIK"
        assert_equal(open_from_file(), "ok")

    def testOpenFileNotExists(self):

        mock.builtins.input = lambda _: "TEST_PLIK_NOT_EXIST"
        assert_equal(open_from_file(), "Błąd")

if __name__ == "__main__":

    open_from_file()