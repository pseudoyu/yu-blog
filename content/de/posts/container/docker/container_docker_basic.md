---
title: "Docker Grundlagen und Praktiken"
date: 2022-09-07T01:30:48+08:00
draft: false
tags: ["container", "docker", "devops", "programming", "work practice series", "work", "practice", "backend"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《后来的我们 - 五月天》" >}}

## Vorwort

Dies ist der erste Artikel im Container-Abschnitt der Arbeitspraxis-Serie, der hauptsächlich die Grundlagen und Praktiken von Docker vorstellt.

Als Backend-Entwickler habe ich zu Beginn meiner Karriere hauptsächlich lokal debuggt und hatte noch keine wirklichen Erfahrungen mit der Verwendung von Docker gemacht. Erst später, als ich mich mit komplexeren Entwicklungen im Bereich der zugrunde liegenden Blockchain beschäftigte, stieß ich auf Probleme. Aufgrund der komplizierten Abhängigkeitsbeziehungen von Blockchains oder deren zugehörigen Tools sowie Versionskonflikten wurde es notwendig, jedes Mal komplexe Umgebungen auf lokalen Maschinen oder Servern zu konfigurieren. Darüber hinaus mussten viele Dienste und Konfigurationen nach jedem Neustart neu bereitgestellt werden, was den Prozess umständlich und anfällig für unerklärliche plattformübergreifende Fehler machte.

Daher begann ich nach und nach, den Ansatz zu verfolgen, projektspezifische Dockerfiles zu schreiben und Images für die anschließende Entwicklung und Fehlersuche zu kompilieren. Bereitstellungsmaschinen mussten nur die Docker-Umgebung (und Docker Compose) installieren, ohne dass verschiedene Abhängigkeiten lokal installiert werden mussten, was sehr praktisch war. Später konfigurierten wir zusammen mit meinem Teamleiter den CI/CD-Prozess des Projekts basierend auf Docker-Images, GitLab CI und der k8s-Umgebung, was die Entwicklungs- und Debugging-Effizienz erheblich verbesserte.

Dieser Artikel fasst Docker-bezogene Konzepte und Praktiken auf der Grundlage dieser Erfahrungen zusammen und hofft, in gewisser Weise hilfreich zu sein.

## Einführung in Docker

Die von uns entwickelten Dienste laufen oft als Binärdateien im Betriebssystem, während Docker eine Container-Technologie ist, die unsere Anwendung und zugehörige Abhängigkeiten in einem Container verpackt. Container basieren in der Regel auf einem leichtgewichtigen Linux-Image und sind ein Stapel mehrerer Bildebenen. Unsere Anwendung befindet sich normalerweise in der obersten Schicht, und diese Abhängigkeitsbeziehungen werden im Dockerfile spezifiziert.

Die Verwendung von Containern für die Bereitstellung hat viele klare Vorteile gegenüber der Bereitstellung auf lokalen Maschinen oder Remote-Servern.

1. Keine Notwendigkeit, verschiedene Umgebungen und Abhängigkeiten im Betriebssystem zu installieren (außer Docker selbst). Wenn wir den ursprünglichen Dienststartmodus übernehmen würden, würde der Entwicklungsprozess sehr umständlich werden und ständige Kommunikation zwischen Entwicklern und Betrieb erfordern, um die Umgebungskonfiguration und Bereitstellung abzuschließen. Darüber hinaus ist es sehr leicht, Abhängigkeits-/Versionskonflikte zu verursachen, wenn mehrere Dienste auf einer Maschine bereitgestellt werden.

2. Kann unabhängige Bereitstellungsumgebungen haben. Wir erstellen Images, indem wir Dockerfiles für verschiedene Projekte schreiben und die für die Anwendung erforderliche Umgebung und Abhängigkeiten im Image verpacken. Dies macht es bequem, verschiedene Versionen derselben Anwendung auszuführen oder mehrere Instanzen gemeinsamer Dienste wie MySQL auszuführen. Diese können über Docker-Befehle oder Docker Compose-Befehle verwaltet werden, was einen Start/Pause mit einem Klick ermöglicht.

3. Docker ist nicht stark von der Version des Betriebssystems selbst abhängig. Dasselbe Docker-Image kann auf verschiedenen Betriebssystemen (Windows, macOS, verschiedene Linux-Distributionen) ausgeführt werden, was die Dienstefreigabe, Migration und plattformübergreifende Bereitstellung erleichtert.

4. Im Vergleich zu virtuellen Maschinen haben Docker-Container keinen Kernel und enthalten nur die Anwendungsschicht, was sie kleiner in der Größe, schneller beim Start und leichtgewichtiger macht.

Natürlich ist die Kompatibilität von Docker-Containern im Vergleich zu Betriebssystemen und virtuellen Maschinen relativ schlechter. Zum Beispiel können VMs jedes andere Betriebssystem ausführen und spezifischere Bedürfnisse erfüllen.

## Grundlegende Docker-Operationen

### Installation von Docker

Die Installation von Docker ist einfach. Laden Sie das Installationspaket für Ihr Betriebssystem von der [offiziellen Website](https://www.docker.com) herunter und folgen Sie den Anweisungen zur Installation.

#### macOS

Für mein persönliches macOS-System habe ich zunächst [Docker Desktop](https://www.docker.com/products/docker-desktop/) installiert, das die Verwaltung von Images und Containern über eine grafische Benutzeroberfläche ermöglicht. Es ist praktisch, verbraucht aber mehr Ressourcen und ist energieintensiv.

Später habe ich [Colima](https://github.com/abiosoft/colima) ausprobiert, eine relativ leichtgewichtige Container-Laufzeitumgebung. Es ist sehr praktisch für lokales Debugging auf macOS-Systemen. Ich empfehle, es zu verwenden. Sie können die Umgebung gemäß der offiziellen Dokumentation des Projekts installieren und konfigurieren. Ich habe es direkt mit dem `brew` Paketmanagement-Tool installiert:

```bash
brew install colima
```

Nach der Installation führen Sie `colima start` aus, um den Container zu starten, und `colima stop`, um den Container zu stoppen. Weitere Befehle können Sie über `colima --help` einsehen.

Ich habe meine übliche Entwicklungsumgebung mit dem folgenden Befehl gestartet, den Sie nach Ihren eigenen Bedürfnissen konfigurieren können:

```bash
colima start -c 8 -m 16 -a x86_64 -p docker-amd
```

#### CentOS

Im Vergleich zur lokalen Entwicklung wird Docker häufiger für die Bereitstellung von Anwendungen auf Servern verwendet. Mein häufig verwendetes Betriebssystem ist `CentOS 7`, das über das `yum` Paketmanagement-Tool installiert werden kann:

```bash
yum install -y yum-utils device-mapper-persistent-data lvm2
yum-config-manager  --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum install docker-ce
```

Nach der Installation starten Sie den Docker-Dienst und konfigurieren ihn so, dass er beim Systemstart automatisch gestartet wird:

```bash
systemctl enable docker
systemctl start docker
```

### Docker Images

Docker hat hauptsächlich zwei Konzepte: Images und Container. Ein Image kann als Vorlage für einen Container betrachtet werden, der über ein Dockerfile kompiliert wurde, während ein Container eine Instanz eines Images ist.

#### Dockerfile

Wir verwenden Dockerfile, um die für die Anwendung erforderliche Umgebung und Abhängigkeiten zu spezifizieren. Das grundlegende Format sieht wie folgt aus:

```dockerfile
FROM <image>

ENV USERNAME=admin \
    PASSWORD=123456

RUN mkdir -p <app-directory>

COPY . /<app-directory>

CMD ["<command>", "<entrypoint file>"]
```

Nach Abschluss des Dockerfiles können wir das Image mit dem Befehl `docker build` im gleichen Verzeichnis erstellen (oder das Dockerfile angeben):

```bash
# Image erstellen
docker build -t <image:tag> .
```

#### Speichern und Laden von Images

Wir können lokal kompilierte Images als `tar`-Pakete für die Weitergabe speichern:

```bash
docker save -o <image-name>.tar <image-name>
```

Wenn wir das Image verwenden müssen, können wir das tar-Paket mit dem Befehl `docker load` laden:

```bash
docker load -i <image-name>.tar
```

#### Hochladen und Herunterladen von Images

Natürlich ist die Weitergabe über Image-`tar`-Pakete nicht so bequem, und einige Images können sehr groß sein, was die Übertragung erschwert. Daher können wir den Befehl `docker push` verwenden, um Images in das offizielle Image-Repository oder Unternehmens-/persönliche private Repositories (wie das Projekt, an dem ich arbeite, verwendet Harbor zur Verwaltung von Images) zu übertragen, und den Befehl `docker pull` zum Herunterladen verwenden.

```bash
# Offizielles Image herunterladen (Kurzform)
docker pull <image:tag>

# Offizielles Image herunterladen (vollständiger Befehl)
docker pull docker.io/library/<image:tag>

# Image in offizielles Image-Repository Docker Hub hochladen
docker push <image:tag>

# Image in privates Repository hochladen (Authentifizierung erforderlich)
docker tag <image:tag> <private-repo-path>/<image:tag>
docker push <private-repo-path>/<image:tag>
```

#### Docker Image-Operationen

Für Docker-Images sind die Operationen, die ich häufig verwende, das Anzeigen, Löschen und Umbenennen von Tags. Weitere Befehle können Sie über `docker image --help` oder auf der offiziellen Website einsehen.

```bash
# Alle Images anzeigen
docker images

# Image löschen
docker rmi <image:tag>

# Image umbenennen
docker tag <old-image:tag> <new-image:tag>
```

### Container-Operationen

#### Anzeigen von Containern

Nachdem wir ein Image über Docker- oder Docker Compose-Befehle gestartet haben, können wir den Dienststatus über die folgenden Befehle anzeigen:

```bash
# Laufende Container anzeigen
docker ps

# Alle Container anzeigen
docker ps -a
```

#### Starten/Stoppen von Instanzen aus Images

Nachdem wir das erforderliche Image über Dockerfile kompiliert haben, können wir eine Image-Instanz über den Befehl `docker run` starten und einige Konfigurationen im Befehl hinzufügen, um unsere Dienstanforderungen zu erfüllen. Meine üblichen Operationen sind wie folgt:

```bash
# Container ausführen
docker run <image:tag>

# Container ausführen und Namen angeben
docker run --name <server-name> <image:tag>

# Container im Hintergrundmodus ausführen
docker run -d <image:tag>

# Port-Mapping
docker run -p6000:6379 <image:tag>

# Umgebungsvariablen konfigurieren
docker run -e USERNAME=admin -e PASSWORD=123456 <image:tag>
```

#### Starten/Stoppen von Container-Diensten

Nachdem wir eine Instanz aus einem Image erstellt haben, können wir den Container-Dienst über die folgenden Befehle starten/stoppen:

```bash
# Container starten/neu starten
docker start <container-id>

# Container anhalten
docker stop <container-id>
```

#### Anzeigen von Logs

Nachdem wir einen Dienst über Docker gestartet haben, müssen wir oft seine Ausführungsprotokolle zur Fehlersuche einsehen. Wir können sie über `docker logs` anzeigen, mit spezifischen Befehlen wie folgt:

```bash
# Logs anzeigen
docker logs <container-id>

# Logs im Folgemodus anzeigen
docker logs -f <container-id>
```

#### Betreten von Containern

Manchmal müssen wir für die Dienstinspektion und Fehlersuche intern in den Docker-Container-Dienst eintreten. Wir können über den Befehl `docker exec` in den Container eintreten, mit spezifischen Befehlen wie folgt:

```bash
# Bestimmten Container nach ID betreten
docker exec -it <container-id> <command>
```

#### Docker-Netzwerk

Docker-Container-Instanzen laufen innerhalb eines Netzwerks. In unseren vorherigen Befehlen haben wir kein Netzwerk angegeben, sodass die Dienste unter dem Standardnetzwerk laufen werden. Wir können Netzwerke über den folgenden Befehl anzeigen:

```bash
# Alle Netzwerke anzeigen
docker network ls
```

Wenn wir nicht im Standardnetzwerk laufen möchten, können wir ein benutzerdefiniertes Netzwerk über den folgenden Befehl erstellen:

```bash
# Benutzerdefiniertes Netzwerk erstellen
docker network create <network-name>
```

Nachdem wir unser benutzerdefiniertes Netzwerk erstellt haben, können wir das Netzwerk beim Erstellen von Container-Instanzen über den Parameter `--network` angeben:

```bash
docker run --network <network-name> <image:tag>
```

#### Docker-Datenpersistenz

Nach dem Ausführen von Diensten mit Docker-Instanzen werden unsere Daten in den Containern gespeichert. Wenn die Container gelöscht werden, werden auch die Daten gelöscht, was bei einigen Diensten, die längere Zeit laufen müssen, zu Datenverlust führen kann. Daher müssen wir die Daten persistieren. Ich verwende üblicherweise Host-Montage und Container-Montage.

Wir können die Persistenz erreichen, indem wir ein bestimmtes Verzeichnis der Host-Maschine in ein Verzeichnis innerhalb des Containers einbinden:

```bash
# Host-Verzeichnis in Container-Verzeichnis einbinden
docker run -v <host-file-path>:<container-file-path> <image:tag>
```

Wir können auch Container-Montage verwenden und Volumes zur Persistenz nutzen:

```bash
# Sie können auf das Volume über den Namen verweisen
# Docker generiert automatisch einen Pfad
# Windows: C:\ProgramData\docker\volumes
# Linux: /var/lib/docker/volumes
# macOS: /var/lib/docker/volumes
docker run -v <volume-name>:<container-file-path> <image:tag>
```

Wenn wir nur einbinden müssen und keine spezifische Dateiverwaltung oder -anzeige benötigen, können wir auch die anonyme Container-Montage verwenden, ohne einen Volume-Namen anzugeben, sondern das automatisch generierte Verzeichnis verwenden:

```bash
# Docker generiert automatisch einen Pfad
# Windows: C:\ProgramData\docker\volumes
# Linux: /var/lib/docker/volumes
# macOS: /var/lib/docker/volumes
docker run -v <container-file-path> <image:tag>
```

## Docker Compose

Docker bietet uns umfangreiche Befehle zur Verwendung, aber die Verwendung von Befehlszeilenoperationen ist nicht einfach zu merken, und wenn eine Anwendung von mehreren Umgebungen/Diensten abhängt, erfordert es das separate Ausführen und Verwalten mehrerer Container, was Unannehmlichkeiten verursacht. Daher können wir das Docker Compose-Tool zur Verwaltung verwenden.

Docker Compose ist ein Tool zum Definieren und Ausführen von Multi-Container-Docker-Anwendungen, das `.yaml`-Dateien zur Konfigurationsverwaltung verwendet. In meiner täglichen Arbeit verwende ich Docker Compose am häufigsten und verwende den `docker run`-Befehl nur zum Starten sehr einfacher Anwendungen, was auch für die einheitliche Verwaltung und nachfolgende Konfigurationsanpassungen praktisch ist.

### Installation

Wenn Sie Docker Desktop auf macOS installiert haben, enthält es bereits Docker Compose, das direkt verwendet werden kann. Wenn es sich um ein Linux-System handelt, muss es separat installiert werden. Hier nehme ich `CentOS 7` als Beispiel:

```bash
curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

Nach der Installation können Sie den Befehl `docker-compose` verwenden.

### Konfigurationsverwaltung

Die Konfigurationsdatei für Docker Compose ist eine `yaml`-Datei, deren Grundformat wie folgt aussieht:

```yaml
version: '3'
services:
	container-1:
    	image: <image-name>
        ports:
        	- <host>:<container>
        volumes:
        	- <host-file-path>:<container-file-path>
        environment:
        	<ENV-KEY>=<ENV-VALUE>
    container-2:
    	image: <image-name>
        ports:
        	- <host>:<container>
        volumes:
        	- <volume-name-1>:<container-file-path>
        environment:
        	<ENV-KEY>=<ENV-VALUE>
volumes:
	volume-name-1:
    	driver: local
```

Die meisten Konfigurationen sind intuitiv, wie Dienstname, Image-Name, Port-Mapping, Dateimontage, Umgebungsvariablen usw.

Dabei repräsentiert `version` die Version der Konfigurationsdatei, `services` die Liste der Dienste und `volumes` die Liste der eingebundenen Volumes.

In spezifischen `services` repräsentiert `image` den Image-Namen, `ports` das Port-Mapping, `volumes` die Dateimontage, `environment` die Umgebungsvariablen. Weitere Konfigurationen können je nach Projektanforderungen eingesehen werden.

### Häufige Befehle

#### Starten/Stoppen von Diensten

Ähnlich wie der Befehl `docker run` bietet Docker Compose auch die Befehle `up` und `down` zum Starten und Stoppen von Diensten.

```bash
# Dienst starten
docker-compose -f <name>.yaml up

# Dienst im Hintergrundmodus starten
docker-compose -f <name>.yaml up -d

# Dienst stoppen
docker-compose -f <name>.yaml down
```

#### Anzeigen von Logs

Wir können Dienstprotokolle über den Befehl `logs` anzeigen.

```bash
# Logs anzeigen
docker-compose logs <container-id>

# Logs im Folgemodus anzeigen
docker-compose logs -f <container-id>
```

## Praktische Betriebsbefehle

Zusätzlich zu den oben genannten grundlegenden Befehlen verwende ich oft die folgenden häufigen Befehle.

### Bereinigung nicht verwendeter Container

Wenn unsere Container-Instanzen aufgrund von Konfigurations- oder Programmlaufzeitfehlern beendet werden, werden sie weiterhin beibehalten. Wir können sie über den Befehl `docker ps -a` anzeigen. Wir können sie über den folgenden kombinierten Befehl bereinigen:

```bash
docker rm `docker ps -a | grep Exited | awk '{print $1}'`
```

### Massenimport lokaler Images

Wenn wir eine große Anzahl lokaler Images in eine Maschine importieren müssen, wäre es sehr umständlich, sie einzeln zu importieren. Wir können die Images in dasselbe Verzeichnis legen und den folgenden Befehl für den Massenimport verwenden:

```bash
for i in `ls`; do docker load < $i ; done
```

## Fazit

Das oben Genannte ist meine Erklärung der Grundlagen und praktischen Operationen der Docker-Container-Technologie. Ich hoffe, es ist für Sie hilfreich. Tatsächlich gibt es noch viel mehr Inhalt über Docker. Zum Beispiel haben wir im vorherigen Projekt versucht, Dockers `Buildkit`-Funktion zu verwenden, die die Größe des endgültig erstellten Images drastisch reduzierte, und `buildx` verwendet, um plattformübergreifende Kompatibilität zu erreichen, usw. Dieser Artikel zielt darauf ab, Grundkenntnisse und häufig verwendete Befehle in der Praxis zu erklären. Wenn Sie an diesen erweiterten Teilen interessiert sind, werde ich sie später aktualisieren.

## Referenzen

> 1. [Docker Offizielle Website](https://www.docker.com)
> 2. [Docker Tutorial für Anfänger](https://www.youtube.com/watch?v=3c-iBn73dDE)