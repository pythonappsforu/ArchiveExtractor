import PySimpleGUI as sg

sg.theme('dark grey 9')

ip_label = sg.Text('Enter path of zip file: ')
zip_path = sg.Input(key='filepath')
file_btn =  sg.FileBrowse('Choose')

op_label = sg.Text('Enter path of destination folder: ')
folder_path = sg.Input(key='folderpath')
folder_btn =  sg.FileBrowse('Browse')

extract_button = sg.Button('Extract')
feedback_label = sg.Text(key='feedback',text_color='green')

window = sg.Window(title='Archive Extractor',layout=[[ip_label,zip_path,file_btn],
                                                     [op_label,folder_path,folder_btn],
                                                     [extract_button,feedback_label]])

window.read()
window.close()