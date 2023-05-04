import PySimpleGUI as sg
from datetime import date
from personalo_valdymas import PersonaloValdymas


def sarasas():
    for darbuotojas in darbuotojai._PersonaloValdymas__darbuotojai.values():
        td.append([darbuotojas['vardas_pavarde'], darbuotojas['komentaras'], darbuotojas['alga'], darbuotojas['priimtas'], darbuotojas['atleistas'], darbuotojas['tel_numeris'], darbuotojas['ak'], darbuotojas['issilavinimas'], darbuotojas['padalinys']])

darbuotojai = PersonaloValdymas()
darbuotojai = PersonaloValdymas.pickle_nuskaitymas(darbuotojai)
td=[]
Headings=['Vardas Pavardė', 'Komentaras', 'Alga', 'Priimtas', 'Atleistas', 'Telefono numeris', 'Asmens kodas', 'Išsilavinimas', 'Skyrius']
layout=[
        [sg.Text(Headings[0], size=(15,1)),sg.Input(size=20,key=Headings[0])],
        [sg.Text(Headings[1], size=(15,1)),sg.Input(size=20,key=Headings[1])],
        [sg.Text(Headings[2], size=(15,1)),sg.Input(size=20,key=Headings[2])],
        [sg.Text(Headings[3], size=(15,1)),sg.Input(size=20,key=Headings[3])],
        [sg.Text(Headings[4], size=(15,1)),sg.Input(size=20,key=Headings[4])],
        [sg.Text(Headings[5], size=(15,1)),sg.Input(size=20,key=Headings[5])],
        [sg.Text(Headings[6], size=(15,1)),sg.Input(size=20,key=Headings[6])],
        [sg.Text(Headings[7], size=(15,1)),sg.Input(size=20,key=Headings[7])],
        [sg.Text(Headings[8], size=(18,1)),sg.Combo(['IT skyrius','Finansai','Administracija'],key=Headings[8])],
        [sg.Button('Pridėti'), sg.Button('Redaguoti'), sg.Button('Išsaugoti',disabled=True), sg.Button('Ištrinti'), sg.Push(), sg.Exit()],
        [sg.Table(td,Headings,key='myTable')]]

window=sg.Window('Personalo valdymo programa',layout)
sarasas()
while True:
    event,values= window.read()
    print (values)
    if event == 'Pridėti':
        td.append([values[Headings[0]], values[Headings[1]], values[Headings[2]], values[Headings[3]], values[Headings[4]], values[Headings[5]], values[Headings[6]], values[Headings[7]], values[Headings[8]]])
        darbuotojai.prideti_darbuotoja(values[Headings[0]], values[Headings[1]], values[Headings[2]], values[Headings[3]], values[Headings[4]], values[Headings[5]], values[Headings[6]], values[Headings[7]], values[Headings[8]])
        darbuotojai.darbuotoju_sarasas()
        window['myTable'].update(values=td)
        for i in range(9):    
            window[Headings[i]].update(value='')
    if event == 'Redaguoti':
        if values['myTable']==[]:
            sg.popup('Pasirinkite eilutę')
        else:
            editRow=values['myTable'][0]
            sg.popup('Redaguoti')
            for i in range(9):  
                window[Headings[i]].update(value=td[editRow][i])
            window['Išsaugoti'].update(disabled=False)
    if event == 'Išsaugoti':
        td[editRow]=([values[Headings[0]],values[Headings[1]], values[Headings[2]], values[Headings[3]], values[Headings[4]], values[Headings[5]], values[Headings[6]], values[Headings[7]], values[Headings[8]]])
        window['myTable'].update(values=td)
        for i in range(9):
            window[Headings[i]].update(value='')
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