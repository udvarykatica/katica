from datetime import datetime

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 10000)  # Egyágyas szoba ára

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 15000)  # Kétágyas szoba ára

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def uj_szoba(self, szoba):
        self.szobak.append(szoba)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

def foglalas_keszitese(szalloda, szobaszam, datum):
    for szoba in szalloda.szobak:
        if szoba.szobaszam == szobaszam:
            foglalas = Foglalas(szoba, datum)
            return foglalas
    return None

def foglalas_lemondasa(foglalas):
    # Egyelőre csak kiírjuk a lemondás tényét
    print(f"A(z) {foglalas.szoba.szobaszam} szobára szóló foglalás törölve.")

def foglalasok_listazasa(foglalasok):
    print("Foglalások:")
    for foglalas in foglalasok:
        print(f"- Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")

def main():
    # Szálloda létrehozása és szobák hozzáadása
    szalloda = Szalloda("Kristály Szálloda")
    szalloda.uj_szoba(EgyagyasSzoba("101"))
    szalloda.uj_szoba(EgyagyasSzoba("102"))
    szalloda.uj_szoba(KetagyasSzoba("201"))

    # Példa foglalások létrehozása
    foglalasok = []
    foglalasok.append(foglalas_keszitese(szalloda, "101", datetime(2024, 5, 1)))
    foglalasok.append(foglalas_keszitese(szalloda, "102", datetime(2024, 5, 2)))
    foglalasok.append(foglalas_keszitese(szalloda, "201", datetime(2024, 5, 3)))

    # Felhasználói interfész
    while True:
        print("\nÜdvözöljük a Kristály Szállodában!")
        print("Válasszon műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Kérem válasszon: ")

        if valasztas == "1":
            # Foglalás
            szobaszam = input("Adja meg a szobaszámot: ")
            datum_str = input("Adja meg a foglalás dátumát (YYYY-MM-DD): ")
            try:
                datum = datetime.strptime(datum_str, "%Y-%m-%d")
                foglalas = foglalas_keszitese(szalloda, szobaszam, datum)
                if foglalas:
                    foglalasok.append(foglalas)
                    print("Sikeres foglalás!")
                else:
                    print("Hibás szobaszám.")
            except ValueError:
                print("Hibás dátum formátum!")

        elif valasztas == "2":
            # Lemondás
            szobaszam = input("Adja meg a szobaszámot a lemondáshoz: ")
            datum_str = input("Adja meg a foglalás dátumát (YYYY-MM-DD): ")
            try:
                datum = datetime.strptime(datum_str, "%Y-%m-%d")
                for foglalas in foglalasok:
                    if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                        foglalas_lemondasa(foglalas)
                        foglalasok.remove(foglalas)
                        break
                else:
                    print("Nem található ilyen foglalás.")
            except ValueError:
                print("Hibás dátum formátum!")

        elif valasztas == "3":
            # Foglalások listázása
            foglalasok_listazasa(foglalasok)

        elif valasztas == "4":
            # Kilépés
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    main()
