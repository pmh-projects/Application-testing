## Testowanie aplikacji
* [Wiki](#wiki)
* [Notatka](#notatka)
* [Otwórz notatkę](#otwórz-notatkę)
* [Lotto](#lotto-symulator)
* [Calc](#calc)
* [Info](#info)

## Wiki

Funkcja wyszukująca, odczytująca i zapisująca do pliku hasło z bazy Wikipedii.
Możliwość wyboru ilości zdań do przeczytania i zapisu. Możliwość wyboru tytułu

Przykładowe testy jednostkowy:
```
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

```
     # Sprawdza czy w funkcji podano nazwę (Rózną od 0). Test na zwykłą nazwe bez liczby
    def testTitleIfNotZero(self):

        mock.builtins.input = lambda _: "Testowy tytul"
        assert_equal(save_to_file_title(), "Testowy tytul")
        
    # Test na zbyt długi tytuł
    def testTitleIfTooLong(self):

        mock.builtins.input = lambda _: "Zbyt Dlugi Tytul do testow maksymalna liczba znaków to dwadzieścia pięć"
        assert_equal(save_to_file_title(), 5)  
        
    # Test zapisu do notatki z TESTowym tytulem zadeklarowanym w tesci
    def testContentPositive(self):

        tytul="TEST"
        mock.builtins.input = lambda _: "Testowy wpis do notatki"
        assert_equal(save_to_file_content(tytul), "Plik został zapisany.")    
        
```

<p align="center">
<img src="https://raw.githubusercontent.com/pmh-projects/tests/main/img/notatkaTest.png">
</p>

## Otwórz notatkę

Funkcja umożliwiająca otwarcie notatki po wskazaniu tytułu.

Przykładowe testy jednostkowy:
```
    # Test otwarcia istniejącego pliku
    def testOpenFileExists(self):

        mock.builtins.input = lambda _: "TEST_PLIK"
        assert_equal(open_from_file(), "ok")

    # Test otwarcia nie istniejącego pliku
    def testOpenFileNotExists(self):

        mock.builtins.input = lambda _: "TEST_PLIK_NOT_EXIST"
        assert_equal(open_from_file(), "Błąd")
```

<p align="center">
<img src="https://raw.githubusercontent.com/pmh-projects/tests/main/img/openTest.png">
</p>

## Lotto Symulator

Symulator lotto umożliwający wybór 6 wskazanych liczb.

Przykładowe testy jednostkowy:
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

Przykładowe testy jednostkowy:
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

## Info

Reszta (kod funkcji oraz testów) z komentarzem w plikach.
