import os
import log
from spreadsheet_manager.xlsx import SS_manager

def write_data (data): 
    """
    Write data scraped in spreadsheet
    """
    
    log.update_status(f"Preparando hoja de cálculo")

    # Open and clean spreadsheet file
    file = os.path.join (os.path.dirname(__file__), "resultados.xlsx")
    ss_manager = SS_manager(file) 
    ss_manager.clean_workbook()
    
    
    # Loop for each market in data
    for market, products in data.items(): 
        
        log.update_status(f"Escribiendo datos: \n{market}")
        
        # Clean market name
        sheet_name = market.replace(":", "")
                
        # Create market sheet
        ss_manager.create_get_sheet(sheet_name[0:30])
        
        # Write header
        header = [["Categoría", "Fecha", "Producto", "Calidad", "Presentación", 
                  "Origen", "Precio Mín", "Precio Max", "Precio Frec", "Obs."]]
        
        ss_manager.write_data(header, start_row=1, start_column=1)
        
        # Write products data 
        ss_manager.write_data(products, start_row=2, start_column=1)
        
        # Apply styles
        ss_manager.format_range(start_cell=(1,1), 
                                end_cell=(1,len (header[0])), 
                                bold=True , 
                                font_size=11)
        
        # Ajust columns width
        ss_manager.auto_width()
    
    ss_manager.save()

