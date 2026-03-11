import sqlite3

class ManagerWydatkow:
    def __init__(self):
        self.conn = sqlite3.connect('wydatki.db')
        self.c = self.conn.cursor()
        self.stworz_tabele()
        self.lista_wydatkow = []
        # Wczytujemy dane przy starcie, żeby lista_wydatkow nie była pusta
        self.wczytaj_dane()

    def stworz_tabele(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS wydatki
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
              kwota REAL, 
              kategoria TEXT, 
              opis TEXT)''')
        self.conn.commit()

    def dodaj_wydatek(self, wydatek_obiekt):
        # 1. Zapisujemy do bazy
        self.c.execute("INSERT INTO wydatki (kwota, kategoria, opis) VALUES (?, ?, ?)",
                       (wydatek_obiekt.kwota, wydatek_obiekt.kategoria, wydatek_obiekt.opis))
        self.conn.commit()
        # 2. Dodajemy do listy, żeby podaj_sume() i pokaz_wszystkie() działały bez odświeżania bazy
        self.lista_wydatkow.append(wydatek_obiekt)

    def wczytaj_dane(self):
        self.lista_wydatkow = [] # Czyścimy listę przed wczytaniem
        self.c.execute("SELECT * FROM wydatki")
        wszystkie_rzedy = self.c.fetchall()

        for rzad in wszystkie_rzedy:
            # rzad[0] to id, rzad[1] to kwota, rzad[2] to kategoria, rzad[3] to opis
            nowy = Wydatek(rzad[1], rzad[2], rzad[3])
            self.lista_wydatkow.append(nowy)

    # Te metody zostają bez zmian – korzystają z self.lista_wydatkow
    def podaj_sume(self):
        return sum(w.kwota for w in self.lista_wydatkow)

    def pokaz_wszystkie(self):
        if not self.lista_wydatkow:
            print("--- Twój portfel jest jeszcze pusty! ---")
        else:
            for w in self.lista_wydatkow:
                print(f"Opis: {w.opis} | Kategoria: {w.kategoria} | Kwota: {w.kwota} zł")

class Wydatek:
    def __init__(self, kwota, kategoria, opis):
        self.kwota = kwota
        self.kategoria = kategoria
        self.opis = opis

    def formatuj_do_pliku(self):
        return f"{self.kwota};{self.kategoria};{self.opis}"


moj_portfel = ManagerWydatkow()
moj_portfel.wczytaj_dane()

while True:
    print("\n--- MENU ---")
    print("1. Dodaj nowy wydatek")
    print("2. Pokaż listę wydatków")
    print("3. Pokaż sumę")
    print("4. Wyjdź i zapisz")

    wybor = input("Wybierz opcję (1-4): ")

    if wybor == "1":
        try:
            k = float(input("Podaj kwotę: "))
            kat = input("Podaj kategorię: ")
            o = input("Podaj opis: ")
            
            # Tworzymy obiekt i od razu wrzucamy go do managera
            nowy_wydatek = Wydatek(k, kat, o)
            moj_portfel.dodaj_wydatek(nowy_wydatek)
            print("Dodano!")
        except ValueError:
            print("Błąd! Kwota musi być liczbą (użyj kropki, nie przecinka).")

    elif wybor == "2":
        print("\nTwoje wydatki:")
        moj_portfel.pokaz_wszystkie()

    elif wybor == "3":
        print(f"\nSuma wszystkich wydatków: {moj_portfel.podaj_sume()} zł")

    elif wybor == "4":
        break

    else:
        print("Niepoprawny wybór, spróbuj ponownie.")