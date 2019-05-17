import pyautogui
import os
import tkinter as tk

def test(imagen,threshold,fase):
    global funcionar,location
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
    

def farmear(dificultad):
    global funcionar,location
    fase = 1

    while funcionar:
        #paso1 pulsar la dificultad
        if fase == 1 :
            test(dificultad + '.png',0.95,fase)
        #paso2 iniciar el mapa
        elif fase == 2 :
            test('fight.png',0.95,fase)
        #paso3 saltar la intro
        elif fase == 3 :
            test('carga.png',0.65,fase)
        #paso4 auto-battle
        elif fase == 4 :
            test('auto.png',0.99,fase)
        #paso5 confirmar auto-battle
        elif fase == 5 :
            test('auto2.png',0.95,fase)
        #paso6 end
        elif fase == 6 :
            test('final.png',0.6,fase)
        #paso7 finalizar
        elif fase == 7:
            test('ok.png',0.9,fase)
        
def parar():
    global funcionar
    funcionar = False
    
global funcionar,location
location = os.getcwd()
funcionar = True
#Dibujar menu
root = tk.Tk()
root.minsize(300,100)
root.geometry("320x100")

dificultad = tk.StringVar()
dificultad_menu = tk.OptionMenu(root, dificultad, 'Infernal', 'Lunatico')
dificultad_menu.pack()
dificultad.set('Lunatico')

boton = tk.Button(root, text="test", command=lambda:farmear(dificultad.get()))
boton.pack()

stop = tk.Button(root, text="Stop", command=lambda:parar())
stop.pack()


root.mainloop()

