#!/usr/bin/env python
# coding: utf-8

from tkinter import *
import socket
from threading import Thread

root = Tk()
root.geometry('{}x{}'.format(int(root.winfo_screenwidth() / 2), int(root.winfo_screenheight() / 2)))
root.wm_title("Python_Bahamas")

class serverSide(Thread): 
    
    def __init__(self):
        Thread.__init__(self)
        self.ip = ""
        self.port = 9998
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.start()

    def run(self): 
        server_render = LabelFrame(root, text = "Information Serveur")
        server_render.pack(fill = "both", expand = "yes")
        client_list = Label(server_render, text = "Liste des utilisateurs connectés").pack()

        self.s.bind((self.ip, self.port))
        self.s.listen(5)

        while True:
            (clientsocket, (ip, port)) = self.s.accept()
            print('1 more user')
            self.info_client_list = Label(root, text = "Un utilisateur connecté pour l'adresse ip %s et le port %s" % (ip, port)).pack()
            Thread(target = self.getMsg,args = (clientsocket, ip)).start()
  
    def getMsg(self, client, address):
        size = 1024
        while True:
            try:
                response = client.recv(1024)
                if response:
                    print(response)
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False



serverSide()            
root.mainloop()
    