# DIS18

* Sollen daten zu 10 Autoren hereusarbeiten und in Wikidata findbar machen Autoren: 1. Konrad U. Förstner, 2. Anke Becker, 3. Jochen Blom, 4. Peer Bork, 5. Thomas Clavel, 6. Marius Dieckmann, 7. Alexander Goesmann, 8. Barbara Götz, 9. Thomas Gübitz, 10. Franziska Hufsky  
* Gibt es Datenschutzgrundsätze welche man beachten muss?
* Muss man die Daten in verschienen Sprachen Bereitstellen? bsp: https://www.wikidata.org/wiki/Q18744528
* Was machen wir bei häufigen Namen? wie stellen wir sicher das die personen unsere sind? (Anhand von Wissenschaftlichen ids?)
* was muss man zum automatisierten hochladen beachten? muss man vorher einträge bearbeiten um zugriff bekommen?
* wie beachten wir das wikidata vokabular? labes descriptions, aliases, claims
* sollten uns für einen Datensatz entscheiden mit welchem wir ein beispiel durcharbeiten (Professor Dr. Alexander Goesmann versuchen laufende Projekte in Wikidata einzufügen https://gepris.dfg.de/gepris/person/188428736)
* wie kann man die q-id effizient suchen? mit namen auf wikidata?
*   - wie ermitteln wir die exakte person? Anke Becker

## Schritte:
1. Urls/IDS herausfinden em die Apis abzurufen   
2. Api der Website abrufen (mit python on einem Jupyter Notebook) brauchen request und/oder Beautiful Soup oder website parsen
3. Spezifizierung welche Daten abgerufen werden(welche personenbezogenen daten, wer hat bei wem promoviert, welche artikel wurden von der Person pupliziert)
4. wie werden daten gespeichert (daten in xml beschaffen und in json umwandeln), welche formate sind mit wikidata kompatibel(am besten json)
5. Daten bereiinigen/cleanen (fehlende oder fehlerhafte daten entfernen)
6. wikidata einträge der autoren automatisiert findbar machen (ids beschaffen)
7. Wikidata daten herunterladen
8. datenabgleich unsere daten/Wikidata daten (Wikidata json export service)
9. löschen von dublikaten 
10. automatisiertes hochladen der daten welche in wikidata nicht existieren (über Api zugriff) welche tool kann man dafür verwenden? (wikitools bibliothek?), muss man vorher schreibzugriff beatragen?

