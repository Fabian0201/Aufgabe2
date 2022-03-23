import mysql.connector


def dbVerbindungAufbauen(host, user, passwd, db):
    """ Funktion zum Verbindungsaufbau mit einer MySQL-Datenbank """
    verbindung = mysql.connector.connect(
        host=host, port=3306, user=user, passwd=passwd, db=db
    )
    return verbindung


def dbVerbindungAbbauen(verbindung):
    """ Funktion zum Verbindungsabbau bei einer MySQL-Datenbank """
    verbindung.close()


def dbNichtAbfrageAnweisung(verbindung, anweisung):
    """ Funktion zur Ausführung einer Nicht-Abfrage-Anweisung bei MySQL-Datenbank """
    cursor = verbindung.cursor()  # Cursor öffnen
    cursor.execute(anweisung)  # Anweisung ausführen
    verbindung.commit()  # Bestättigen
    cursor.close()  # Cursor schliessen


def dbAbfrageAnweisung(verbindung, anweisung):
    """ Funktion zur Ausführung einer Nicht-Abfrage-Anweisung bei MySQL-Datenbank """
    cursor = verbindung.cursor()  # Cursor öffnen
    cursor.execute(anweisung)  # Anweisung ausführen
    ergebnisMenge = cursor.fetchall()  # Ergebnismenge abholen
    cursor.close()  # Cursor schliessen
    return ergebnisMenge