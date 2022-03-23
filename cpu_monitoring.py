from pickle import TRUE
from random import random

import mysql.connector
import psutil

import dblib


def dbZugriffswerte():
    """ Funktion, die die Zugriffsdaten für eine MySQL-Datenbank liefert """
    return "localhost", "root", "", "cpu_monitoring"


def init():
    # Verbindung zur Datenbank aufbauen
    print("Verbindung zur Datenbank aufbauen")
    print("")
    host, user, passwd, db = dbZugriffswerte()
    connection = dblib.dbVerbindungAufbauen(host, user, passwd, db)

    
    print("Werte in Datenbank schreiben")
    # Frage die Auslastung jede Sekunde ab und trage diese in die Datenbank ein 
    while True:
        cpu = psutil.cpu_percent(interval=1)
        print(cpu)                    
        sqlStatement = "INSERT INTO werte ( t1_wert) VALUES ( " + str(cpu) + ")"
        dblib.dbNichtAbfrageAnweisung(connection, sqlStatement)   
init()
