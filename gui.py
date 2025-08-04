import pygame

class Button():
    '''
    Button that can display a text and on click run a function.
    Adds itself to "objects".
    ----
    '''
    def __init__(self, objects: list, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False, font = ['Arial', 40]):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#FF99C7',
            'pressed': '#E75480',
        }
        self.font = font

        self.buttonText = buttonText
        self.edit_buttonText(buttonText)
        objects.append(self)
        self.objects = objects

    def edit_buttonText(self, text):
        # surface that contains the buttonText
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = pygame.font.SysFont(self.font[0], self.font[1]).render(text, True, (20, 20, 20))

    def process(self, info):
        '''
        Precesses the onclick funtion of the button. Should be run inside game loop
        ----
        '''
        screen = info[0]
        self.edit_buttonText(self.buttonText)
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        # blitting the text onto the buttonSurface and then this surface onto the screen
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)