
import random
import sys
import unittest
import mock
import sys
from nose.tools import *
from unittest import mock
from unittest.mock import patch
from mock import patch
import io
import pytest
from mock import *
import unittest

def first():
    check_var0 = isinstance('a', int)
    while check_var0 is False or a < 1 or a > 49:
        try:
                a = check_var0 = int(input("Podaj pierwszą liczbę: "))

        except Exception as e:

            print("Nie podałeś prawidłowej wartości.")
    print(a)
    return a

def second(a):

    check_var1 = isinstance('a', int)
    while check_var1 is False or b < 1 or b > 49 or b == a:

        try:
                b = check_var1 = int(input("Podaj drugą liczbę: "))

        except Exception as e:

            print("Nie podałeś prawidłowej wartości.")

    print(b)
    return b

def third(a, b):

    check_var2 = isinstance('a', int)
    while check_var2 is False or c < 1 or c > 49 or c == a or c == b:

        try:

           c = check_var2 = int(input("Podaj trzecią liczbę: "))

        except Exception as e:

            print("Nie podałeś prawidłowej wartości.")

    return c

def fourth(a, b, c):

    check_var3 = isinstance('a', int)
    while check_var3 is False or d < 1 or d > 49 or d == a or d == b or d == c:

        try:
            d = check_var3 = int(input("Podaj czwarta liczbę: "))

        except Exception as e:

            print("Nie podałeś prawidłowej wartości.")

    print(d)
    return d

def fifth(a, b, c, d):

    check_var4 = isinstance('a', int)
    while check_var4 is False or f < 1 or f > 49 or f == a or f == b or f == c or f == d:

        try:
            f = check_var4 = int(input("Podaj piatą liczbę: "))

        except Exception as e:

            print("Nie podałeś prawidłowej wartości.")

    print(f)
    return f


def sixth(a, b, c, d, f):
    check_var5 = isinstance('a', int)
    while check_var5 is False or g < 1 or g > 49 or a == g or b == g or c == g or d == g or f == g:

        try:
            g = check_var5 = int(input("Podaj szóstą liczbę: "))

        except Exception as e:

            print("Nie podałeś prawidłowej wartości.")

    print(g)
    return g

def lotto_draw(a, b, c, d, f, g):

        given_numbers = [a, b, c, d, f, g]

        lotto_draw = []
        i = 0

        while i < 6:
            r = random.randint(1, 49)
            if lotto_draw.count(r) == 0:
                lotto_draw.append(r)
                i += 1
        hit_numbers = []

        for x in lotto_draw:
            y = len(given_numbers)
            t = 0
            while t < y:
                z = given_numbers[t]
                if x == z:
                    hit_numbers.append(z)
                t = t + 1

        print("Wybrane Liczby: ")
        given_numbers.sort()
        print(given_numbers)
        lotto_draw.sort()
        print("Wylosowane Liczby: ")
        print(lotto_draw)
        print("Trafione liczby: ")
        hit_numbers.sort()

        if not hit_numbers:
            print("Brak.")
            return ("no")
        else:
            print(hit_numbers)
            return ("yes")


class Test(unittest.TestCase):
    # Test przypisania wartości to liczby
    def testFirst(self):
        mock.builtins.input = lambda _: "1"
        assert_equal(first(), 1)

    def testSecond(self):
        a = 5
        mock.builtins.input = lambda _: "10"
        assert_equal(second(a), 10)

    def testThird(self):
        a = 5
        b = 10
        mock.builtins.input = lambda _: "15"
        assert_equal(third(a, b), 15)

    def testFourth(self):
        a = 5
        b = 10
        c = 17
        mock.builtins.input = lambda _: 25
        assert_equal(fourth(a, b, c), 25)

    def testFifth(self):
        a = 5
        b = 10
        c = 17
        d = 25
        mock.builtins.input = lambda _: "32"
        assert_equal(fifth(a, b, c, d), 32)

    def testSixth(self):
        a = 5
        b = 10
        c = 17
        d = 25
        e = 32
        mock.builtins.input = lambda _: "35"
        assert_equal(sixth(a, b, c, d, e), 35)

if __name__ == "__main__":

    a = first()
    b = second(a)
    c = third(a, b)
    d = fourth(a, b, c)
    f = fifth(a, b, c, d)
    g = sixth(a, b, c, d, f)

    lotto_draw(a, b, c, d, f, g)
