---
title: "Aufbau eines Website-Analysesystems mit GoatCounter und Zeabur"
date: 2024-08-06T19:00:42+08:00
draft: false
tags: ["statistic-system", "serverless", "zeabur", "blog", "goatcounter"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

## Vorwort

In meinem Artikel "[Was hat sich in meinem Blog 2024 geändert](https://www.pseudoyu.com/en/2024/06/29/what_changed_in_my_blog_2024/)" habe ich das von mir aufgebaute Blog-System unter Verwendung von Serverless-Plattformen und einigen Open-Source-Projekten vorgestellt. Ich habe auch diese Reihe von Tutorials begonnen, um den gesamten Prozess der Einrichtung und Bereitstellung zu dokumentieren.

Dieser Artikel konzentriert sich auf die Lösung des Analysesystems.

## Lösung für das Analysesystem

Im Vergleich zum Blog selbst und dem Kommentarsystem hatte ich lange Zeit kein Augenmerk auf ein Analysesystem gelegt (~~hauptsächlich, weil es damals nicht viele Leser gab~~). Ich hatte nicht viel über SEO oder andere Werbemaßnahmen nachgedacht. Allerdings entdeckte ich nach und nach, dass die gesammelten Daten nicht nur ein hübsches Diagramm für Twitter sind; sie haben einen großen Referenzwert für die Auswahl von Blog-Themen und -Inhalten.

Tatsächlich können ausgereifte Mainstream-Lösungen die grundlegenden Bedürfnisse erfüllen. Selbst das kostenlose Google Analytics ist mehr als ausreichend. Während der Entwicklung meines Blogs durchlief ich jedoch aus verschiedenen Gründen mehrere Iterationen und entschied mich schließlich für GoatCounter als meine Lösung.

### splitbee

Anfangs verwendete ich ein kostenloses Tool namens splitbee. Es bot ein kostenloses Grundkontingent für Analysen, hatte eine schöne Benutzeroberfläche und unterstützte komplexes Benutzer-Tracking, A/B-Tests usw. Aber soweit ich mich erinnere, behielt es die Daten nur für ein halbes Jahr und erforderte ein Upgrade nach Überschreiten von 5000 Seitenaufrufen pro Monat, weshalb ich es später aufgab.

### Cloudflare + Google Search Console

![cloudflare_web_stats](https://image.pseudoyu.com/images/cloudflare_web_stats.png)

Nachdem ich splitbee aufgegeben hatte, integrierte ich lange Zeit keine zusätzlichen Analyse-Anwendungen. Stattdessen nutzte ich die eingebauten Website-Statistiken von Cloudflare. Allerdings stellte ich fest, dass diese nur den gesamten Netzwerkverkehr verfolgten, einschließlich vieler ineffektiver Daten wie Crawler, und Details bis zur Pfadebene fehlten.

![google_search_console](https://image.pseudoyu.com/images/google_search_console.png)

Später, nachdem ich das Konzept von SEO kennengelernt hatte, fügte ich [Google Search Console](https://search.google.com/search-console/about) als eine weitere Analysedimension hinzu. Dies sind derzeit die Daten, die ich für mein Blog-Schreiben am sinnvollsten finde. Sie zeigen hauptsächlich die Suchbegriffe, die Benutzer verwenden, um meine Blog-Seite in Suchmaschinen zu erreichen, und die Seitenpfade, über die sie von den Suchergebnissen aus in meinen Blog gelangen.

Wie Sie sehen können, brachte mir ein Artikel mit dem Titel "[Warp, iTerm2 oder Alacritty? Meine Terminal-Tüftel-Notizen](https://www.pseudoyu.com/en/category/tools/)" viele Besucher, während Themen über Blog-Einrichtung und Smart-Contract-Entwicklung ebenfalls die ersten Eindrücke meines Blogs für die meisten natürlichen Benutzer sind, die von Suchmaschinen kommen.

### Umami + Supabase + Netlify

![yu_umami_record](https://image.pseudoyu.com/images/yu_umami_record.png)

Die beiden oben genannten Methoden zeigen jedoch immer noch nur die Gesamtdaten der Website. Um die Leistung eines bestimmten Artikels über einen Zeitraum oder Echtzeit-Zugriffsdaten nach der Veröffentlichung eines Artikels genau zu verfolgen, ist immer noch ein Analysesystem erforderlich. Nach der Lektüre von Reorx's Artikel "[Umami für die Sammlung persönlicher Website-Statistiken bereitstellen | Reorx's Forge](https://reorx.com/blog/deploy-umami-for-personal-website/)" entschied ich mich für die Verwendung von umami, einem Open-Source, leicht selbst bereitstellbaren Analysesystem. Es hat eine übersichtliche Oberfläche, benutzerfreundliche Funktionen und lässt sich leicht in das eigene Blog-System integrieren.

Ich benutzte es anderthalb Jahre lang ohne Probleme. Allerdings gab es möglicherweise, weil ich es recht früh zu nutzen begann, während eines größeren Versions-Updates eine inkompatible Feldaktualisierung im Datenbankmigrationsscript. Ich fand es etwas schwer zu verstehen, warum ein Open-Source-Projekt dieser Größenordnung solch ein Problem haben würde. Ich sah auch viele andere Benutzer mit den gleichen Bedenken in den Issues, aber letztendlich wurde keine gute Lösung angeboten.

Das größte Problem war jedoch, dass ein Analysesystem auf zwei Plattformen angewiesen war, was in Bezug auf Bereitstellung und Wartung zu schwerfällig war. Wenn entweder die Datenbank oder Netlify Probleme hatte oder migriert werden musste, würde dies viele zusätzliche Kosten verursachen. Als ich also kürzlich das Kommentarsystem meines Blogs aktualisierte, dachte ich, ich könnte genauso gut zum leichteren GoatCounter wechseln.

### GoatCounter + Zeabur

![goatcounter_stats](https://image.pseudoyu.com/images/goatcounter_stats.png)

Ich stieß auf dieses Nischen-Analysesystem, als ich die Code-Updates von Reorx's Blog überprüfte. Ich war sofort von seinem Retro-Internet-Stil angezogen. Es hat fast keine überflüssigen Schaltflächen, dennoch ist die Funktionalität sehr vollständig. Darüber hinaus verwendet es eine go-Einzelbinärdatei + sqlite-Einzeldatei-Datenbankarchitektur, die leichtgewichtig und einfach bereitzustellen ist. Also beschloss ich zu migrieren.

Tatsächlich ist mein eigener GoatCounter auf [fly.io](https://fly.io/) bereitgestellt, aber ich habe die Betriebsanweisungen für fly bereits in meinem vorherigen Artikel über Remark42 sehr detailliert erklärt. Ich wollte mich nicht zu sehr wiederholen. Zufälligerweise habe ich in letzter Zeit [Zeabur](https://zeabur.com?referralCode=pseudoyu), eine Serverless-Plattform, intensiv genutzt. Daher wird in diesem Artikel [Zeabur](https://zeabur.com?referralCode=pseudoyu) als Beispiel verwendet, obwohl die Methode gleichermaßen auf andere ähnliche Plattformen anwendbar ist.

Ich habe auch Konfigurationsdateien für die fly.io-Bereitstellung und docker-compose-Bereitstellung auf VPS nach der Zeabur-Bereitstellungslösung zur Referenz bereitgestellt.

## GoatCounter Bereitstellungsanleitung

Der GoatCounter-Code selbst ist Open Source - "[GitHub - arp242/goatcounter](https://github.com/arp242/goatcounter)", mit klarer und leicht lesbarer Dokumentation. Sie können ihn nach Ihren tatsächlichen Bedürfnissen konfigurieren. Die GoatCounter + Zeabur-Lösung beinhaltet nur einen einzigen Dienst, wobei die Datenbank sqlite in einem Volume eingebunden ist, sodass die Bereitstellung sehr einfach ist.

### Bereitstellung mit Zeabur

[Zeabur](https://zeabur.com?referralCode=pseudoyu) erfordert einen Developer Plan für die Bereitstellung von Container-Anwendungen, der 5$/Monat kostet. Für Bilddienste wie diesen sind die Gesamtnutzung und die Kosten jedoch relativ gering, und das monatliche Kontingent reicht aus, um viele Dienste bereitzustellen. Sie können je nach Ihren Bedürfnissen wählen. Der gesamte Bereitstellungsprozess ist im Vergleich zu fly.io viel einfacher. Alle Vorgänge können über die Weboberfläche durchgeführt werden, ohne dass zusätzliche Kommandozeilentools installiert werden müssen.

#### Bei zeabur registrieren

![zeabur_login](https://image.pseudoyu.com/images/zeabur_login.png)

Besuchen Sie die offizielle [Zeabur](https://zeabur.com?referralCode=pseudoyu) Website und klicken Sie oben rechts, um sich mit Ihrer GitHub-Kontoautorisierung anzumelden.

#### Ein neues Projekt erstellen

![zeabur_new_project](https://image.pseudoyu.com/images/zeabur_new_project.png)

Nachdem Sie die Hauptoberfläche aufgerufen haben, klicken Sie oben rechts auf die Schaltfläche `Projekt erstellen`.

![zeabur_hk_region](https://image.pseudoyu.com/images/zeabur_hk_region.png)

Ich habe das AWS-Rechenzentrum in Hongkong gewählt. Verschiedene Rechenzentren haben einige Unterschiede in Zugriffsgeschwindigkeit, Leistung und Preis. Sie können je nach Ihren Bedürfnissen wählen.

#### Image-Bereitstellung konfigurieren

![zeabur_build](https://image.pseudoyu.com/images/zeabur_build.png)

Im nächsten Schritt wählen Sie die Bereitstellung mit einem Docker-Container-Image.

![zeabur_docker_custom_config](https://image.pseudoyu.com/images/zeabur_docker_custom_config.png)

Da wir ein selbst erstelltes Image verwenden und es keine offizielle GoatCounter-Vorlage gibt, klicken wir auf Benutzerdefiniert auswählen.

![zeabur_prebuilt_edit_toml](https://image.pseudoyu.com/images/zeabur_prebuilt_edit_toml.png)

In diesem Schritt können Sie verschiedene Konfigurationselemente selbst in der Oberfläche ausfüllen, aber vielleicht weil ich an den Dateikonfigurationsmodus von fly.io gewöhnt bin, habe ich `TOML-Datei bearbeiten` in der unteren linken Ecke gewählt. Sie können auch direkt meine Konfigurationsdatei kopieren und modifizieren.

```toml
name = "yu-goatcounter"

[source]
image = "pseudoyu/goatcounter"

[[ports]]
id = "web"
port = 8080
type = "HTTP"

[[volumes]]
id = "goatcounter-data"
dir = "/data"

[env]
PORT = { default = "8080" , expose = true }
GOATCOUNTER_DB = { default = "sqlite3://data/goatcounter.sqlite3" , expose = true }
```

![zeabur_prebuilt_goatcounter_toml](https://image.pseudoyu.com/images/zeabur_prebuilt_goatcounter_toml.png)

Nach der Konfiguration klicken Sie auf die Schaltfläche Bereitstellen in der unteren rechten Ecke.

#### Bereitstellung abgeschlossen

![yu-goatcounter_project](https://image.pseudoyu.com/images/yu-goatcounter_project.png)

Nach dem Klicken auf Bereitstellen warten Sie einen Moment, und es wird ein generierter Standardprojektname angezeigt. Sie können ihn in den Einstellungen oben links in einen besser lesbaren Namen ändern, wie z.B. `yu-goatcounter`.

#### Benutzerdefinierte Domain konfigurieren

![zeabur_create_domain](https://image.pseudoyu.com/images/zeabur_create_domain.png)

Nachdem der Dienst bereitgestellt wurde, müssen wir eine Domain binden, um über das öffentliche Netzwerk auf die Website zugreifen zu können. Zeabur bietet kostenlose Domains der zweiten Ebene wie `xx.zeabur.app` an, oder Sie können Ihre eigene Domain binden.

![zeabur_custom_domain](https://image.pseudoyu.com/images/zeabur_custom_domain.png)

Die generierte Domain kann direkt ohne weitere Konfiguration verwendet werden, wie z.B. `goatcounter.zeabur.app`. Wenn Sie eine benutzerdefinierte Domain verwenden, müssen Sie in Ihrem Domain-Management-Backend einen CNAME-Eintrag hinzufügen, der auf eine Rechenzentrumsadresse im Format `xxx.cname.zeabur-dns.com` verweist.

![cloudflare_goatcounter_config](https://image.pseudoyu.com/images/cloudflare_goatcounter_config.png)

Zum Beispiel wird meine Domain bei Cloudflare gehostet, und der hinzugefügte CNAME-Eintrag ist wie im obigen Bild gezeigt. Ich habe beim offiziellen Support nachgefragt, und sie sagten, wenn Sie das AWS HK Rechenzentrum wählen, können Sie Cloudflare's Proxy verwenden, was theoretisch schneller wäre. Sie können je nach Ihren Bedürfnissen konfigurieren.

Zusätzlich müssen Sie, wenn Sie das Huawei Cloud Rechenzentrum wählen, eine Domainregistrierung beantragen und einen zusätzlichen TXT-Eintrag hinzufügen. Sie können den Anweisungen folgen, um dies durchzuführen.

![zeabur_custom_domain_success](https://image.pseudoyu.com/images/zeabur_custom_domain_success.png)

Eine grüne Anzeige zeigt die erfolgreiche Konfiguration an. An diesem Punkt ist unsere GoatCounter-Dienstbereitstellung abgeschlossen.

#### Datensicherung

Wir hatten diesen Abschnitt in unserer Konfiguration:

```toml
[[volumes]]
id = "goatcounter-data"
dir = "/data"
```

Diese Funktion bindet das `/data`-Verzeichnis innerhalb des Containers (wo sich unsere sqlite-Datenbank befindet) an ein Speichervolume mit der ID `goatcounter-data`. Wenn Sie kein Speichervolume einbinden, gehen Daten verloren, wenn der Container neu gestartet oder neu bereitgestellt wir