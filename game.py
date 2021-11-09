from pygame import display
from pygame.image import load

tamanho = (500,500)

superficie = display.set_mode(
    display=0,
    size=tamanho
    )
display.set_caption(
    'teste'
)
fundo = load('images/01.jpg')

while True:
    display.update()
