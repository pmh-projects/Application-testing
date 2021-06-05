import pyautogui
import unittest
import mock
import sys
import io
import pytest
from nose.tools import *
from unittest import mock
from unittest.mock import patch
from mock import patch

def screenshot():

            title = input("Podaj nazwę pod jaką mam zapisać plik:\n")

            if title != '':

                image = pyautogui.screenshot()
                image.save(title + '.png')
                return ("Zapisano screenshot")

            else:
                x = "Brak tytułu."
                print(x)
                return (x)

class Test(unittest.TestCase):

    def testSceen(self):
        mock.builtins.input = lambda _: "Testowy tytuł"
        self.assertEqual(screenshot(), "Zapisano screenshot")

    def testSceenEmpty(self):
        mock.builtins.input = lambda _: ""
        self.assertEqual(screenshot(), "Brak tytułu.")

if __name__ == "__main__":
    screenshot()
