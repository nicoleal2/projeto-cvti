
import PySimpleGUI as sg

sg.theme('black')
layout = [
    [sg.Text('Agende sua Aula.', font=40)],
    [sg.Text('Horários Disponíveis:', font=20)],
    [sg.Listbox(values=['Manhã 1 - 08:00 às 9:30', 'Manhã 2 - 10:00 às 11:30'],size=(60, 2))],
    [sg.Listbox(values=['Tarde 1 - 13:30 às 15:00', 'Tarde 2 - 16:00 às 15:00'],size=(60, 2))],
    [sg.Listbox(values=['Noite 1 - 18:30 às 20:00', 'Noite 2 -20:00 às 21:30'], size=(60, 2))],
    [sg.Text('Escolha o melhor horário para você:')],
    [sg.Checkbox('Manhã 1', default= 0, key='m1')],
    [sg.Checkbox('Manhã 2', default= 0, key='m2')],
    [sg.Checkbox('Tarde 1', default= 0, key='t1')],
    [sg.Checkbox('Tarde 2', default= 0, key='t2')],
    [sg.Checkbox('Noite 1', default= 0, key='n1')],
    [sg.Checkbox('Noite 2', default= 0, key='n2')],
    [sg.Button('Ok!')]
    ]
janela = sg.Window('Agendamento de Aulas').Layout(layout)
#função que lida com o salvamento  
def salvar_dados(valores):
    arquivo = open("dados.csv", "w")
    arquivo.write("Horarios escolhidos:"+ str(valores))
    arquivo.close()
    sg.popup("Aula agendada com sucesso!")

#loop da janela principal
while True:
    evento, valores = janela.Read()
    if evento== sg.WINDOW_CLOSED:
        break
    elif evento == 'Ok!':
        salvar_dados(valores)


