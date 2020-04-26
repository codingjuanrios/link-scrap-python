#PARA REVISAR LOS LINKS DE LAS PAGINAS

from bs4 import BeautifulSoup

from selenium import webdriver
#-------------------------------------------------------- from time import sleep

import csv, smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


#DATOS DEL EMAIL
sender_email = "pythonmorgan@gmail.com"
receiver_email = "jriotri@gmail.com"

#PARA MARCOS mortilotti@gmail.com
password = input("Type your password and press enter: ")

print("Iniciando scrapeo")

#PARA HACER HEADLESS EL NAVEGADOR
from selenium.webdriver.firefox.options import Options
options = Options()
options.headless = True

file = open("./resultado.txt", "w", encoding="utf-8")
file.write("<html><body><h1>Repaso de hosting</h1><p>He sido generado con python</p>")

#PARA HACER VISIBLE EL NAVEGADOR
#------------------------------------------------- browser = webdriver.Firefox()
#PARA HACER INVISIBLE EL NAVEGADOR
browser = webdriver.Firefox(options=options)

##REPASAR PARA ANALIZAR LA PAGINA - EMPEZAMOS CON SOFIA CORTES
srv = "Sofia Cortes en cliente.morganmedia.es"
browser.get("http://cliente.morganmedia.es/sofiacortes/")
page = BeautifulSoup(browser.page_source,"html.parser")
browser.close()

#--------------------------------------------------- menu = page.find_all('nav')

links_menu = []

navegar = page.find('nav')

for link in navegar.find('a'):
    links_menu.append(link.get('href'))

print(str(links_menu))

for link in links_menu:
    if link == '#':
        continue
    else:
        browser.get(link)
        page = BeautifulSoup(browser.page_source,'html.parser')
        browser.close()
        
            #desde aqui
        links = []
        
        for link in page.find_all('a'):
            links.append(link.get('href'))
        
        
        
        print(f'{srv} - link: {links}')
        
        file.write('<h3>')
        file.write(str(srv))
        file.write('</h3>')
        
        if links:
            for link in links:
                file.write("<h3>")
                file.write("Encontrado: ")
                file.write(str(link))
                file.write("</h3>")
        else:
            file.write("<h3>")
            file.write(str(srv))
            file.write(": Sin links")
            file.write("</h3>")
        
        print('links extraidos')
        
        
    
    
    #hasta aqui

file.write("</html></body>")
file.close

file = open("./resultado.txt", "r", encoding="utf-8")
resultado = file.read()
file.close

print('terminado')

print("Mandando email...")

message = MIMEMultipart("alternative")
message["Subject"] = "Revision de links"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Repaso de links

No contestes a este email: es automatico"""
html = str(resultado)

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    with open("contactos.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email in reader:
            server.sendmail(
                sender_email,
                email,
                message.as_string(),
            )
    
    
    #---------------------------------------------------------- server.sendmail(
        #--------------------- sender_email, receiver_email, message.as_string() otra opcion: message.format(name=name),
        #--------------------------------------------------------------------- )

quit()





#------------------------ #PARA VIGILAR LAS IP DE LOS SERVIDORES DE MORGAN MEDIA
#------------------------------------------------------------------------------ 
# #------------------------------------------------- from bs4 import BeautifulSoup
# #------------------------------------------------ from selenium import webdriver
# #-------------------------------------------------------- from time import sleep
#------------------------------------------------------------------------------ 
#----------------------------------------------------------- import smtplib, ssl
#------------------------------------------ from email.mime.text import MIMEText
#-------------------------------- from email.mime.multipart import MIMEMultipart
#------------------------------------------------------------------------------ 
#-------------------------------------------------------------- #DATOS DEL EMAIL
#--------------------------------------- sender_email = "pythonmorgan@gmail.com"
#------------------------------------------ receiver_email = "jriotri@gmail.com"
#------------------------------------------------------------------------------ 
#--------------------------------------------- #PARA MARCOS mortilotti@gmail.com
#---------------------- password = input("Type your password and press enter: ")
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#-------------------------------------- #LISTA DE LOS CINCO SERVIDORES DE MORGAN
# lista_servers = ["185.34.192.190", "134.0.9.43", "185.34.194.93", "134.0.8.167", "185.34.194.74"]
#----------------------------- srv01, srv02, srv03, srv04, srv05 = lista_servers
#------------------------------------------------------------------------------ 
# #--------------------------------------------------------- #PARA PRUEBAS RAPIDAS
# #-------------------------------------------- lista_servers = ["185.34.192.190"]
# #--------------------------------------------------------- srv01 = lista_servers
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
# #----------------------------------------------- POR SI HAY UN ELEMENTO DROPDOWN
# #------------------- dropdown = Select(browser.find_element_by_id('btnAction3'))
# #------------------------------------- dropdown.select_by_visible_text('Banana')
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------- #PARA COMPROBAR CADA ELEMENTO DE LA LISTA
#----------------------------------------------------- for srv in lista_servers:
    #------------------------------------------ #PARA HACER VISIBLE EL NAVEGADOR
    # #--------------------------------------------- browser = webdriver.Firefox()
    #---------------------------------------- #PARA HACER INVISIBLE EL NAVEGADOR
    #------------------------------ browser = webdriver.Firefox(options=options)
#------------------------------------------------------------------------------ 
    #---------------------- browser.get("https://www.blacklistmaster.com/check")
    #-------------------------- search_form = browser.find_element_by_name('ip')
    #------------------------------------------------ search_form.send_keys(srv)
    #---------------------------- boton = browser.find_element_by_name('Submit')
    #------------------------------------------------------------- boton.click()
#------------------------------------------------------------------------------ 
    # # HACER LA ESPERA DE 15 SEGUNDOS FUNCIONA PARA ESTA WEB https://www.blacklistmaster.com/check
    #----------------------------------------------------------------- sleep(15)
#------------------------------------------------------------------------------ 
    #------------------- page = BeautifulSoup(browser.page_source,"html.parser")
    #----------------------------------------------------------- browser.close()
#------------------------------------------------------------------------------ 
    # #------------------------------ AQUI LOCALIZAMOS LA TABLA COMPLETA DE RESULTADOS
#------------------------------------------------------------------------------ 
    #----------------------------------------- links = page.select('.myip800 a')
    #------------------------------------------- print(f'{srv} - link: {links}')
#------------------------------------------------------------------------------ 
    #----------------------------------------------------------------- if links:
        #---------------------------------------------------- for link in links:
            #------------------------------------------------ file.write("<h3>")
            #---------------------------------------------- file.write(str(srv))
            #------------------------------------ file.write(": encontrado en ")
            #--------------------------------------------- file.write(str(link))
            #----------------------------------------------- file.write("</h3>")
    #--------------------------------------------------------------------- else:
        #---------------------------------------------------- file.write("<h3>")
        #-------------------------------------------------- file.write(str(srv))
        #------------------------------------------------ file.write(": Limpio")
        #--------------------------------------------------- file.write("</h3>")
#------------------------------------------------------------------------------ 
    # #-------------------------------------------------------- for link in links:
        # #---------------------------------------------------- file.write("<h3>")
        # #-------------------------------------------------- file.write(str(srv))
        # #---------------------------------------- file.write(": encontrado en ")
        # #------------------------------------------------- file.write(str(link))
        # #--------------------------------------------------- file.write("</h3>")
# #------------------------------------------------------------------------------
        # #---------------------------------------------------------- if not link:
            # #------------------------------------------------ file.write("<h3>")
            # #---------------------------------------------- file.write(str(srv))
            # #-------------------------------------------- file.write(": Limpio")
            # #----------------------------------------------- file.write("</h3>")
#------------------------------------------------------------------------------ 
    #------------------------------------------------- print(f"{srv} terminado")
#------------------------------------------------------------------------------ 
#-------------------------------------------------- file.write("</html></body>")
#-------------------------------------------------------------------- file.close
#------------------------------------------------------------------------------ 
#---------------------------- file = open("./codigo.txt", "r", encoding="utf-8")
#------------------------------------------------------- resultado = file.read()
#-------------------------------------------------------------------- file.close
#------------------------------------------------------------------------------ 
#---------------------------------------------------- print("Mandando email...")
#------------------------------------------------------------------------------ 
#---------------------------------------- message = MIMEMultipart("alternative")
#----------------------------------------- message["Subject"] = "Revision de IP"
#------------------------------------------------ message["From"] = sender_email
#------------------------------------------------ message["To"] = receiver_email
#------------------------------------------------------------------------------ 
#---------------------- # Create the plain-text and HTML version of your message
#------------------------------------------------------------------- text = """\
#------------------------------------------------------------------ Hola, Marcos
# Menuda sorpresa cuando veas este email y sepas que lo he realizado usando python
#--------------------------------------------------------------- Vamooossss!!!!!
#------------------------------------------------------------------------------ 
#------------------------------ No contestes a este email: es solo una prueba"""
#--------------------------------------------------------- html = str(resultado)
#------------------------------------------------------------------------------ 
#--------------------------------- # Turn these into plain/html MIMEText objects
#----------------------------------------------- part1 = MIMEText(text, "plain")
#------------------------------------------------ part2 = MIMEText(html, "html")
#------------------------------------------------------------------------------ 
#-------------------------- # Add HTML/plain-text parts to MIMEMultipart message
#--------------------- # The email client will try to render the last part first
#--------------------------------------------------------- message.attach(part1)
#--------------------------------------------------------- message.attach(part2)
#------------------------------------------------------------------------------ 
#------------------------- # Create secure connection with server and send email
#---------------------------------------- context = ssl.create_default_context()
#------ with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    #-------------------------------------- server.login(sender_email, password)
    #---------------------------------------------------------- server.sendmail(
        #--------------------- sender_email, receiver_email, message.as_string()
    #------------------------------------------------------------------------- )
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#----------------------------------------------------------- print('terminado ')
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------ quit()