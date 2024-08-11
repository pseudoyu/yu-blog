---
title: "Einführung und Architektur von Blockchain-as-a-Service (BaaS) Plattformen"
date: 2021-09-07T10:00:52+08:00
draft: false
tags: ["blockchain", "hyperledger fabric", "baas"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Vorwort

In meiner aktuellen Arbeit bin ich für den Bereich der Chaincode-Verwaltung einer Blockchain-as-a-Service (BaaS) Plattform für Hyperledger Fabric verantwortlich. Ich interessiere mich sehr für die Architektur und Implementierung von BaaS-Plattformen. Als eine Plattform, die Entwicklern eine One-Stop-Lösung für die Erstellung, Verwaltung und Wartung von Blockchain-Anwendungen bietet, wie sieht ihre Architektur aus?

Dieser Artikel ist eine Zusammenfassung und Analyse der BaaS-Plattform-Architektur.

## Einführung in BaaS

Blockchain ist ein komplexes verteiltes System, insbesondere Enterprise-Konsortium-Chain-Plattformen wie Hyperledger Fabric, bei denen die Bereitstellung und der Betrieb äußerst komplex sind. Als Anwendungsentwickler müssen wir uns mit vielen Umgebungsproblemen auseinandersetzen (wie z.B. Zertifikaten, Docker-Umgebungen usw.), was zahlreiche Herausforderungen mit sich bringt.

Daher sind BaaS-Plattformen entstanden. Es handelt sich um Anwendungsplattformen, die Benutzern bei der Erstellung, Verwaltung und Wartung von Blockchain-Systemen auf Unternehmensebene helfen. Benutzer können die Blockchain über eine benutzerfreundliche Weboberfläche bedienen. Durch BaaS-Plattformen können Benutzer flexibel Blockchain-Netzwerke aufbauen, Blockchain-Geschäfte und verschiedene Modulfunktionen verwalten, Smart Contracts entwickeln und bereitstellen sowie Echtzeitüberwachung und -betrieb durchführen.

Mit BaaS-Plattformen können Entwickler schnell Blockchain-Geschäftsentwicklungen durchführen, was die Gesamtkosten erheblich reduziert und dazu beiträgt, die Systemstabilität, Sicherheit und Benutzerfreundlichkeit zu verbessern.

![baas_framework](https://image.pseudoyu.com/images/baas_framework.png)

## Plattform-Architektur

Als One-Stop-Anwendungsdienst ist eine BaaS-Plattform primär in die folgenden Schichten von unten nach oben unterteilt:

1. Ressourcenschicht
2. Überwachungs- und Betriebsschicht
3. Blockchain-Grundlagenschicht
4. Blockchain-Serviceschicht
5. Anwendungsschicht

Je nach den geschäftlichen Unterschieden jedes Systems variieren die Architektur und die Funktionsmodule jeder Schicht. Im Folgenden werde ich die hierarchischen Strukturen mehrerer gängiger Plattformen beschreiben.

### Hyperledger Cello

![hyperledger_cello_overview](https://image.pseudoyu.com/images/hyperledger_cello_overview.png)

[Hyperledger Cello](https://github.com/hyperledger/cello), als eines der Top-Level-Projekte von IBM Hyperledger, ist eine Open-Source-Blockchain-Managementplattform, die Funktionen für Bereitstellung, Laufzeitverwaltung und Datenanalyse unterstützt.

Cello unterstützt derzeit die Hyperledger Fabric Blockchain und kann den Lebenszyklus von Fabric-Chains effektiv verwalten. Es umfasst hauptsächlich die folgenden Module:

![hyperledger_cello_architecture](https://image.pseudoyu.com/images/hyperledger_cello_architecture.png)

Neben der effizienten Erstellung und Bereitstellung von Netzwerken bietet Cello einige Verwaltungsfunktionen für Blockchains:

- Blockchain-Lebenszyklus-Management
- Unterstützung für mehrere zugrunde liegende Architekturen wie Docker, Swarm, Kubernetes usw.
- Unterstützung für mehrere zugrunde liegende Blockchain-Plattformen mit anpassbaren Konfigurationen
- Laufzeitüberwachung und Betriebsunterstützung
- Pluginfähiges Framework-Design, das die Erweiterung von Drittanbieter-Funktionen durch Plugins ermöglicht, wie z.B. Ressourcenplanung, Treiberagenten usw.

### Hyperchain BaaS

Laut der offiziellen Website ist BlocFace eine neu eingeführte Blockchain-Service-Plattform von Hyperchain Technology für Unternehmen und Entwickler. Sie bietet Benutzern One-Click-Bereitstellung von Konsortialketten, visuelle Überwachung und Betrieb sowie Smart-Contract-Entwicklung, unter anderen One-Stop-Entwicklungsdiensten. Die Plattformarchitektur sieht wie folgt aus:

![hyperchain_baas](https://image.pseudoyu.com/images/hyperchain_baas.png)

## Fazit

Das Obige ist eine Einführung und Architekturanalyse von Blockchain-as-a-Service (BaaS) Plattformen. Da mein derzeitiger Vorgesetzter der Projektinitiator und Kernentwickler von Hyperledger Cello ist, werde ich ermutigt, aktiv an der Open-Source-Entwicklung von Cello teilzunehmen. Zeit, hart zu arbeiten!

## Referenzen

> 1. [Blockchain: Grundsätze, Design und Anwendungen](https://book.douban.com/subject/27127839/)
> 2. [Hyperledger Cello Projekt-Repository](https://github.com/hyperledger/cello)
> 3. [BlocFace Offizielle Website](https://www.hyperchain.cn/products/blocface)