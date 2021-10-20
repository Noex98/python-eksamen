class Materiale(object):
    def __init__(self, idnr, titel, antal, antaludlaan, aarstal):
        self.idnr = idnr
        self.titel = titel
        self.antal = antal
        self.antaludlaan = antaludlaan
        self.aarstal = aarstal
        self.låneperiode = 14

class Bog(Materiale):
    def __init__(self, idnr, titel, antal, antaludlaan, aarstal, antalsider, forfatter, låneperiode):
        super().__init__(idnr, titel, antal, antaludlaan, aarstal)
        self.antalsider = antalsider
        self.forfatter = forfatter
        self.låneperiode = låneperiode

    def toString(self):
        return f'"{self.titel}" \n    Type: {__class__.__name__}\n    id: {self.idnr}\n    ledige: {self.antal - self.antaludlaan}\n  '

    

class Film(Materiale):
    def __init__(self, idnr, titel, antal, antaludlaan, aarstal, instruktor, laengde):
        super().__init__(idnr, titel, antal, antaludlaan, aarstal)
        self.instruktor = instruktor
        self.laengde = laengde

    def toString(self):
        return f'"{self.titel}" \n    Type: {__class__.__name__}\n    id: {self.idnr}\n    ledige: {self.antal - self.antaludlaan}\n  '

    
