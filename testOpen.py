from nose.tools import *
from unittest import mock
from unittest.mock import patch
from mock import patch
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
