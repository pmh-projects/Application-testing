import webbrowser
import pytest
import unittest
from googlesearch import search
from nose.tools import *
from unittest import mock
from unittest.mock import patch
from mock import patch


def searchTerm():

    try:

        vargoogle = input("Podaj hasło do wyszukania: ")

        print("Przeszukuję sieć...")

        if vargoogle != "":

            for url in search(vargoogle, lang='pl', num_results=5):
                print(url)

            webbrowser.open("https://duckduckgo.com/?q=" + vargoogle)
            return ("Znaleziono")

        else:

            print("Nie podano hasła.")
            return ("Brak hasła")

    except Exception as e:

        print(e)


class Test(unittest.TestCase):

    def testSearch(self):
        mock.builtins.input = lambda _: "Testowanie"
        self.assertEqual(searchTerm(), "Znaleziono")

    def testSearchNoValue(self):
        mock.builtins.input = lambda _: ""
        self.assertEqual(searchTerm(), "Brak hasła")


if __name__ == "__main__":
    searchTerm()
