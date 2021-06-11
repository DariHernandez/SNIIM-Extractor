import sniim_email
import sniim_scraper
import sniim_spreadsheet
import globals

def run (): 
    """ Merge and run all main scripts of the project
    """

    # Run scraper for get data
    if globals.loading:
        data = sniim_scraper.get_data()

    # Write data generated in xlsx sheet
    if globals.loading:
        sniim_spreadsheet.write_data(data)

    # Send file in email
    if globals.loading:
        sniim_email.send_file()
    
    # End loading screen
    globals.loading = False