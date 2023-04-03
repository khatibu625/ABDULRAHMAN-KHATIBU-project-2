import PySimpleGUI as sg
import qrcode 

#GENRATED QR CODE LAYOUT
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
    )
layout = [
    [sg.Input(key = "data")],
    [sg.Button('Create')],
    [sg.Image(key = 'QR code')]
    ]

window = sg.Window('QR Code Generator', layout)

#EVENT LOOP
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Create':
        text = values['data']
        img = qrcode.make(text)
        img.save('qr.png')
        window['QR code'].update(filename = 'qr.png')

window.close()
