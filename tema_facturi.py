class Factura:
    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.seria = "F"
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, bucati):
        self.cantitate += bucati
        print(f'Ati adaugat {bucati} la cantitatea initiala.')
        print(f'Acum aveti {self.cantitate}')

    def schimba_pret(self, adaos):
        self.pret_buc += adaos
        print(f'Pretul pe bucata s-a marit cu {adaos}.')
        print(f'Pretul unui produs este acum {self.pret_buc}')

    def schimba_nume_preodus(self, nume):
        self.nume_produs = nume
        print(f"Produsul {self.nume_produs} a devenit {nume}")

    def Total(self):
        return self.cantitate * self.pret_buc

    def genereaza_factura(self):
        from datetime import date
        today = date.today()
        print(f'Factura seria {self.seria} numar {self.numar}')
        print('Date: ', today)
        from prettytable import PrettyTable
        mytable = PrettyTable(["Produs", "Cantitate", "Pret bucata", "Total"])
        mytable.add_row([self.nume_produs, self.cantitate, self.pret_buc, self.cantitate*self.pret_buc])
        print(mytable)

if __name__=="__main__":
    p1 = Factura(15, "Telefon", 7, 700)
    p1.genereaza_factura()









