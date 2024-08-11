---
title: "Einrichtung eines lokalen IPFS-Knotens (Kommandozeile)"
date: 2021-03-27T18:46:17+08:00
draft: false
tags: ["blockchain", "ipfs", "storage"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Vorwort

In unserem vorherigen Artikel "[Prinzipien der verteilten Dateispeicherung mit IPFS](https://www.pseudoyu.com/en/2021/03/25/blockchain_ipfs_structure/)" haben wir detailliert die Konzepte, Funktionen, Arbeitsprinzipien und IPNS des IPFS-Systems vorgestellt. Wie richten wir nun einen IPFS-Knoten lokal ein?

Dieser Beitrag demonstriert die Einrichtung eines IPFS-Knotens (Kommandozeilenversion) auf dem `macOS 11.2.3`-System und führt praktische Operationen zum Hochladen, Herunterladen, zur Netzwerksynchronisation, `pin`, `GC`, `IPNS` usw. durch, um das Verständnis der IPFS-Arbeitsprinzipien zu vertiefen.

## Praktische Umsetzung

### Installation

```sh
wget https://dist.ipfs.io/go-ipfs/v0.8.0/go-ipfs_v0.8.0_darwin-amd64.tar.gz
tar -xvzf go-ipfs_v0.8.0_darwin-amd64.tar.gz
cd go-ipfs
./install.sh
ipfs --version
```

### Inbetriebnahme

```sh
# Knoten starten
ipfs init

# Eine Datei hochladen
ipfs add ipfs_init_readme.png

# Eine Datei hochladen und nur den Hash-Wert ausgeben
ipfs add -q ipfs_init_readme.png

# Ein Verzeichnis hochladen
ipfs add -r [Verzeichnis]

# Datei anzeigen
ipfs cat /ipfs/QmQPeNsJPyVWPFDVHb77w8G42Fvo15z4bG2X8D2GhfbSXc/readme
ipfs cat /ipfs/QmQPeNsJPyVWPFDVHb77w8G42Fvo15z4bG2X8D2GhfbSXc/quick-start

# Ihre hochgeladene Datei anzeigen
ipfs cat QmaP3QS6ZfBoEaUJZ3ZfRKoBm3GGuhQSnUWtkVCNc8ZLTj

# Bild anzeigen und in Datei ausgeben
ipfs cat QmfViXYw7GA296brLwid255ivDp1kmTiXJw1kmZVsg7DFH > ipfsTest.png

# Datei herunterladen
ipfs get QmfViXYw7GA296brLwid255ivDp1kmTiXJw1kmZVsg7DFH -o ipfsTest.png

# Datei komprimieren und herunterladen
ipfs get QmfViXYw7GA296brLwid255ivDp1kmTiXJw1kmZVsg7DFH -Cao ipfsTest.png
```

![ipfs_init_readme](https://image.pseudoyu.com/images/ipfs_init_readme.png)

### Dienst starten/beitreten

```sh
# Aktuelle Knoteninformationen anzeigen
ipfs id

# IPFS-Konfigurationsinformationen anzeigen
ipfs config show

# Knotenserver starten
ipfs daemon
```

API-Dienst, standardmäßig auf Port 5001, kann über http://localhost:5001/webui aufgerufen werden

![ipfs_webui](https://image.pseudoyu.com/images/ipfs_webui.png)

Gateway-Dienst, standardmäßig auf Port 8080. Um Dateien im Browser aufzurufen, müssen Sie den von IPFS bereitgestellten Gateway-Dienst verwenden. Der Browser greift zuerst auf den Gateway zu, und der Gateway ruft die Dateien aus dem IPFS-Netzwerk ab. Zugriff auf in IPFS hochgeladene Dateien über http://localhost:8080/ipfs/[Datei-Hash]

### Dateioperationen

```sh
# Dateien auflisten
ipfs files ls

# Verzeichnis erstellen
ipfs files mkdir

# Datei löschen
ipfs files rm

# Datei kopieren
ipfs files cp [Datei-Hash] /[Zielverzeichnis]

# Datei verschieben
ipfs files mv [Datei-Hash] /[Zielverzeichnis]

# Status
ipfs files stat

# Lesen
ipfs files read
```

### Verwendung von IPNS zur Lösung von Dateiaktualisierungsproblemen

```sh
# IPNS verwenden, um Inhalte für automatische Aktualisierungen zu veröffentlichen
ipfs name publish [Datei-Hash]

# Den vom Knoten-ID angezeigten Hash abfragen
ipfs name resolve

# Wenn mehrere Websites aktualisiert werden müssen, können Sie ein neues Schlüsselpaar generieren und mit dem neuen Schlüssel veröffentlichen
ipfs key gen --type=rsa --size=2048 mykey
ipfs name publish --key=mykey  [Datei-Hash]
```

### Pinning

Wenn wir Dateien aus dem IPFS-Netzwerk anfordern, synchronisiert IPFS den Inhalt lokal, um Dienste bereitzustellen, und verwendet einen Cache-Mechanismus zur Verwaltung von Dateien, um zu verhindern, dass der Speicherplatz kontinuierlich wächst. Wenn eine Datei für eine gewisse Zeit nicht verwendet wird, wird sie "recycelt". Der Zweck des Pinnings besteht darin, sicherzustellen, dass Dateien lokal nicht "recycelt" werden.

```sh
# Eine Datei pinnen
ipfs pin add [Datei-Hash]

# Abfragen, ob ein Hash gepinnt ist
ipfs pin ls [Datei-Hash]

# Pin-Status entfernen
ipfs pin rm -r [Datei-Hash]

# GC-Operation
ipfs repo gc
```

## Fazit

Dieser Artikel beschäftigte sich hauptsächlich mit der lokalen Bereitstellung des IPFS-Dateisystems und testete grundlegende Operationen, basierend auf `macOS 11.2.3` und der Version `go-ipfs_v0.8.0_darwin-amd64`. Die Operationen auf verschiedenen Systemen können aufgrund von Versions- oder Abhängigkeitsproblemen variieren. Bei etwaigen Fehlern oder Auslassungen stehe ich gerne für Kommunikation und Korrekturen zur Verfügung.

## Referenzen

> 1. [IPFS Offizielle Website](https://ipfs.io)