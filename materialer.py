from klasser import *

#   Oprettelse af vores data

listMaterialer = [
    Bog(
        idnr = 1, 
        titel = 'Python crash course', 
        antal = 234, 
        antaludlaan = 198, 
        aarstal = 2012, 
        antalsider = 421, 
        forfatter = 'Henning',
        låneperiode = 8
    ),
    Bog(
        idnr = 2, 
        titel = 'Webdesign for beginners', 
        antal = 168, 
        antaludlaan = 87, 
        aarstal = 2016, 
        antalsider = 365, 
        forfatter = 'Jørgen',
        låneperiode = 6
    ),
    Bog(
        idnr = 3, 
        titel = 'Da Vinci Mysteriet', 
        antal = 120, 
        antaludlaan = 79, 
        aarstal = 2009, 
        antalsider = 610, 
        forfatter = 'Dan brun',
        låneperiode = 14
    ), 
    Film(
        idnr = 4,
        titel = 'Titanic',
        antal = 42,
        antaludlaan = 9,
        aarstal = 1999,
        instruktor = 'Torsten',
        laengde = 90
    ),
    Film(
        idnr = 5,
        titel = 'Titanic 2',
        antal = 42,
        antaludlaan = 9,
        aarstal = 2000,
        instruktor = 'Torsten',
        laengde = 120
    ),
    Film(
        idnr = 6,
        titel = 'Titanic 3',
        antal = 42,
        antaludlaan = 42,
        aarstal = 2001,
        instruktor = 'Torsten',
        laengde = 100
    ),
]