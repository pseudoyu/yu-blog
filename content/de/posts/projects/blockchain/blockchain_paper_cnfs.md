---
title: "Blockchain-Netzwerkspeicherung und Optimierung basierend auf CNFS"
date: 2021-08-20T09:30:25+08:00
draft: false
tags: ["blockchain", "ipfs", "cnfs", "storage"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

# Forschung zur Cloud-Computing-Verarbeitung und Optimierung verteilter Computer

## Vorwort

Nach einem Jahr blockchain-bezogener Studien an der HKU entwickelte ich ein Interesse am Bereich der verteilten Speicherung. Mein Abschlussprojekt stand ebenfalls in Verbindung mit IPFS, wie in "[Uright - Blockchain Music Copyright Management ÐApp](https://www.pseudoyu.com/de/2021/05/10/uright_case_study/)" detailliert beschrieben. Nach meiner Rückkehr aufs Festland hatte ich die Gelegenheit, mit Dr. Sun Ye vom CNFS Protocol Lab zusammenzuarbeiten, um dieses Paper "Forschung zur Cloud-Computing-Verarbeitung und Optimierung verteilter Computer (Blockchain-Netzwerkspeicherung und Optimierung basierend auf CNFS)" zu verfassen, was mein Verständnis von verteilter Netzwerkspeicherung und -berechnung vertiefte. Ich dokumentiere diese Erfahrung hier.

Dieses Paper wurde in die ICCEA (2021 International Conference on Electronic, Electrical and Computer) aufgenommen.

## Zusammenfassung

Mit der rasanten Entwicklung des Netzwerkverkehrs werden durch Videos, Bilder und Informationen große Datenmengen erzeugt, was Probleme bei der Berechnung und Speicherung von Computern verursacht. Angesichts der steigenden Nachfrage nach Computerverarbeitungskapazität kann die herkömmliche Computermethode die gesellschaftlichen Bedürfnisse nicht mehr erfüllen und entwickelt sich allmählich in Richtung Cloud Computing (im Folgenden als CDC bezeichnet) und verteiltes Computing. Durch verteiltes Computing kann der Computer eine große Aufgabe in viele kleine Aufgaben zerlegen, die auf verschiedene Rechenressourcen verteilt werden können. Daher ist verteiltes Computing zur Hauptmethode der CDC-Verarbeitung geworden, die den bestehenden Markt bedienen kann. Gleichzeitig ist CNFS die Abkürzung für Computer Network File System, ein globales, Peer-to-Peer verteiltes Dateisystem. Durch CNFS können wir alle Rechengeräte mit demselben Dateisystem verbinden, was als Informationsverarbeitungssystem bezeichnet werden kann. Zunächst analysiert diese Arbeit die verwandten Konzepte. Dann untersucht sie die Architektur von CDC. Abschließend werden einige Vorschläge unterbreitet.

## 1. Einleitung

Mit der Entwicklung der IT sind Computerinformationen zu einem unverzichtbaren Teil des menschlichen Lebens geworden, was uns dazu zwingt, die Informationsverarbeitungsfähigkeit kontinuierlich zu verbessern [1]. Daher ist verteiltes Computing zur Hauptmethode geworden, die eine effizientere Berechnung und Verarbeitung ermöglicht [2]. CNFS (Computer Network File System) ist ein Peer-to-Peer verteiltes Dateisystem, das darauf abzielt, das herkömmliche HTTP-System zu ersetzen [3]. Deshalb hat CNFS viele Lehren aus den erfolgreichen Systemen der Vergangenheit gezogen und ist zum Eckpfeiler von CDC und Cloud-Speicherung geworden. Gleichzeitig wird CNFS zum Grundstein der Blockchain werden. Die Schlüsseltechnologie von CDC ist die Dezentralisierung. CNFS ist jedoch eine perfekte Lösung, die eine bedeutende Rolle spielen kann [4-6]. Die dezentrale Technologie von CNFS wurde in vielen Bereichen angewendet und kann viele Probleme bestehender Plattformen lösen [7].

## 2. Verwandte Konzepte

### 2.1 Verteiltes Computing

Verteiltes Computing bedeutet, eine große Aufgabe in viele kleine Aufgaben zu unterteilen, die auf verschiedene Rechenressourcen verteilt werden können. Ein verteiltes System ist eine Sammlung unabhängiger Computer. Daher ist das verteilte Computersystem wie ein Computer, der das Gleichgewicht zwischen Kosten, Effizienz und Skalierbarkeit effektiv lösen kann. Seit den 1980er Jahren ist der verteilte Computer in den Fokus der Forschung gerückt und umfasst verschiedene Systeme wie Middleware, SOA, Grid Computing, Webservices, Hadoop-Plattform und so weiter [8]. Vor dem Aufkommen von CDC war Grid Computing der typischste Vertreter des verteilten Computing. Indem es die über das Internet verstreuten Hardware-, Software- und Informationsressourcen zu einem riesigen Ganzen verbindet, kann Grid Computing es den Menschen ermöglichen, die geografisch verteilten Ressourcen zu nutzen, um eine Vielzahl von großen, komplexen Berechnungs- und Datenverarbeitungsaufgaben zu erledigen. Grid Computing ist eine internetweite verteilte Berechnungsmethode, die hauptsächlich die verteilten Rechenressourcen im Internet nutzt. Grid Computing kommt CDC am nächsten und kann eine zentralisierte parallele Verarbeitung großer Rechenaufgaben erreichen. Die Entwicklung der Grid-Computing-Technologie trägt jedoch viel dazu bei und ist zur technischen Grundlage der CDC-Entwicklung geworden [9]. Verteiltes Computing ist eine der wichtigsten unterstützenden Technologien von CDC. Am Beispiel von Google CDC umfassen verteilte Computing-Fälle hauptsächlich das verteilte Datenspeichersystem GFS, das verteilte Datenmanagementsystem Big Table, die Open-Source-Hadoop-Plattform usw. Im Bereich PAAS und SAAS von CDC wird verteiltes Computing eine wichtige Technologie sein. Mit der Methode des verteilten Computing können wir die Bindungsbeziehung zwischen Benutzern und großen Anwendungssystemen lösen. Insgesamt züchtet verteiltes Computing CDC. In der CDC-Umgebung gestaltet verteiltes Computing die Anwendungsform und Serviceform von CDC neu und bietet eine einfache und praktikable Berechnungsmethode für Big-Data-Anwendungen [10].

### 2.2 Vorteile von CNFS

CNFS bietet eine neue verteilte Internet-Infrastruktur. Auf dieser Infrastruktur können wir viele verschiedene Arten von Anwendungen aufbauen. Daher ist CNFS ein globales, montierbares und versioniertes Dateisystem mit vielen Vorteilen [11]. Erstens ist die Dezentralisierung schneller. Alle Daten in CNFS werden auf dem eigenen Computer des Benutzers gespeichert, was dem Verteilen des zentralen Servers von HTTP auf jeden Benutzer entspricht. Wenn andere Benutzer die Daten erhalten möchten, können sie sie vom nächstgelegenen Computer des Benutzers extrahieren. Zweitens verringert sich die Abhängigkeit vom Backbone. Die Übertragungsmittel von CNFS unterscheiden sich deutlich von denen von HTTP. HTTP hängt hauptsächlich vom Backbone-Netzwerk ab [12-14]. CNFS wird hauptsächlich über Knoten übertragen, die von einem Knoten zum anderen übertragen werden können. Daher kann CNFS sofort zu einem anderen Knoten wechseln, selbst wenn ein Knoten ausfällt. Drittens permanente Datenspeicherung. Der Speichermodus von CNFS ist sehr speziell, es handelt sich um einen fragmentierten Speichermodus. CNFS-Daten können in viele Teile unterteilt werden, was dazu führt, dass Menschen keine vollständigen Daten erhalten können. Daher können Daten sicher und dauerhaft gespeichert werden [15].

## 3. CDC-Verarbeitung

### 3.1 K-Nächste-Nachbarn-Methode

K-Nächste-Nachbarn (KNN) ist ein typischer Ranking-Klassifizierungsalgorithmus. Nach einer Beurteilung kann der Sortieralgorithmus Dokumente ausgeben, die zu mehreren Kategorien gehören. Durch KNN können wir die Ähnlichkeit jedes Textes im Trainingsstichprobensatz berechnen, um die k ähnlichsten Trainingstexte zu finden. Gleichzeitig können wir einen Schwellenwert auswählen, der nach dem Score sortiert werden kann. Die Ähnlichkeit zwischen den k nächsten Nachbarn der Trainingsstichprobe und der Teststichprobe wird in Formel 1 gezeigt. K Nachbarn berechnen das Gewicht jeder Klasse, wie in Formel 2 gezeigt.

![cnfs_knn_formula](https://image.pseudoyu.com/images/cnfs_knn_formula.png)

### 3.2 CDC-Architektur

CDC kann elastische Ressourcen auf Abruf bereitstellen, was eine Sammlung von Diensten ist. Die Architektur von CDC kann in drei Ebenen unterteilt werden: Kerndienst, Dienstverwaltung und Benutzerzugriffsschnittstelle, wie in Abbildung 1 gezeigt.

![cnfs_cdc_architecture](https://image.pseudoyu.com/images/cnfs_cdc_architecture.png)

### 3.3 Dateispeicherüberprüfungsschema

Das Dateispeicherüberprüfungsschema ist die Grundlage für Dienstanbieter, um die Integrität ihrer gespeicherten Daten gegenüber Dienstverbrauchern nachzuweisen. Nach jedem Service werden die Serviceinformationen in die Blockchain geschrieben. Daher ist CDC zu einem wichtigen Berechnungs- und Speichermodus der Blockchain geworden. Die Dateispeichermethode ist in Abbildung 2 dargestellt.

![cnfs_block_structure](https://image.pseudoyu.com/images/cnfs_block_structure.png)

## 4. Wichtige Technologien von CDC

### 4.1 Standortbasierter Dienst auf Basis mobiler Cloud

Als unverzichtbare unterstützende Technologie des mobilen CDC können standortbasierte Dienste eine Vielzahl von standortbasierten Diensten rund um die Architektur standortbasierter Dienste bereitstellen, wie z.B. Mainstream-Lokalisierungstechnologie, Standortindex, Abfrageverarbeitung und so weiter. Standortdienste, die auf traditionellen Positionierungstechnologien wie GPS basieren, decken einen großen Bereich ab und wurden in vielen Bereichen wie Militär, Transport usw. weit verbreitet eingesetzt. GPS hat jedoch viele Probleme, wie schwache Durchdringung, hoher Positionierungsenergieverbrauch usw., die die Anforderungen neuer mobiler Anwendungen wie genaue Innenpositionierung und Benutzerbewegungserkennung nicht vollständig erfüllen können. Durch CDC können wir Standortdienste mobiler Cloud abschließen, wie z.B. automatischen Einkaufsführerservice, Patientenüberwachung im Smart Home usw. Das mobile CDC-Modell wurde verwendet, um neue Standortdienste aufzubauen, die lösen und eine wichtige unterstützende Technologie bilden können.

### 4.2 Energiespartechnologie für mobile Endgeräte

Die Batteriekapazität mobiler Endgeräte wächst langsam, und der Widerspruch zwischen den schnellen und reichhaltigen mobilen Anwendungen und der begrenzten Leistung mobiler Endgeräte wird immer deutlicher. Durch CDC können wir in vielen Aspekten Energie sparen, wie z.B. Energieeinsparung bei der Datenübertragung. Der Anteil des Energieverbrauchs für die drahtlose Datenübertragung am Energieverbrauch mobiler Endgeräte nimmt ebenfalls zu. Durch die Übertragung von Daten über das Mobilfunknetz können wir normalerweise das RRC-Protokoll für die Messung des Energieverbrauchs mobiler Endgeräte während des gesamten Prozesses verwenden. Die Ergebnisse zeigen, dass es im Prozess der Datenübertragung zu viel Schwanzenergieverbrauch gibt, was die Energieausnutzung mobiler Endgeräte reduziert. Durch Ändern der Zeitschwelle des Schwanzenergieverbrauchs können wir die Anzahl und Zeit des Springens in den Zustand des Schwanzenergieverbrauchs reduzieren. Durch Übertragungsplanung können wir den Schwanzenergieverbrauch reduzieren. Durch den virtuellen Endmechanismus und den Doppelwarteschlangen-Planungsalgorithmus können wir die Vorabruf-Daten und die verzögerte Übertragung planen, was die Zeitschwelle anpassen kann.

### 4.3 Datensicherheit und Datenschutz

Während mobile Benutzer reiche Dienste von CDC erhalten, werden sie mit mehr Sicherheitsbedrohungen wie Datenschutzverletzungen konfrontiert. Dies erfordert, dass wir die Datensicherheit und den Datenschutz von CDC verstärken. In der mobilen CDC-Umgebung migrieren die Daten und Rechenaufgaben der Benutzer über das drahtlose Netzwerk, was Online-Abfragen, Datenaustausch zwischen mehreren Benutzern usw. ermöglicht und unterstützt. Angesichts der begrenzten Rechenressourcen und Mobilität mobiler Endgeräte kann die Cloud-Authentifizierungsplattform die Verschlechterung der Serviceleistung vermeiden, die durch parallelen Zugriff mehrerer Benutzer verursacht wird. Durch eine Reihe neuer kryptografischer Mechanismen können wir zwischen Verschlüsselung und attributbasierter Verschlüsselung wählen. Durch die Einführung einer Zugriffsstruktur zur Verknüpfung von Chiffretext oder Benutzer-Privatschlüssel mit Attributen können wir Zugriffsrichtlinien flexibel darstellen, was eine feingranulare Zugriffsberechtigung für Daten bietet.

## 5. Schlussfolgerung

Gegenwärtig ist CDC zu einer wichtigen Methode der Datenverarbeitung und -speicherung geworden, die Dezentralisierung und andere Maßnahmen optimieren kann. CNFS ist eine neue Anwendung basierend auf HTTP, die ein Versuch neuer Technologie ist. Daher wird verteiltes Computing in Zukunft zur Hauptberechnungsmethode von Computern werden, was eine Vielzahl von IT-Anwendungen verbessern kann.

## Referenzen

> [1]	Cui Yong, Song Jian, Miao congcongcong, Tang Jun. research progress and trend of mobile CDC [J]. Acta computer Sinica, 2017, 40 (02): 273-295.