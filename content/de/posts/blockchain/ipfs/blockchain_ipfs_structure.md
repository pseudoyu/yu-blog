---
title: "Analyse und Reflexionen über das IPFS verteilte Speicherprotokoll"
date: 2021-03-25T16:30:17+08:00
draft: false
tags: ["blockchain", "ipfs", "storage"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Vorwort

Kürzlich habe ich an einem Fallstudienprojekt für die Universität gearbeitet, einem Musikurheberrechtsverwaltungsprojekt basierend auf der `Ethereum`-Plattform. Es verwendet die IPFS-Technologie für verteilte Dateispeicherung zum Hochladen von Musikwerken und Urheberrechtsnachweisdokumenten, wobei hauptsächlich die Deduplizierungsfunktion zur Erkennung von Verstößen genutzt wird. Ich wurde neugierig auf das IPFS-System und las die [IPFS-Artikelserie](https://tech.hyperchain.cn/tag/ipfs/) auf der [QTech-Plattform](https://tech.hyperchain.cn). Zudem konsultierte ich einige verwandte Materialien und werde sie in diesem Artikel zusammenfassen. Falls es Fehler oder Auslassungen gibt, diskutieren und korrigieren Sie diese bitte.

## Überblick

Wenn wir in unserem Alltag Cloud-Speicher oder andere Dienste nutzen, greifen wir meist auf Dateien auf bestimmten Servern (IP-Adressen) zu, fordern Dateien an und laden sie über das HTTP-Protokoll lokal herunter. Dies basiert im Wesentlichen auf ortsbasierter Adressierung, wobei URLs Schicht für Schicht aufgerufen werden, um bestimmte Dateien zu finden. Während diese Methode bequem ist, hat sie einige Probleme. Dateien sind von bestimmten Servern abhängig, sodass bei einem Ausfall des zentralisierten Servers oder dem Löschen der Datei der Inhalt dauerhaft verloren geht. Zudem wird die Zugriffsgeschwindigkeit langsam sein, wenn der Server weit entfernt ist oder viele Personen gleichzeitig auf die Datei zugreifen. Darüber hinaus kann dieselbe Datei mehrfach auf verschiedenen Servern gespeichert sein, was Ressourcen verschwendet. Außerdem bestehen ernsthafte Sicherheitsrisiken, da Angriffe wie DDoS, XSS und CSRF die Dateisicherheit gefährden können.

> Gibt es eine bessere Lösung?

Stellen Sie sich vor, wir würden Dateien in einem verteilten Netzwerk speichern, in dem jeder Knoten Dateien speichern könnte und Benutzer Dateien vom nächstgelegenen Knoten über einen verzeichnisähnlichen Ansatz anfordern könnten. Dies ist der Lösungsansatz des IPFS (InterPlanetary File System), einem Peer-to-Peer-Hypermedia-Dateispeicherungs-, Indexierungs- und Austauschprotokoll, das von Juan Benet im Mai 2014 initiiert wurde.

### Merkmale

IPFS zielt darauf ab, alle Computergeräte weltweit mit demselben Dateisystem zu verbinden und ein verteiltes Netzwerk aufzubauen, das das traditionelle zentralisierte Servermodell ersetzt. Jeder Knoten kann Dateien speichern, und Benutzer können Dateien über eine `DHT (Distributed Hash Table)` erhalten, was es schneller, sicherer und mit stärkerer Netzwerksicherheit macht.

Da Dateien, die über IPFS gespeichert werden, ihren Inhalt als Adressen durch Berechnung von Hash-Werten in Blöcken speichern, handelt es sich im Wesentlichen um eine dezentralisierte, aber inhaltsadressierte Methode. Durch die Verschlüsselung der Daten selbst wird ein eindeutiger Hash zur Suche generiert. Auf diese Weise führt selbst eine winzige Änderung zu einem völlig anderen Hash, wodurch Inhaltsmanipulationen leicht am Hash erkannt werden können, ohne auf die Datei selbst zuzugreifen.

Im Gegensatz zu traditionellen Servermodellen ist IPFS ein einheitliches Netzwerk. Daher werden Dateien mit gleichem Inhalt, die bereits hochgeladen wurden, nicht mehrfach gespeichert (überprüfbar durch Hash-Werte), was die gesamten Netzwerkressourcen erheblich spart und die Effizienz verbessert. Theoretisch werden Dateien dauerhaft erhalten, solange die Anzahl der Knoten eine bestimmte Größenordnung erreicht, und dieselbe Datei kann von mehreren (und näheren) Knoten heruntergeladen werden, was die Kommunikationseffizienz verbessert.

Aufgrund der verteilten Netzwerkspeicherung können zudem traditionelle Angriffe wie DDoS natürlich vermieden werden.

### Funktionen

Neben der Dateispeicherung verfügt IPFS auch über Funktionen wie DHT-Vernetzung und Bitswap-Dateiaustausch, die in separaten Blogbeiträgen später erklärt werden.

## Funktionsprinzip

Als Dateispeicherungssystem sind das Hochladen und Herunterladen von Dateien die beiden grundlegendsten Operationen. Lassen Sie uns die Prinzipien jeder Operation erklären.

### IPFS add Befehl

> Im IPFS-System wird durch Ausführung der add-Operation der Upload-Vorgang abgeschlossen. Wie wird hochgeladen?

Im IPFS-Dateispeicherungssystem wird bei jedem Hochladen einer neuen Datei die einzelne Datei in mehrere 256-KB-Blöcke unterteilt. Jeder Block hat eine eindeutige CID zur Identifikation, was später ausführlich erklärt wird. Dann wird der Hash-Wert jedes Blocks berechnet und in einem Array gespeichert. Schließlich wird der Hash dieses Arrays berechnet, um den endgültigen Hash-Wert der Datei zu erhalten. Dann wird ein Objekt erstellt, das aus dem Hash der Datei und dem Array aller Block-Hashes besteht und eine Indexstruktur bildet. Zuletzt werden alle Dateiblöcke und diese Indexstruktur zum IPFS-Knoten hochgeladen und mit dem IPFS-Netzwerk synchronisiert.

Beim Hochladen von Dateien gibt es zwei bemerkenswerte Situationen: 1. Wenn die Datei besonders klein ist, weniger als 1 KB, wird kein Block verschwendet und sie wird direkt mit dem Hash zu IPFS hochgeladen. 2. Wenn die Datei besonders groß ist, zum Beispiel wenn zuvor ein 1-GB-Video hochgeladen wurde und dann eine wenige KB große Untertiteldatei hinzugefügt wurde, wird in diesem Fall der unveränderte 1-GB-Teil nicht neu zugewiesen, sondern nur der hinzugefügte Untertiteldateiteil erhält neue Blöcke, und der Hash wird erneut hochgeladen.

Daher ist es leicht zu verstehen, dass selbst die gleichen Teile verschiedener Dateien nur einmal gespeichert werden und die Indizes vieler Dateien auf denselben Block zeigen, wodurch eine MerkleDAG-Datenstruktur entsteht.

Es ist erwähnenswert, dass wenn ein Knoten die add-Operation ausführt, dies im lokalen Blockstore gehalten wird, aber nicht sofort aktiv in das IPFS-Netzwerk hochgeladen wird. Mit anderen Worten, die damit verbundenen Knoten werden diese Datei nicht speichern, es sei denn, ein bestimmter Knoten hat diese Blockdaten angefordert! Daher ist es keine automatische Backup-verteilte Datenbank. IPFS hat es so konzipiert, um Netzwerkbandbreite, Zuverlässigkeit und andere Aspekte zu berücksichtigen.

Ein weiteres Detail ist, dass wenn ein Knoten den `add`-Befehl ausführt, er auch seine Blockinformationen überträgt und eine Liste aller Blockanfragen pflegt, die an diesen Knoten gesendet wurden. Sobald der add-Befehl Daten hinzufügt, die dieser Liste entsprechen, wird er aktiv Daten an die entsprechenden Knoten senden und die Liste aktualisieren.

### IPFS get Befehl

> Nachdem die Datei hochgeladen wurde, wie kann man sie suchen und darauf zugreifen?

Dies bezieht sich auf die oben erwähnte IPFS-Indexstruktur, die `DHT` (Distributed Hash Table) ist. Durch Zugriff auf `DHT` können Daten schnell abgerufen werden.

![ipfs_dht](https://image.pseudoyu.com/images/ipfs_dht.png)

> Was ist, wenn Sie Daten finden möchten, die nicht lokal verfügbar sind?

![ipfs_get](https://image.pseudoyu.com/images/ipfs_get.gif)

Im IPFS-System bilden alle mit dem aktuellen Knoten verbundenen Knoten ein Schwarm-Netzwerk. Wenn ein Knoten eine Dateianforderung sendet (d.h. `get`), sucht er zunächst nach den angeforderten Daten im lokalen Blockstore. Wenn sie nicht gefunden werden, sendet er eine Anfrage an das Schwarm-Netzwerk und findet den Knoten, der die Daten hat, über das `DHT Routing` im Netzwerk.

> Woher weiß man, welcher Knoten (oder welche Knoten) im Netzwerk diese angeforderte Datei hat?

Wie beim `add`-Befehl oben erwähnt, teilt ein Knoten, wenn er dem IPFS-Netzwerk beitritt, anderen Knoten mit, welche Inhalte er gespeichert hat (durch Übertragung von `DHT`). Auf diese Weise werden andere Knoten dem Benutzer mitteilen, den gewünschten Inhalt von diesem Knoten zu holen, wann immer ein Benutzer Inhalte abrufen möchte, die zufällig auf diesem Knoten sind.

Sobald der Knoten mit diesen Daten gefunden ist, werden die angeforderten Daten zurückgemeldet, und der lokale Knoten speichert eine Kopie der empfangenen Blockdaten im lokalen Blockstore zwischen. Auf diese Weise hat das gesamte Netzwerk eine zusätzliche Kopie der ursprünglichen Daten, was es einfacher macht, sie zu finden, wenn mehr Knoten die Daten anfordern. Daher basiert die Nicht-Verlust von Daten auf diesem Prinzip. Solange ein Knoten diese Daten behält, können sie vom gesamten Netzwerk abgerufen werden.

> Im Projekt können hochgeladene Dateien direkt über das `ipfs.io`-Gateway zugegriffen werden, ähnlich wie Webseitenadressen wie `https://ipfs.io/ipfs/Qm.....`. Was ist das Prinzip dahinter?

![ipfs_io_get](https://image.pseudoyu.com/images/ipfs_io_get.gif)

Das `ipfs.io`-Gateway ist eigentlich ein IPFS-Knoten. Wenn wir den obigen Weblink öffnen, senden wir tatsächlich eine Anfrage an diesen Knoten. Daher wird das `ipfs.io`-Gateway uns helfen, diesen Block von dem Knoten anzufordern, der diese Daten hat (wenn diese Datei gerade durch den `add`-Befehl zum lokalen Knoten hinzugefügt wurde, wird sie auf diese Weise in das IPFS-Netzwerk hochgeladen). Nachdem die Daten über `DHT Routing` im `swarm`-Netzwerk erhalten wurden, speichert das Gateway selbst eine Kopie und sendet die Daten dann über das HTTP-Protokoll an uns. So können wir diese Datei direkt im Browser sehen!

Wenn ein anderer Computer über einen Browser auf diesen Link zugreift, da das `ipfs.io`-Gateway diese Datei bereits zwischengespeichert hat, muss es bei erneuter Anfrage keine Daten vom ursprünglichen Knoten anfordern, sondern kann die Daten direkt aus dem Cache an den Browser zurückgeben.

### Content Identifier CID

Betrachten wir nun eine andere Frage: Wir sind mit Bildformaten wie `.jpg`, `.png` und gängigen Videoformaten wie `.mp4` vertraut, die direkt anhand der Dateierweiterung beurteilt werden können. Dateien, die über IPFS hochgeladen werden, können auch mehrere Typen haben und viele Informationen enthalten. Wie unterscheidet man sie?

In den frühen Stadien von IPFS wurde hauptsächlich `base58btc` verwendet, um `multihash` zu kodieren, aber im Prozess der Entwicklung von IPLD (hauptsächlich verwendet, um Daten zu definieren und zu modellieren) traten viele formatbezogene Probleme auf. Daher wurde ein Dateiadressierungsformat namens `CID` verwendet, um Daten verschiedener Formate zu verwalten. Die offizielle Definition lautet:

> `CID` ist ein selbstbeschreibender, inhaltsadressierter Identifikator, der eine kryptografische Hashfunktion verwenden muss, um die Adresse des Inhalts zu erhalten

Einfach ausgedrückt verwendet `CID` einige Mechanismen, um den in der Datei enthaltenen Inhalt selbst zu beschreiben, einschließlich Versionsinformationen, Format usw.

#### CID-Struktur

Derzeit gibt es zwei Versionen von `CID`: `v0` und `v1`. Die `v1`-Version von `CID` wird von `V1Builder` generiert

```sh
<cidv1> ::= <mb><version><mcp><mh>
# oder, erweitert:
<cidv1> ::= <multibase-prefix><cid-version><multicodec-packed-content-type><multihash-content-address>
```

Wie im oben aufgeführten Code gezeigt, wird der verwendete Mechanismus `multipleformats` genannt und umfasst hauptsächlich: `multibase-prefix` zeigt an, dass `CID` in eine Zeichenfolge kodiert ist, `cid-version` zeigt die Versionsvariable an, `multicodec-packed-content-type` zeigt den Typ und das Format des Inhalts an (ähnlich dem Suffix, aber als Teil des Identifikators, die unterstützten Formate sind begrenzt und Benutzer können sie nicht beliebig ändern), `multihash-content-address` zeigt den Hash-Wert an (ermöglicht `CID` die Verwendung verschiedener Hash-Funktionen).

Derzeit umfassen die von `CID` unterstützten `multicodec-packed`-Kodierungen natives `protobuf`-Format, `IPLD CBOR`-Format, `git`, Bitcoin- und Ethereum-Objekte usw., und die Unterstützung für weitere Formate wird schrittweise entwickelt.

Detaillierte Erklärung des `CID`-Codes:

```go
type Cid struct {str string}
type V0Builder struct {}
type V1Builder struct {}

Codec uint64
MhType uint64
MhLength int // Standard: -1
```

`Codec` repräsentiert den Kodierungstyp des Inhalts, wie `DagProtobuf`, `DagCBOR` usw. `MhType` repräsentiert den Hash-Algorithmus, wie `SHA2_256`, `SHA2_512`, `SHA3_256`, `SHA3_512` usw. `MhLength` repräsentiert die Länge des generierten Hashs.

Die `v0`-Version von `CID` wird von `V0Builder` generiert, beginnt mit der Zeichenfolge `Qm`, ist rückwärtskompatibel, mit `multibase` immer als `base58btc`, `multicodec` immer als `protobuf-mdag`, `cid-version` immer als `cidv0`, und `multihash` dargestellt als `cidv0 ::= <multihash-content-address>`.

#### Designphilosophie

Durch die binäre Natur von `CID` wird die Kompressionseffizienz von Datei-Hashes stark verbessert, sodass es direkt als Teil der URL für den Zugriff verwendet werden kann; die Kodierungsform von `multibase` (wie `base58btc`) verkürzt die Länge von `CID`, was die Übertragung erleichtert; es kann die Ergebnisse jedes Formats und jeder Hash-Funktion darstellen, was sehr flexibel ist; es kann die Kodierungsversion durch den `cid-version`-Parameter in der Struktur aktualisieren; es ist nicht durch historische Inhalte eingeschränkt.

### IPNS

Wie oben erwähnt, führen Änderungen des Dateiinhalts in IPFS zu Änderungen seines Hash-Werts. In praktischen Anwendungen, wenn Anwendungen, die Versionsupdates und Iterationen benötigen, wie über IPFS gehostete Websites, jedes Mal über aktualisierte Hashes aufgerufen werden, ist dies sehr unbequem. Daher wird ein Mapping-Schema benötigt, um die Benutzererfahrung zu gewährleisten, sodass Benutzer beim Zugriff nur eine feste Adresse aufrufen müssen.

`IPNS (Inter-Planetary Naming System)` bietet einen solchen Dienst. Es stellt eine durch einen privaten Schlüssel begrenzte Hash-ID (normalerweise PeerID) bereit, die auf bestimmte IPFS-Dateien zeigt. Nach der Aktualisierung der Datei wird der Zeiger der Hash-ID automatisch aktualisiert.

Obwohl der Hash-Wert fest bleiben kann, ist er immer noch nicht leicht zu merken und einzugeben. Daher gibt es eine weitere Lösung.

IPNS ist auch mit DNS kompatibel. Sie können den `DNS TXT`-Eintrag verwenden, um die IPNS-Hash-ID zu erfassen, die dem Domänennamen entspricht, sodass Sie den Domänennamen verwenden können, um die IPNS-Hash-ID für den Zugriff zu ersetzen, was es leichter macht, sie zu lesen, zu schreiben und sich zu merken.

## Fazit

Das oben Genannte ist eine Zusammenfassung der Prinzipien der verteilten IPFS-Speicherung. Seine Komponenten, Details des Speicherprozesses, GC-Mechanismus, Datenaustauschmodul Bitswap, Netzwerk und praktische Anwendungsszenarien haben viele Aspekte, die es wert sind, eingehend erforscht zu werden.

> Empfohlene Lektüre: QTech-Plattform von Hyperchain Technology《[IPFS-Artikelserie](https://tech.hyperchain.cn/tag/ipfs/)》

## Referenzen

> 1. [IPFS Offizielle Website](https://ipfs.io)
> 2. [So speichert IPFS Dateien](https://tech.hyperchain.cn/ipfs/), *QTech, Hyperchain Technology*
> 3. [Wie funktioniert IPFS tatsächlich?](https://cloud.tencent.com/developer/news/277198), *Zhihui*
> 4. [IPFS aus der Perspektive von Web3.0 verstehen](https://learnblockchain.cn/2018/12/12/what-is-ipfs), *Tiny Bear, Dengchain Community*
> 5. [IPFS CID-Forschung](https://medium.com/@kidinamoto/ipfs-cid-研究-717c4ceb14a0), *Sophie Huang*