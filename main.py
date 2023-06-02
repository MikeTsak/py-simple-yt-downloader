from pytube import YouTube #pip intall pytube
import PySimpleGUI as sg #pip install pysimplegui

sg.theme('DarkBrown4')
sg.set_options(font=('Arial Bold', 16))

def secs_to_mins(secs):
    mins = secs // 60
    secs = secs % 60
    return str(mins) + ":" + str(secs)

while True:
    #layout for GUI
    layout = [[sg.Text("Enter the link of the video")],
              [sg.Input(key='-LINK-')],
              [sg.Button('Ok'), sg.Button('Cancel')]]

    #create window
    window = sg.Window('Youtube Downloader', layout)

    #event loop
    event, values = window.read()
    window.close()

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    #get link from user
    link = values['-LINK-']

    
    #create youtube object
    yt = YouTube(link)
    time = secs_to_mins(yt.length)
    layout = [[sg.Text("Title: " + yt.title)],
              [sg.Text("Views: " + str(yt.views))],
                [sg.Text("Length: " + str(time))],
                [sg.Text("Download Audio or Video?")],
                [sg.Button('Download Audio Only'), sg.Button('Download Video + Audio')],
                [sg.Button('Cancel')]]
    window = sg.Window('Youtube Downloader', layout)
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    window.close()

    if event == 'Download Audio Only':
        stream = yt.streams.filter(only_audio=True).get_audio_only()
        stream.download()
    elif event == 'Download Video + Audio':
        # download video oin hiest possible resolution
        stream = yt.streams.get_highest_resolution()
        stream.download()

    #final window to show download is complete
    layout = [[sg.Text("Download Complete")],
                [sg.Button('Ok')]]
    window = sg.Window('Youtube Downloader', layout)
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Ok':
        window.close()
    break

# input()

