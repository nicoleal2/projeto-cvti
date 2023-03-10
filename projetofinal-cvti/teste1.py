import csv
import PySimpleGUI as sg

sg.theme('black')
layout = [
    [sg.Text('Agende sua Aula.', font=40)],
    [sg.Text('Horários Disponíveis:', font=20)],
    [sg.Listbox(values=['Manhã 1 - 08:00 às 9:30', 'Manhã 2 - 10:00 às 11:30'],size=(60, 2))],
    [sg.Listbox(values=['Tarde 1 - 13:30 às 15:00', 'Tarde 2 - 16:00 às 15:00'],size=(60, 2))],
    [sg.Listbox(values=['Noite 1 - 18:30 às 20:00', 'Noite 2 -20:00 às 21:30'], size=(60, 2))],
    [sg.Text('Escolha o melhor horário para você:')],
    [sg.Checkbox('Manhã 1', default=False)],
    [sg.Checkbox('Manhã 2', default=False)],
    [sg.Checkbox('Tarde 1', default=False)],
    [sg.Checkbox('Tarde 2', default=False)],
    [sg.Checkbox('Noite 1', default=False)],
    [sg.Checkbox('Noite 2', default=False)],
    [sg.Button('Ok!')]
    ]
#janela 
janela = sg.Window('Aulas', layout)

while True: 
 janela.read()
#  arquivo = open ("layout", "a")
 file1 = open("layout")  
 print(file1.read()) 
 if janela == sg.WIN_CLOSED():
  janela.close()
# eventos 

