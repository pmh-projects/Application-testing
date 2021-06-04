import random
import sys
import math
import unittest
import mock
import sys
import io
import pytest
from nose.tools import *
from unittest import mock
from unittest.mock import patch
from mock import patch

def liczba0():

    try:
         print("Podaj pierwszą liczbę")
         x = float(input("Pierwsza: "))
         return x

    except Exception as e:

         print(e)
         return ("Błąd")

def liczba1(x):

    if x == "Błąd":
        wyjscie()

    try:

         print("Podaj drugą liczbę")
         y = float(input("Druga: "))
         return y

    except Exception as e:

         print(e)
         return ("Błąd")


def calculator(x, y):

    try:

        if y == "Błąd":
            wyjscie()

        dzialanie = 99
        while dzialanie != 0:

            dzialanie = int(input(
                "Jakie działanie wykonać? "
                "\n1. Dodawanie 2. Odejmowanie 3. Mnożenie 4. Dzielenie "
                "\nAby wyjść wybierz 0\n "))

            if (dzialanie == 1):

                z = round((x + y), 2)
                print(z)
                return z

            elif (dzialanie == 2):

                z = round((x - y), 2)
                print(z)
                return z
            elif (dzialanie == 3):

                z = round((x * y), 2)
                print(z)
                return z

            elif (dzialanie == 4):

                if y == 0:

                    print("Pamiętaj cholero nie dziel przez zero")
                    return "Zero"

                else:
                    z = round((x / y), 2)
                    print(z)
                    return z

            elif (dzialanie == 0):
                print("Wyjscie")
                return("Wyjscie")
                wyjscie()

            else:
                print("Dzialanie z poza zakresu")
                return("Błąd")

    except Exception as e:

         print(e)
         return ("Błąd")

def wyjscie():
    sys.exit()
class Test(unittest.TestCase):

    def testDodawanie(self):

        x = 5
        y = 10
        mock.builtins.input = lambda _: "1"
        assert_equal(calculator(x, y), 15)


    def testOdejmowanie(self):

        x = 25
        y = 19
        mock.builtins.input = lambda _: "2"
        assert_equal(calculator(x, y), 6)


    def testMnozenie(self):

        x = 5
        y = 5
        mock.builtins.input = lambda _: "3"
        assert_equal(calculator(x, y), 25)


    def testDzielenie(self):

        x = 15
        y = 5
        mock.builtins.input = lambda _: "4"
        assert_equal(calculator(x, y), 3)


    def testDzielenieZero(self):

        x = 15
        y = 0
        mock.builtins.input = lambda _: "4"
        assert_equal(calculator(x, y), "Zero")


    def testWyjscie(self):

        x = 15
        y = 5
        mock.builtins.input = lambda _: "0"
        assert_equal(calculator(x, y), "Wyjscie")


    def testLiczbaZPozaZakresu(self):

        x = 15
        y = 5
        mock.builtins.input = lambda _: "8"
        assert_equal(calculator(x, y), "Błąd")


    def testNieLiczbaKalk(self):

        x = 15
        y = 5
        mock.builtins.input = lambda _: "Nie jestem liczbą"
        assert_equal(calculator(x, y), "Błąd")


    def testNieLiczba0(self):

        mock.builtins.input = lambda _: "test"
        assert_equal(liczba0(), "Błąd")


    def testNieLiczba1(self):

        mock.builtins.input = lambda _: "test"
        assert_equal(liczba1(5), "Błąd")


if __name__ == "__main__":

    x = liczba0()
    y = liczba1(x)

    calculator(x, y)

