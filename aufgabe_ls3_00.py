"""Aufgabe_ls3_00 - Ausgangsprogramm

    Ein Beispielprogramm, welches das Zusammenspiel von Python mit
    MySQL demonstriert.

    Ausgangsprogramm

    Einordnung:			FISI-LF5-LS3-Aufgabe-ls3-00
    Aufgabe: 			aufgabe_ls3_00

    Name:			    Markus Breuer
    Organisaion:		BK-GuT

    Erstellt:			14.04.2020
    Letzte Änderung:    26.01.2021
    """
import dblib
import mysql.connector
from random import random


### lokale Funktionen für die Datenbanknutzung ###########################################################





def dbZugriffswerte():
    """ Funktion, die die Zugriffsdaten für eine MySQL-Datenbank liefert """
    return "localhost", "root", "", "aufgabe_ls3_01"


### Hauptprogramm ###################################################################################
def init():
    # Verbindung zur Datenbank aufbauen
    print("Verbindung zur Datenbank aufbauen")
    print("")
    host, user, passwd, db = dbZugriffswerte()
    connection = dblib.dbVerbindungAufbauen(host, user, passwd, db)

    # 50 Werte in Datenbank schreiben
    print("50 Werte in Datenbank schreiben")
    i = 1
    while i <= 50:
        wert = random() * 100
        wert = round(wert, 2)
        sqlStatement = "INSERT INTO t1_demo ( t1_wert) VALUES ( " + str(wert) + ")"
        dblib.dbNichtAbfrageAnweisung(connection, sqlStatement)
        i = i + 1
    print("")

    # Tabelleninhalt ausgeben
    print("Tabelleninhalt ausgeben:")
    print("------------------------")
    print("")
    print(" Nr : Zeitpunkt : Wert")
    result = dblib.dbAbfrageAnweisung(connection, "SELECT * FROM t1_demo")
    for zeile in result:  # Ergebnis zeilenweise durchlaufen und ausgeben
        print(str(zeile[0]) + " : " + str(zeile[1]) + " : " + str(zeile[2]))

    print("")

    # Verbindung zur Datenbank abbauen
    print("Verbindung zur Datenbank abbauen")
    print("")
    dblib.dbVerbindungAbbauen(connection)

init()
