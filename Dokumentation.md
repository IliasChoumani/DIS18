# Daten zu Forscher:innen, ihren Themen und Projekten in einen Knowledge Graph überführen (in Wikidata)

## Übersicht
Dieses Projekt bietet eine Sammlung von Python-Tools zur Verarbeitung und Analyse von Daten aus Wikidata und Gepris-Projekten. Die Notebooks in diesem Projekt enthalten Skripte zum Ermitteln von Autoren-IDs, Herunterladen von JSON-Daten von Websites, Konvertieren von JSON-Daten in CSV und Überprüfen der Existenz von Projekten in Wikidata.

## Ziele
1. Automatisiertes Ermitteln von Autoren-IDs in Wikidata: Identifikation und Extraktion von Autoren-IDs für wissenschaftliche Arbeiten.  
2. Herunterladen von JSON-Daten von Websites: Automatisches Herunterladen und Speichern von JSON-Daten für die spätere Verarbeitung.  
3. Konvertieren von JSON-Daten in CSV: Umwandlung von JSON-Datenformaten in CSV zur weiteren Analyse und Verwendung.  
4. Überprüfen der Existenz von Projekten in Wikidata: Validierung und Abgleich von Projektdaten zwischen Gepris und Wikidata.

## Vorgehensweise
####  Ermitteln von Autoren-IDs in Wikidata
Notebook: Wikidata_QID_Autor_Ermitteln.ipynb    
Beschreibung: Dieses Notebook enthält Skripte zur Abfrage von Wikidata, um die QIDs (Wikidata IDs) von Autoren wissenschaftlicher Arbeiten zu ermitteln
#### Vorgehensweise
Verbindung zur Wikidata-API herstellen.  
Abfrage nach Autoreninformationen durchführen.  
QIDs der Autoren extrahieren und speichern.  
\n
\n
#### Herunterladen von JSON-Daten
Notebook: Wikidata_Json_Website_Download_erstmal_unrelevant.ipynb  
Beschreibung: Dieses Notebook bietet Funktionen zum Herunterladen von JSON-Daten von verschiedenen Websites.  
#### Vorgehensweise
Ziel-URLs definieren.  
HTTP-Anfragen senden und JSON-Daten empfangen.  
Heruntergeladene JSON-Daten speichern.  

#### Konvertieren von JSON-Daten in CSV
Notebook: json_in_csv_Gepris_Projekte.ipynb  
Beschreibung: Dieses Notebook enthält Skripte zur Konvertierung von JSON-Datenformaten in CSV.  
#### Vorgehensweise
JSON-Daten laden.  
JSON-Daten parsen und in tabellarisches Format umwandeln.  
Daten als CSV-Datei speichern.  

#### Überprüfen der Existenz von Projekten in Wikidata
Notebook: GuckenObProjekteInWikidataExistieren.ipynb  
Beschreibung: Dieses Notebook enthält Skripte zur Überprüfung, ob bestimmte Projekte in Wikidata existieren.  
#### Vorgehensweise
Projektinformationen von Gepris laden.  
Abgleich der Projekte mit Wikidata-Daten.  
Ergebnisse der Überprüfung speichern und ausgeben.  

#### Extrahieren von Namen und Links von Projekten
Notebook: Get_Names_Projekts_Links_Gepris.ipynb  
Beschreibung: Dieses Notebook extrahiert Namen und Links von Projekten aus Gepris und bereitet sie für die weitere Verwendung vor.  
#### Vorgehensweise
Projektlisten von Gepris laden.  
Projektnamen und Links extrahieren.  
Ergebnisse speichern und ausgeben.  


#### Instilationsanleitung
Um Projekttools zu verwenden müssen vorab die richtigen Bibliotheken installiert sein. Dies kann durch Ausführen des folgenden Befehls in deinem Terminal erfolgen:   
pip install -r requirements.txt  

#### Verwendungsanleitung
Klone das Repository auf deinen lokalen Computer.  
Installiere die Abhängigkeiten mit dem oben genannten Befehl.  
Öffne die Notebooks mit Jupyter Notebook oder Jupyter Lab.  
Führe die Notebooks aus, um die jeweiligen Aufgaben zu erledigen.  

