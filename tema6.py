#ex1
class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descriere_cerc(self):
        print(f'Cercul are culoarea {self.culoare} si raza {self.raza}.')


    def aria(self):
        A = 3.14 * self.raza**2
        return A

    def diametrul(self):
        d = 2*self.raza
        return d

    def circumferinta(self):
        C = 2*3.14*self.raza
        return C

if __name__ == "__main__":
    c1 = Cerc(4, 'red')
    c1.descriere_cerc()
    print(f'Cercul are aria egala cu: {c1.aria()}')
    print(f'cercul are diametrul: {c1.diametrul()}')
    print(f'Cercul are circumferinta: {c1.circumferinta()}')


#ex 2

class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere_dr(self):
        print(f'Avem un dreptunghi cu urmatoarele caracteristici: lungime {self.lungime}, latime {self.latime} si culoare {self.culoare}')

    def aria_dr(self):
        return self.lungime * self.latime

    def perimetrul(self):
        return 2*(self.lungime + self.latime)

    def schimba_culoarea(self, new_color):
        self.culoare = new_color

if __name__=="__main__":
    d1 = Dreptunghi(8, 5, 'negru')
    d1.descriere_dr()
    print(f'Aria dreptungi este: {d1.aria_dr()}')
    print(f'perimetrul dreptunghiului este: {d1.perimetrul()}')
    print('Schimbam culoarea...')
    new_color = input("Noua culoare este :")
    d1.schimba_culoarea(new_color)
    d1.descriere_dr()


#ex3
class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere(self):
        print(f'Angajatul {self.nume} {self.prenume} are salariul {self.salariu} RON')

    def nume_prenume(self):
        return self.nume + self.prenume
    def salariu_lunar(self):
        return self.salariu
    def salariu_anual(self):
        return self.salariu * 12
    def marire_salariu(self, procent_marire):
        self.salariu = int(self.salariu * ((100+procent_marire)/100))



if __name__=="__main__":
    a1 = Angajat("Pava", "Anca", 3000)
    print(a1.salariu_anual())
    a1.marire_salariu(10)
    print(a1.salariu_anual())



    









