/*
    Das SQL-Skript erzeugt eine neue Beispieldatenbank.
	In dieser wird eine Tabelle mit einigen Einträgen angelegt.
 
    Einordnung:			FISI-LF5-LS3-Aufgabe-01
    Aufgabe: 			aufgabe_ls3_01.sql

    Name:				Markus Breuer
    Organisaion:		BK-GuT

    Erstellt:			14.04.2029
    Letzte Änderung:	11.05.2021

*/

DROP DATABASE IF EXISTS aufgabe_ls3_01;                       # Evtl. vorhandene Datenbank löschen

CREATE DATABASE aufgabe_ls3_01 default character set utf8;    # Neue Beispieldatenbank anlegen

USE aufgabe_ls3_01;                                           # Mit neuer Datenbank verbinden

CREATE TABLE t1_demo (                                        # Neue Tabelle in Beispieldatenbank anlegen
	t1_ID	int(11) NOT NULL AUTO_INCREMENT,
    t1_zeit	DATETIME DEFAULT NOW(),
    t1_wert	DECIMAL(9,2),
    PRIMARY KEY (t1_ID)
    );

INSERT INTO t1_demo (t1_zeit, t1_wert)                        # Einige Beispieldaten in die Tabelle eintragen
	VALUES ( '2019-03-13 12:00:00', 5.12);
INSERT INTO t1_demo (t1_zeit, t1_wert)
	VALUES ( '2019-03-13 13:00:00', 8.00);
INSERT INTO t1_demo (t1_zeit, t1_wert)
	VALUES ( '2019-03-13 14:00:00', 7.56);
INSERT INTO t1_demo (t1_zeit, t1_wert)
	VALUES ( '2019-03-13 15:00:00', 2);
INSERT INTO t1_demo (t1_zeit, t1_wert)
	VALUES ( '2019-03-13 16:00:00', 5.88);
INSERT INTO t1_demo (t1_zeit, t1_wert)
	VALUES ( '2019-03-13 17:00:00', 10.12);