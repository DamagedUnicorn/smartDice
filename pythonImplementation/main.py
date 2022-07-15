#!/usr/bin/env python3# -*- coding: utf-8 -*-"""Created on Mon Jul  4 22:25:57 2022@author: thorknudsen"""""" REQUIREMENTS- python 3.6.12- numpy 1.17.0- tk 8.6.12- tkmacosx 0.1.6- requests 2.27.1- pyserial 3.5"""from character import Characterfrom serialCommunication import SerialCommunicationfrom gui import GUIcharacterId = 45441447#65349741                         #65349572#65349741#78416455port = "/dev/cu.usbmodem14301"baudRate = 9600if __name__ == "__main__":        character = Character(characterId)        serialCommunication = SerialCommunication(port, baudRate)    gui = GUI(character, serialCommunication)    while serialCommunication.isConnected:        serialCommunication.readData(gui)    gui.window.mainloop()