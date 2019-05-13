import pyautogui
import os

global parar,location
parar = False
location = os.getcwd()

def test(imagen,threshold):
    global parar,location
    
    pos = pyautogui.locateOnScreen(location +'\\img\\'+ imagen,30,confidence= threshold)
    if pos == None:
        parar = True
        print('Posible Fallo')
        
    posx, posy = pyautogui.center(pos)
    pyautogui.click(x=posx, y=posy)

n = 1
while parar == False:
    print(n)
    #paso1 pulsar la dificultad
    test('Infernal.png',0.95)
    #paso2 iniciar el mapa
    test('fight.png',0.95)
    #paso3 saltar la intro
    test('carga.png',0.65)
    #paso4 auto-battle
    test('auto.png',0.99)
    #paso5 confirmar auto-battle
    test('auto2.png',0.95)
    #paso6 end
    test('final.png',0.6)
    #paso7 finalizar
    test('ok.png',0.95)
    n+=1
    
