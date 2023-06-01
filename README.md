<div><a href='https://github.com/github.com/darideveloper/blob/master/LICENSE' target='_blank'>
            <img src='https://img.shields.io/github/license/github.com/darideveloper.svg?style=for-the-badge' alt='MIT License' height='30px'/>
        </a><a href='https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=' alt='Linkedin' height='30px'/>
            </a><a href='https://t.me/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Telegram&color=26A5E4&logo=Telegram&logoColor=FFFFFF&label=' alt='Telegram' height='30px'/>
            </a><a href='https://github.com/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=181717&logo=GitHub&logoColor=FFFFFF&label=' alt='Github' height='30px'/>
            </a><a href='https://www.fiverr.com/darideveloper?up_rollout=true' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Fiverr&color=222222&logo=Fiverr&logoColor=1DBF73&label=' alt='Fiverr' height='30px'/>
            </a><a href='https://discord.com/users/992019836811083826' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Discord&color=5865F2&logo=Discord&logoColor=FFFFFF&label=' alt='Discord' height='30px'/>
            </a><a href='mailto:darideveloper@gmail.com?subject=Hello Dari Developer' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Gmail&color=EA4335&logo=Gmail&logoColor=FFFFFF&label=' alt='Gmail' height='30px'/>
            </a></div><div align='center'><br><br><img src='https://github.com/darideveloper/SNIIM-Extractor/blob/master/logo.png?raw=true' alt='SNIIM Extractor' height='80px'/>

# SNIIM Extractor

Bot for extract data from page [www.economia-sniim.gob.mx,](http://www.economia-sniim.gob.mx/nuevo/Home.aspx?opcion=Consultas/MercadosNacionales/PreciosDeMercado/Agricolas/ConsultaFrutasYHortalizas.aspx?SubOpcion=4%7C0) with CLI and GUI

Start date: **2021-06-11**

Last update: **2023-03-28**

Project type: **client's project**

</div><br><details>
            <summary>Table of Contents</summary>
            <ol>
<li><a href='#buildwith'>Build With</a></li>
<li><a href='#media'>Media</a></li>
<li><a href='#details'>Details</a></li>
<li><a href='#install'>Install</a></li>
<li><a href='#settings'>Settings</a></li>
<li><a href='#run'>Run</a></li>
<li><a href='#roadmap'>Roadmap</a></li></ol>
        </details><br>

# Build with

<div align='center'><a href='https://www.python.org/' target='_blank'> <img src='https://cdn.svgporn.com/logos/python.svg' alt='Python' title='Python' height='50px'/> </a></div>

# Media

![gui home](https://github.com/darideveloper/SNIIM-Extractor/blob/master/imgs/home.PNG?raw=true)

![gui config](https://github.com/darideveloper/SNIIM-Extractor/blob/master/imgs/config.PNG?raw=true)

# Details

Then bot extract the products from the [page,](http://www.economia-sniim.gob.mx/nuevo/Home.aspx?opcion=Consultas/MercadosNacionales/PreciosDeMercado/Agricolas/ConsultaFrutasYHortalizas.aspx?SubOpcion=4%7C0), create a report in excel and send it by email.\r
\r
The bot have the options for run in CLI or with GUI

# Install

## Tird party modules\r
\r
Install the python modules with the commad:\r
\r
\\`\\`\\` bash\r
$ python -m pip install -r requirements.txt\r
\\`\\`\\`\r
\r
## Programs\r
\r
You shoud have follow the following programs:\r
\r
* [Google Chrome](https://www.google.com/intl/es/chrome) última versión

# Settings

## Config GUI\r
\r
The configuration screen is as follows:\r
\r
![Config screen](https://i.imgur.com/X4SN2SB.png)\r
\r
### EMAIL\r
\r
In this section, the email address from which the emails will be sent and the email address that will receive them are set.\r
\r
NOTE: The program supports emails from: gmail.com, outlook.com, hotmail.com, live.com, yahoo.com, and aol.com, but some of these email services require special configuration.\r
\r
If you want to change the email address from which emails are sent, please contact me.\r
\r
### TARGET MARKET\r
\r
List of target markets to obtain data from.\r
\r
NOTE: Each market must be written exactly as shown on the page: capitalization, quotation marks, punctuation, etc.\r
\r
### PRODUCTS\r
\r
List of products to extract, with their respective quality (optional).\r
\r
NOTE: They must be the same names shown on the page, but capitalization does not matter.\r
\r
## config.json\r
\r
All configurations are saved in the config.json file, so it can be manually edited.

# Run

## GUI\r
\r
For **run** the program with **graphic user interface**, **run** with yout **python 3.9** interpreter, the file **__ main__.py**.\r
\r
The GUI allow you to use the program and update the settings\r
\r
![Home](https://i.imgur.com/MxUmYe7.png)\r
\r
## Terminal\r
\r
For  **run** the program **in terminal** / without gui, **run** the file **sniim_run.py** with your **python 3.9** interpreter.\r
\r
Running the program in this way **will not allow updating configurations** and it will run with the **last configuration set** (more details in the configuration section).

# Roadmap

* [X] Extract info\r
* [X] Save data in excel\r
* [X] Submit email\r
* [X] CLI\r
* [X] GUI


