import pandas as pd
import PySimpleGUI as sg

sg.theme('black')
layout = [
    [sg.Text('Agende sua Aula.', font=40)],
    [sg.Text('Horários Disponíveis:', font=20)],
    [sg.Listbox(values=['Manhã 1 - 08:00 às 9:30', 'Manhã 2 - 10:00 às 11:30'],size=(60, 2))],
    [sg.Listbox(values=['Tarde 1 - 13:30 às 15:00', 'Tarde 2 - 16:00 às 15:00'],size=(60, 2))],
    [sg.Listbox(values=['Noite 1 - 18:30 às 20:00', 'Noite 2 -20:00 às 21:30'], size=(60, 2))],
    [sg.Text('Escolha o melhor horário para você:')],
    [sg.Checkbox('Manhã 1', default=False, key='m1')],
    [sg.Checkbox('Manhã 2', default=False, key='m2')],
    [sg.Checkbox('Tarde 1', default=False, key='t1')],
    [sg.Checkbox('Tarde 2', default=False, key='t2')],
    [sg.Checkbox('Noite 1', default=False, key='n1')],
    [sg.Checkbox('Noite 2', default=False, key='n2')],
    [sg.Button('Ok!')]
    ]
#janela 
janela = sg.Window('Aulas', layout)
mid = pd.read_csv('layout.csv')
op = ['m1','m2','t1','t2','n1','n2']
while True: 
 event, values = janela.read()
 
 #arquivo = open ('"layout.csv", "a")
 #file1 = open("layout")  
 
 if event == sg.WIN_CLOSED:
  break
 if event == 'Ok!':
  for val in op:
   if values[val]:
    mid.append({'hora':val})
   
   df = pd.DataFrame(mid)
   df.to_csv('layout.csv', index= False)
janela.close()
# eventos 