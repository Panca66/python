from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    def __init__(self, Pi):
        self.Pi = 3.14

    def decriere(self):
        print('Cel mai probabil am colturi!')

    @abstractmethod
    def arie(self):
        a = self.Pi * r
        pass


class Patrat(FormaGeometrica):
    def __init__(self, Pi, latura):
        FormaGeometrica.__init__(self, Pi)
        self.latura = latura

    def get_latura(self):
        return self.latura
    def set_latura(self, new_latura):
        self.latura = new_latura

    def del_latura(self):
        del self.latura

    def arie(self):
        a = self.latura**2
        print(f'Aria patratului este {a}')

class Cerc(FormaGeometrica):
    def __init__(self, Pi, raza):
        FormaGeometrica.__init__(self, Pi)
        self.raza = raza

    def get_raza(self):
        return self.raza

    def set_raza(self, new_raza):
        self.raza = new_raza

    def del_raza(self):
        del self.raza
    def arie(self):
        a = self.Pi * self.raza
        print(f'Aria cercului este {a}')

    def decriere(self):
        print('Eu nu am colturi!')




if __name__=="__main__":
    f1 = Patrat(3.14, 4)
    f1.get_latura()
    print(f'Latura patratului este de {f1.get_latura()}')
    f1.decriere()
    print('Modificam lungimea laturei.')
    new_latura = int(input('Noua lungime este: '))
    f1.set_latura(new_latura)
    print(f'Latura patratului are acum lungimea {f1.get_latura()}')
    f1.arie()

    f2 = Cerc(3.14, 2)
    f2.get_raza()
    print(f'Raza cercului initial este {f2.get_raza()}')
    f2.decriere()
    print('Modificam raza.')
    new_raza = int(input('Raza este :'))
    f2.set_raza(new_raza)
    print(f'Raza noului cerc este {f2.get_raza()}')
    f2.arie()
    f3 = Cerc(3.14, 5)
    f4 = Cerc(3.14, 4)
    forms_list = [f1, f2, f3, f4]
    for form in forms_list:
        print(type(form))
        form.arie()
        form.decriere()





