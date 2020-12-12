import PySimpleGUI as sg

sg.theme("Dark Amber")

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
            Toca(num)
            break
        window["-nun-"].update(tex)

    window.close()

def Toca(n):
    print(n)
    lay2=[[sg.Button("Pausar"),sg.Button("Parar"),sg.Text(font=(16,16),size=(8,1),key="-nu-")]]

    window2=sg.Window("Toncando",lay2)

    while True:
        e, v=window2.read()
        if e== sg.WINDOW_CLOSED or e=="Parar":
            init()
            break
        window["-nun-"].update(1)

    window2.close()

init()