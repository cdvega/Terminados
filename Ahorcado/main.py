from typing import no_type_check
import pygame
import time
import PySimpleGUI as sg
from settings import Settings, Button
from intro import intro
from palabras import Palabras


def main():
    pygame.init()
    juego = Settings()

    screen = pygame.display.set_mode(
        (juego.screen_width, juego.screen_height))
    pygame.display.set_caption(juego.caption)

    # Pantalla para elegir opciones
    opcion = intro(juego, screen)

    # Elección de la palabra
    if opcion == 'nombres':
        titulo = 'Nombres'
        juego.palabra = Palabras().nombres()
    elif opcion == 'paises':
        titulo = 'Países'
        juego.palabra = Palabras().paises()
    elif opcion == 'cuatro':
        titulo = 'Palabras de 4 letras'
        juego.palabra = Palabras().cuatro()
    elif opcion == 'largas':
        titulo = 'Palabras largas'
        juego.palabra = Palabras().largas()
    else:
        palabrita = Palabras().ninos()
        titulo = palabrita[0]
        juego.palabra = palabrita[1]

    titulo = juego.subtitulo.render(titulo, True, juego.white)
    botones = [None]*27

    for i in range(27):
        if i < 14:
            botones[i] = Button(juego.screen_width//2 -
                                (13*60+13*20)//2 + 80*i, 150, chr(65+i), juego)
        elif i == 14:
            botones[i] = Button(juego.screen_width//2 -
                                (12*60+12*20)//2 + 80*(i-14), 230, 'Ñ', juego)
        else:
            botones[i] = Button(juego.screen_width//2 -
                                (12*60+12*20)//2 + 80*(i-14), 230, chr(64+i), juego)

    # Inicializando variables
    juego.fallos = 0
    juego.miPalabraLista = ['_' for _ in juego.palabra]
    juego.pulsadas = set()

    # IMÁGENES
    rutas = ['images/hangman1.png', 'images/hangman2.png',
             'images/hangman3.png', 'images/hangman4.png',
             'images/hangman5.png', 'images/hangman6.png']
    imagenes = [None]*6
    for i, ruta in enumerate(rutas):
        imagenes[i] = pygame.image.load(ruta)

    # Funciones

    def imprimir_palabra(screen, juego):
        '''
        Muestra en pantalla lo que tenemos de la palabra
        '''
        ancho_letra = juego.guess.render('_', True, juego.white)
        pos_x = juego.screen_width // 2 - \
            ((20+ancho_letra.get_width())*len(juego.palabra)) // 2
        for i, letra in enumerate(juego.miPalabraLista):
            letra = juego.guess.render(letra, True, juego.white)
            screen.blit(letra, [pos_x+i*(20+ancho_letra.get_width()), 780])

    def comprobar_letra(letra, juego):
        '''
        Comprueba si la letra está en la palabra
        '''
        if letra in juego.palabra:
            sound = pygame.mixer.Sound('sounds/right.wav')
            sound.play()
            for i, l in enumerate(juego.palabra):
                if l == letra:
                    juego.miPalabraLista[i] = letra
        else:
            sound = pygame.mixer.Sound('sounds/wrong.mp3')
            sound.play()
            juego.fallos += 1

    def nueva_imagen(imagenes, juego, screen):
        '''
        Se muestra cuando has fallado una letra
        '''
        for i in range(juego.fallos):
            imag_actual = imagenes[i]
            screen.blit(imag_actual, [i * 200, 550 -
                        imag_actual.get_height()//2])

    def terminado(juego):
        if juego.fallos == 6:
            sound = pygame.mixer.Sound('sounds/game_over.mp3')
            sound.play()
            time.sleep(1)
            perder_texto = f'No te quedan más intentos, has perdido. La palabra era {juego.palabra}.\n¿Quieres jugar otra vez?'
            # answer = sg.popup_yes_no(
            #     perder_texto, title='Has perdido', font=('sans', 14))
            answer = sg.popup(
                perder_texto, title='Has perdido', font=('sans', 14), custom_text=('Sí', 'No'))
            if answer == 'Sí':
                main()
            juego.done = True
        if list(juego.palabra) == juego.miPalabraLista:
            sound = pygame.mixer.Sound('sounds/applause.wav')
            sound.play()
            ganar_texto = f'¡Felicidades; has ganado! ¿Quieres jugar otra vez?'
            answer = sg.popup(
                ganar_texto, title='Has ganado', font=('sans', 14), custom_text=('Sí', 'No'))
            if answer == 'Sí':
                main()
            juego.done = True

        # LOOP PRINCIPAL
    while not juego.done:
        screen.fill(juego.bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                juego.done = True
            elif event.type == pygame.MOUSEBUTTONUP:
                for i in range(27):
                    cursor = pygame.mouse.get_pos()
                    if abs(botones[i].x-cursor[0]) < botones[i].radius and abs(botones[i].y-cursor[1]) < botones[i].radius:
                        if botones[i].text not in juego.pulsadas:
                            letra = botones[i].text
                            botones[i].negro = True
                            juego.pulsadas.add(letra)
                            comprobar_letra(letra, juego)

        # LÓGICA
        aviso = f'Fallos restantes: {6-juego.fallos}'
        aviso = juego.normal.render(aviso, True, juego.grey)
        screen.blit(aviso, [juego.screen_width//2-aviso.get_width()//2, 290])
        imprimir_palabra(screen, juego)
        nueva_imagen(imagenes, juego, screen)

        # Título
        centex_x = juego.screen_width // 2 - titulo.get_width() // 2  # Posic. text
        screen.blit(titulo, [centex_x, 30])  # Texto en pantalla

        for i in range(27):
            botones[i].draw_button(juego, screen)
        if any(boton.rect.collidepoint(pygame.mouse.get_pos()) for boton in botones):
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()
        terminado(juego)
    pygame.quit()


main()
