import dblib
import mysql.connector

def dbZugriffswerte():
    """ Funktion, die die Zugriffsdaten für eine MySQL-Datenbank liefert """
    return "localhost", "root", "", "cpu_monitoring"


def init():
    # Verbindung zur Datenbank aufbauen
    print("Verbindung zur Datenbank aufbauen")
    print("")
    host, user, passwd, db = dbZugriffswerte()
    connection = dblib.dbVerbindungAufbauen(host, user, passwd, db)



    # Tabelleninhalt ausgeben
    print("Tabelleninhalt ausgeben:")
    print("------------------------")
    print("")
    print("Nr   \t :\t Zeitpunkt\t         :\t Wert\t:")
    print("---------------------------------------------------------")
    result = dblib.dbAbfrageAnweisung(connection, "SELECT * FROM werte")
    for zeile in result:  # Ergebnis zeilenweise durchlaufen und ausgeben
        print(str(zeile[0]) + "\t :\t " + str(zeile[1]) + "\t :\t " + str(zeile[2])+ "%" +"\t:")
    query = "SELECT AVG(t1_wert) as durchschnitt, MIN(t1_wert) as minimum, MAX(t1_wert) as maximum FROM werte" 
    result = dblib.dbAbfrageAnweisung(connection, query)
    print("")
    print("Durschnitt:\t" + str(round(result[0][0] * 100) / 100)   + "% \nMinimum:\t " + str(result[0][1]) + "% \nMaximum:\t" + str(result[0][2])+ "%") 
    print("")

init()