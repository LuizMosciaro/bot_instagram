import random
import pyautogui as p
from time import sleep as s

s(3)
p.hotkey('win','r')
p.write('https://www.instagram.com/explore/')
p.press('enter')
s(8)

#click na primeira foto o bloco
p.click(365,180)
s(random.randrange(4,6))

y = 0
while True:
    x = 0
    while True:
        #procurando o botao de like
        like = p.locateOnScreen('coracao.png', confidence=0.7,grayscale=True)
        p.click(like)
        s(random.randrange(4,7))
        #procurando o botao de proximo
        p.press('right')
        s(random.randrange(4,7))

        #depois de 12 curtidas eles tem q carregar a pagina
        if x >= 12:
            p.press('esc')
            s(random.randrange(4,7))
            p.press('end')
            p.press('end')
            s(random.randrange(4,7))
            p.click(365,180)
            s(random.randrange(4,7))
            x = x-12
            
        x+=1
        if y >= 100:
            p.press('f5')
            s(random.randrange(4,7))
        y+=1
        print(f"Bot deu {y} likes")