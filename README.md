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
* wie kann man die labels-ids (P31) ermitteln? = Q5 (Personen) p106 (Occupation)
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

## Anmerkungen:
* haben Programm das eine Liste mit QID ermittelt, welche den Autorennamen beinhaltet.
* halb automatisiertes Programm, welches auswählt, ob es sich bei QIDs um Personen handelt.
* wenn es mehrere gleichnamige personen gibt wird per Input befehl die richtige und für und relevante ausgewählt
* diese personen werden in einem dictonary mit dem label und description gespeichert. 
* Wikidata einträge als Json export File gedownloadet

## Fragen: 
* ist es sinvoll die json dateien von wikidata mit unseren projekten zu aktuallisieren?(kann man diese dann hochladen und die wikidata website so ändern?) denke es ist sinvoller unsere json dateien direkt in wikidata hochzuladen.  
* wikitools?
* ist der Wikidata JSON Export Service sinvoll? denek nicht, da wir die wikidata seiten nicht zwanghaft als json benötigen um neue daten hochzuladen. 
* wie legen wir die projekte am besten an (gepris projekt id P4870)
* solltle man für jedes projekt eine entität anlegen? wenn ja wie?

## TO Do:
* abfrage gestellten ob das projekt schon existiert (suchen nach der gepris projekt id und speichern alle artikel die wir finden) (glaube es existiert noch kein projekt)
* wenn das projekt da ist brauchen wir die qid, welche in liste gespeichert wird (glaube es existiert noch kein projekt)
    
* wenn nicht da ist müssen wir es anlegen (wie automatisiert?) und neue qid in liste speichern!!! Oder das Projekt der person hinzufügen und erstmal keine eigene seite fürs projekt erstellen. (aber denke eigene seite sinvoller, siehe gepris project id projekte)
* dann haben wir eine liste mit allen projekten und deren qids in wikidata  
* diese können wir dann der person hinzufügen.
  
### Bis zum gespräch
*wie sehe ich ob der bot genemigt wurde?
*sollte ich die projekte als eigenständige seiten erstellen oder nur dem autor hinzufügen. (denke erstmal eigene seiten der Projekte erstellen)
*diese projektseiten kann man dann mit den personenseiten verknüpfen und die projekte in die personenseiten intigrieren. (dann haben wir unsere ersten aktualierten wikidata personeneinträge)
*Weiter ausbauen (promovierung weiter ausbauen)

  
