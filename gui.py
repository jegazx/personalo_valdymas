import PySimpleGUI as sg
from datetime import date
from personalo_valdymas import PersonaloValdymas
import json

def sarasas():
    for darbuotojas in darbuotojai._PersonaloValdymas__darbuotojai.values():
        td.append([darbuotojas['vardas_pavarde'], darbuotojas['komentaras'], darbuotojas['alga'], darbuotojas['priimtas'], darbuotojas['tel_numeris'], darbuotojas['ak'], darbuotojas['issilavinimas'], darbuotojas['padalinys']])

darbuotojai = PersonaloValdymas()
darbuotojai = PersonaloValdymas.pickle_nuskaitymas(darbuotojai)
td=[]
headings=['Vardas Pavardė', 'Komentaras', 'Alga', 'Priimtas', 'Telefono numeris', 'Asmens kodas', 'Išsilavinimas', 'Skyrius']

layout=[
        [sg.Text(headings[0], size=(15,1)),sg.Input(size=20,key=headings[0])],
        [sg.Text(headings[1], size=(15,1)),sg.Input(size=20,key=headings[1])],
        [sg.Text(headings[2], size=(15,1)),sg.Input(size=20,key=headings[2])],
        [sg.Text(headings[3], size=(15,1)),sg.Input(size=20,key=headings[3])],
        [sg.Text(headings[4], size=(15,1)),sg.Input(size=20,key=headings[4])],
        [sg.Text(headings[5], size=(15,1)),sg.Input(size=20,key=headings[5])],
        [sg.Text(headings[6], size=(15,1)),sg.Input(size=20,key=headings[6])],
        [sg.Text(headings[7], size=(18,1)),sg.Combo(['IT skyrius','Finansai','Administracija'],key=headings[7])],
        [sg.Button('Pridėti'), sg.Button('Redaguoti'), sg.Button('Išsaugoti',disabled=True), sg.Button('Ištrinti'), sg.Push(), sg.Exit()],
        [sg.Table(td,headings,key='myTable')]]

window=sg.Window('Personalo valdymo programa',layout)
sarasas()
while True:
    event,values= window.read()
    print (values)
    if event == 'Pridėti':
        values = [values[h] for h in headings]
        td.append(values)
        darbuotojai.prideti_darbuotoja(*values)
        darbuotojai.darbuotoju_sarasas()
        window['myTable'].update(values=td)
        for i in range(len(headings)):    
            window[headings[i]].update(value='')
    if event == 'Redaguoti':
        if values['myTable']==[]:
            sg.popup('Pasirinkite eilutę, kurią norite redaguoti')
        else:
            editRow=values['myTable'][0]
            for i in range(len(headings)):  
                window[headings[i]].update(value=td[editRow][i])
            window['Išsaugoti'].update(disabled=False)
    if event == 'Išsaugoti':
        td[editRow]=([values[h] for h in headings])
        window['myTable'].update(values=td)
        for i in range(len(headings)):
            window[headings[i]].update(value='')
        window['Išsaugoti'].update(disabled=True)
    if event == 'Ištrinti':
        if values['myTable']==[]:
            sg.popup('Pasirinkite eilutę')
        else:
            if sg.popup_ok_cancel('Ar tikrai norite tęsti?') == 'OK':
                pasirinkta_eilute = values['myTable'][0]
                pasirinktas_vardas = td[pasirinkta_eilute][0]
                print(pasirinktas_vardas)
                del td[pasirinkta_eilute]
                data = date.today()
                data_str = data.strftime('%Y-%m-%d')
                darbuotojai.atleisti_darbuotoja(pasirinktas_vardas, data_str)
                darbuotojai.atleistu_darbuotoju_sarasas()
                darbuotojai.darbuotoju_sarasas()
                window['myTable'].update(values=td)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
window.close()