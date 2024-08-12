---
title: "Wochenrückblick #67 - Neugestaltung meines Informationseingabesystems mit Follow"
date: 2024-08-05T05:30:00+08:00
draft: false
tags: ["review", "life", "tools", "follow", "work", "painting", "programming"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/photograph.mp3" caption="'Photograph - Ed Sheeran'" >}}

## Vorwort

![weekly_review_20240805](https://image.pseudoyu.com/images/weekly_review_20240805.png)

Dieser Beitrag ist eine Aufzeichnung und Reflexion meines Lebens vom `31.07.2024` bis zum `04.08.2024`.

Die erfreulichste Erfahrung dieser Woche war das Ausprobieren von Follow, einer Anwendung, die mich nach langer Zeit wieder begeistert hat. Ich habe es mit Readwise verglichen und beschlossen, mein Abonnement zu kündigen. Außerdem habe ich eine selbst gehostete Web-Archive-Lösung implementiert, und es fühlte sich großartig an, mein eigenes Produkt zu nutzen. Ich arbeitete weiter mit meinem Senior an dem Wandgemälde, und es gab viele andere interessante Ereignisse.

## Neugestaltung meines Informationseingabesystems mit Follow

### Mein Informationseingabesystem

Vor langer Zeit war ich stark informationsabhängig. Wann immer ich auf gute Blogs oder Nachrichtenseiten stieß, fügte ich sie schnell zu meinen RSS-Feed-Quellen hinzu und freute mich über die ordentlich kategorisierte und getaggte Liste. Wenn ich gute Newsletter fand, abonnierte ich sie sofort mit meiner E-Mail-Adresse. Das Erste, was ich jeden Morgen tat, war, die ungelesenen Einträge in Reeder 4, das ich damals benutzte, zu löschen und dann die Newsletter-E-Mails der Reihe nach durchzusehen.

Anfangs schien es in Ordnung zu sein. Ich war zufrieden, dass ich alle Nachrichten und Artikel, die mich interessierten, lesen konnte, sobald sie verfügbar waren. Aber nach und nach wurde es überwältigend. Ich verbrachte jeden Morgen immer mehr Zeit damit, zwang mich sogar dazu, Artikel zu verdauen, die mich nicht interessierten. Anstatt Informationen zu erwerben, wurde es mehr zu einem Verlangen nach Informationen und einer Kompensation für Informationsangst. Die Wirkung war natürlich da - die Informationen hinterließen Spuren in meinem Gehirn, aber die Effizienz der Verdauung war nicht hoch.

Nachdem ich die Artikel "Using Automated Workflows to Aggregate Information Intake and Output" und "Saying No to Newsletters" gelesen hatte, nahm ich erhebliche Anpassungen vor.

In Bezug auf Informationsquellen meldete ich mich von allen WeChat-Offiziellen-Konten und Newslettern ab und reduzierte meine RSS-Feed-Quellen auf etwa 50. Der größte Teil der verbleibenden Eingaben kam von Twitter und den Telegram-Kanälen anderer Leute, was in gewissem Maße Informationskokonabildung vermied und gleichzeitig die Eingabe unter Kontrolle hielt.

Darüber hinaus synchronisiere ich durch die Verwendung von n8n + Telegram-Kanal zum Aufbau eines automatischen Synchronisationssystems für Ein- und Ausgabequellen alle meine gefilterten Informationsquellen automatisch mit meinem Telegram-Kanal "Yu's Life", was es mir bequem macht, sie anzusehen und zu überprüfen. Es dient auch als persönlicher Sharing-Kanal. Der Druck der Öffentlichkeit motiviert mich auch umgekehrt dazu, Informationsquellen sorgfältiger zu filtern.

Diese Lösung hat jedoch immer noch zwei Probleme:

1. Sie hat das Problem meiner verstreuten Informationsquellen noch nicht gelöst. Ich muss häufig zwischen Twitter und verschiedenen TG-Kanälen wechseln, was leicht ablenkt und dazu führen kann, dass ich einige Nachrichten verpasse.
2. Ich benutze den Kanal oft in gewissem Maße als mein Lesezeichen. Manchmal sind viele Informationen sehr persönlich, und mit der wachsenden Zahl der Follower des Kanals habe ich auch einen gewissen psychologischen Druck und befürchte, für andere zu Informationsrauschen zu werden.

Das Aufkommen von Follow füllt genau diese Lücke in meiner Lösung.

### Follow

#### Einführung

> Next generation information browser

Dies ist Follows Slogan. Vor seiner Veröffentlichung betrachtete ich es lediglich als eine Alternative zu RSS-Readern. Obwohl ich mit RSSHub vertraut war und meine selbst bereitgestellte Instanz intensiv nutzte, konnte ich mir immer noch nicht vorstellen, wie viel Entwicklungsspielraum es basierend auf diesem alten Protokoll geben könnte, bis ich nach seiner Veröffentlichung und einigen Tagen intensiver Nutzung dieses Konzept allmählich verstand.

In der heutigen Zeit, in der RSS bereits im Niedergang begriffen ist, behalten abgesehen von unabhängigen Blogs, die sich in einer ähnlichen Situation befinden und fast alle noch vollständige RSS-Unterstützung beibehalten, die meisten Nachrichten-, Informations- und verschiedene Nischenwebsites sie nicht mehr bei. RSSHub ist dann die perfekte und fast einzige Lösung, die Webinformationsquellen einschließlich, aber nicht beschränkt auf Twitter, TG Channel, Bilibili und NetEase Music-Playlisten in ein Standard-RSS-Format umwandeln kann, sodass diese Informationsquellen wie das Abonnieren von Artikeln aktualisiert werden können.

RSSHub ist jedoch immer noch eher ein Middleware-Tool. Selbst mit standardisierten RSS-Daten können die meisten Reader nur Textanzeigen verarbeiten, und die Behandlung von Audio, Video und Bildern bleibt im Grunde genommen auf der Ebene, sie als URL zu behandeln. Daher wende ich es meist in meinem n8n-Synchronisations-Workflow als Benachrichtigung an, behalte nur seinen Titel und Link bei und klicke immer noch auf den Quelllink, um zur entsprechenden Webseite zu springen, um sie anzusehen, was sich oft etwas unzusammenhängend anfühlt.

Follows größtes Merkmal ist natürlich die Vererbung der "alles kann RSS sein" Philosophie von RSSHub, die auf der Anwendungsebene Präsentationsmethoden für verschiedene Inhaltsformen wie Videos, Bilder, Blog-Audio, Artikel, soziale Medien usw. bietet. Es fühlt sich wirklich wie ein Sprung von reinem HTML zu modernen CSS-Effekten an, nachdem man es lange Zeit betrachtet hat. Eigentlich ist es keine sehr hohe technische Hürde, diesen Schritt zu erreichen. Ob es sich um Video-iFrame, Audio-Player oder Bildvorschau handelt, es gibt relativ ausgereifte Komponenten zur Verwendung. Aber Follow ist fast das einzige Produkt, das sich immer noch auf dieses Protokoll konzentriert und es gut macht. Manchmal reicht es aus, etwas besser zu machen.

#### Erfahrung

![follow_homepage](https://image.pseudoyu.com/images/follow_homepage.png)

Als Informationsbrowser/Reader sind die intuitivsten und wichtigsten Aspekte die Benutzeroberfläche und Interaktion. Die Kombination von DIYGod + Shiyier setzte meine Erwartungen von Anfang an auf das Höchste, aber selbst die erste Beta-Version überraschte mich immer noch mit ihrer Vollständigkeit und Erfahrung. Davor sollte Reeder 4 das modernste gewesen sein, und Follow, obwohl es Electron und nicht rein nativ ist, behält immer noch ein äußerst exquisites Design und Interaktion bei.

Ich habe zuvor mehrere Reader verwendet, darunter NetNewsWire, Reeder 4, Miniflux und Readwise Reader, aber weil die Leseerfahrung oft nicht so gut war wie die ursprüngliche Webseite, habe ich mich meist dafür entschieden, zum Link zu springen, um anzusehen. Die Seiten und Interaktionen von Follow selbst lassen mich es jedoch genießen. Es gibt auch eine interessante Anzeige der kürzlich gelesenen Geschichte, wo man sehen kann, welche Besucher diesen Artikel gelesen haben, und man kann in ihre Homepage klicken, um ihre Abonnements zu sehen, was soziale Attribute und Informationsquellen-Akkumulation kombiniert. Ich habe durch diese Methode viele persönliche Blogs entdeckt, auf die ich vorher nicht geachtet hatte.

Darüber hinaus kann Follow aufgrund seiner tiefen Integration mit RSSHub durch Eingabe von Twitter-Handle, Bilibili-uid und YouTube-Kanalnamen direkte Abonnements von sozialen Medien erreichen, ohne den entsprechenden Weg in der Dokumentation der RSSHub-Website finden oder eine eigene Instanz einrichten zu müssen, was sehr benutzerfreundlich ist.

![follow_pic](https://image.pseudoyu.com/images/follow_pic.png)

![follow_video](https://image.pseudoyu.com/images/follow_video.png)

Die direkte Anzeige von Videos und Bildern ist auch ein Highlight. Ich habe gesehen, wie ein Benutzer die Twitter-Accounts einiger Designer als Quelle für Designinspiration und ästhetische Akkumulation nutzt, was auch ein sehr sinnvolles Anwendungsszenario ist.

Audio/Podcasts können global in Follow abgespielt werden. Zum Beispiel spielte ich in der unteren linken Ecke der vorherigen Screenshots gleichzeitig eine Episode von "Beyond Code" ab. Dies löst auch das Problem, dass ich wiederholt zwischen mehreren Podcast-Apps wie Apple Podcast, Spotify und Xiaoyuzhou wechseln musste.

Sie können auch bequem Ihre Abonnements teilen: <https://web.follow.is/profile/pseudoyu>

Es gibt tatsächlich noch einige weitere Designs, wie das Action-Modul und Power-Tipping, aber dieser Artikel ist keine Software-Rezension, sondern eine persönliche Erfahrung, daher werde ich nicht zu sehr ins Detail gehen. Sie können es selbst erleben, wenn es später geöffnet wird, und einige Überraschungen behalten. Als Nächstes möchte ich über den Vergleich mit Readwise Reader, den ich derzeit verwende, sprechen und warum ich plane, zu Follow zu wechseln.

#### Readwise Reader -> Follow

![readwise_sub](https://image.pseudoyu.com/images/readwise_sub.png)

Ich habe etwa im September letzten Jahres die Readwise Full Mitgliedschaft abonniert. Obwohl es einen 50%igen Rabatt für Entwicklungsländer bietet, kostet es immer noch fast $50 pro Jahr. Es ist umfassend, aber die Kernfunktionen, die ich nutze, sind tatsächlich nur drei Punkte:

1. RSS-Reader
2. Später lesen, Artikel speichern und Hervorhebungen annotieren
3. Tägliche Zusammenfassung

Darunter ist der erste Punkt der häufigste, als bequemer Reader zur Verwaltung meiner Artikelabonnements usw. Es hat auch eine mobile App zum Lesen jederzeit. Während der Nutzung stellte ich jedoch fest, dass manchmal der Anzeigestil und das Laden von Bildern nicht sehr gut sind und die Klassifizierung und Verknüpfungen etwas zu komplex sind. Es unterstützt hauptsächlich Artikel, was offensichtlich vollständig durch Follow ersetzt werden kann (warte auf eine mobile App).

Ich habe früher ziemlich oft Hervorhebungsanmerkungen verwendet, mit Plugins einige Notizen zu einigen Artikeln gemacht und sie in Readwise gespeichert, dann meine Artikel durch n8n zum Telegram-Kanal synchronisiert. Aber es ist tatsächlich ein bisschen zu abhängig von der Plattform. Wenn ich diese hervorgehobenen Notizen wirklich verdauen und in einige geformte Ideen oder Artikel organisieren möchte, muss ich zu Readwise zurückkehren, um sie anzusehen. Selbst wenn ich sie zur Organisation mit Logseq oder Heptabase synchronisiere, ist es immer noch nicht bequem. Besonders jetzt, da ich zu Apple Notes als mein Haupt- und einziges Notizwerkzeug gewechselt bin, stellte ich fest, dass das direkte Exzerpieren/Aufzeichnen einiger Ideen am effizientesten ist und eher Wert generiert. Daher verschwand die Hervorhebungsfunktion allmählich aus meinem Notizworkflow.

![save_website](https://image.pseudoyu.com/images/save_website.jpg)

Wie wir alle wissen, entwickelt sich "Später lesen" oft zu "Nie später lesen", also ist meine aktuelle Strategie, fast nie "Später lesen" zu verwenden und zu versuchen, es sofort zu lesen, soweit es möglich ist, mit nur sehr wenigen längeren Artikeln, die vorübergehend gespeichert werden, und zu versuchen, die Liste am selben Tag zu löschen. Jetzt verwende ich den ungelesenen Modus als Standardanzeige in Follow, oft durchstöbere ich es. Wenn ich auf einen Artikel stoße, der mich interessiert und den ich durchgelesen habe, verwende ich die Sternchen-Funktion, um ihn in meinen Favoriten zu speichern. Wenn ich fertig gelesen habe und etwas gewonnen habe, verwende ich ein von mir erstelltes Browser-Plugin + Cloudflare Worker API + n8n, um den Artikel-Link und die Quell-HTML-Datei in der D1-Datenbank zu speichern, wodurch ich Web-Archivierung erreiche und automatisch mit meinem Telegram-Kanal synchronisiere.

Der dritte Punkt, die tägliche Zusammenfassung, hilft mir, einige meiner Notizen oder Artikel zu überprüfen. Dies ist nützlich, aber nicht hochfrequent. Ich habe nicht im Detail recherchiert, ob das Follow Action-Modul einige Operationen an mehreren Artikeln durchführen kann.

Da meine Kernbedürfnisse alle auf Follow übertragen werden können, habe ich mich entschlossen, Readwise abzubestellen. Ich kann deutlich spüren, dass sich mein Informationsaufnahmevolumen und die Qualität in diesen wenigen Tagen auch erheblich verbessert haben. Eine gute Software ist tatsächlich nicht nur ein Hilfsmittel, sie hat einen tiefgreifenderen Einfluss auf Denken und Gewohnheiten.

## Persönliche Lebenssplitter

### Electron-Fehler

![talk_with_innei](https://image.pseudoyu.com/images/talk_with_innei.jpg)

Ich habe gerade entdeckt, dass es ein Problem mit der Follow-Client-Aktualisierung gibt.

Das Klicken auf "Zum Neustart klicken" versteckt das Fenster, anstatt es zu beenden. Es ist ein vertrauter Fehler, ich habe genau den gleichen geschrieben, als ich EpubKit entwickelte 🤣 Ich habe es Shiyier gemeldet, es ist wie der Austausch von Electron-Krankheitserfahrungen.

### macOS Desktop-Dekoration

![macos_widgets](https://image.pseudoyu.com/images/macos_widgets.png)

Dies ist mein erster Versuch mit macOS-System-Desktop-Widgets. Es ist ziemlich frisch, aber ich wechsle im Grunde genommen Anwendungen mit Raycast-Verknüpfungen und sehe den Desktop kaum jemals...

### Garagenwandmalerei

![car_painting_week2](https://image.pseudoyu.com/images/car_painting_week2.jpg)

Gesamtfortschritt diese Woche: 20%, es nimmt bereits Gestalt an.

Mein Fortschritt diese Woche: fünf oder sechs Ziegel bemalt 🤣

## Interessante Dinge und Objekte

### Eingabe

Obwohl die meisten interessanten Eingaben automatisch im "Yu's Life" Telegram-Kanal synchronisiert werden, wähle ich immer noch einen Teil aus, um ihn hier aufzulisten, was sich mehr wie ein Newsletter anfühlt. Und ich habe einen Microblog - "daily.pseudoyu.com" unter Verwendung von Telegram-Kanalnachrichten als Inhaltsquelle erstellt, was bequemer zu durchsuchen ist.

#### Sammlungen

- [pseudoyu | Follow](https://web.follow.is/profile/pseudoyu)
- [DIYgod | Follow](https://web.follow.is/profile/DIYgod)
- [n8n Chinesisches Tutorial | Einfach und leicht verständliche moderne Magie](https://n8n.akashio.com/)
- [Dengtab - Bleiben Sie fokussiert und reduzieren Sie soziale Medien-Ablenkungen, während Sie kleine Gewohnheiten kultivieren.](https://dengtab.com/)
- [SixD - SwiftUI & Interaktionsdesign](https://www.haolunyang.com/sixd)
- [ccbikai/BroadcastChannel](https://github.com/ccbikai/BroadcastChannel)

#### Podcasts

- [Folge 10 | Affenkönig vom Blumen-Frucht-Berg spricht über Karriereentscheidungen, wie man sich durch Verkauf etabliert, Wohnmobilreisen und neues Leben in Großbritannien](https://www.listennotes.com/e/7f2efa4ad8394de79591a3ee2da6a5d1)
- [Ep 48. Exklusives Interview mit Gao Tian: Um ein guter Bilibili-Uploader zu sein, wurde ich Python-Kernentwickler](https://www.listennotes.com/e/5e5454656bb146499bef687dcec00e65)

#### Artikel

- [Fastenaufzeichnung](https://blog.douchi.space/intermittent-fasting/#gsc.tab=0)
- [Einige Erforschungen zur De-Cloudflare-isierung von WebP-Cloud-Diensten](https://blog.webp.se/de-cloudflarize-zh/)
- [P5r: Das Leben hat sich verändert](https://jesor.me/2024/persona5r-life-changed/)
- [Reflexionen inmitten der Geschäftigkeit: Leben, Arbeit und Unterhaltung - Ruhiger Wald](https://innei.in/notes/175)
- [Mein Verständnis von Cloud Native](https://gist.github.com/sljeff/cce768194a9e68d5279bfde861ff5f76)
- [Wie Stripe Zahlungen sicher sammelt und Betrug und Kartentests vermeidet](https://dmesg.app/stripe-fraud.html)

#### Videos

- [Eine Auszeit von der Schule nehmen + Millionen-Yuan-Jahresgehalt ablehnen, Leben ist nicht nur etwas zu erreichen](https://www.bilibili.com/video/BV1dx4y1x7mz)
- [Lerne mit mir - HTMX und HonoJS](https://www.youtube.com/watch?v=hMcE8E8JjXA)
- [【He Tongxue】Du kannst nie wieder in den Sommer zurückkehren, als du 19 warst...](https://www.bilibili.com/video/BV15b42177rL)
- [In 450 Tagen zum Python-Kernentwickler werden](https://www.bilibili.com/video/BV1of421972c)
- [Nach 10 Jahren, 9 Millionen](https://www.bilibili.com/video/BV1jT42167Xb)

#### Filme

- [**Drifting**](https://movie.douban.com/subject/35956190/), Ich mag wirklich die Kinematographie der Autobahnstau-Szene am Ende, das Leben ist nichts als Stopps und Starts.