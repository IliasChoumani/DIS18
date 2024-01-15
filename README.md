# DIS18

* Sollen daten zu 10 Autoren hereusarbeiten und in Wikidata findbar machen Autoren: 1. Konrad U. Förstner, 2. Anke Becker, 3. Jochen Blom, 4. Peer Bork, 5. Thomas Clavel, 6. Marius Dieckmann, 7. Alexander Goesmann, 8. Barbara Götz, 9. Thomas Gübitz, 10. Franziska Hufsky  
* Gibt es Datenschutzgrundsätze welche man beachten muss?
* Muss man die Daten in verschienen Sprachen Bereitstellen? bsp: https://www.wikidata.org/wiki/Q18744528
* Was mahcen wir bei häufigen Namen? wie stellen wir sicher das die personen unsere sind? (Anhand von Wissenschaftlichen ids?)
* was muss man zum automatisierten hochladen beachten? muss man vorher einträge bearbeiten? 

## Schritte:
1. 
1. Api der Website abrufen (mit python on einem Jupyter Notebook) brauchen request und/oder Beautiful Soup
2. Spezifizierung welche Daten abgerufen werden(welche personenbezogenen daten, wer hat bei wem promoviert, welche artikel wurden von der Person pupliziert), wie daten gespeichert werden(daten in xml beschaffen und in json umwandeln), welche formate sind mit wikidata kompatibel(am besten json)
3. Daten bereiinigen/cleanen (fehlende oder fehlerhafte daten entfernen)
4. datenabgleich unsere daten/Wikidata daten (Wikidata json export service)
5. automatisiertes hochladen der daten welche in wikidata nicht existieren (über Api zugriff) welche tool kann man dafür verwenden? (wikitools bibliothek?), muss man vorher schreibzugriff beatragen?
