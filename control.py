import PySimpleGUI as sg
from time import sleep

sg.theme("Dark Amber")

tic=0
timerGeral=''

def init():
    num=[]
    tex=''
    Gat=True

    lay=[[sg.Button("Play"),sg.Button("Limpar"),sg.Text(tex,font=(16,16),size=(8,1),key="-nun-")]]

    window=sg.Window('PyCron',lay, return_keyboard_events=True)

    while Gat:
        e, v =window.read()
        window["-nun-"].update(tex)
        if e== sg.WINDOW_CLOSED:
            exit()
        if e=='0' or e=='1' or e=='2' or e=='3' or e=='4' or e=='5' or e=='6' or e=='7' or e=='8' or e=='9':
            print(len(tex))
            if len(tex)<=7:
                if len(tex)==2 or len(tex)==5:
                    tex=':'+tex
                tex=e+tex

                n=[int(e)]
                n.extend(num)
                num=n
        if e=="Limpar":
            tex=''
            num=[]
        if e=="Play" and num!=[]:
            break
        window["-nun-"].update(tex)

    window.close()
    Toca(num)

def Toca(n):
    
    timer=100
    boolCont=True
    valor='00:00:00'
    seg=0
    minu=0
    hor=0
    Segtmp=''
    Mintmp='00'
    Hortmp='00'
    print(n)
    lay2=[[sg.Button("Pausar"),sg.Button("Parar"),sg.Text(font=(16,16),size=(8,1),key="-nu-")]]

    window2=sg.Window("Toncando",lay2)

    while True:
        global timerGeral
        global tic
        tic+=1
        # Velocidade do while
        if boolCont:
            timer=100
        else:
            timer=None

        e, v=window2.read(timer)

        if e== sg.WINDOW_CLOSED or e=="Parar":
            timerGeral=''
            break
        if e=="Pausar":
            # Pausar o contador
            if boolCont:
                boolCont=False
            else:
                boolCont=True
        
        if tic==10:
            # Segundo contador
            seg+=1
            Segtmp=str(seg)

            if seg==60:
                seg=0
                minu+=1
                if minu==60:
                    minu=0
                    hor+=1
                    # Hora contador
                    Hortmp=str(hor)
                    if hor<10:
                        Hortmp='0'+str(hor)
                # Minutos contador
                Mintmp=str(minu)
                if minu<10:
                    Mintmp='0'+str(minu)


            if seg<10:
                segn='0'+str(seg)
                Segtmp=segn

            timerGeral=Hortmp+':'+Mintmp+':'+Segtmp
            tic=0
        
        # Atualização do texto do timer
        window2["-nu-"].update(timerGeral)

    window2.close()
    init()

init()


