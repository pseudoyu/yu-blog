---
title: "Wochenrückblick #55 - Erfahrung mit Ölmalerei, Upgrade des Blogsystems und Gedanken zum Self-Hosting"
date: 2024-03-24T05:20:00+08:00
draft: false
tags: ["review", "life", "painting", "blog", "cusdis", "remark42", "goatcounter", "self-hosting", "flyio"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/fix_you.mp3" caption="'Fix You - Coldplay'" >}}

## Vorwort

![weekly_review_20240324](https://image.pseudoyu.com/images/weekly_review_20240324.png)

Dieser Beitrag ist eine Aufzeichnung und Reflexion meines Lebens vom `17.03.2024` bis zum `24.03.2024`.

Diese Woche habe ich viel von meiner Begeisterung für Arbeit und Lernen wiedergefunden und die seit langem auf meiner TODO-Liste stehende Migration des Blog-Kommentarsystems und des Datenstatistiksystems abgeschlossen, was mir das Gefühl gab, meinen Schreibtisch aufgeräumt zu haben. Am Wochenende habe ich zum ersten Mal Ölmalerei ausprobiert und mir selbst einen neuen Avatar gemalt, was mich mit einem Gefühl der Erfüllung erfüllte. Ich nahm meine Fitnessroutine wieder auf, setzte mein Fahrunterricht fort und meldete mich für die zweite Stufe der Fahrprüfung an. Es gab auch viele andere interessante Ereignisse.

## Erfahrung mit Ölmalerei und neuer Avatar

Meine Kommilitonin und ich haben sehr unterschiedliche Persönlichkeiten und Interessen. Sie hat viele Hobbys, die ich noch nie ausprobiert habe, und was mich fasziniert, scheint für sie oft unbekanntes Terrain zu sein. Deshalb haben wir uns kürzlich einige Ziele gesetzt, um uns gegenseitig unsere eigenen Hobbys/Fähigkeiten vorzustellen. Ich wählte die Doppel-Pinyin-Eingabemethode und Programmierung, wobei erstere bereits deutliche Fortschritte zeigt. Diese Woche nahm sie mich mit zu einem Ölmalkurs.

Ich bin eigentlich ein völliger Neuling, wenn es um Malerei geht, und dachte nie, dass ich irgendeine Begabung für solche künstlerischen Tätigkeiten hätte. Ich war lediglich neugierig, welche Art von Anziehungskraft sie dazu motivieren könnte, einen halben Nachmittag in einem Zeichen- oder Ölmalerei-Studio zu sitzen und akribisch an kleinen Details zu arbeiten. Ich war sowohl aufgeregt als auch ein bisschen nervös.

![oil_painting_experience](https://image.pseudoyu.com/images/oil_painting_experience.png)

Normalerweise würden Anfänger nicht mit komplexen Motiven wie Porträts beginnen, aber ich wollte einen neuen Avatar. Die Studiolehrerin war sehr entgegenkommend und bereit, mich anzuleiten. Wir wählten ein Foto, das sich hauptsächlich auf den "Kopf" konzentrierte, und begannen. Die Umrisse zeichnen, Farben mischen, Farbe auftragen, Details basierend auf Licht und Position hinzufügen - alles war interessanter, als ich es mir vorgestellt hatte. Die Kombination weniger einfacher Farben konnte viele Schichten erzeugen, und der Schaffensakt selbst war so faszinierend wie Magie.

![yu_painting](https://image.pseudoyu.com/images/yu_painting.jpg)

Das Ergebnis eines Nachmittags Arbeit ist in dem Bild zu sehen. Obwohl die Pinselstriche noch anfängerhaft sind, ist es ein Werk, das ich mit meinem eigenen Pinsel geschaffen habe und das eine einzigartige Bedeutung hat. Ich habe meinen Avatar auf allen Plattformen zu diesem Gemälde geändert.

## Upgrade des Blogsystems

### Von Cusdis zu Remark42

Ich hatte zuvor einen Artikel "Leichtgewichtige Open-Source kostenlose Blog-Kommentarsystem-Lösung (Cusdis + Railway)" geschrieben, in dem ich darüber sprach, wie ich das selbst gehostete Open-Source-[Cusdis](https://cusdis.com/)-Kommentarsystem von [Randy](https://lutaonan.com/) verwendete. Ich benutze es seit Mitte 2021, also seit vollen drei Jahren. Abgesehen von einigen anfänglichen Schwierigkeiten mit Deployment-Plattformen, als Heroku und Railway anfingen, Gebühren zu erheben, lief es stetig.

Allerdings bin ich während der Nutzung auf einige Probleme gestoßen:

1. Wahrscheinlich aufgrund einiger Änderungen im eingebauten Browser von WeChat ist die Kommentarkomponente nicht sichtbar, wenn der Blog aus WeChat-Chats/Dialogen geöffnet wird.
2. Obwohl eine E-Mail-Adresse eingegeben werden kann, unterstützt es nicht das Abonnieren von Kommentarantworten.
3. Kommentare müssen manuell vom Administrator genehmigt werden, aber der Kommentarbenachrichtigungs-TG-Bot fällt oft aus, was dazu führt, dass ich Kommentare verpasse.

Darüber hinaus scheint es im Vergleich zu anderen ausgereifteren Kommentarsystemen etwas rudimentär, da seine Kernfunktionalität seit langem nicht aktualisiert wurde. Allerdings hatte ich nach dem Prinzip "wenn es funktioniert, ist es gut genug" nicht in Erwägung gezogen, zu migrieren/aktualisieren. Ich beteiligte mich sogar an einigen Entwicklungen der Cusdis V2-Version während einer Zeit, in der ich Frontend lernte, aber die Entwicklungsgruppe wurde kurz darauf inaktiv.

In den letzten Monaten, weil ich meinen Blog kaum aktualisierte, erhielt ich keine Benachrichtigungen vom Kommentar-TG-Bot. Ich dachte, es gäbe keine Kommentare, bis ich kürzlich den Connection String der Supabase-Plattform, die die Datenbank hostet, ändern musste. Ich entdeckte, dass es Dutzende von Kommentaren gab, die nach und nach eingingen, einige drückten Fürsorge und Ermutigung aus, andere erkundigten sich nach technischen Problemen. Als ich sie sah, war es bereits ein oder zwei Monate später, was mich ziemlich in Verlegenheit brachte.

Zusätzlich warf Vercel bei der Änderung der Datenbank-URI ständig Fehler auf. Also beschloss ich, von Cusdis zu migrieren. Nach einiger Recherche entschied ich mich für [Remark42](https://remark42.com/), das auch [reorx](https://reorx.com/) in seinem Artikel "Changing Blog Comment Systems" ausgewählt hatte.

Allein in Bezug auf die Konfigurationsoptionen ist es erheblich reicher als Cusdis. Ich habe derzeit mehrere gängige Social-Account-Logins eingerichtet (GitHub, Twitter, Telegram, E-Mail), anonyme Kommentare erlaubt, E-Mail-Abonnements für Antwortbenachrichtigungen unterstützt und auch TG-Bot-Benachrichtigungen eingerichtet. Es ist auf [fly.io](https://fly.io) bereitgestellt, mit Go-Single-Binary + Single-File-Datenbank, eine sehr komfortable Lösung.

Da ich zuvor viele Kommentardaten angesammelt hatte und Cusdis pg verwendet, während Remark42 eine boltdb-Einzeldatei-Datenbank verwendet, unterstützt letztere keine Remote-Verbindungen, so dass ich nicht direkt mit SQL-Anweisungen schreiben konnte. Ich musste zuerst die erforderlichen Felder über eine verknüpfte Abfrage in eine JSON-Datei exportieren und dann manuell das Migrator-Skript ausführen (und da das offizielle nur WordPress, Disqus und Commento unterstützt, musste ich die Konvertierungslogik manuell implementieren). Glücklicherweise ist es in Go geschrieben, womit ich vertraut bin. Es hat mich eine ganze Nacht gekostet, den [PR](https://github.com/pseudoyu/remark42/pull/1/files) fertigzustellen!!!

Nach der Migration stellte ich fest, dass ich im Laufe der Jahre insgesamt 438 Kommentare angesammelt hatte. Ich war selbst überrascht, aber sie sind alle wieder da!!!

### Von Umami zu GoatCounter

Mit der Einstellung "wenn ich schon das Kommentarsystem geändert habe, kann ich auch gleich das Datenstatistiksystem aktualisieren, das mir Sorgen bereitet hat", ging ich auch daran, es zu aktualisieren.

Umami hatte eigentlich keine Probleme verursacht und lief fleißig eineinhalb Jahre lang, bis ich es ersetzte. Allerdings gab es möglicherweise, weil ich es ziemlich früh zu benutzen begann, während eines größeren Versions-Updates eine inkompatible Feldaktualisierung im Datenbank-Migrations-Skript. Ich verstehe nicht ganz, warum ein Open-Source-Projekt dieser Größenordnung solche Probleme haben würde. Ich sah viele andere Benutzer in den Issues mit ähnlichen Bedenken, aber letztendlich wurde keine gute Lösung angeboten.

Aber weil ich es schon ein halbes Jahr lang laufen hatte, wollte ich die vorherigen Daten nicht verlieren. Also schob ich es immer wieder auf, bis ich jetzt immer noch auf einer alten Version bin, die ich geforkt habe. Obwohl ich nicht viele funktionale Anforderungen an die neue Version habe, fühlt es sich einfach ein bisschen unangenehm an, wie leichter OCD, aber ich habe es einfach immer wieder aufgeschoben.

Also wechselte ich, die Gelegenheit dieser großen Blog-Konstruktion nutzend, zu [goatcounter](https://www.goatcounter.com/). Wieder einmal ist es eine Go-Single-Binary + sqlite-Einzeldatei-Datenbank, die auf fly.io bereitgestellt wird, eine weitere sehr komfortable Konfiguration.

Interessanterweise bietet der Autor von goatcounter, weil er sehr hartnäckig glaubt, dass die Containerisierung solcher Einzeldatei-Anwendungen tatsächlich die Wartungskosten erhöhen würde, keine offiziellen Images an. Es ist jedoch immer noch praktisch, ein Image zu haben, um es auf dem eigenen VPS oder einer serverlosen Plattform bereitzustellen, also habe ich Github Actions verwendet, um eine CI zu erstellen, die täglich den neuesten Code zieht, das Image baut und es auf Docker Hub hochlädt. Wenn Sie es benötigen, können Sie es verwenden. Die entsprechende Dockerfile und Docker Compose-Datei können aus [diesem PR](https://github.com/pseudoyu/goatcounter/pull/1/files) referenziert werden.

```bash
docker pull pseudoyu/goatcounter
```

![yu_umami_record](https://image.pseudoyu.com/images/yu_umami_record.png)

Die Häufigkeit der wöchentlichen Berichte im letzten halben Jahr ist besorgniserregend niedrig. Abgesehen von einem langen Artikel über Informationsmanagementsysteme gab es keinen zufriedenstellenden Output. Also beschloss ich, die vorherigen Besuchsdaten nicht zu migrieren (die Komplexität sollte auch viel höher sein). Danke an jeden Cyber-Freund, der auf meine Blog-Website geklickt hat, Screenshot zur Erinnerung.

In letzter Zeit habe ich das Gefühl, dass meine Stimmung, an diesen Software/Hardware/Service-Konfigurationen herumzubasteln, zurückgekehrt ist, und ich habe auch viele Blog-Ideen. Die neuen Daten werden ein Neuanfang sein 🫡

![yu_goatcounter_data](https://image.pseudoyu.com/images/yu_goatcounter_data.png)

Die größte Motivation für die Änderung war, dass goatcounters Oberfläche, wie mein altmodisches Blog-Thema, perfekt meinen ästhetischen Sweet Spot trifft. Ich habe das Gefühl, ich könnte ewig auf diese Oberfläche starren 🤩 Ich kann diesem Retro-Internet-Design nicht widerstehen.

## Einige Gedanken zum Self-Hosting

Ich habe tatsächlich viele Runden des Herumbastelns und Hin und Her mit VPS und serverlosen Plattformen durchgemacht. Es mag nicht als Einsichten zählen, aber es ist sicherlich Erfahrungswissen nach tiefgreifender Erfahrung.

Ich war früher ein Befürworter von Serverless. Zu dieser Zeit würde ich, wenn möglich, auf Vercel/Railway und anderen PaaS-Plattformen bereitstellen, anstatt selbst einzurichten. In der Lage zu sein, mit fast keinen Wartungskosten eine Stabilität zu erreichen, die mit großen Plattformen vergleichbar ist, praktizierte ich tatsächlich die Serverless-Isierung all meiner Dienste, und es war in der Tat eine lange Zeit lang eine sorgenfreie und mühelose Erfahrung.

Nachdem ich jedoch erlebt hatte, wie Heroku und Railway nacheinander ihre Abrechnungsmodelle zwischendurch änderten, und als n8n auf Railway eine Rechnung von über zehn Dollar pro Monat auflaufen ließ, entdeckte ich nach und nach einige Nachteile. Serverless reduzierte in der Tat die Anforderungen an die Wartung meiner eigenen Server, aber entsprechend war ich auch den Regeln dieser Plattformen unterworfen.

Das Abrechnungsmodell ist nur ein Teil des Grundes. Im Vergleich zur Miete eines gut konfigurierten Servers selbst sind die Kosten eigentlich nicht schlecht. Es scheint nur, dass es meine Dienste und Daten wieder an eine zentralisierte Plattform gebunden hat, was ein Gefühl der Unsicherheit gibt, anderen ausgeliefert zu sein. Und wenn man zu einer anderen Plattform migrieren möchte, bietet die Plattform oft keine bequeme Lösung. Die Komplexität des Selbstbastelns ist viel höher als das direkte Kopieren von docker-compose-Dateien plus gemounteten Volumes zwischen Servern.

![vps_service_01](https://image.pseudoyu.com/images/vps_service_01.png)

![vps_service_02](https://image.pseudoyu.com/images/vps_service_02.png)

Daher habe ich viele meiner Dienste auf dem Server platziert, die seit 430+ Tagen stabil laufen.

![xiao_self_hosted](https://image.pseudoyu.com/images/xiao_self_hosted.png)

Vor einigen Tagen, als ich mit [reorx](https://reorx.com/) über Lösungen für die Bereitstellung von Diensten sprach, erwähnte er, dass er jetzt Self-Host-Lösungen mit sqlite oder anderen ähnlichen Datei-Datenbanken priorisiert, was viele Wartungs- und Migrationskosten und -komplexität reduzieren kann.

Später dachte ich darüber nach. Ob auf VPS oder serverlosen Plattformen, es ist im Wesentlichen eine Wahl des Self-Hosting. Was mehr benötigt wird, ist, über die Abhängigkeiten der bereitgestellten Dienste selbst nachzudenken. Zum Beispiel kamen viele der Instabilitäten meines vorherigen Cusdis und Umami tatsächlich daher, dass die Serverseite auf PaaS wie Vercel und Netlify war, während die Daten auf DaaS wie Supabase gehostet wurden. Ein Selbstnutzungsdienst, der gleichzeitig von zwei Plattformen abhängt, würde bei jedem Problem mit einer der beiden zu einer Nichtverfügbarkeit des Dienstes führen. Was VPS tut, ist lediglich, dieses Risiko in einen einzigen Punkt der Selbstwartung zu verwandeln.

![flyio_services](https://image.pseudoyu.com/images/flyio_services.png)

Also begann ich nach langer Zeit wieder zu basteln und Remark42 und GoatCounter auf [fly.io](https://fly.io) bereitzustellen. Aufgrund von Single Binary + Datei-Datenbank liegt der Leistungsverbrauch vollständig im Bereich des kostenlosen Plans. Ich platziere weiterhin RSSHub, n8n, Bildablage und andere Anwendungen, die relativ abhängiger sind und mehr externe Dienste bereitstellen müssen, zentraler auf VPS. Und ich betreibe einige Dienste mit höherem Leistungs- oder Speicherverbrauch auf dem Home Server und stelle sie durch Intranet-Penetrationslösungen bereit.

## Sonstiges

![applite_overview](https://image.pseudoyu.com/images/applite_overview.png)

Ich habe die auf Mac installierten Softwareprogramme aus verschiedenen Quellen vereinheitlicht. Das Prinzip ist, alles neu zu installieren, was über brew cask installiert werden kann. Zuvor, wenn ich nach Befehlszeilentools suchen musste, habe ich nicht viel gespürt, aber jetzt mit einer GUI-Ansicht stellte ich fest, dass die Softwarequellen tatsächlich viel reicher sind als gedacht. Diese Methode ist bequem für die Verwaltung/Migration und kann relativ die Sicherheit der Softwarequellen gewährleisten 🫡

Ich bin von RapidAPI zu einem neuen API-Debugging-Tool [Bruno](https://www.usebruno.com/) gewechselt, habe seine Golden Edition vorbestellt, und die Erfahrung war bisher sehr gut.

## Interessante Dinge

### Input

Obwohl die meisten interessanten Inputs automatisch im "Yu's Life" Telegram-Kanal synchronisiert werden, wähle ich trotzdem einige aus, um sie hier aufzulisten, was sich mehr wie ein Newsletter anfühlt.

#### Bücher

- [**Rot und Schwarz**](https://book.douban.com/subject/35781152/), sah eine Erklärung aus einem Video, die Beschreibung von Juliens Selbstwertgefühl und der Arroganz, die er infolgedessen zeigt, hinterließ einen tiefen Eindruck, lese derzeit.
- [**Notizbücher**](https://book.douban.com/subject/34802764/) von Albert Camus, gerade erst begonnen zu lesen.

#### Sammlungen

- [GitHub - milanvarady/Applite](https://github.com/milanvarady/Applite)
- [GitHub - usebruno/bruno](https://github.com/usebruno/bruno)
- [GitHub - plankanban/planka](https://github.com/plankanban/planka)

#### Artikel

- [Psychische Gesundheit in Open Source](https://antfu.me/posts/mental-health-oss)
- [Heptabase neu verstehen](https://justgoidea.com/posts/2024-009/)
- [Docker für JavaScript entmystifizieren](https://fly.io/javascript-journal/demystify-docker-js/)

#### Videos

- [In Tokio mache ich nur drei Dinge!](https://www.bilibili.com/video/BV131421Q7KT)

#### TV-Serien

- [**Die Trisolaris-Trilogie Staffel 1**](http://movie.douban.com/subject/35196946/), schaue derzeit.