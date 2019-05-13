import pyautogui
import os

def test(imagen,threshold):
    global parar,location,fase
    pos = pyautogui.locateOnScreen(location +'\\img\\'+ imagen,30,confidence= threshold)
    if pos == None:
        pass
    else :
        posx, posy = pyautogui.center(pos)
        pyautogui.click(x=posx, y=posy)
        
    if fase < 7 :
        fase += 1
    else :
        fase = 1
    

#Main  
global parar,location,n_error,fase

parar = False
location = os.getcwd()
n = 0
fase = 1

while parar == False:
    #paso1 pulsar la dificultad
    if fase == 1 :
        test('Infernal.png',0.95)
    #paso2 iniciar el mapa
    elif fase == 2 :
        test('fight.png',0.95)
    #paso3 saltar la intro
    elif fase == 3 :
        test('carga.png',0.65)
    #paso4 auto-battle
    elif fase == 4 :
        test('auto.png',0.99)
    #paso5 confirmar auto-battle
    elif fase == 5 :
        test('auto2.png',0.95)
    #paso6 end
    elif fase == 6 :
        test('final.png',0.6)
    #paso7 finalizar
    elif fase == 7:
        test('ok.png',0.9)
        n+=1
        print(n)
    
