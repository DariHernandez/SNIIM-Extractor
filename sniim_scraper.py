import time
import datetime
import pprint
import config
import log
from scraping_manager.automate import Web_scraping

def get_data (): 
    """Return data extracted frlom page economia-sniim.gob.mx
    """

    seach_page = "http://www.economia-sniim.gob.mx/nuevo/Home.aspx?opcion=Consultas/MercadosNacionales/PreciosDeMercado/Agricolas/ConsultaFrutasYHortalizas.aspx?SubOpcion=4|0"

    scraper = Web_scraping(headless=True)
    
    log.update_status(f"Iniciando scraper")
    
    # Get products and qualities
    products_qualities_list = config.get_credential("products")
    products_list = [] 
    for item in products_qualities_list: 
        products_list.append(str(item[0]).lower().strip())        
    
    # Loop for each target market in config file
    data = {}    
    target_markets = config.get_credential("target markets")
    for market in target_markets: 
        
        log.update_status(f"Buscando datos: \n{market}")
    
        scraper.set_page(seach_page)
        scraper.refresh_selenium()

        # Get and format current date
        scraper.switch_to_frame("ifraHome")
        start_date_selector = '#txtFechaInicio'
        start_date_text = scraper.get_attrib(start_date_selector, "value")
        date_format = "%d/%m/%Y"
        start_date = datetime.datetime.strptime(start_date_text, date_format)

        # subtract one day from the date
        back_day = datetime.timedelta(days=1)
        yesterday_date = start_date - back_day
        yesterday_date_text = yesterday_date.strftime(date_format)

        # Set start date in form
        scraper.get_elem(start_date_selector).clear()
        scraper.send_data(start_date_selector, yesterday_date_text)

        # Set market
        selector_market = "#ddlDestino"
        scraper.send_data(selector_market, market)

        # Seach botton
        selector_search = "#btnBuscar"
        scraper.click_js(selector_search)

        more_pages = True
        category = ""
        data_rows = []
        while more_pages: 

            # Wait to load page
            scraper.wait_die(selector_search, time_out=60)

            log.update_status(f"Extrayendo productos: \n{market}")
        
            # Rows counter
            row_selector = "#tblResultados > tbody > tr"
            rows_num = len(scraper.get_elems(row_selector)) + 1
            
            # Loop for each row
            for row_index in range (2, rows_num): 
                
                current_row_selector = row_selector + f":nth-child({row_index})"
                
                category_selector = current_row_selector + " > td"
                class_list = scraper.get_attrib(category_selector, "class")
                if "encabACT2" in class_list: 

                    # Get category
                    category = scraper.get_text(category_selector)
            
                else: 
                
                    # Get row data
                    
                    date_selector = current_row_selector + " > td:nth-child(1)"
                    product_selector = current_row_selector + " > td:nth-child(2)"
                    quality_selector = current_row_selector + " > td:nth-child(3)"
                    presentation_selector = current_row_selector + " > td:nth-child(4)"
                    origin_selector = current_row_selector + " > td:nth-child(5)"
                    min_price_selector = current_row_selector + " > td:nth-child(6)"
                    max_price_selector = current_row_selector + " > td:nth-child(7)"
                    regular_price_selector = current_row_selector + " > td:nth-child(8)"
                    obs_selector = current_row_selector + " > td:nth-child(9)"
                    
                    date = scraper.get_text(date_selector)
                    product = scraper.get_text(product_selector)
                    quality = scraper.get_text(quality_selector)
                    presentation = scraper.get_text(presentation_selector)
                    origin = scraper.get_text(origin_selector)
                    min_price = scraper.get_text(min_price_selector)
                    max_price = scraper.get_text(max_price_selector)
                    regular_price = scraper.get_text(regular_price_selector)
                    obs = scraper.get_text(obs_selector)
                    
                    # Filter product name
                    product_formated = str(product).lower().strip()
                    quality_formated = str(quality).lower().strip()
                    
                    if product_formated in products_list: 
                        
                        # Filter category
                        index_product = products_list.index(product_formated)
                        quality_from_list = products_qualities_list[index_product][1]
                        quality_from_list = str(quality_from_list).lower().strip()
                        
                        if quality_from_list: 
                            
                            if quality_from_list != quality_formated:                             
                                continue
                            
                        # Save row                        
                        data_row = [category, date, product, quality, presentation, 
                               origin, min_price, max_price, regular_price, obs]
                        data_rows.append(data_row)
                        
                    else:                         
                        continue
                                    
            
            # Get paginator
            selector_label_pagination = "#lblPaginacion"
            label_pagination = scraper.get_text(selector_label_pagination)
            pages = label_pagination.replace ("Página", "").replace ("de ", "").strip()
            current_page, last_page = pages.split()
            
            
            if current_page < last_page: 
                # Go to next page
                selector_next_page = 'input[name="ibtnSiguiente"]'
                scraper.click_js(selector_next_page)
                more_pages = True
            else: 
                # End loop
                more_pages = False
                
        
          
        data[market] = data_rows
        
    return data      
