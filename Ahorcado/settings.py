import pygame


class Settings():
    '''Guarda los settings del juego'''

    def __init__(self):
        """Inicializa the game's settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 900
        self.bg_color = (00, 80, 180)
        self.caption = 'Adivina la palabra'

        # Colores
        self.white = (255, 255, 255)
        self.grey = (170, 170, 170)
        self.black = (0, 0, 0)
        self.red = (100, 0, 0)

        # Desarrollo
        self.done = False
        self.opciones = ['nombres', 'paises', 'cuatro', 'largas', 'ninos']

        # Fuentes
        self.titulo = pygame.font.SysFont('sans serif', 80, italic=False)
        self.subtitulo = pygame.font.SysFont('sans serif', 70, italic=True)
        self.normal = pygame.font.SysFont('sans serif', 50)
        self.tiny = pygame.font.SysFont('sans serif', 30, italic=True)
        self.guess = pygame.font.SysFont('monospace', 70, bold=True)


class TextButton(pygame.sprite.Sprite):
    '''
    Botones que son solo texto
    '''

    def __init__(self, x, y, text, juego):
        super().__init__()
        self.x = x
        self.y = y
        self.text = text
        self.font = pygame.font.SysFont('sans serif', 60)
        self.color = juego.white
        self.text_img = self.font.render(self.text, True, self.color)
        self.size = self.text_img.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def muestra_boton(self, juego, screen):

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.color = juego.white
        else:
            self.color = juego.grey
        self.text_img = self.font.render(self.text, True, self.color)
        screen.blit(self.text_img, [self.x, self.y])


class Button():
    def __init__(self, x, y, text, juego):
        self.x = x
        self.y = y
        self.text = text
        self.color = juego.grey
        self.negro = False
        self.font = pygame.font.SysFont('monospace', 40, bold=True)
        self.radius = 30
        self.rect = pygame.Rect(self.x-self.radius//2, self.y-self.radius //
                                2, self.x+self.radius//2, self.y+self.radius//2)

    def draw_button(self, juego, screen):
        pygame.draw.circle(screen, juego.black, (self.x, self.y), self.radius)
        if not self.negro:
            cursor = pygame.mouse.get_pos()
            if abs(self.x-cursor[0]) < self.radius and abs(self.y-cursor[1]) < self.radius:
                self.color = juego.black
            else:
                self.color = juego.grey
            pygame.draw.circle(screen, self.color,
                               (self.x, self.y), self.radius-2)
            self.letra_boton = self.font.render(self.text, True, juego.white)
            screen.blit(self.letra_boton, [self.x-12, self.y-20])
        else:
            self.letra_boton = self.font.render(self.text, True, juego.red)
            screen.blit(self.letra_boton, [self.x-12, self.y-20])


if __name__ == '__main__':
    pygame.init()
    juego = Settings()
    prueba = TextButton(0, 0, 'Holaskk', juego)
    print(prueba.size[0], prueba.size[1])
