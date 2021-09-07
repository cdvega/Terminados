from random import randrange
import csv
import json


def leer_csv(filename):
    '''
    Devuelve una lista a partir de un csv
    '''
    with open(filename) as f:
        reader = csv.reader(f)
        lista = [row[0].rstrip(';') for row in reader]
        return lista


def normalize(s):
    '''
    En una string, quita tildes a las mayúscula acentuadas
    '''
    sustituciones = (
        ('Á', 'A'),
        ('É', 'E'),
        ('Í', 'I'),
        ('Ó', 'O'),
        ('Ú', 'U')
    )
    for (a, b) in sustituciones:
        s = s.replace(a, b)
    return s


class Palabras:
    '''
    Produce palabras aleatorias pertenecientes a una serie de categorías
    '''

    def cuatro(self):
        '''
        Devuelve una palabra de 4 letras de entre las 100000 más usadas (de todo tipo).
        Con 12000 líneas del archivo original se obtienen unas 700 palabras.
        Todas las palabras en mayúsculas, sin tildes ni apóstrofes.
        '''
        filename = 'crea.txt'
        with open(filename) as f:
            lineas = f.readlines()
            lista_palabras = [normalize(linea.split()[1].upper())
                              for linea in lineas[1:12000] if len(linea.split()[1]) == 4 and linea.split()[1].isalpha()]
            return lista_palabras[randrange(len(lista_palabras))]

    def largas(self):
        '''
        Devuelve una palabra de más de 8 letras de entre las 100000 más usadas (de todo tipo).
        Con 12000 líneas del archivo original se obtienen casi 4000 palabras.
        Todas las palabras en mayúsculas, sin tildes ni apóstrofes.
        '''
        filename = 'crea.txt'
        with open(filename) as f:
            lineas = f.readlines()
            lista_palabras = [normalize(linea.split()[1].upper())
                              for linea in lineas[1:12000] if len(linea.split()[1]) > 8 and linea.split()[1].isalpha()]
            return lista_palabras[randrange(len(lista_palabras))]

    def nombres(self):
        '''
        Devuelve un nombre (de hombre o mujer) aleatorio a partir de listas
        con los más habituales (INE)
        '''
        hombres = leer_csv('hombres.csv')
        mujeres = leer_csv('mujeres.csv')
        lista_nombres = list(set(hombres + mujeres))
        return lista_nombres[randrange(len(lista_nombres))]

    def paises(self):
        '''
        Devuelve un nombre de país aleatorio (en mayúsculas, sin tildes, 
        y de una sola palabra (los de varias los obvia))
        '''
        filename = 'countries.json'
        # Atención al encoding; necesario
        with open(filename, encoding='utf-8-sig') as f:
            countries = json.load(f)
        lista_paises = []
        for pais in countries['countries']:  # pais es un dict
            if pais['name'].isalpha():
                lista_paises.append(normalize(pais['name'].upper()))
        return lista_paises[randrange(len(lista_paises))]

    def ninos(self):
        '''
        Devuelve una palabra fácil sobre un tema aleatorio
        '''
        filename = 'ninos.json'
        # Atención al encoding; necesario
        with open(filename, encoding='utf-8-sig') as f:
            listas = json.load(f)
        titulo = list(listas)[randrange(len(listas))]
        lista_palabras = []
        for palabra in listas[titulo]:  # palabra es un dict
            lista_palabras.append(palabra['nombre'])
        return titulo, lista_palabras[randrange(len(lista_palabras))]
