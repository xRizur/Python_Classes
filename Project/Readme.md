# Generowanie labiryntu - Algorytm Kruskala - Maciej Pajak
## Krotkie wprowadzenie do projektu

Projekt stworzony w jezyku python, ktory generuje labirynty za pomoca algorytmu Kruskala, ktore mozna przechodzic za pomoca biblioteki PyGame 
z kolejnymi poziomami utrudniajacymi rozgrywke.

## Uzyte technologie

Język - Python
Biblioteki:
- Pygame 2.5.2 do interaktywnego przechodzenia labiryntu i generowania graficznego
- Random do generowania losowych wartosci usuwania scian

## Uruchomienie programu
Glowny program ktory uruchamia gre to main.py, dlatego nalezy uzyc polecenia python main.py oraz zainstalowac biblioteke pyGame za pomoca:
pip install pygame
## Krotki opis klas
Klasa Cell:

Inicjalizacja: Kazda komorka (Cell) jest zainicjowana z okreslonymi wspolrzednymi (x, y) oraz slownikiem walls, ktory sledzi, ktore ze scian komorki sa obecne. Poczatkowo wszystkie sciany sa ustawione na True, co oznacza, ze kazda komorka jest w pelni zamknieta. Usuwanie scian: Metoda remove_wall pozwala na "usuwanie" sciany miedzy biezaca komorka a sasiednia komorka.

Klasa DisjointSet

Uzywana do zarzadzania zbiorami rozlaczonymi komorek w labiryncie, co jest pomocne przy generowaniu labiryntu algorytmem Kruskala.

Klasa Maze

Inicjalizacja: Tworzy siatke komorek (Cell) o okreslonej szerokosci i wysokosci. Generowanie labiryntu: Algorytm generowania labiryntu zaczyna od utworzenia pelnego zestawu scian, a nastepnie losowo usuwa niektore sciany (zachowujac strukture labiryntu), uzywajac struktury DisjointSet do sledzenia i laczania komorek w sposob, ktory zapobiega tworzeniu cykli. Rysowanie: Metoda draw przechodzi przez wszystkie komorki labiryntu i rysuje ich sciany na ekranie.

Glowna funkcja gry (run_maze_game)

Inicjalizuje Pygame, ustawia ekran i zarzadza glowna petla gry, ktora obejmuje wyswietlanie menu, generowanie labiryntu, obsluge eventow: ruchow gracza i sprawdzanie warunkow zwyciestwa. Gracz moze poruszac sie w czterech kierunkach i jego ruch jest ograniczony przez sciany labiryntu. Gdy gracz dotrze do konca labiryntu, gra przechodzi na kolejny poziom, zwiekszajac trudnosc(wielkosc labiryntu).

Klasa Player

Reprezentuje gracza w labiryncie z metodami do ruchu i rysowania. Metoda move pozwala graczowi poruszac sie w czterech kierunkach,

## Obsługa programu
Po wlaczeniu gry, operujemy myszka i mamy do wyboru nowa gre oraz wyjscie.
W glownym menu mamy w lewym gornym rogu poziom oraz czas gry. W trakcie gry za pomoca escape mozemy zrestartowac gre, wyjsc lub wrocic do gry.
W trakcie gry poruszamy sie strzalkami i celem jest przejscie do drugiego rogu ekranu -> prawy dolny.

## Algorytm
proces generowania labiryntu wykorzystuje algorytm Kruskala do tworzenia labiryntu, w którym istnieje dokładnie jedna ścieżka między dowolnymi dwoma punktami. Algorytm Kruskala jest algorytmem znajdowania minimalnego drzewa rozpinającego dla grafu. W kontekście generowania labiryntu, można go interpretować w następujący sposób:

Wierzchołki i krawędzie: Każda komórka labiryntu traktowana jest jako wierzchołek grafu, a ściany między komórkami są krawędziami, które można usunąć. Początkowo każda komórka (wierzchołek) jest odizolowanym poddrzewem.

Zbioru rozłączne: Algorytm wykorzystuje strukturę zbiorów rozłącznych (Disjoint Set Union, DSU), by śledzić, które komórki (wierzchołki) są już połączone. Początkowo każda komórka stanowi własny zbiór.

Łączenie komórek: Algorytm losowo wybiera ścianę (krawędź) do potencjalnego usunięcia. Jeśli dwie komórki po obu stronach ściany nie należą do tego samego zbioru rozłącznego (co oznacza, że usunięcie ściany między nimi nie utworzy cyklu), ściana jest usuwana, a komórki są łączone, tj. ich zbiory są łączone w jeden zbiór.

Minimalne drzewo rozpinające: Proces ten kontynuowany jest do momentu, gdy wszystkie komórki labiryntu zostaną połączone, tworząc minimalne drzewo rozpinające. W rezultacie otrzymujemy labirynt, w którym istnieje dokładnie jedna ścieżka łącząca dowolne dwie komórki, bez żadnych cykli.
