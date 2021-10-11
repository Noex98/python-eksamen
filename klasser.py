class Materiale(object):
    def __init__(self, idnr, titel, antal, antaludlaan, aarstal):
        self.idnr = idnr
        self.titel = titel
        self.antal = antal
        self.antaludlaan = antaludlaan
        self.aarstal = aarstal

class Bog(Materiale):
    def __init__(self, idnr, titel, antal, antaludlaan, aarstal, antalsider, forfatter):
        super().__init__(idnr, titel, antal, antaludlaan, aarstal)
        self.antalsider = antalsider
        self.forfatter = forfatter

    def toString(self):
        return f'{__class__.__name__}: "{self.titel}", ledige eksamplerer: {self.antal - self.antaludlaan}'

class Film(Materiale):
    def __init__(self, idnr, titel, antal, antaludlaan, aarstal, instruktor, laengde):
        super().__init__(idnr, titel, antal, antaludlaan, aarstal)
        self.instruktor = instruktor
        self.laengde = laengde

    def toString(self):
        return f'{__class__.__name__}: "{self.titel}", ledige eksamplerer: {self.antal - self.antaludlaan}'
