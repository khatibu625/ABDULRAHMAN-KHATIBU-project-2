import PySimpleGUI as sg
import pyttsx3
layout = [
    [sg.Input(key='text'),sg.Button('Speak')],
    [sg.Text('Select Voice Type'),sg.Radio('Male','RADIO',key='-male-',default=True),
     sg.Radio('Female','RADIO',key='-female-')],
    # [sg.Text('Volume:'),sg.Text('Speed:',pad=(150,0))],

    #  sg.Slider(range=(0,10),default_value=5,orientation='h',size=(20,15),key='-SPEED-')]
]

window =sg.Window('Text to Speech App',layout)

while True:
    event,values = window.read()
    engine = pyttsx3.init()
    
    if event== sg.WIN_CLOSED:
        break
    elif event == 'Speak':
        text = values['text']
        voices = engine.getProperty('voices') 
        # rate = engine.getProperty('rate')   


        if values['-male-']:
           engine.setProperty('voice', voices[0].id)
        else:
           engine.setProperty('voice', voices[1].id)
        
        engine.say(text)
        engine.runAndWait()
        # speed = values['-SPEED-']
        # volume = values['-VOLUME-']
window.close()





#voices = engine.getProperty('voices')  
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for    male
# engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female


