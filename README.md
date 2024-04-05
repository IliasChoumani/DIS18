# DIS18

* Sollen daten zu 10 Autoren hereusarbeiten und in Wikidata findbar machen Autoren: 1. Konrad U. Förstner, 2. Anke Becker, 3. Jochen Blom, 4. Peer Bork, 5. Thomas Clavel, 6. Marius Dieckmann, 7. Alexander Goesmann, 8. Barbara Götz, 9. Thomas Gübitz, 10. Franziska Hufsky  
* Gibt es Datenschutzgrundsätze welche man beachten muss?
* Muss man die Daten in verschienen Sprachen Bereitstellen? (er meinte auf englisch aber die projekte sind auf deutsch)bsp: https://www.wikidata.org/wiki/Q18744528
* Was machen wir bei häufigen Namen? wie stellen wir sicher das die personen unsere sind? (Anhand von Wissenschaftlichen ids?)
* was muss man zum automatisierten hochladen beachten? muss man vorher einträge bearbeiten um zugriff bekommen?
* wie beachten wir das wikidata vokabular? labes descriptions, aliases, claims
* sollten uns für einen Datensatz entscheiden mit welchem wir ein beispiel durcharbeiten (Professor Dr. Alexander Goesmann versuchen laufende Projekte in Wikidata einzufügen https://gepris.dfg.de/gepris/person/188428736)
* wie kann man die q-id effizient suchen? mit namen auf wikidata?
    - wie ermitteln wir die exakte person? Anke Becker
* wie kann man die labels-ids (P31) ermitteln?
* am Beispiel von GEPRIS project ID (P4870) = wie können wir Projekte, an denen der Forscher teilgenommen hat, in wikidata anlegen oer finden?

## Schritte:
1. Urls/IDS herausfinden em die Apis abzurufen
3. Api der Website abrufen (mit python on einem Jupyter Notebook) brauchen request und/oder Beautiful Soup oder website parsen
4. Spezifizierung welche Daten abgerufen werden(welche personenbezogenen daten, wer hat bei wem promoviert, welche artikel wurden von der Person pupliziert)
5. wie werden daten gespeichert (daten in xml beschaffen und in json umwandeln), welche formate sind mit wikidata kompatibel(am besten json)
6. Daten bereiinigen/cleanen (fehlende oder fehlerhafte daten entfernen)
7. wikidata einträge der autoren automatisiert findbar machen (ids beschaffen)
8. Wikidata daten herunterladen
9. datenabgleich unsere daten/Wikidata daten (Wikidata json export service)
10. löschen von dublikaten 
11. automatisiertes hochladen der daten welche in wikidata nicht existieren (über Api zugriff) welche tool kann man dafür verwenden? (wikitools bibliothek?), muss man vorher schreibzugriff beatragen?

Infos aus dem Meeting:
https://www.wikidata.org/wiki/Q98380344
https://www.wikidata.org/wiki/Property:P4870
