#!/usr/bin/env python
# coding: utf-8

from tkinter import *
import random
import socket
from threading import Thread

root = Tk()
root.geometry('{}x{}'.format(int(root.winfo_screenwidth() / 2), int(root.winfo_screenheight() / 2)))
root.wm_title("Amazing client chat")
client_render = LabelFrame(root, text = "Information Client")
client_render.pack(fill = "both", expand = "yes")

defaultChannel = "Accueil"

class clientSide(Thread) : 

    def __init__(self):
        Thread.__init__(self)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(("", 9998))
        self.username = "user" + str(random.randint(0, 123456789))
        status = Label(root, text = "Connexion au serveur réussi").pack()
        Label(root, text = "Bienvenue {0}".format(self.username)).pack() 
        self.start()

    def run(self):
        messages_var = StringVar()
        messages = Entry(client_render, textvariable=messages_var, width=30).pack()
        send_messages = Button(client_render, text = "Envoyer", command = lambda : self.get_message(messages_var.get())).pack()
        

    def get_message(self, message):
        message_box = Label(client_render, text = message)
        message_box.pack()
        msg_into_byte = bytes(message.encode('utf-8'))
        self.s.send(msg_into_byte)
        

clientSide()
root.mainloop()