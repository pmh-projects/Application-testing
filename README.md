## Testowanie aplikacji
* [Info](#info)
* [Wiki](#wiki)
* [Notatka](#notatka)
* [Otwórz notatkę](#otwórz-notatkę)
* [Lotto](#lotto-symulator)
* [Calc](#calc)
* [Wyszukiwarka](#wyszukiwarka)
* [Screenshot](#screenshot)
* [Pogoda](#pogoda)

## Info

Testowanie aplikacji asystenta, która została podzielona na kilka plików. Funkcje zostały wyodrębnione na potrzeby testów.
Przy testowaniu użyto głównie modułów <b>unittest, pytest, mock</b>.
<br>
Kod funkcji oraz testów z komentarzem w plikach.

## Wiki

Funkcja wyszukująca, odczytująca i zapisująca do pliku hasło z bazy Wikipedii.
Możliwość wyboru ilości zdań do przeczytania i zapisu. Możliwość wyboru tytułu

Przykładowe testy jednostkowe:
```
class Test(unittest.TestCase):

    # Test podanego hasła
    def testWhatWiki(self):
        mock.builtins.input = lambda _: "testowanie"
        self.assertEqual(whatWiki(), "testowanie")
        
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

```
	
<p align="center">
<img src="https://raw.githubusercontent.com/pmh-projects/tests/main/img/wikiTest.png">
</p>

## Notatka

Funkcja tworząca notatkę wraz z możliwością nadania tytułu.

Przykładowe testy jednostkowe:
```
    # Sprawdza czy w funkcji podano nazwe (Rozne od 0). Test na zwykla nazwe bez liczby
    def testTitleIfNotZero(self):

        mock.builtins.input = lambda _: "Testowy tytul"
        self.assertEqual(save_to_file_title(), "Testowy tytul")
    
    # Test funkcji w wypadku podania braku tytulu
    def testTitleIfEmpty(self):

        mock.builtins.input = lambda _: ""
        self.assertEqual(save_to_file_title(), "Brak tytulu")
	
    # Test zbyt dlugiego tytulu
    def testTitleIfTooLong(self):

        mock.builtins.input = lambda _: "Zbyt Dlugi Tytul do testow maksymalna liczba znaków to dwadzieścia pięć"
        self.assertEqual(save_to_file_title(), 5)
	
    # Test wpisu do notatki z TESTowym tytulem zadeklarowanym w tesci
    def testContentShort(self):

        tytul="TEST2"
        mock.builtins.input = lambda _: "test"
        self.assertEqual(save_to_file_content(tytul), "Notatka zbyt krotka")
	
    # Test wpisu do notatki z TESTowym tytulem zadeklarowanym w tesci
    def testContentPositive(self):

        tytul="TEST"
        mock.builtins.input = lambda _: "Testowy wpis do notatki"
        self.assertEqual(save_to_file_content(tytul), "Plik został zapisany.")
        
```

<p align="center">
<img src="https://raw.githubusercontent.com/pmh-projects/tests/main/img/notatkaTest.png">
</p>

## Otwórz notatkę

Funkcja umożliwiająca otwarcie notatki po wskazaniu tytułu.

Przykładowe testy jednostkowe:
```

    def testOpenFileExists(self):

        mock.builtins.input = lambda _: "TEST_PLIK"
        self.assertEqual(open_from_file(), "ok")

    def testOpenFileNotExists(self):

        mock.builtins.input = lambda _: "TEST_PLIK_NOT_EXIST"
        self.assertEqual(open_from_file(), "Błąd")
	
```

<p align="center">
<img src="https://raw.githubusercontent.com/pmh-projects/tests/main/img/openTest.png">
</p>

## Lotto Symulator

Symulator lotto umożliwający wybór 6 wskazanych liczb.

Przykładowe testy jednostkowe:
```
    # Test przypisania wartości to liczby
    def testFirst(self):
        mock.builtins.input = lambda _: "1"
        self.assertEqual(first(), 1)

    def testSecond(self):
        a = 5
        mock.builtins.input = lambda _: "10"
        self.assertEqual(second(a), 10)
```

<p align="center">
<img src="https://raw.githubusercontent.com/pmh-projects/tests/main/img/lottoSimTest.png">
</p>

## Calc

Prosty kalkulator umożliwiający wykonie jedno z działaniń: dodawanie, odejmowanie, mnożenie, dzielenie.

Przykładowe testy jednostkowe:
```
    def testMnozenie(self):

        x = 5
        y = 5
        mock.builtins.input = lambda _: "3"
        assert_equal(calculator(x, y), 25)
        
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
```        

<p align="center">
<img src="https://raw.githubusercontent.com/pmh-projects/tests/main/img/calcTest.png">
</p>

## Wyszukiwarka

Funkcja umożliwiająca wpisanie hasła i wyszukanie w wyszukiwarce.

Przykładowe testy jednostkowe:
```    
    # Test wpisania hasła do wyszukawania.
    def testSearch(self):
        mock.builtins.input = lambda _: "Testowanie"
        self.assertEqual(searchTerm(), "Znaleziono")

    # Test pominięcia wpisania hasła do wyszukawania.
    def testSearchNoValue(self):
        mock.builtins.input = lambda _: ""
        self.assertEqual(searchTerm(), "Brak hasła")

```    

<p align="center">
<img src="https://raw.githubusercontent.com/pmh-projects/tests/main/img/searchTest.png">
</p>
<p align="center">
<img src="https://raw.githubusercontent.com/pmh-projects/tests/main/img/searchTest2.png">
</p>

## Screenshot

Funkcja umożliwiająca zrobienie screenshotu oraz nadanie tytułu dla pliku.

Przykładowe testy jednostkowe:
```
    def testSceen(self):
        mock.builtins.input = lambda _: "Testowy tytuł"
        self.assertEqual(screenshot(), "Zapisano screenshot")

    def testSceenEmpty(self):
        mock.builtins.input = lambda _: ""
        self.assertEqual(screenshot(), "Brak tytułu.")
```
<p align="center">
<img src="https://raw.githubusercontent.com/pmh-projects/tests/main/img/screenTest.png">
</p>

## Pogoda

Funkcja umożliwiająca sprawdzenie pogody dla lokalizacji w Polsce.

Przykładowe testy jednostkowe:
```
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
	
    # Przypadek podania miasta z poza obszaru
    def testWeatherOut(self):

        mock.builtins.input = lambda _: "Saloniki"
        self.assertEqual(weather(), 99)	
```
<p align="center">
<img src="https://raw.githubusercontent.com/pmh-projects/tests/main/img/weatherTest.png">
</p>
