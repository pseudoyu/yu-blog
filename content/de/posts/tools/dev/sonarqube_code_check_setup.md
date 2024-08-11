---
title: "SonarQube Code-Qualitätsprüfungs-Tool Konfiguration"
date: 2021-10-27T01:57:23+08:00
draft: false
tags: ["code check", "devops"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

## Vorwort

In letzter Zeit war ich für die Verwaltung von Code-Repositorys und die Durchführung von Code-Reviews für einige Unternehmensprojekte verantwortlich. Ich habe SonarQube verwendet, ein Tool zur Überprüfung der Code-Qualität, das bei Integration mit GitLab CI automatisch Code-Qualitätsprüfungen durchführen und Prüfberichte für jede Merge-Anfrage oder jeden Commit ausgeben kann.

Dieser Artikel dokumentiert den vollständigen Konfigurationsprozess für den Import von Projekten über GitLab-Repositorys und dient als Referenz für die Konfiguration anderer Projekte.

## SonarQube Projektkonfiguration

### Projekt-Dashboard

![sonarqube_homepage](https://image.pseudoyu.com/images/sonarqube_homepage.png)

Das SonarQube-Projekt-Dashboard ist im obigen Bild zu sehen, das die Code-Qualität des Projekts anhand eines Bewertungssystems analysiert. Nach jeder Code-Analyse liefert es eine mehrdimensionale Analyse des Codes auf visuell intuitive Weise. Vor dem Zusammenführen von Branches können sich die Einreicher auf die Analyseergebnisse beziehen, um ihren Code zu modifizieren und zu verbessern, wodurch unnötiger Arbeitsaufwand für Code-Prüfer reduziert wird.

![sonarqube_code_detail](https://image.pseudoyu.com/images/sonarqube_code_detail.png)

Durch Klicken auf bestimmte Metriken kann man tiefer in die Code-Dateien eintauchen, erkannte Probleme identifizieren und eine effektive Referenz für manuelle Code-Reviews bereitstellen.

### Projekteinrichtung

![how_to_analyze](https://image.pseudoyu.com/images/how_to_analyze.png)

Klicken Sie oben rechts auf "Add Project", um aus verschiedenen Analysemethoden zu wählen. Es unterstützt gängige Code-Repository-Automatisierungs-Workflows wie Jenkins, GitLab CI und GitHub Actions. Dieser Artikel wird hauptsächlich die Konfigurationsmethode für GitLab CI erklären.

![import_gitlab_project](https://image.pseudoyu.com/images/import_gitlab_project.png)

Nach der Auswahl von GitLab CI wählen Sie das Projekt-Repository aus Ihrem verknüpften GitLab-Konto aus, um mit der weiteren Konfiguration fortzufahren.

![project_code](https://image.pseudoyu.com/images/project_code.png)

Am Beispiel eines Go-Projekts müssen wir zunächst manuell eine `sonar-project.properties`-Datei erstellen und die Konfigurationsinformationen gemäß den Anweisungen einfügen.

![create_token.png](https://image.pseudoyu.com/images/create_token.png.png)

![config_cicd_var](https://image.pseudoyu.com/images/config_cicd_var.png)

Anschließend müssen wir einen Token für das Projekt erstellen und die Token- und URL-Variablenwerte in GitLab unter "Settings" - "CI/CD" - "Variables" Konfigurationsoptionen ausfüllen.

### CI-Konfiguration

Nach der grundlegenden Projektkonfiguration müssen wir den GitLab CI-Workflow über `.gitlab-ci.yml` konfigurieren. Meine Konfiguration ist im Bild unten zu sehen:

![config_gitlan_ci](https://image.pseudoyu.com/images/config_gitlan_ci.png)

Ich habe es hauptsächlich so eingerichtet, dass bei einer Merge-Anfrage an das Repository, wenn es Änderungen im `src`-Verzeichnis gibt, die `testing`-Pipeline ausgeführt wird, die eine Code-Qualitätsprüfung durch SonarQube durchführt.

GitLab CI kann auch Bereitstellungsskripte enthalten, die in Verbindung mit dem SonarQube-Tool zur Optimierung von Workflows verwendet werden. Für das CI-Skript des Projekts müssen entsprechende Runner hinzugefügt werden, um ausgeführt zu werden.

![sonar_check_begin](https://image.pseudoyu.com/images/sonar_check_begin.png)

Wenn eine Merge-Anfrage erkannt wird, wird die sonarqube-check ausgelöst und ausgeführt, und letztendlich werden die Ausführungsergebnisse zurückgegeben.

![sonar_check_success](https://image.pseudoyu.com/images/sonar_check_success.png)

![sonarqube_status](https://image.pseudoyu.com/images/sonarqube_status.png)

An dieser Stelle wird beim Öffnen der Projektseite in SonarQube die Analyseinformation angezeigt, womit diese Code-Qualitätsprüfung abgeschlossen ist.

## Fazit

Das oben Beschriebene stellt den vollständigen Prozess der Konfiguration des SonarQube Code-Qualitätsprüfungs-Tools für ein bestehendes Go-Projekt in einem GitLab-Repository dar. Automatisierte Code-Qualitätsprüfungen sind ein wichtiger Bestandteil standardisierter Entwicklungs- und Betriebsprozesse, insbesondere in Teamprojekten. Gute Standards helfen dabei, Arbeitsabläufe zu optimieren und die Gesamtqualität des Projekts zu verbessern.

In Zukunft werde ich weiterhin die Konfiguration und Verwendung von Open-Source-Tools für Entwicklungs- und Betriebsstandards dokumentieren, die in der Arbeit verwendet werden. Falls es Fehler oder Auslassungen gibt, können Sie sich gerne mitteilen und korrigieren.

## Referenzen

> 1. [SonarQube Dokumentation](https://docs.sonarqube.org/latest/)