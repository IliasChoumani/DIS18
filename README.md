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

____________________________________________

1. Überprüfen, ob der Forscher angelegt ist oder nicht, wenn nicht anlegen
2. Gesammelte Informationen (Gepris, Orcid etc.) in einheitliches Format bringen
   --> JSON mit allen Projekten (Projekt Name & Projekt Link) = zum Überprüfen, ob Projekt existiert und Anlegen der Projekte
   --> JSON mit allen Projekt Links und beteiligten Forschern = für die Verknüpfung zwischen Projekt und Forscher
3. Überprüfen, ob Projekt bereits auf wikidata existiert
   --> Bei Nicht-Existenz: Projekt neu anlegen
4. Projekte mit den Forschern verknüpfen


## Anmerkungen:
* haben Programm das eine Liste mit QID ermittelt, welche den Autorennamen beinhaltet.
* halb automatisiertes Programm, welches auswählt, ob es sich bei QIDs um Personen handelt.
* wenn es mehrere gleichnamige personen gibt wird per Input befehl die richtige und für und relevante ausgewählt
* diese personen werden in einem dictonary mit dem label und description gespeichert. 
* Wikidata einträge als Json export File gedownloadet

## Fragen:

* sollte man einen neuen abschnitt für projekte hinzufügen, gibt es einen p für projeknamen, oder soll man nur die gepris projekt id den jeweiligen personen zuordnen?
* Wie sehen wir, ob wir die Berechtigungen für den Bot haben? Dauert es einfach nur lange?
* Personen (Alexander Goesmann) haben über 250 Projekte - sollen alle hochgeladen werden?
* Können bspw. bei Gepris und Orcid die gleichen Projekte auftauchen?
* Welche IDs für Projekte nehmen wir (Gepris-Id und bspw.: bei Orcid DOI)


## TO Do:
* abfrage gestellten ob das projekt schon existiert (suchen nach der gepris projekt id und speichern alle artikel die wir finden) (glaube es existiert noch kein projekt)
* wenn das projekt da ist brauchen wir die qid, welche in liste gespeichert wird (glaube es existiert noch kein projekt)
* wenn die Person nicht existiert müssen wir einen wikidata eintrag für sie anlegen (glaube aber existieren alle)

* wenn nicht da ist müssen wir es anlegen (wie automatisiert?) und neue qid in liste speichern!!! (Oder das Projekt der person hinzufügen und erstmal keine eigene seite fürs projekt erstellen.) (aber denke eigene seite sinvoller, siehe gepris project id projekte, am besten auch direkt angeben welche person zum projekt gehört)
* dann haben wir eine liste mit allen projekten, deren qids in wikidata und die personen ebenfalls schon in wikidata 
* diese können wir dann der personenseite hinzufügen.

* diese projektseiten kann man dann mit den personenseiten verknüpfen und die projekte in die personenseiten intigrieren. (dann haben wir unsere ersten aktualierten wikidata personeneinträge)  
* Weiter ausbauen (promovierung weiter ausbauen

## Letztes To-Do:
Notebooks aufräumen und besser für leute von auserhalb verwendbar machen.   
Neue Daten gewinnen:  
Peer Bork Reparieren.  
mit Peer review Orcid erweitern:  
https://orcid.org/0000-0002-1481-2996

  
