import pygame
import settings


def intro(juego, screen):
    '''
    Pantalla de introducción al juego
    '''
    # TEXTOS
    titulo = juego.titulo.render("Adivina la palabra", True, juego.white)
    credits = juego.tiny.render("hormigo software, 2021", True, juego.white)
    explica = juego.normal.render(
        "Elige un tipo de palabra para jugar:", True, juego.grey)

    # IMÁGENES
    rutas = ['images/nombres.png', 'images/paises.png',
             'images/cuatro.png', 'images/largas.png', 'images/ninos.png']
    imagenes = [None]*5
    for i, ruta in enumerate(rutas):
        imagenes[i] = pygame.image.load(ruta)
        imagenes[i] = pygame.transform.scale(imagenes[i], (100, 100))

    # BOTONES
    botones_texto = [
        ['Nombres', 'Nombres de personas de entre los 200 más frecuentes.'],
        ['Países', 'Nombres de los países del Mundo.'],
        ['Palabras de 4 letras',
            'Elegidas de entre las más habituales, incluídos nombres propios'],
        ['Palabras largas',
         'De más de 8 letras, incluidos nombres propios.'],
        ['Para niños', 'Palabras fáciles sobre un tema aleatorio.']
    ]

    botones = pygame.sprite.Group()
    botones = [settings.TextButton(
        250, 230+i*135, botones_texto[i][0], juego) for i in range(5)]
    textitos = [juego.tiny.render(boton[1], True, juego.grey)
                for boton in botones_texto]

    while not juego.done:
        screen.fill(juego.bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                juego.done = True
            elif event.type == pygame.MOUSEBUTTONUP:
                for i in range(5):
                    if botones[i].rect.collidepoint(pygame.mouse.get_pos()):
                        return juego.opciones[i]

        # Título
        centex_x = juego.screen_width // 2 - titulo.get_width() // 2  # Posic. text
        screen.blit(titulo, [centex_x, 50])  # Texto en pantalla

        # Créditos
        screen.blit(credits, [juego.screen_width-50 -
                    credits.get_width(), juego.screen_height-50])

        # Texto explicación
        screen.blit(explica, [100, 150])

        # Opciones
        for i, imagen in enumerate(imagenes):
            screen.blit(imagen, [100, 215 + 135*i])

        # Botones
        for boton in botones:
            boton.muestra_boton(juego, screen)

        if any(boton.rect.collidepoint(pygame.mouse.get_pos()) for boton in botones):
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
        for i, texto in enumerate(textitos):
            screen.blit(texto, [250, 275+i*135])

        pygame.display.flip()

    pygame.quit()
