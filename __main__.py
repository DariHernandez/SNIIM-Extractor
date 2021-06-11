import globals
import config
import log
import sniim_run
import PySimpleGUI as sg
from gui_manager import gui

def main (): 
    """Main function of the project with gui
    """
    
    # Get theme from config file
    theme = config.get_credential("theme")
    
    # Create json file if it doesn't exist
    if not theme: 
        
        config_data = {
            "theme": "Dark2",
            "rows": 3, 
            "db_server": "", 
            "db_name": "",
            "db_user": "", 
            "db_password": "",
        }
        
        theme = config_data["theme"]
        
        config.create_config(config_data)
                
    # Set theme
    sg.theme(theme)

    # Main screedn layout
    layout = [
        [
          sg.Button("Ejecutar", size=(33,1), key="run"),  
        ],
        [
            sg.Button("Tema", size=(8,1), key="Theme"), 
            sg.Button("Configuración", size=(12,1), key="config"),  
            sg.Button("Salir", size=(8,1), key="Quit"),
        ]
    ]
    
    # Create window
    window = sg.Window("SNIIM EXTRACTOR", layout, no_titlebar=False)
    
    while True:
        
        
        reopen = False
    
        event, values = window.read()
        
        # RUN BUTTONS                 
                   
        # End program when close windows
        if event == sg.WIN_CLOSED or event == 'Quit':
            break
            
            
        if event == "Theme": 
            
            # Select new theme
            gui.theme_selector()
            
            # Update theme in current window
            theme = config.get_credential("theme")
            sg.theme(theme)
            reopen = True
            break  
        
        if event == "run": 
            
            # Show loading status and run function in thread
            
            gui.loading(sniim_run.run)            
            gui.show_status("Programa terminado. Estatus final:")
            
        if event == "config":
            
            log.info ("Credentials and options updated")
            
            # Get credentials
            last_products = config.get_credential("products")
            last_target_markets = config.get_credential("target markets") 
            last_email = config.get_credential("email")
            last_password = config.get_credential("password")
            last_to_email = config.get_credential("to_email")
            
            # Show config gui
            config_gui(last_products, 
                       last_target_markets, 
                       last_email, 
                       last_password, 
                       last_to_email)
                    
    # End window
    window.close()
    
    # Reopen window after changes
    if reopen: 
        main()
        
def config_gui (last_products, last_target_markets, last_email, 
                last_password, last_to_email): 
    """ Update crdentials and user options
    """
    
    # Get theme from config file
    theme = config.get_credential("theme")
                
    # Set theme
    sg.theme(theme)

    # EMAIL LAYOUT
    
    email_layout = [
        [
            sg.Text ("CORREO", size=(20,1)),  
        ],
        [    
            sg.Text (""),   
        ],
        [
            sg.Text ("Email:", size=(15,1)),  
            sg.Input (size=(30,1), default_text=last_email, key="email"),  
        ],
        [
            sg.Text ("Contraseña:", size=(15,1)),  
            sg.Input (size=(30,1), default_text=last_password, key="password", password_char="*"),  
        ],
        [
            sg.Text ("Correo de destino:", size=(15,1)),  
            sg.Input (size=(30,1), default_text=last_to_email, key="to_email"),  
        ],
    ]
    
    
    # MARKET LAYOUT
    
    
    markets_list = config.get_credential ("target markets")
    rows_markets_layout = []
    
    # Title
    rows_markets_layout.append([sg.Text ("MERCADO DE DESTINO", size=(20,1))])
    rows_markets_layout.append([sg.Text ("")])
    
    # Inputs
    for index in range (0, len (markets_list)): 
        row = [sg.Input(size=(45,1), 
                        key=f"row_markets_{index}", 
                        default_text=markets_list[index], 
                        enable_events=True)]
        rows_markets_layout.append(row)
        
    # Add and remove buttons
    rows_markets_layout.append([
        sg.Button("+", size=(4,1), key=f"market_add"), 
        sg.Button("-", size=(4,1), key=f"market_remove")
        ])
    
    
    # PRODUCTS LAYOUT
    
    
    products_list = config.get_credential ("products")
    rows_products_layout = []
    
    # Titles
    rows_products_layout.append([sg.Text ("PRODUCTOS", size=(20,1))])
    rows_products_layout.append([sg.Text ("")])
    rows_products_layout.append([
        sg.Text ("Nombre", size=(22,1)), 
        sg.Text ("Calidad", size=(20,1))])
    
    # Inputs
    for index in range (0, len (products_list)): 
        row = [
            sg.Input(size=(25,1), 
                    key=f"row_products_name_{index}", 
                    default_text=products_list[index][0], 
                    enable_events=True), 
            sg.Input(size=(25,1), 
                    key=f"row_products_queality_{index}", 
                    default_text=products_list[index][1], 
                    enable_events=True)]
        rows_products_layout.append(row)
        
    # Add and remove buttons
    rows_products_layout.append([
        sg.Button("+", size=(4,1), key=f"products_add"), 
        sg.Button("-", size=(4,1), key=f"products_remove")
        ])
    
    
    # Merse email_layout and rows_markets_layout secction
    
    email_markets = []
    email_markets += email_layout
    email_markets.append ([sg.Text ("")])
    email_markets.append ([sg.Text ("")])
    email_markets += (rows_markets_layout)
    
    
    # Main screed layout
    layout = [
        [
            sg.Column(email_markets),
            sg.Column(rows_products_layout),
        ],
        [
            sg.Text (""),
        ],
        [
            sg.Button("Gudardar", size=(8,1), key="save"), 
            sg.Button("Salir", size=(8,1), key="Quit"),
        ]
    ]
        
    # Create window
    window = sg.Window("Configuración", layout, no_titlebar=False)
    
    while True:
        
        
        reopen = False
    
        event, values = window.read()
        
        # RUN BUTTONS                 
        
        # End program when close windows
        if event == sg.WIN_CLOSED or event == 'Quit':
            
            # Restart las credentials
            config.update_credential("products", last_products)
            config.update_credential("target markets", last_target_markets)
            config.update_credential("email", last_email)
            config.update_credential("password", last_password)
            config.update_credential("to_email", last_to_email)
            
            break
        
        # Update gui temporal options
        if "add" in event or "remove" in event: 
            
            # Update last products
            last_products = []
            for key, value in values.items(): 
                if str(key).startswith("row_products_name_"): 
                    
                    id_product = str(key)[str(key).rfind("_")+1:]
                    
                    product = values[f"row_products_name_{id_product}"]
                    queality = values[f"row_products_queality_{id_product}"]
                    
                    last_products.append ([product, queality])
                    
            # Update last markets
            last_target_markets = []
            for key, value in values.items(): 
                if str(key).startswith("row_markets_"): 
                    last_target_markets.append (value)
                    
            last_email = values["email"]
            last_password = values["password"]
            last_to_email = values["to_email"]
        
        if event == "products_add": 
            last_products.append([ "", ""])
            config.update_credential("products", last_products)
            reopen = True
            break
        
        if event == "products_remove": 
            last_products.pop()
            config.update_credential("products", last_products)
            reopen = True
            break
        
        if event == "market_add": 
            last_target_markets.append("")
            config.update_credential("target markets", last_target_markets)
            reopen = True
            break
        
        if event == "market_remove": 
            last_target_markets.pop()
            config.update_credential("target markets", last_target_markets)
            reopen = True
            break
        
        if event == "save": 
            
            # Update products
            products = []
            for key, value in values.items(): 
                if str(key).startswith("row_products_name_"): 
                    
                    id_product = str(key)[str(key).rfind("_")+1:]
                    
                    product = values[f"row_products_name_{id_product}"]
                    queality = values[f"row_products_queality_{id_product}"]
                    
                    if product: 
                        products.append ([product, queality])
                    
            # Update markets
            markets = []
            for key, value in values.items(): 
                if str(key).startswith("row_markets_") and value: 
                    markets.append (value)
            
            # Update credentials
            config.update_credential("products", products)
            config.update_credential("target markets", markets)
            config.update_credential("email", values["email"])
            config.update_credential("password", values["password"])
            config.update_credential("to_email", values["to_email"])
            
            break     
        
        # if str(event).startswidth ("row"): 
            
        #     if "markets" in event: 
        
        # print (event)
                    
    # End window
    window.close()
    
    # Reopen window after changes
    if reopen: 
        config_gui(last_products, 
                   last_target_markets, 
                   last_email, 
                   last_password,
                   last_to_email)

if __name__ == "__main__":
    main()