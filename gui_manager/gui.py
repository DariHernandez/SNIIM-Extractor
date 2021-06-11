import json
import os
import threading
import time
import globals
import config
import PySimpleGUI as sg
from playsound import playsound

current_file = os.path.basename(__file__)
current_folder = os.path.dirname(__file__)  
config_path = os.path.join(current_folder, "config.json")
sound_file = os.path.join (current_folder, "alert.wav")


def theme_selector (): 
    """
    GUI for select theme and save it in config file
    """  
    
    # Apply config theme
    theme = config.get_credential("theme")
    sg.theme(theme)
    
    layout = [[sg.Text('List of InBuilt Themes')],
            [sg.Text('Please Choose a Theme  to see Demo window')],
            [sg.Listbox(values = sg.theme_list(),
                        size =(20, 12),
                        key ='-LIST-',
                        enable_events = True)]]
    
    window_theme = sg.Window('Theme selector', layout, no_titlebar=False)
    
    # Event loop
    while True:  
        event, values = window_theme.read()
        
        # End program when close windows
        if event == sg.WIN_CLOSED:
            break
        
        # Update theme in current GUI
        if values != None:
            sg.theme(values['-LIST-'][0])
        
            # nUpdate theme in config file
            result = sg.popup_ok_cancel('Do you want to use this theme: {}'.format(values['-LIST-'][0]))
            if result == "OK": 
                
                config.update_credential ("theme", values['-LIST-'][0])            
                break
        
    # Close
    window_theme.close()

def data_base (): 
    """
    GUI for data base configuration
    """
    
    # Relationship between confi credentials and gui credentials
    # config : gui
    credentials = {
        "db_server"   : "input_db_server", 
        "db_name"     : "input_db_name",
        "db_user"     : "input_db_user", 
        "db_password" : "input_db_password"
    }
    
    # Get default values
    db_server   = config.get_credential("db_server")
    db_name     = config.get_credential("db_name")
    db_user     = config.get_credential("db_user")
    db_password = config.get_credential("db_password")
    
    # Set theme from gui module
    theme = config.get_credential("theme")
    sg.theme(theme)

    layout = [
        [
            sg.Text("Server", size=(12,0)), 
            sg.InputText(default_text=db_server, key="input_db_server")
        ],
        
        [
            sg.Text("Database name", size=(12,0)), 
            sg.InputText(default_text=db_name, key="input_db_name")
        ],
        
        [
            sg.Text("User", size=(12,0)), 
            sg.InputText(default_text=db_user, key="input_db_user")
        ],
        
        [
            sg.Text("Password", size=(12,0)), 
            sg.InputText(default_text=db_password, key="input_db_password", password_char="*")
        ],
        
        [
            sg.Button("Save", key="btn_save"), 
            sg.Button("Cancel", key="btn_cancel")
        ]
    ]
    
    window = sg.Window("Database settings", layout)

    # Display and interact with the window
    while True:
        
        reopen = False
    
        event, values = window.read()
                        
        # End program when close windows
        if event == sg.WIN_CLOSED or event == 'btn_cancel':
            break
    
        if event == 'btn_save':
            # Update credentials and data base manager
            config.update_credentials (values, credentials)
            
            globals.db_manager = DB_manager (
                values["input_db_server"], 
                values["input_db_name"], 
                globals.tables, 
                values["input_db_user"], 
                values["input_db_password"])
                
            break

    # End window
    window.close()
    
def show_status (pre_text="Process end."): 
    """
    Show results / status in pop window with sound
    """
    
    # Show results
    if not "Loading" in globals.status:
        playsound(sound_file)
        sg.popup_ok(f"{pre_text} \n\n{globals.status}")   
        
    time.sleep(3)
                
def loading (thread_function=None): 
    """
    Loading web scraping window
    """
    
    globals.loading = True
    
    # Run function in second thread
    thread_obj = threading.Thread(target=thread_function)
    thread_obj.start()
    
    # Update status
    local_status = "loading"
    globals.status = "Loading..."
    
    # Set theme from gui module
    theme = config.get_credential("theme")
    sg.theme(theme)
    
    layout = [
        [sg.Text(globals.status, key="status", size=(45,3))], 
        [sg.Text("(when the process finishes, you will receive an alert)", size=(45,1))], 
        [sg.Button("Stop", key="Stop")]
    ]
    
    # Create window
    window = sg.Window("Extracting articles", layout, no_titlebar=False, keep_on_top=True)
    
    reopen = False 

    while True:
                
        event, values = window.read(timeout=1)
        
        # Exit events
        if event == sg.WIN_CLOSED or event == 'Stop':
            
            menssage = "Some data has not been extracted. \nDo you want to finish the process?"
            end_program = sg.popup_ok_cancel(menssage, keep_on_top=True)
            if end_program == "OK": 
                time.sleep(2)
                globals.loading = False
        
            if event == sg.WIN_CLOSED: 
                reopen = True
            
            break
                
        if globals.loading:      
            
            # Update status
            window["status"].update(value=globals.status)
        
        else: 
            
            break
            
        
    # End window
    window.close()
    
    if reopen: 
        loading()
    
    if not "ERROR" in globals.status:
        return True 
    else: 
        return False

    