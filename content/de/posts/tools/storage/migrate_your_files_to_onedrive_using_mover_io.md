---
title: "Nahtlose Migration von Cloud Drive-Dateien zu OneDrive mit dem mover.io-Service"
date: 2022-05-22T13:06:12+08:00
draft: false
tags: ["data", "mover.io", "onedrive", "google drive"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《Here, After Us - Mayday》" >}}

## Vorwort

Kürzlich informierte die Schule per E-Mail darüber, dass sie den E-Mail-Dienst von Google zu Microsoft wechseln würde und der bisher unbegrenzte Google Drive-Speicher eingestellt und durch 5TB OneDrive-Speicher ersetzt werden würde. Ich hatte den Dateidienst von Google Drive genutzt, um Dateien über meine mehreren Geräte hinweg zu synchronisieren und zu sichern, wobei sich fast 300 GB an Daten angesammelt hatten. Aufgrund der langsamen Download-Geschwindigkeiten von Google Drive in Festlandchina, die einen Proxy erfordern, entschied ich mich für den offiziell empfohlenen [mover.io](https://mover.io)-Service, um eine Cloud-Migration durchzuführen und so das lokale Herunterladen und erneute Hochladen von Dateien zu vermeiden. Hier dokumentiere ich den Migrationsprozess.

## mover.io-Service

![mover_io](https://image.pseudoyu.com/images/mover_io.png)

Der mover.io-Service ist ein von Microsoft bereitgestelltes Cloud-Speicher-Migrationstool. Es unterstützt die Migration von Dateien verschiedener Cloud-Service-Anbieter zu Microsoft OneDrive, einschließlich Google Drive, Dropbox, Box und anderen. Es bietet Migrationsdienste für Organisationen, Schulen und Einzelpersonen gleichermaßen.

Für Einzelnutzer verwenden wir den Transfer-Assistenten, um die Migration durchzuführen.

![mover_transfer_wizard](https://image.pseudoyu.com/images/mover_transfer_wizard.png)

## Migrationsprozess

### Registrieren/Anmelden eines mover.io-Kontos

Zunächst müssen wir ein mover.io-Konto registrieren und uns anmelden. Sie können die Microsoft-Autorisierung zur Anmeldung nutzen oder Ihr bestehendes mover.io-Konto verwenden.

![mover_io_login](https://image.pseudoyu.com/images/mover_io_login.png)

### Autorisierung der Migrations-Datenquelle

Nach erfolgreicher Anmeldung bietet die Oberfläche klare Bedienungsanweisungen. Folgen Sie einfach den Schritten.

![mover_transfer_wizard_setting](https://image.pseudoyu.com/images/mover_transfer_wizard_setting.png)

#### Migrationsquelle auswählen

Klicken Sie auf die Schaltfläche "Neue Verbindung autorisieren", wählen Sie Google Drive (Einzelbenutzer), wählen Sie das Google-Konto aus, das die zu migrierenden Dateien enthält, und autorisieren Sie.

![mover_source_google](https://image.pseudoyu.com/images/mover_source_google.png)

Nach der Autorisierung erscheint eine Liste aller zu migrierenden Dateien.

![mover_source_done](https://image.pseudoyu.com/images/mover_source_done.png)

#### Migrationsziel auswählen

Klicken Sie auf die Schaltfläche "Neue Verbindung autorisieren", wählen Sie OneDrive for Business (Einzelbenutzer), wählen Sie diese Datenquelle und autorisieren Sie. Derzeit unterstützt die Ziel-Datenquelle nur Microsoft-Familienprodukte wie OneDrive und SharePoint.

![mover_choose_dest](https://image.pseudoyu.com/images/mover_choose_dest.png)

![mover_dest_onedrive](https://image.pseudoyu.com/images/mover_dest_onedrive.png)

Nach der Autorisierung erscheint eine Dateiliste des Migrations-Ziel-Cloud-Speichers.

![mover_dest_onedrive_done](https://image.pseudoyu.com/images/mover_dest_onedrive_done.png)

### Daten migrieren

Sobald sowohl die Quell- als auch die Ziel-Datenquellen eingerichtet sind, können Sie "Kopieren starten" auswählen, um den Migrationsprozess zu beginnen.

![mover_start_copy](https://image.pseudoyu.com/images/mover_start_copy.png)

### Warten auf den Abschluss der Migration

Nach Abschluss der obigen Vorgänge beginnt der Migrationsprozess. Sie müssen nur warten, bis er abgeschlossen ist. Sie können den Fortschritt über den Migrationsmanager nach der Anmeldung überprüfen.

![mover_wait_migration_done](https://image.pseudoyu.com/images/mover_wait_migration_done.png)

Aufgrund von Unterschieden in den Quelldateigrößen variieren die Migrationszeiten für jeden Einzelnen. Basierend auf Tests ist die Migrationsgeschwindigkeitsreferenz wie folgt:

![mover_migration_speed](https://image.pseudoyu.com/images/mover_migration_speed.png)

## Fazit

Das Obige beschreibt den Prozess, den ich verwendet habe, um alle Google Drive-Dateien mit dem mover.io-Service zu OneDrive zu migrieren. Ich hoffe, dass sich dies für alle als hilfreich erweist.

## Referenzen

> 1. [mover.io Offizielle Website](https://mover.io/)
> 2. [Google Drive übertragen
(HKU Connect Google Drive > HKU Microsoft OneDrive)](https://its.hku.hk/kb/ways-on-reducing-storage-on-google-drive-google-photos-and-gmail/#b-transfer-google-drive)