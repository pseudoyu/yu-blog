---
title: "Workflow zur Entwicklung von Thin Clients basierend auf frp-Intranet-Penetration"
date: 2022-07-05T10:00:16+08:00
draft: false
tags: ["frp", "proxy", "network", "dev-environment", "devices", "tools"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="'Here After Us - Mayday'" >}}

## Vorwort

![leopold_fc660c](https://image.pseudoyu.com/images/leopold_fc660c.jpg)

In meinem vorherigen Projekt ["GitHub - Personal Toolbox"](https://github.com/pseudoyu/yu-tools) erwähnte ich, dass ich zu Hause ein Mac Studio habe, das immer eingeschaltet ist, und einen Raspberry Pi 3b+ Mikrocomputer, auf dem Ubuntu läuft. Wenn ich zu Hause bin, bediene ich normalerweise das Mac Studio, das an einen Monitor angeschlossen ist, oder greife über SSH vom Terminal meines Chromebooks darauf zu.

Nach dem Ende der Fernarbeit muss ich täglich zwischen Büro und Zuhause pendeln. Da ich nicht jeden Tag einen Laptop mit mir herumtragen möchte, habe ich meinen vorherigen 16-Zoll MacBook Pro Hauptentwicklungsrechner (der wirklich schwer ist) im Büro für die Entwicklung von Arbeitsprojekten gelassen. Obwohl ich Code über GitHub und GitLab sowie Dateien über OneDrive und iCloud synchronisieren kann, hatte ich trotzdem das Gefühl, jeden Tag zwei Desktop-Entwicklungsumgebungen zu pflegen. Einige Konfigurationsänderungen der Umgebung erforderten den doppelten Arbeitsaufwand, was eine erhebliche mentale Belastung mit sich brachte.

Darüber hinaus ist die Leistung des M1 Max Chip-Geräts zu Hause weitaus besser als die des alten Intel MacBook Pro Laptops. Also begann ich, Lösungen zu erkunden, um von zu Hause aus über das öffentliche Netzwerk auf Geräte zuzugreifen, und praktizierte einen Workflow für Thin Clients. Dieser Artikel ist eine Aufzeichnung und Zusammenfassung dieses Workflows.

## Thin Client Workflow

Ich wurde durch diese Episode des ["Teahour"](https://teahour.fm) Podcasts inspiriert: ["#95 - Wie ist es, auf einem Chromebook zu entwickeln?"](https://teahour.fm/95), wo ich zum ersten Mal von dem Thin-Client-Entwicklungsmodell erfuhr.

### Grundlegende Konzepte

Die Entwicklung von Thin Clients ist ein zunehmend beliebtes Entwicklungsmodell. Die Hauptidee besteht darin, dass die von Ihnen verwendeten Entwicklungseingabegeräte (wie Laptops, Tablets usw.) keine verschiedenen Entwicklungsumgebungen installieren. Stattdessen verwenden sie Terminal, VS Code Remote oder Jetbrains Client und andere Client-Programme als Eingangspunkte, um eine Verbindung zu Ihrem Remote-Host oder Server herzustellen. Diese Methode hat folgende Vorteile:

1. Sie kann Ihre Entwicklungsumgebung weitestgehend vereinfachen. Sie benötigen nur ein Terminal und einen Browser, um die meisten Entwicklungsarbeiten durchzuführen, was die Gerätekosten reduzieren kann. Sie können sogar ein Chromebook oder iPad verwenden, um die tägliche Entwicklungsarbeit zu erledigen.
2. Sie reduziert die Einschränkungen des Bürostandorts. Sie können tragbare Geräte mitnehmen und frei in Cafés oder anderen Orten arbeiten. Im Vergleich zum lokalen Betrieb verschiedener Entwicklungsumgebungen hat diese Methode auch eine längere Akkulaufzeit.
3. Unabhängig davon, welches Gerät Sie für den Entwicklungszugriff verwenden, können Sie sicherstellen, dass Ihre Entwicklungsumgebung und Ihr Fortschritt konsistent bleiben, wodurch die Kosten für die Synchronisierung und Wartung der Umgebung reduziert werden.
4. Oft ist unsere Entwicklungsumgebung ein macOS- oder Windows-Betriebssystem. Manchmal kann die lokale Entwicklungsumgebung einige Unterschiede zur tatsächlichen Projektlaufzeitumgebung aufweisen. Die Fernentwicklung in einem Linux-System kann diese Unterschiede effektiv reduzieren und die Entwicklungseffizienz verbessern.
5. Wir können den Großteil unserer Kosten auf ein relativ leistungsfähiges Gerät konzentrieren, um langfristige Entwicklungsbedürfnisse zu erfüllen.
6. Wenn es vorübergehende Entwicklungsbedürfnisse gibt, können wir nach Bedarf einige Cloud-Server starten und stoppen, was Kosten spart und die Entwicklungseffizienz verbessert.
7. In Bereichen wie Deep Learning, die spezielle Geräte wie GPUs für Berechnungen erfordern, kann die Entwicklung nicht auf lokalen Maschinen durchgeführt werden.

### Mein Thin Client Workflow

![thin_client_structure](https://image.pseudoyu.com/images/thin_client_structure.png)

Um Kosten zu reduzieren, basiert mein Thin-Client-Workflow hauptsächlich auf einer selbst eingerichteten Intranet-Penetrationslösung (das Schemaprinzip und die Einrichtungsmethode werden später detailliert erklärt). Er greift von verschiedenen Clients im öffentlichen Netzwerk auf den leistungsfähigeren Host und Server zu Hause zu, um die Hauptentwicklungsarbeit abzuschließen.

Meine Hauptgeräte auf der Clientseite sind derzeit:

1. 16-Zoll MacBook Pro, langfristig im Büro platziert, als Arbeitsgerät genutzt, hauptsächlich zum Durchsuchen von Webseiten, Dokumenten und zum Verbinden mit verschiedenen Remote-Hosts oder Servern für Entwicklungsarbeiten durch das iTerm2-Terminal-Tool und zum Verwalten von Code und Projekten über Git.
2. Google Pixelbook Go, hauptsächlich in Cafés, auf der Couch zu Hause oder an anderen Orten für technisches Lernen, Blogschreiben oder persönliche Projektentwicklung verwendet.

Meine Server sind in folgende Kategorien unterteilt:

1. Mac Studio Host, an die Stromversorgung angeschlossen und immer eingeschaltet, ist mein Hauptserver. Er ist für Clients aus dem öffentlichen Netzwerk durch Intranet-Penetration zugänglich. Wenn ich zu Hause arbeite oder studiere, kann er auch als Client verwendet werden, um sich mit anderen Server-Hosts zu verbinden, wenn er an einen Bildschirm und eine Tastatur/Maus angeschlossen ist.
2. Raspberry Pi, mit Ubuntu-System installiert als Hauptservice-Lauf- und Debugging-Umgebung, hauptsächlich für den Betrieb einiger Dienste, für Clients aus dem öffentlichen Netzwerk durch Intranet-Penetration zugänglich.
3. Persönlicher Alibaba Cloud ECS, Tencent Cloud Lightweight Server oder andere vom Unternehmen bereitgestellte Projektentwicklungsumgebungen, hauptsächlich für den Betrieb und das Debugging einiger Projektdienste, wie z.B. Chain-Umgebungen.
4. GitHub Codespaces, am internen Test teilgenommen. GitHub stellt Laufzeitumgebungen für bis zu 10 persönliche Projekte bereit. Ich verwende es hauptsächlich für die Entwicklung von Solidity-, Rust- oder Frontend-Lernprojekten. Auf diese Weise kann ich eine konsistente Umgebung sicherstellen, wenn ich mich von verschiedenen Maschinen oder sogar Browsern aus verbinde, ohne sie selbst neu konfigurieren und einrichten zu müssen. Aus Sicherheitsüberlegungen werde ich jedoch keine Arbeitsprojekte oder einige Projekte mit persönlichen sensiblen Informationen ausführen.

### Meine Erfahrung mit der Thin-Client-Entwicklung

Der Thin Client ist nicht nur eine Optimierung von Werkzeugen und Techniken; seine ursprüngliche Absicht ist eine Art "Minimalismus" im Arbeitsmodus. Nach mehrmonatiger Praxis dieses Entwicklungsmodus kann ich deutlich spüren, dass die Zeit, die ich für das Debugging und die Wartung der Entwicklungsumgebung aufwende, abgenommen hat, und ich mehr Aufmerksamkeit auf den Code und die Dienste selbst gelegt habe. Das nahtlose Umschalten zwischen den Modi "sofortige Verwendung" und "bei Bedarf" ermöglicht es mir auch, jederzeit Arbeitszustände und Projekte zu wechseln, was die Zeitkosten wie Umgebungs-Kaltstart und Konfiguration erheblich reduziert.

Obwohl ich meine eigene Verfolgung der Software- und Hardware-Benutzererfahrung habe, bin ich keine Person, die in allen Aspekten Extreme verfolgt. Stattdessen folge ich einer "Just Enough"-Philosophie, die meine aktuellen Nutzungsbedürfnisse befriedigt. Zum Beispiel habe ich in Bezug auf die Netzwerkumgebung zu Hause nur eine gewöhnliche 100M-Breitbandnetzwerkumgebung und habe nicht absichtlich an Bandbreite und Routern herumgebastelt. Insgesamt ist die Netzwerklatenz während des Betriebs, sei es bei der Tastatureingabe oder beim Erhalten von Echtzeitanzeigen, fast vernachlässigbar (mein Hauptnutzungsszenario ist die Verwendung von VS Code Remote oder iTerm2-Terminal-Tool auf macOS-System, um über SSH eine Verbindung zu Remote-Hosts oder Servern für die Entwicklung herzustellen, und gelegentlich die Verwendung der SFTP-Funktion von Termius für die Dateiübertragung, als Referenz). Es gibt fast keine Unterbrechungen aufgrund der Netzwerkumgebung.

Ich habe VNC nur für die Remote-Desktop-Steuerung bei der Konfiguration des Raspberry Pi verwendet und keine anderen Operationen durchgeführt, die stark von der grafischen Benutzeroberfläche abhängig sind. Die Netzwerklatenz ist akzeptabel, aber nicht sehr empfehlenswert.

## Anforderungsanalyse für den Fernzugriff auf das Netzwerk

![raspberry_pi](https://image.pseudoyu.com/images/raspberry_pi.jpg)

Bezüglich der Schemata und Prinzipien des Fernzugriffs auf das Netzwerk hat der Artikel ["Leitfaden für den Fernzugriff auf LAN"](https://sspai.com/prime/story/remote-lan-access-guide-01) auf Sspai bereits verschiedene Schemata detailliert und bewertet. Ich berücksichtige nur die Benutzerfreundlichkeit und die Kosten des Schemas gemäß den persönlichen Bedürfnissen. Sie können selbst lesen und das geeignete Schema auswählen.

Zunächst habe ich die Netzwerkbedingungen und Anforderungen sortiert.

Netzwerkbedingungen:

1. Kurzfristig eingerichtetes Breitband für die Miete, keine öffentliche IP bereitgestellt, eine zu beantragen ist wahrscheinlich sehr umständlich.
2. Der Heim-WLAN-Router scheint nur ein gewöhnlicher Xiaomi-Router zu sein, habe nicht viel daran herumgebastelt.
3. Aufgrund von Arbeits- und persönlichen Entwicklungsbedürfnissen habe ich langfristig Server auf Alibaba Cloud und Tencent Cloud erneuert, mit öffentlichen IPs.

Anforderungen an die Fernverbindung:

1. Zugriff auf den Mac Studio Host über SSH durch das öffentliche Netzwerk und bei Bedarf Öffnung spezifischer Ports.
2. Zugriff auf den Raspberry Pi über SSH durch das öffentliche Netzwerk und bei Bedarf Öffnung spezifischer Ports.
3. Erfordert eine stabile und schnelle Verbindung und versucht, bestehende Software und Dienste wiederzuverwenden, um zusätzliche Kosten zu vermeiden.
4. Einfach zu erweitern für neue Geräte (wie den Kauf neuer Raspberry Pis) und zur Konfiguration neuer Port-Mappings (Öffnung neuer Dienste).
5. Da das Heimnetzwerk vollständig von Surge als Software-Router verwaltet wird, wurden bereits Konfigurationen wie das Schließen von DHCP vorgenommen, also versuchen Sie, keine Konfigurationen auf der Ebene des optischen Modems und Routers vorzunehmen.
6. Fähigkeit, den Verbindungsstatus der Heimnetzwerkumgebung und den Ressourcenstatus des Raspberry Pi-Servers in Echtzeit zu überwachen.

## frp Intranet-Penetrationslösung

Nach einigen Recherchen habe ich mich für das Open-Source-Projekt ["GitHub - fatedier/frp"](https://github.com/fatedier/frp) entschieden. Laut seiner offiziellen Dokumentation:

> frp ist eine leistungsstarke Reverse-Proxy-Anwendung, die sich auf Intranet-Penetration konzentriert. Es unterstützt mehrere Protokolle wie TCP, UDP, HTTP, HTTPS. Es kann Intranet-Dienste sicher und bequem über Knoten mit öffentlicher IP in das öffentliche Netzwerk exponieren. Durch die Bereitstellung des frp-Servers auf Knoten mit öffentlicher IP können Intranet-Dienste leicht in das öffentliche Netzwerk durchdrungen werden, während viele professionelle Funktionen bereitgestellt werden.

Dies erfüllt perfekt meine Bedürfnisse. Ich muss nur meinen gekauften Alibaba Cloud Server mit öffentlicher IP als Transitserver wiederverwenden, den frp-Server bereitstellen, die entsprechenden Ports exponieren, den frp-Client auf Heimgeräten bereitstellen, die vom öffentlichen Netzwerk aus zugänglich sein müssen, und Port-Mapping durchführen, um Intranet-Penetration zu erreichen.

### Lösungsarchitektur

![frp_structure](https://image.pseudoyu.com/images/frp_structure.png)

Zunächst habe ich den frp-Server auf meinem Server mit öffentlicher IP bereitgestellt und die entsprechenden Ports exponiert.

In meiner Heimintranet-Umgebung gibt es hauptsächlich zwei Geräte, die immer an die Stromversorgung angeschlossen und eingeschaltet sind, ein Mac Studio Host und ein Raspberry Pi Server mit Ubuntu-Betriebssystem, die hauptsächlich über Netzwerkkabel/WLAN mit dem WLAN-Router verbunden sind. Ich habe den frp-Client auf beiden Maschinen gemäß den offiziellen Anweisungen installiert und ausgeführt, konfiguriert, um eine Verbindung zum frp-Server herzustellen, und die Dienstports gemappt, die geöffnet werden müssen (wie z.B. das Mapping des SSH-Dienstports 22 des Raspberry Pi auf Port 6002 des Alibaba Cloud Servers). Erwähnenswert ist, dass der frp-Client aktiv Anfragen an den Server sendet, sodass keine Neukonfiguration erforderlich ist, selbst wenn sich die Netzwerkumgebung ändert, solange seine Netzwerkumgebung auf den Transitserver zugreifen kann, auf dem der frp-Server installiert ist.

An diesem Punkt kann mein Alibaba Cloud Transitserver unsere Intranet-Umgebung und -Dienste der öffentlichen Netzwerkumgebung zugänglich machen. Wenn ich im Büro bin, kann ich über das öffentliche Netzwerk des Alibaba Cloud Servers + den entsprechenden Dienstport mit einem Laptop, Tablet oder Telefon darauf zugreifen, z.B. um über das Terminal eine Remote-SSH-Verbindung zum Mac Studio für Entwicklungsarbeiten herzustellen.

Gleichzeitig wollen wir den Status der Heimnetzwerkumgebung und der beiden Hosts in Echtzeit für Wartungszwecke überwachen. Ich habe den Surge macOS-Client als Software-Router verwendet, um alle Geräte im Heimnetzwerk zu verwalten, und die Cloud-Benachrichtigungsfunktion des Surge iOS-Clients genutzt, um den Status des Heimnetzwerks in Echtzeit zu überwachen. Darüber hinaus habe ich die ServerCat-Software verwendet, um die Ressourcen des Raspberry Pi-Servers zu Hause zu überwachen, sogar bis hin zur Temperatur, was sich nicht von der Cloud-Server-Erfahrung unterscheidet.

![servercat_monitor_raspberry_pi](https://image.pseudoyu.com/images/servercat_monitor_raspberry_pi.png)

Die Konfiguration von frp ist relativ einfach, folgen Sie einfach der offiziellen Dokumentation. Mein Konfigurationsprozess ist wie folgt.

### frp Server-Konfiguration

Meine Alibaba Cloud ist mit dem CentOS-Betriebssystem installiert, andere Linux-Distributionen sind ähnlich.

#### Service-Installation und -Konfiguration

Melden Sie sich zunächst am Terminal des Alibaba Cloud Servers an und installieren und laden Sie das frp-Programm über die folgenden Befehle herunter (beachten Sie, dass Sie die Version herunterladen müssen, die Ihrem Betriebssystem entspricht, von der [Releases](https://github.com/fatedier/frp/releases)-Seite des ["GitHub - fatedier/frp"](https://github.com/fatedier/frp)-Projekts), entpacken Sie es und wechseln Sie in das Verzeichnis.

```bash
wget https://github.com/fatedier/frp/releases/download/v0.43.0/frp_0.43.0_linux_amd64.tar.gz
tar -zxvf frp_0.43.0_linux_amd64.tar.gz
cd frp_0.43.0_linux_amd64/
```

Die `frps` und `frps.ini` sind die Dateien, auf die wir uns konzentrieren müssen. `frps` ist das Serverprogramm, während `frps.ini` die entsprechende Konfigurationsdatei ist. Wir verwenden `vi frps.ini`, um die Konfigurationsdatei zu bearbeiten:

```plaintext
[common]
bind_port = 7000
dashboard_port = 7002
token = password
dashboard_user = admin
dashboard_pwd = 123456
vhost_http_port = 8080
```

Da ich den Betrieb unseres frp-Dienstes über die Konsole visualisieren möchte, habe ich auch dashboard-bezogene Parameter konfiguriert, die Sie nach Ihren eigenen Bedürfnissen wählen können. Speichern oder merken Sie sich diese Konfiguration, da sie später benötigt wird, wenn der frp-Client eine Verbindung zum Server herstellt. Nach dem Speichern der Konfiguration können Sie den Server mit `./frps -c frps.ini` starten.

Natürlich müssen wir es so konfigurieren, dass es automatisch startet und im Hintergrund läuft, um zu vermeiden, dass wir bei jedem Neustart des Servers neu konfigurieren müssen.

```bash
vi /lib/systemd/system/frps.service
```

Fügen Sie den folgenden Inhalt hinzu und speichern Sie ihn, beachten Sie, dass Sie die Pfade von `frps` und `frps.ini` zu Ihren tatsächlichen Pfaden ändern müssen.

```plaintext
[Unit]
Description=frps service
After=network.target syslog.target
Wants=network.target

[Service]
Type=simple
ExecStart=/path/to/frps -c /path/to/frps.ini

[Install]
WantedBy=multi-user.target
```

#### Service-Start und Konfiguration des automatischen Starts beim Booten

Nach Abschluss der Konfiguration können Sie den Server mit `systemctl start frps` starten.

Wir geben den folgenden Befehl in der Befehlszeile ein, um den Dienst so zu konfigurieren, dass er beim Booten automatisch startet:

```bash
systemctl enable frps
```

An diesem Punkt ist unsere Serverkonfiguration abgeschlossen.

### frp Client-Konfiguration

#### Service-Installation und -Konfiguration

Die frp-Client-Konfiguration ähnelt der Serverkonfiguration. Laden Sie die entsprechende Version des frp-Programms über den `wget`-Befehl herunter, entpacken Sie es und wechseln Sie in das Verzeichnis.

```bash
wget https://github.com/fatedier/frp/releases/download/v0.43.0/frp_0.43.0_linux_amd64.tar.gz
tar -zxvf frp_0.43.0_linux_amd64.tar.gz
cd frp_0.43.0_linux_amd64/
```

Die `frpc` und `frpc.ini` sind die Dateien, auf die wir uns konzentrieren müssen. `frpc` ist das Client-Programm, während `frpc.ini` die entsprechende Konfigurationsdatei ist. Wir verwenden `vi frpc.ini`, um die Konfigurationsdatei zu bearbeiten:

```plaintext
[common]
server_addr = 114.114.114.114
server_port = 7000
token = password

[pi]
type = tcp
local_ip = 127.0.0.1
local_port = 22
remote_port = 6001
```

Die `server_addr` und `server_port` hier müssen mit der tatsächlichen öffentlichen IP und dem Port des Transitservers ausgefüllt werden, und `token` muss mit dem zuvor konfigurierten Token ausgefüllt werden; darunter befindet sich die Port-Mapping-Konfiguration für den Dienst, den Sie verbinden müssen, `local_ip` und `local_port` müssen mit der lokalen IP und dem Port des Clients ausgefüllt werden, wie z.B. `127.0.0.1` und `22`, wenn Sie den SSH-Dienst aktivieren müssen, während der letzte `remote_port` das Port-Mapping dieses Ports im Transitserver ist.

#### Service-Start und Konfiguration des automatischen Starts beim Booten

##### Ubuntu

Im Ubuntu-System des Raspberry Pi erstellen oder bearbeiten wir die fprc-Dienstkonfigurationsdatei über `vi /etc/systemd/system/frpc.service`, fügen den folgenden Inhalt hinzu und speichern ihn. Ähnlich müssen Sie `fprc` und `fprc.ini` zu Ihren tatsächlichen Pfaden ändern.

```plaintext
[Unit]
Description=frpc daemon
After=syslog.target  network.target
Wants=network.target

[Service]
Type=simple
ExecStart=/path/to/frpc -c /path/to/frpc.ini
Restart= always
RestartSec=1min
ExecStop=/usr/bin/killall frpc

[Install]
WantedBy=multi-user.target
```

Nach Abschluss der Konfiguration aktivieren Sie den automatischen Dienststart mit `sudo systemctl enable frpc.service` und starten den Client-Dienst mit `sudo systemctl start frpc.service`.

##### macOS

Im macOS-System bearbeiten wir die plist über `vi ~/Library/LaunchAgents/frpc.plist`, um den automatischen Dienststart hinzuzufügen. Ähnlich müssen Sie `fprc` und `fprc.ini` zu Ihren tatsächlichen Pfaden ändern.

```plaintext
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC -//Apple Computer//DTD PLIST 1.0//EN
http://www.apple.com/DTDs/PropertyList-1.0.dtd >
<plist version="1.0">
<dict>
<key>Label</key>
<string>frpc</string>
<key>ProgramArguments</key>
<array>
<string>/path/to/frpc</string>
<string>-c</string>
<string>/path/to/frpc.ini</string>
</array>
<key>KeepAlive</key>
<true/>
<key>RunAtLoad</key>
<true/>
</dict>
</plist>
```

An diesem Punkt können wir in der öffentlichen Netzwerkumgebung über die entsprechenden Ports des Transitservers auf unsere Intranet-Dienste zugreifen, und die Dienste starten automatisch beim Booten, sowohl auf der Serverseite als auch auf der Clientseite. Wir können auf die frp-Konsole über `<öffentliche IP>` + den `dashboard_port`-Port zugreifen, den wir gerade auf der Serverseite konfiguriert haben, um die Verkehrssituation jedes Dienstes zu sehen.

![frp_dashboard](https://image.pseudoyu.com/images/frp_dashboard.png)

## Fazit

Das oben Genannte ist meine Praxis und Zusammenfassung des öffentlichen Netzwerk-Fernzugriffs auf Heimgeräte und des Thin-Client-Workflows. Dies bringt eine interessante Entwicklungserfahrung, die sich vom traditionellen Modus unterscheidet. Interessierte Leser können es selbst ausprobieren. Ich hoffe, dieser Artikel ist für Sie hilfreich.

## Referenzen

> 1. [GitHub - fatedier/frp](https://github.com/fatedier/frp)
> 2. [Teahour #95 - Wie ist es, auf einem Chromebook zu entwickeln?](https://teahour.fm/95)