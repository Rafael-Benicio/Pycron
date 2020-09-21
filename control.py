import PySimpleGUI as sg
from time import sleep

nuns=''
Pau=False
SleepTime=0
Hou=0
Min=0
Sec=0
event=''

layout=[[sg.Button('Tocar '),sg.Button('Pausar'),sg.Button('Parar '),sg.Text('',size=(7,1),key='val',font="Helvetica "  + str(20))]]

sg.theme('Dark Purple')

window=sg.Window('Crônos',layout, no_titlebar=True, auto_size_buttons=False, keep_on_top=True, grab_anywhere=True, return_keyboard_events=True,use_default_focus=True)


# Para receber o valor passado no timer   
def Recebe():
    global nuns
    if len(nuns)<=7  and event == '1' or len(nuns)<=7  and event == '2' or len(nuns)<=7  and event == '3' or len(nuns)<=7  and event == '4' or len(nuns)<=7  and event == '5' or len(nuns)<=7  and event == '6' or len(nuns)<=7  and event == '7' or len(nuns)<=7  and event == '8' or len(nuns)<=7  and event == '9' or len(nuns)<=7  and event == '0':
        nuns=nuns+event
        if len(nuns)==2 or len(nuns)==5:
            nuns=nuns+':'
        window['val'].update(nuns)

# Transformação de str para int 
def Inicia():
    global Pau
    Pau=True
    try:
        Hou=int(nuns[0]+nuns[1])
    except:
        Hou=00
    try:
        Min=int(nuns[3]+nuns[4])
    except:
        Min=00
    try:
        Sec=int(nuns[6]+nuns[7])   
    except:
        Sec=00
    print(Hou, Min, Sec)

# Atalhos de Teclado
def Snipper():
    global event
    if event == 'F12:96':
        window.close()
    if event == 'F1:67' or event == 'Tocar ':
        if Pau==False:
            Inicia()
        event=''
    if event == 'F2:68' or event == 'Pausar':
        Pausar()
        event=''
    if event == 'F3:69' or event == 'Parar ':
        Parar()
        event=''

# Apaga o ultimo valor da timer
def ApagaLetra():
    global nuns
    newNun=''
    key=len(nuns)-1
    if event == ']':
        for i in range(key):
            newNun+=nuns[i]
        nuns=newNun
        window['val'].update(nuns)
        print(nuns)

# Pausar ou Rodar
def Pausar():
    global Pau
    if Pau==False:
        Pau=True
    else:
        Pau=False
    print(Pau)

# Para o processo
def Parar():
    global Pau 
    Pau=False
    print(Pau)

# Timer
def Tocar():
    global Sec 
    global Min
    global Hou
    global event
    global SleepTime
    sleep(1)
    SleepTime+=1
    
        # if Sec == 0 and Min == 0 and Hou == 0:
                # Finaliza e toca musica
    print(SleepTime)
    
# Loop Principal
while True:
    event,value=window.read(100)
    if event == sg.WIN_CLOSED:
        break
    Snipper()
    Recebe()
    ApagaLetra()
    if Pau:Tocar()
    if Pau:
        window['val'].update(f'{Hou}:{Min}:{Sec}')


window.close()
