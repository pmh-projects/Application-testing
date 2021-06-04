import sys
from nose.tools import *
from unittest import mock
from unittest.mock import patch
from mock import patch
import io
import pytest
import unittest


def save_to_file_title():
        print("Wpisz nazwe tytulu lub 0, aby wyjsc")
        title = input("Podaj nazwe tytulu: ")

        if title == "0":

            return 0

        elif title == "":
            w = "Brak tytulu"
            print("Nie podano tytułu. Pamiętaj, aby zmienić tytuł po zapisaniu.\n"
                  "Brak zmiany może spowodować nadpisanie notatki!")
            return w

        elif len(title) > 25:
            print("Wprowadzono zbyt dlugi tytul. Prosze sprobowac jeszcze raz!")
            w = 5
            return 5

        else:
            print("Wprowadzono tytul:" + title)
            return title

def save_to_file_content(tytul):

        try:

            if tytul == 0 or tytul == 5:

                sys.exit()

            content = input("Podaj tresc notatki: ")
            if len(content) < 5:
                q = "Notatka zbyt krotka"
                print(q)
                return q

            else:

                f = open(tytul + '.txt', 'w+')
                f.write(content)
                w = "Plik został zapisany."
                print(w)

                return w

        except Exception as e:

            print(e)

class Test(unittest.TestCase):

    # Sprawdza czy w funkcji podano nazwe (Rozne od 0). Test na zwykla nazwe bez liczby
    def testTitleIfNotZero(self):

        mock.builtins.input = lambda _: "Testowy tytul"
        assert_equal(save_to_file_title(), "Testowy tytul")


    # Test zapisu tytulu w postaci liczby
    def testTitleIfNumber(self):

        mock.builtins.input = lambda _: "123"
        assert_equal(save_to_file_title(), "123")


    # Test funkcji w wypadku podania braku tytulu
    def testTitleIfEmpty(self):

        mock.builtins.input = lambda _: ""
        assert_equal(save_to_file_title(), "Brak tytulu")


    # Test zbyt dlugiego tytulu
    def testTitleIfTooLong(self):

        mock.builtins.input = lambda _: "Zbyt Dlugi Tytul do testow maksymalna liczba znaków to dwadzieścia pięć"
        assert_equal(save_to_file_title(), 5)


    # Test wpisu do notatki z TESTowym tytulem zadeklarowanym w tesci
    def testContentPositive(self):

        tytul="TEST"
        mock.builtins.input = lambda _: "Testowy wpis do notatki"
        assert_equal(save_to_file_content(tytul), "Plik został zapisany.")


    # Test zapisu tresci w postaci samych liczb
    def testContentNumbers(self):

        tytul = "TEST4"
        mock.builtins.input = lambda _: "123456"
        assert_equal(save_to_file_content(tytul), "Plik został zapisany.")


    # Test wpisu do notatki z TESTowym tytulem zadeklarowanym w tesci
    def testContentNameShort(self):

        tytul="TEST2"
        mock.builtins.input = lambda _: "test"
        assert_equal(save_to_file_content(tytul), "Notatka zbyt krotka")

    # Test z brakiem wpisu do notatki z TESTowym tytulem zadeklarowanym w tesci
    def testContentEmpty(self):

        tytul="TEST3"
        mock.builtins.input = lambda _: ""
        assert_equal(save_to_file_content(tytul), "Notatka zbyt krotka")



if __name__ == "__main__":

    tytul = save_to_file_title()
    tresc = save_to_file_content(tytul)
