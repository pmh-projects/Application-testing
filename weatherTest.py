import unittest
import mock
import sys
import io
import pytest
import pyowm
from nose.tools import *
from unittest import mock
from unittest.mock import patch
from mock import patch
from pyowm.utils.config import get_default_config

def weather():
    try:
        check_city = input("Podaj nazwę miejscowości:\n")

        if check_city == "":
            print("Nie podano miasta. Spróbuj jeszcze raz.")
            return("Brak miasta")

        else:
            print(check_city)

            # https://pyowm.readthedocs.io/en/latest/v3/code-recipes.html
            # from pyowm.owm import OWM
            # from pyowm.utils.config import get_default_config
            # config_dict = get_default_config()
            # config_dict['language'] = 'pt'  # your language here, eg. Portuguese
            # owm = OWM('your-api-key', config_dict)

            config_dict = get_default_config()
            config_dict['language'] = 'pl'
            owm = pyowm.OWM('klucz_API', config_dict)
            mng = owm.weather_manager()
            obs = mng.weather_at_place(check_city + ', PL')
            w = obs.weather
            temp = w.temperature('celsius')

            print(w)
            act_temp = int(temp['temp'])
            print(act_temp)
            print("Aktualna temperatura w stopniach celcjusza w mieście " + check_city + " wynosi:")
            print(act_temp)
            print("Odczuwalna:")
            print(temp['feels_like'])
            print("Minimalna temparatura:")
            print(temp['temp_min'])
            print("Maksymalna temperatura:")
            print(temp["temp_max"])
            actstat = w.detailed_status
            print(actstat)
            print("Aktualnie jest na dworze:")
            print(actstat)

            if 'deszcz' in actstat or 'burza' in actstat or 'mżawka' in actstat or 'śnieg' in actstat:
                print('Lepiej dobrze się ubierz.')

            return 0

    except Exception as e:

        print(e)
        print("Prawdopodnie podano nieprawidłowe parametry. Spróbuj jeszcze raz.")

        return 99

class Test(unittest.TestCase):

    # Test polskiego miasta
    def testWeather(self):

        mock.builtins.input = lambda _: "Sopot"
        self.assertEqual(weather(), 0)

    # Przypadek braku miasta
    def testWeatherEmpty(self):

        mock.builtins.input = lambda _: ""
        self.assertEqual(weather(), "Brak miasta")

    # Przypadek podania przypadkowego zlepku liter
    def testWeatherErr(self):

        mock.builtins.input = lambda _: "Xyz"
        self.assertEqual(weather(), 99)

    # Przypadek podania ciągu cyfr
    def testWeatherErrNum(self):

        mock.builtins.input = lambda _: "123"
        self.assertEqual(weather(), 99)

    # Przypadek podania miasta z poza obszaru
    def testWeatherOut(self):

        mock.builtins.input = lambda _: "Saloniki"
        self.assertEqual(weather(), 99)

if __name__ == "__main__":
    weather()
