import PySimpleGUI as sg

td=[]
Headings=['Vardas', 'Pavardė', 'Skyrius']

layout=[
        [sg.Text(Headings[0]),sg.Input(size=20,key=Headings[0])],
        [sg.Text(Headings[1]),sg.Input(size=20,key=Headings[1])],
        [sg.Text(Headings[2]),sg.Combo(['IT skyrius','Finansai','Administracija'],key=Headings[2])],
        [sg.Button('Pridėti'),sg.Button('Redaguoti'),        # New buttons
            sg.Button('Išsaugoti',disabled=True),sg.Button('Ištrinti'),sg.Exit()],
        [sg.Table(td,Headings,key='myTable')]]

window=sg.Window('Personalo valdymo programa',layout)

while True:
    event,values= window.read()
    print (values)
    if event == 'Pridėti':
        td.append([values[Headings[0]],values[Headings[1]],values[Headings[2]]])
        window['myTable'].update(values=td)
        for i in range(3):    
            window[Headings[i]].update(value='')
    if event == 'Redaguoti':
        if values['myTable']==[]:
            sg.popup('Pasirinkite eilutę')
        else:
            editRow=values['myTable'][0]
            sg.popup('Redaguoti')
            for i in range(3):  
                window[Headings[i]].update(value=td[editRow][i])
            window['Išsaugoti'].update(disabled=False)
    if event == 'Išsaugoti':
        td[editRow]=[values[Headings[0]],values[Headings[1]],values[Headings[2]]]
        window['myTable'].update(values=td)
        for i in range(3):
            window[Headings[i]].update(value='')
        window['Išsaugoti'].update(disabled=True)
    if event == 'Ištrinti':
        if values['myTable']==[]:
            sg.popup('Pasirinkite eilutę')
        else:
            if sg.popup_ok_cancel('Ar tikrai norite tęsti?') == 'OK':
                del td[values['myTable'][0]]
                window['myTable'].update(values=td)

    if event in (sg.WIN_CLOSED, 'Exit'):
        break
window.close()