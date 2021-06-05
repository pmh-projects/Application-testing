import wikipedia
import unittest
import mock
import sys
from nose.tools import *
from unittest import mock
from unittest.mock import patch
from mock import patch
import io
import pytest

def whatWiki():
    varwiki = input("Podaj hasło:\n")
    return varwiki

def sentencesWiki():
    number = int(input("Podaj liczbe zdan do przeczytania z wiki:\n"))
    return number

def saveWiki(wikifound):
    save_wiki = input("Czy zapisać treść do pliku? tak/nie:\n")

    if save_wiki == "tak":
        wikiSaveToFile(wikifound)
        return ("ok")

    else:
        return ("nieOk")

def wikipedia_search(varwiki, number):
    # Deklaracja języka polskiego

    try:

        wikipedia.set_lang("pl")

        # Podsumowanie i zapis treści do zmiennej wikifound wraz z ograniczeniem liczby zdań do podanej wartości
        wikifound = wikipedia.summary(varwiki, sentences=number)

        print("Jak mówi wikipedia: ")
        print(wikifound)
        saveWiki(wikifound)
        return ("ok")

    except Exception as e:

        return ("nook")

def wikiSaveToFile(wikifound):

            title = input("Podaj tytul pliku:\n")

            f = open(title + '.txt', 'w+')
            f.write(wikifound)

            if title != '':
                print("Plik o nazwie " + title + " został zapisany.")
                return("ok")

            else:

                print("Plik nie zostal zapisany")
                return("no")


class Test(unittest.TestCase):

    # Test podanego hasła
    def testWhatWiki(self):
        mock.builtins.input = lambda _: "testowanie"
        self.assertEqual(whatWiki(), "testowanie")

    # Test sprawdzający input hasła różny od return
    def testWhatWikiErr(self):
        mock.builtins.input = lambda _: "test"
        self.assertNotEqual(whatWiki(), "testowanie")

    # Test podanej liczby zdań do przeczytania
    def testSentencesWiki(self):
        mock.builtins.input = lambda _: 1
        self.assertEqual(whatWiki(), 1)

    # Test sprawdzający input różny od return
    def testSentencesWikiErr(self):
        mock.builtins.input = lambda _: 2
        self.assertNotEqual(whatWiki(), 1)

    # Test sprawdzający input tekstowy różny od return
    def testSentencesWikiErr2(self):
        mock.builtins.input = lambda _: "test"
        self.assertNotEqual(whatWiki(), 1)

    # Test sprawdzający return wyszukiwania hasła
    @patch('sys.stdout', new_callable=io.StringIO)
    def testWikiSearch(varwiki, number):
        varwiki = "Testowanie"
        number = 2
        assert "ok" == wikipedia_search(varwiki, number)

    # Test sprawdzający wyjątek braku podanego hasła
    @patch('sys.stdout', new_callable=io.StringIO)
    def testWikiSearchErr(varwiki, number):
        # varwiki = "Testowanie"
        number = 5
        assert "nook" == wikipedia_search(varwiki, number)
    # Test sprawdzający input pytania "Czy zapisać plik" - tak
    def testSaveViki(self):
        mock.builtins.input = lambda _: "tak"
        self.assertNotEqual(saveWiki(wikifound), "ok")
    # Test sprawdzający input pytania "Czy zapisać plik" - nie
    def testSaveViki(wikifound):
        mock.builtins.input = lambda _: "nie"
        assert_equal(saveWiki(wikifound), "nieOk")
    # inne..
    def testSaveViki(wikifound):
        mock.builtins.input = lambda _: "123"
        assert_equal(saveWiki(wikifound), "nieOk")

    def testWikiSaveToFile(wikifound):
        wikifound = "Przykladowy tekst znaleziony dla funkcji wikiSaveToFile"
        mock.builtins.input = lambda _: "TestowanieJestOkExtra"
        assert_equal(wikiSaveToFile(wikifound), "ok")


if __name__ == "__main__":
    varwiki = whatWiki()
    number = sentencesWiki()
    wikifound = wikipedia_search(varwiki, number)

