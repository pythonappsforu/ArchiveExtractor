import PySimpleGUI as sg
from extractArchive import extract_archive
import zipfile

sg.theme('dark grey 9')

ip_label = sg.Text('Enter path of zip file: ')
zip_path = sg.Input(key='filepath')
file_btn =  sg.FileBrowse('Choose')

op_label = sg.Text('Enter path of destination folder: ')
folder_path = sg.Input(key='folderpath')
folder_btn =  sg.FolderBrowse('Browse')

extract_button = sg.Button('Extract')
feedback_label = sg.Text(key='feedback',text_color='green')

window = sg.Window(title='Archive Extractor',layout=[[ip_label,zip_path,file_btn],
                                                     [op_label,folder_path,folder_btn],
                                                     [extract_button,feedback_label]])

while True:
    event,values = window.read()
    print(event,values)
    try:
        extract_archive(filepath=values['filepath'],dest_folder=values['folderpath'])
        window['feedback'].update('files extracted successfully')
    except zipfile.BadZipFile as e:
        sg.popup(e)
#todo implement try except for all scenarios




window.close()