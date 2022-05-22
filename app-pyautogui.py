import random
import pyautogui as p
from time import sleep as s
import keyboard

s(2)
p.hotkey('win','r')
p.write('https://www.instagram.com/explore/')
p.press('enter')
s(8)

#click na primeira foto o bloco
p.click(365,180)
s(random.randrange(3,5))


x = 0
while True:

    #procurando o botao de like
    like = p.locateOnScreen('coracao.png', confidence=0.7,grayscale=True)
    p.click(like)
    s(random.randrange(2,4))
    #procurando o botao de proximo
    p.press('right')
    s(random.randrange(2,4))

    #depois de 12 curtidas eles tem q carregar a pagina
    if x >= 12:
        p.press('esc')
        s(random.randrange(2,4))
        p.press('end')
        s(random.randrange(3,5))
        p.click(365,180)
        s(random.randrange(2,4))
        x = x-12
    else:
        pass

    x+=1