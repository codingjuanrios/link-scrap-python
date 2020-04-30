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
srv = "OsoBogey.com"
browser.get("http://osobogey.com/")
page = BeautifulSoup(browser.page_source,"html.parser")
browser.close()

#--------------------------------------------------- menu = page.find_all('nav')

links_menu = []

navegar = page.find('header')

for link in navegar.find_all('a'):
    links_menu.append(link.get('href'))

print(str(links_menu))

links_menu.remove('#')


print(str(links_menu))

for link in links_menu:
    print(link)
    browser = webdriver.Firefox(options=options)
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
message["Subject"] = f"Revision de links - {srv}"
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