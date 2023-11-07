import PySimpleGUI as sg
from extractArchive import extract_archive
import zipfile

sg.theme('dark grey 9')

ip_label = sg.Text('Enter path of zip file: ')
zip_path = sg.Input(key='filepath')
file_btn =  sg.FileBrowse('Choose',target='filepath')

op_label = sg.Text('Enter path of destination folder: ')
folder_path = sg.Input(key='folderpath')
folder_btn =  sg.FolderBrowse('Browse',target='folderpath')

extract_button = sg.Button('Extract')
feedback_label = sg.Text(key='feedback',text_color='green')

col1 = sg.Column([[ip_label],[op_label]])
col2 = sg.Column([[zip_path],[folder_path]])
col3 = sg.Column([[file_btn],[folder_btn]])

window = sg.Window(title='Archive Extractor',layout=[[col1,col2,col3],[extract_button,feedback_label]])

while True:
    event,values = window.read()
    print(event,values)
    if values['filepath'] == '' or values['folderpath'] == '':
        sg.popup("Please choose directories before attempting to compress files.",
                 font=("Helvetica", 12))
    else:
        try:
            extract_archive(filepath=values['filepath'],dest_folder=values['folderpath'])
            window['feedback'].update('files extracted successfully')
        except zipfile.BadZipFile as e:
            sg.popup(e)
#todo implement try except for all scenarios




window.close()