---
title: "Wochenrückblick #25 - Persönliches Informationsausgabe- und Synchronisationssystem basierend auf Crossbell (Refaktorisiert)"
date: 2023-01-09T19:12:56+08:00
draft: false
tags: ["review", "life", "home", "mood", "miniflux", "rss", "information", "serverless", "pkm", "system", "xlog", "xsync", "crossbell"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="'Here After Us - Mayday'" >}}

## Vorwort

Dies ist eine Aufzeichnung und Reflexion meines Lebens vom 1. Januar 2023 bis zum 9. Januar 2023.

Dies ist der erste Wochenrückblick des Jahres 2023. Obwohl sich das Neujahrsfest noch wie gestern anfühlt, ist die erste Januarwoche bereits vorüber. Vielleicht ist meine psychologische Zeitwahrnehmung zunehmend abgestumpft.

Während des Neujahrs verfasste ich eine recht detaillierte Jahresübersicht, in der ich die verschiedenen Ereignisse des vergangenen Jahres Revue passieren ließ. Nach der Fertigstellung bemerkte ich, dass die Länge meine Erwartungen übertroffen hatte. Zudem hatte ich meine Gedanken zu Neujahrsplänen und Erwartungen noch nicht geklärt, also ließ ich diesen Teil aus. Daher werde ich diese Gelegenheit im ersten Wochenrückblick des neuen Jahres nutzen, um einige bescheidene Ziele zu setzen. Einige sind kleine Gewohnheitsbildungen, andere sind langfristige Pläne voller Ungewissheiten. Ich weiß nicht, ob ich sie alle im kommenden Jahr erfüllen kann, aber sie aufzulisten wird eine gewisse Motivation bieten und als eine Form der Selbstüberwachung dienen.

Nachdem ich fast zwei Monate zu Hause geblieben war, beschloss ich schließlich, am Wochenende auszugehen, um bei einem Freund zu Hause zu essen und einen schönen Tag zu verbringen (andernfalls hatte ich das Gefühl, vergessen zu haben, wie man von Angesicht zu Angesicht spricht). Obwohl die Erfolgsquote der Fotos fragwürdig war, gelang es mir, die Fotos zu bearbeiten und zwei Fotosammlungen zu veröffentlichen. Ich organisierte meine verschiedenen Software- und Hardware-Dienste (ein jährliches Ritual, immer mit dem Gefühl, dass ich nach dem Aufräumen mehr Motivation haben werde, neu zu beginnen). Beim Aufräumen erinnerte ich mich an einige frühere kleine Projekte und richtete eine Website ein, um die [IPFS-Version von ZLibrary](https://zlib.pseudoyu.com/) zu betreiben, was unerwartet Aufmerksamkeit erregte und mich über Nacht dazu brachte, den Server und die Netzwerkrouten zu optimieren. Und viele andere interessante Dinge passierten.

## Restrukturierung persönlicher Dienste

### Dienstverwaltung

Wie in den Vorjahren begann ich das Jahr damit, meine verschiedenen Dienste zu organisieren. Ich entdeckte, dass ich mittlerweile bis zu 20 habe, wobei die Hälfte davon serverlos ist. Meine Fähigkeit, kostenlose Ressourcen zu nutzen, hat sich in diesem Jahr stark verbessert. Zur einfacheren Verwaltung richtete ich einen Überwachungsdienst mit dem Open-Source-Tool Uptime Kuma ein, verband ihn mit einem Telegram-Bot für Warnungen, was mir viel mehr Seelenfrieden gab.

![uptime_kuma_yu_services](https://image.pseudoyu.com/images/uptime_kuma_yu_services.png)

Interessanterweise fand ich die Verwaltung von Websites auf Servern immer lästig. Jedes Mal, wenn ich Dienste migrieren oder ändern musste, war es immer ein Ärgernis. Also habe ich die meisten meiner Dienste auf Railway, Vercel, Supabase und anderen Serverless-Plattformen gehostet. Da die meisten persönliche Dienste ohne hohe Konfigurationsanforderungen sind, reicht es, solange sie sicher und stabil sind. Ich hatte mich nicht mit Nginx-Reverse-Proxy, https-Zertifikaten und dergleichen beschäftigt.

Wie ich schon erwähnte, helfe ich einem anime-liebenden Freund bei der Verwaltung und technischen Unterstützung von Bilibili-Livestreams. Ich dachte darüber nach, eine kostenlose Oracle Japan-Maschine speziell für die Livestream-Überwachung und automatische Aufzeichnung zu verwenden. Manchmal muss mein Freund auch in der Lage sein, direkt anzusehen und herunterzuladen, also müssen natürlich ein einprägsamer Domainname, die Zugriffsgeschwindigkeit unter inländischen Netzwerkbedingungen, die Download-Bandbreite usw. berücksichtigt werden. Serverless-Dienste waren bei weitem nicht ausreichend (und nicht sehr kosteneffektiv), also erkundete ich einige Lösungen und wählte [Nginx Proxy Manager](https://nginxproxymanager.com/), ein praktisches Reverse-Proxy-Tool.

![npm_yu_dashboard](https://image.pseudoyu.com/images/npm_yu_dashboard.png)

Ich habe es auf einer BandwagonHost-Maschine mit guter Netzwerkverbindung (CN2 GIA) bereitgestellt, um meine verschiedenen Dienste zu hosten und eine anständige Zugriffserfahrung zu gewährleisten. Es kann auch direkt https-Zertifikate für meine `*.pseudoyu.com`-Subdomains durch Wildcard-Matching und automatische Erneuerung ausstellen, was sehr praktisch ist. In Kombination mit der zuvor erwähnten Überwachung benutze ich es jetzt seit einer Woche, und es ist ziemlich komfortabel.

Die offizielle Dokumentation ist klar und detailliert, und mit der benutzerfreundlichen Container-Dienstverwaltungsmethode von docker-compose ist es schnell zu beginnen. Allerdings könnte ich trotzdem in Erwägung ziehen, später ein Tutorial zu erstellen, um Freunden, die kleine Dienste wie Blogs hosten möchten, eine Referenz zu bieten.

### RSS-Eingabe

Im Jahr 2022 konzentrierte ich mich hauptsächlich auf Blog-Ausgabe und meinen Telegram-Kanal, ohne viel über Eingabe und Synchronisation über verschiedene Plattformen nachzudenken. Dies führte zu einer Anhäufung von RSS-Abonnements, und Newsletter wurden auch etwas überwältigend. Ich war nicht in der Lage, meine Eingabe-Informationsquellen richtig zu filtern. Also löschte ich NetNewsWire, das ich lange Zeit benutzt hatte, und richtete ein leichtgewichtigeres Miniflux mit Railway + Supabase als meinen Hauptleser ein. Ich filterte auch meine RSS-Informationsquellen und beschränkte sie auf 52, fast ausschließlich persönliche Blogs. Ich werde in Zukunft weiter optimieren und anpassen.

![miniflux_yu_page](https://image.pseudoyu.com/images/miniflux_yu_page.png)

Obwohl Miniflux eine anständige Leseerfahrung bietet, bevorzuge ich es tatsächlich, in den Originalartikel zu klicken. Ich habe immer das Gefühl, dass es bei persönlichen Blogs nicht nur um den Inhalt geht; der Stil-Design der Website, einige verwandte Artikel und Themen sind alle integrale Teile des Bloggers, die ein vollständigeres Lesevergnügen bringen können.

Für mich dient der RSS-Reader mehr als ein Aggregationstool erster Stufe. Da Miniflux ein webbasierter Dienst ist, kann er keine sehr zeitnahen Benachrichtigungen bereitstellen. Da ich mich jeden Tag stark auf Telegram verlasse, richtete ich meine eigene Telegram-Benachrichtigung basierend auf [RSS to Telegram Bot](https://github.com/Rongronggg9/RSS-to-Telegram-Bot) ein, um Updates von diesen Informationsquellen an mich zu pushen. Wenn ich einige interessante Titel sehe, mache ich mir eine geistige Notiz und gehe dann zu Miniflux, um sie alle auf einmal zu lesen und zu überprüfen, wenn ich freie Zeit habe.

![yu_rss_to_tg_bot](https://image.pseudoyu.com/images/yu_rss_to_tg_bot.png)

Auf diese Weise verpasse ich weniger wahrscheinlich Artikel, die ich lesen möchte, und es verursacht keine zu große Informationsanhäufung. Dieses Setup hat bisher sehr gut funktioniert. Übrigens hat das Sehen verschiedener Wochenrückblicke jedes Wochenende auch einen signifikanten Anreizeffekt (~~Ich ging am Sonntag spielen, verzögerte die Aktualisierung vernünftigerweise~~).

### Telegram-Ausgabe

Ich habe auch meinen eigenen n8n-Synchronisationsdienst basierend auf Railway + Supabase eingerichtet, um meine Eingabe von verschiedenen Plattformen mit meinem Kanal zu synchronisieren. Für eine detaillierte Beschreibung können Sie sich auf diesen Artikel "[\[Wochenrückblick #12 - Cyber Space, Selbstdefinition und Grenzen\](https://www.pseudoyu.com/de/2022/09/19/weekly_review_20220919/)" beziehen.

Zuvor basierte die Plattform auf [Reorx's](https://github.com/reorx) Lösung mit einigen meiner eigenen Anpassungen, aber ich hatte keine weiteren Informationsquellen hinzugefügt, und es gab weniger inländische Quellen.

Obwohl ich derzeit selten auf verschiedenen inländischen Plattformen teile, ist es immer noch ein Teil von mir. Zusätzlich fügte ich Sspai als Veröffentlichungskanal für einige meiner Arbeitseffizienzartikel hinzu. Also, nachdem mein Freund [Tujunjie](https://blog.tujunjie.com/) die Integration von RSSHub und n8n empfohlen hatte, implementierte ich einen Satz [RSSHub](https://github.com/DIYgod/RSSHub)-Dienste auf meinem Server, um es auszuprobieren. Ich fand es sofort als eine beeindruckende Lösung und fügte schnell Synchronisationsunterstützung für NetEase Cloud Music, Weibo, Bilibili und Sspai zu meinem Telegram-Informationsflusskanal hinzu, was den Inhalt anreicherte.

### Crossbell-Synchronisation

Obwohl Plattformen wie Twitter und Telegram relativ groß sind, sind sie immer noch zentralisierte Produkte. Mit den jüngsten verschiedenen Umwälzungen fühle ich mich immer unwohl dabei, Telegram als Endstation für die Aggregation dieser Informationsquellen zu verwenden, besonders wenn ich oft fast versehentlich auf Löschen aller Nachrichten klicke, wenn ich versuche, eine einzelne Nachricht zu löschen (seltsame Benutzererfahrung). Daher ist die Synchronisation und der Export von Informationen auch ein sehr wichtiger Aspekt.

Das Side Project, das ich zuvor erwähnte, macht auch so etwas, aber als Web3-Praktiker habe ich natürlich schon lange auf blockchain-basierte Lösungen geschielt. Tatsächlich war mein Abschlussprojekt eine [ÐApp zum Schutz des Dateneigentums basierend auf Ethereum und IPFS](https://github.com/pseudoyu/uright), aber dieses papierdünne Demo-Projekt konnte natürlich meine verschiedenen Bedürfnisse nicht erfüllen, und der Code war so chaotisch geschrieben, dass ich keine Lust hatte, ihn zu refaktorisieren. Also begann ich, nach On-Chain-Lösungen zu suchen.

Ich hatte [Crossbell](https://crossbell.io/) schon lange verfolgt, und durch einen seltsamen Zufall lernte ich ziemlich viele Freunde von [RSS3](https://rss3.io/) kennen. Aber mein früherer Eindruck von Crossbell beschränkte sich noch auf das [CrossSync](https://crosssync.app/) Browser-Plugin, das [Diygod](https://diygod.me/) auf Twitter gepostet hatte, das auf dieser Kette basierte. Damals öffnete ich den Link auf meinem Handy, und es war nicht praktisch, die Wallet zu verknüpfen, also legte ich es beiseite.

Also dachte ich daran, die offizielle Website zu besuchen, und zu meiner Überraschung fand ich, dass es bereits mehrere Anwendungen wie [xLog](https://xlog.app/), [xSync](https://xsync.app/), [xChar](https://xchar.app/), [xFeed](https://crossbell.io/feed) usw. gab. Das xSync, das mich am meisten interessierte, unterstützte zufällig den Telegram-Kanal und passte perfekt zu meinen Bedürfnissen.

#### xLog Synchrone Blog-Veröffentlichung

Also begann ich eine Reihe von Konfigurationen und Dekorationen. Zuerst synchronisierte ich meine persönlichen reflektionsbezogenen Blogbeiträge zu xLog. Der visuelle Effekt und die Erfahrung sind gut, und es ist sehr praktisch, basierend auf der Crossbell-Adresse zu folgen und zu kommentieren.

Dies ist meine xLog-Zugangsadresse: [xlog.pseudoyu.com](https://xlog.pseudoyu.com/). Interessierte Freunde können ihr auch folgen. Aufgrund von Überlegungen zum Anpassungsniveau, verschiedenen historischen Artikel-Migrationsroutingproblemen, Änderungen in meinen verschiedenen Datenstatistikdiensten usw. ist es im Moment jedoch eher ein Synchronisations-Verteilungskanal. Ich plane vorerst nicht, meinen Blog vollständig zu migrieren.

![yu_xlog_homepage](https://image.pseudoyu.com/images/yu_xlog_homepage.png)

Die eingebaute [NFT-Vitrine](https://xlog.pseudoyu.com/nft) ist sehr schön, wahrscheinlich integriert mit [Unidata](https://unidata.app/). Ich wollte es vorher in meinen Hugo-Blog integrieren, bin aber nie dazu gekommen (~~einen fertigen zu haben, machte mich noch fauler~~).

![yu_xlog_nft](https://image.pseudoyu.com/images/yu_xlog_nft.png)

#### xSync Automatische Synchronisation von Telegram und Twitter

Ich war wirklich aufgeregt, als ich sah, dass xSync Telegram-Kanal-Daten synchronisieren konnte. Es erforderte keine Änderungen, um ein weiteres Backup und Archiv meines aggregierten Kanals zu erstellen, und ich konfigurierte es schnell. ~~Ich verspürte plötzlich den Drang, mein eigenes Side Project aufzugeben~~.

![yu_xsync_homepage](https://image.pseudoyu.com/images/yu_xsync_homepage.png)

Es ist jedoch etwas bedauerlich, dass nur ein Teil der historischen Daten synchronisiert wurde. Es scheint keine Option für manuelle Backup-Synchronisation von Daten vor der Integration zu geben, und ich weiß nicht, ob es ein Konfigurationselement oder zukünftiges Feature gibt, das dies lösen kann. Wenn irgendwelche RSS3-Freunde eine Lösung kennen, lasst es mich bitte wissen. Danke!

Nachdem alles konfiguriert ist, können Sie alle Ihre Nachrichten über xChar anzeigen. Es ist eine perfekte Lösung. Dies ist meine xCharacter persönliche Homepage: [xchar.app/pseudoyu](https://xchar.app/pseudoyu), wo Sie auch meinen Informationsfluss sehen können.

![yu_xchar_profile](https://image.pseudoyu.com/images/yu_xchar_profile.png)

Eine weitere kleine Anekdote ist, dass ich lächelte, als ich sah, dass ich `pseudoyu@crossbell` in das Profil setzen musste. Als ich mein Abschlussprojekt zur Copyright-Schutz-ÐApp machte, verwendete ich die Oraclize-API im Solidity-Vertrag, um auf Off-Chain-Daten zuzugreifen, was auch den eindeutigen Identifikator aus der YouTube-Beschreibung als Beweis für den Kontobesitz erfasste. Es gab mir ein seltsames Gefühl der Vertrautheit, haha. Ich werde später die Gelegenheit haben, den Code zu studieren.

Diese auf Crossbell basierende Lösung für Informationseingabe und -ausgabe kann gesagt haben, mein ursprüngliches persönliches Verwaltungssystem umstrukturiert zu haben. Ich hoffe, basierend auf diesem System einige eigene Versuche zu unternehmen.

## Neujahrspläne

Es scheint, dass das Auflisten einiger Jahrespläne jedes Jahr zu einer ungeschriebenen Gewohnheit geworden ist, aber in so vielen Jahren meiner Vergangenheit gab es nur wenige, die ich tatsächlich durchgehalten und erreicht habe. Dieses Jahr habe ich mehr öffentliche Ausdruckskanäle hinzugefügt, was mir anscheinend mehr Motivation zum Üben gibt.

Ich las zuvor [Xuanwos](https://xuanwo.io/) Artikel "[2022-37: Öffentlicher Workflow basierend auf Github](https://xuanwo.io/reports/2022-37/)", und nach ein bisschen Recherche zu GitHub Projects fand ich es einfach, aber ausreichend. Obwohl ich normalerweise etwas grundlegendes GTD basierend auf Logseq mache, ist es immer noch schwierig, es als Kanban-Board zu verwenden. Ich werde es dieses Jahr versuchen und mir auch etwas entsprechenden Druck geben.

Es ist schwer, die Granularität von Neujahrsplänen zu kontrollieren, also werde ich einfach mit dem Fluss gehen. Ich werde keine großen und leeren mehr schreiben. Es geht mehr um einige Indikatoren. Einige sind Ideen zur freien Erforschung, einige sind langfristige Ziele und einige sind kurzfristige Dinge, die es zu erreichen gilt. Ich habe ein Checkbox-Format verwendet. Vielleicht werde ich später mehr hinzufügen, wenn mir etwas einfällt. Ich werde zurückkommen, um zu überprüfen und zu überprüfen, wenn ich sie abschließe oder während der Jahresend-Zusammenfassung des neuen Jahres.

- [ ] Gut auf Nini aufpassen, sie gut beschützen
- [ ] Nach Japan gehen oder nach Hongkong zurückkehren für Arbeit / einen Remote-Job, den ich genieße / einen Arbeitsmodus mit zufriedenstellender Freiheit, je nach Priorität wählen
- [ ] Reisen zu mindestens 6 Städten, in denen ich noch nie war, vorzugsweise lang vermisste Freunde treffen, wenn auch nicht viele
- [ ] Ausdauer im Schreiben von Wochenrückblicken, 48 Stücke abschließen
- [ ] Mindestens 48 originale Blogbeiträge neben den Wochenrückblicken aktualisieren, hauptsächlich technisch
- [ ] Mehr nach draußen gehen, um Fotos zu machen, mindestens 12 Stücke in der neu eröffneten Fotografiesammlung aktualisieren (ich habe bereits zwei KPI-Beiträge an Neujahr gepostet) und Komposition, Farbe und Nachbearbeitung eingehend studieren
- [ ] Mindestens 12 übersetzte Artikel zu GoCN beitragen
- [ ] 10 Artikel auf Sspai veröffentlichen, Geld für Katzenfutter verdienen
- [ ] Anfangen, ein Bilibili-Up und Youtuber zu sein, mindestens 10 Videos veröffentlichen, können nicht zu oberflächlich sein
- [ ] Ausdauer im Trainieren/Laufen an mindestens vier Tagen pro Woche (Ring Fit Adventure oder Keep zählt auch), werde auch Check-ins in Wochenrückblicken aufzeichnen
- [ ] Ausdauer im Gitarrenüben, mindestens 3 Lieder aufnehmen und veröffentlichen
- [ ] Skateboard-Fähigkeiten wieder aufnehmen, mindestens zweimal pro Woche üben
- [ ] Mindestens 24 bedeutungsvolle Bücher lesen, aber nicht herunterschlingen, muss meine Gedanken auf Plattformen wie Douban veröffentlichen
- [ ] Japanisches N2-Zertifikat, Vorbereitung für einige zukünftige Pläne in Japan, werde ein separates Modul im Wochenrückblick öffnen, um den Lernfortschritt zu überprüfen, könnte für die Juli-Prüfung pauken, ~~wenn nicht, im Dezember erneut versuchen~~
- [ ] CKAD-Zertifikat, letztes Jahr zur Hälfte vorbereitet, aber vergessen, mich später für die Prüfung anzumelden und zu kaufen, ohne Druck wurde ich tatsächlich faul
- [ ] Code zu mehr Open-Source-Projekten beitragen, erfordere keine Menge, aber hoffe auf mehr bedeutungsvolle Einreichungen
- [ ] Eine Showcase-Website für mein Open-Source-Toolbox-Projekt "[Yu Tools](https://github.com/pseudoyu/yu-tools)" schreiben und Nutzungserfahrungen für die Software- und Hardware-Artikel darin schreiben (ein großes Projekt), kontinuierlich optimieren und iterieren
- [ ] Das Open-Source-Guide-Projekt "[Blockchain Guide](https://guide.pseudoyu.com/)" verbessern, mehr von den blockchain-zugrundeliegenden und Web3-bezogenen Projekterfahrungen und Ingenieurerfahrungen aus Arbeit und Studium des letzten Jahres abdecken, beschämenderweise wurden die meisten Artikel geschrieben, als ich für meinen Master in Hongkong studierte
- [ ] Das Side Project-Startup-Projekt, das ich mit Freunden mache, erfolgreich starten und kontinuierlich optimieren
- [ ] Mehr interessante Technologien erkunden, sie weiterhin genießen
- [ ] Mehr interessante Menschen treffen
- [ ] Gut weiterleben

## Persönliche Lebensfragmente

Seit der schweren Epidemie in Peking im November lebe ich seit zwei Monaten zu Hause. Vielleicht habe ich anständige körperliche Verteidigungsattribute (ich beziehe mich darauf, das einzige bisschen Medizin, das ich zur Hand hatte, einem Freund zu schicken, mich rein darauf verlassend, nicht auszugehen, um mich vor dem Virus zu isolieren) und Glückspunkte (jeden Tag wie gewohnt Essen bestellen und sogar Hausverwaltung für einen Nachmittag zu meinem Haus kommen lassen, um sich mit einem Wasserleck zu befassen), es ist mir gelungen, bis jetzt negativ zu bleiben, schon in der letzten Runde.

Aber die Konsequenz ist, dass Freunde, die sich bereits erholt haben und negativ geworden sind, überall hinreisen, während ich immer noch voll bewaffnet bin, nur um den Müll rauszubringen, geschweige denn wage, weit zu reisen. Also verbrachte ich diese zwei Monate mit meiner Katze.

Obwohl ich tatsächlich zu Hause bleibe, schien es, als die Epidemie sich öffnete, kein Ende in Sicht. Also wurde meine Denkweise entspannter. An diesem Wochenende wurde ich eingeladen (~~nicht wirklich, nur unter dem Vorwand, mit meiner Katze zu Besuch zu kommen~~), zum Haus von Senior Bo Yi zum Abendessen zu gehen. Ich atmete die nicht so frische Luft draußen ein (~~immerhin ist es Peking~~) und aß auch selbstgekochte Mahlzeiten, die ich lange nicht mehr hatte. Ich faulenzte den ganzen Tag herum, fühlte mich aber zufrieden und glücklich.

![wonderful_meal_with_boyi](https://image.pseudoyu.com/images/wonderful_meal_with_boyi.jpg)

Ich plane, am 18. Januar nach Hangzhou zurückzukehren. Tatsächlich war meine Zeit zu Hause im Jahr 2022 im Vergleich zu den letzten Jahren nicht kurz. Mit verschiedenen angepassten Feiertagen und Urlauben summierte es sich auf etwa einen Monat vor und nach dem Nachhausegehen. Es ist nur so, dass die Epidemie oft wiederkehrte und ich keine Chance hatte, in meine Heimatstadt zurückzukehren. Vor zwei Jahren im Januar starb meine Großmutter, und ich steckte aufgrund der Epidemie in Hongkong fest und konnte nicht nach Hause gehen. Letztes Frühlingsfest war ich wieder in Peking gestrandet aufgrund eines plötzlichen Ausbruchs. Es ist Zeit, zurückzugehen und zu sehen. Je älter ich werde, desto mehr Orte besuche ich, aber die Heimat scheint immer weiter weg zu rücken.

Ich habe eine Weile gezögert, nach Hause zu gehen, besorgt über mögliche Veränderungen, aber ich möchte trotzdem zurückgehen und sehen. In dieser Situation fühle ich mich jedoch nicht wohl dabei, meine Katze in einem Tierhotel oder bei unbekannten Personen zu lassen. Später, als ich dies beiläufig während eines Meetings erwähnte, fand ich eine Lösung. Ich beschloss, Nini im Haus des kleinen Leiters meines Projekts unterzubringen. Seine Tochter hat schon lange eine Katze im Auge. Nachdem dies geklärt war, fühlte ich mich endlich erleichtert.

Mit all diesen Schwierigkeiten werde ich mich wahrscheinlich infizieren. In dem Wissen gab mir Senior Bo Yi ein luxuriöses Anti-Epidemie-Geschenkpaket, was rührend war.

![medicines_from_boyi](https://image.pseudoyu.com/images/medicines_from_boyi.jpg)

Dann vor einer Weile, als Senior Bo Yi im Lingyin-Tempel war, machte sie einen Wunsch für mich: "Möge 2023 dir erlauben, das zu tun, was du magst, und mehr Hobbys nach deinem Wunsch zu erkunden." Sie brachte mir auch ein schönes buddhistisches Armband mit. Ich erkläre sie einseitig zur besten Seniorin der Welt. Ich hoffe, das neue Jahr wird auch für sie gut sein.

Plötzlich erinnerte ich mich daran, dass ich, als ich an der Universität war, mehr als ein Jahr lang ein buddhistisches Armband vom Lingyin-Tempel trug, das Ni mir gegeben hatte, bis die Schnur fast abgenutzt war und die Perlen kurz davor waren, abzufallen, bevor ich es wegpackte. Ich fühlte mich seltsamerweise tatsächlich in jenem Jahr glücklicher. Manchmal braucht man vielleicht einfach etwas Seelenfrieden.

Ich werde zurückgehen, um den Wunsch zu erfüllen, einen doppelten Wunsch.

![wonderful_gift_with_boyi](https://image.pseudoyu.com/images/wonderful_gift_with_boyi.jpg)

## Sonstiges

Dieser Abschnitt wird einige meiner Inputs und Outputs sowie andere Dinge, die ich interessant finde, aufzeichnen.

Diese Woche habe ich zwei sehr berührende Videos auf Bilibili gesehen. Eines ist von meinem Lieblings-Up主 "[Xiaolu Lawrence](https://space.bilibili.com/37029661)" mit dem Titel "[Dies ist mein fleißigstes Jahr, aber es ließ die Firma um die Hälfte schrumpfen | Jahresend-Zusammenfassung 2022](https://www.bilibili.com/video/BV1Mx4y1G7zW)". Ich hatte einige Gedanken:

> Ich schaue seit mehreren Jahren in Folge und sehe mir diese zurückhaltende Jahresend-Zusammenfassungsspalte immer wieder viele, viele Male an.

> Ich habe Mitgefühl empfunden, als ich in der gleichen Phase war, wurde von einigen Videos bewegt; ich war viele, viele Tage glücklich, als Lu-ge auf meine Dynamik antwortete und mich ermutigte; Öfter begleitete er mich durch eine Nacht nach der anderen, aufwachend, um mit Anstrengung weiterzuleben. Vielleicht aufgrund der Vertrautheit ließen mich die leichte Pause beim ersten Öffnen der neuen Studiotür, das Stocken beim Sagen "weil die Unterstützung der Familie einmal dein Vertrauen war", die BGM des Blumenstraußes, das bittere Lachen beim Rückblick auf dieses Jahr, alle meine Emotionen schwanken und Tränen fließen.

> "Es ist nicht so, dass du dich verändert hast, als du erwachsen wurdest, sondern dass du erwachsen geworden bist, und die Welt begonnen hat, dir all ihre Wahrheiten zu offenbaren". Vielleicht ist die oft beschriebene Jugendlichkeit und studentische Ausstrahlung über mich nur die Überziehung des Glücks, das ich in der Vergangenheit erlebt habe, und der Schutz derer um mich herum, der es mir erlaubt, in meinen Wochenberichten immer wieder über mich selbst zu sprechen, immer wieder nach Schönheit zu streben. Und im Jahr 2022 ist alles wieder zum Ausgangspunkt zurückgekehrt. Glücklicherweise behalte ich immer noch die Gewohnheit des "Aufzeichnens" bei und habe die Fähigkeit zu "fühlen" nicht verloren. Klein, aber wertvoll.

> "Dieses Jahr habe ich zu viel verloren, zu viel. Jeder kleine Tod und Zusammenbruch wird unerträglich". Ja, 2022 war einfach zu schwierig, unbeschreiblich. Im neuen Jahr muss ich mich anstrengen, allein zu leben.

> Danke, Lu-ge, für deine Begleitung und die Emotionen, die du im vergangenen Jahr gebracht hast. Im neuen Jahr lasst uns weitermachen!

Es gibt auch einen sehr scharfsinnigen Up主 "[Lao Jiang Ju Kao Pu](https://space.bilibili.com/119801456)" mit "[Verabschiede dich von dem unbeschreiblichen und unnötigen Jahr - Meine Neujahrsansprache](https://www.bilibili.com/video/BV17M411y7es)". Meine Gedanken:

> Ich mag Lao Jiangs Denkweise und Erzählstil wirklich, schlicht, aufrichtig, aber mutig und nicht ohne Schärfe. Es ist die beste Neujahrsansprache, die ich gesehen habe.

> 2022 ist einfach so vorbeigegangen, viele Dinge können nicht gesagt werden, viele Dinge passieren, viele Dinge werden nie wieder passieren, unbeschreiblich ist wahrscheinlich die beste Beschreibung.

## Zusammenfassung

Die erste Woche des Jahres 2023, dieses Jahr hat einen ziemlich guten Start hingelegt.