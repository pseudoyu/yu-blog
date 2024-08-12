---
title: "Wochenrückblick #65 - Adventure X Erlebnis, Apple Notes Praxis und EpubKit"
date: 2024-07-21T08:30:00+08:00
draft: false
tags: ["review", "life", "adventurex", "hackathon", "epubkit", "work", "apple notes"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/photograph.mp3" caption="'Photograph - Ed Sheeran'" >}}

## Vorwort

![weekly_review_20240721](https://image.pseudoyu.com/images/weekly_review_20240721.png)

Dieser Beitrag zeichnet mein Leben vom 10. bis 21. Juli 2024 auf und reflektiert darüber.

Diese anderthalb Wochen waren recht ereignisreich. Die Arbeit war etwas geschäftig. Ich nahm am Adventure X Event teil, was sehr viel Spaß machte. Ich experimentierte mit dem Remix-Framework und bereitete einen Workshop vor. Ich traf mich mit Randy, und gemeinsam planten wir die Neugestaltung und anschließende Entwicklung von EpubKit, im Grunde hielten wir unseren eigenen Hackathon für uns "Mittelalter-Hippies" ab, die nicht am Wettbewerb teilnehmen konnten. Ich wechselte von Obsidian zu Apple Notes und implementierte P.A.R.A. Ich plane, die Wände meiner Garage zu streichen. Ich besuchte den Apple Store, um das Apple Vision Pro zu erleben. Und es gab viele andere interessante Ereignisse.

## Adventure X

Dies war ein Hackathon-Event für junge Entwickler bis 26 Jahre. Ich hatte früh davon gehört, war aber leider knapp über der Altersgrenze für eine Teilnahme. Allerdings wurde ich eingeladen, als Juror für den von OpenBuild gesponserten "Web 3.0 Development Tools" Track zu fungieren und vor Ort als Workshop-Leiter tätig zu sein, was mir ermöglichte, den gesamten Prozess zu beobachten.

Das Event zog fast 200 Entwickler an, und ihre Energie und Leidenschaft waren spürbar (vielleicht macht die 26-Jahre-Altersgrenze doch Sinn). Ich traf auch viele bekannte Gesichter von Twitter und "Crazy Thursday" und führte interessante Gespräche mit mehreren neuen und alten Freunden.

### Workshop

![adventurex_workshop](https://image.pseudoyu.com/images/adventurex_workshop.jpg)

Meine Hauptaufgabe bestand darin, als Mentor und Workshop-Leiter zu fungieren, mit dem Thema "Entwicklung einer Full-Stack AdventureX Badge ÐApp mit Solidity und Remix".

Ich habe schon recht viele Lektionen und Workshops in verschiedenen Umgebungen gegeben. Anfangs half ich nur Ians OpenBuild-Community, da ich gerne Tutorials schreibe und Wissen teile. Aber als diese Gelegenheiten häufiger wurden, bemerkte ich einige Veränderungen an mir selbst. Ich verwende nicht mehr die gleichen Folien, um ähnliche Inhalte jedes Mal zu wiederholen. Stattdessen betrachte ich jede Gelegenheit als neue Lernmöglichkeit für mich selbst, fordere mich heraus, innerhalb einer begrenzten Zeit etwas Interessantes zu erschaffen und es dann zu lehren. Es ist eine Art Praxis der Feynman-Lerntechnik.

Für diesen Workshop wollte ich das Remix-Frontend-Framework erlernen. Ich schrieb eine einfache ÐApp zum Beanspruchen von Event-Badges. Sie können sie unter "adventure-x.pseudoyu.com" erleben, und die PPT-Folien sind unter "AdventureX_Workshop_20240716.pdf" verfügbar.

Obwohl ich etwa einen Monat im Voraus von diesem Workshop wusste, verschob ich ihn unvermeidlich bis auf die letzten paar Tage. Ich verbrachte einen Abend damit, aus Randys "Remix Practical Guide" Booklet zu lernen und den UI-Teil fertigzustellen. Am nächsten Abend schrieb ich den Solidity-Vertragsteil und beendete die Interaktionslogik zwischen dem Frontend und dem Vertrag, dann stellte ich es online mit Zeabur. Prokrastination ist wirklich ein Killer.

Aber Remix ist in der Tat benutzerfreundlich. Ich schaffte das Kunststück, eine Anwendung mit null useEffect und null useState zu erstellen. Ich überlege, ob es in Zukunft in verschiedenen Szenarien Next.js vollständig ersetzen kann.

Vor Ort erschienen mehr Leute als ich erwartet hatte. Der Workshop dauerte doppelt so lange wie die geplanten 45 Minuten und endete kurz vor 22 Uhr. Es war jedoch eine interessante Erfahrung, und der Workshop war recht erfolgreich.

### "Mittelalter-Hippie" Hackathon

![code_with_randy_hackathon](https://image.pseudoyu.com/images/code_with_randy_hackathon.png)

Randy kam auch als Gastjuror aus Guangdong. Wir beide fanden, dass es etwas zu langweilig war, nur die Hackathon-Atmosphäre zu beobachten, also beschlossen wir, gemeinsam an der Neugestaltung von EpubKit zu arbeiten.

Wir diskutierten die aktuelle Betriebslogik und UI-Stiländerungen für das gesamte EpubKit. Es war sehr angenehm. Wir verbrachten mehrere Stunden damit, am Abend gemeinsam zu entwickeln und fanden ein Gefühl der Teilnahme als "Mittelalter-Hippies". Wir diskutierten auch viele Ideen und Arbeitsteilung für die Zukunft des Produkts, auf die ich mich freue.

Jeder ist herzlich eingeladen, [EpubKit](https://epubkit.app/) herunterzuladen und zu erleben, um Ihre eigenen E-Books zu erstellen.

![yu_with_randy](https://image.pseudoyu.com/images/yu_with_randy.jpg)

Als jemand, der nicht gerne fotografiert wird, wurde ich zufällig von den Mitarbeitern aufgenommen, während ich mit Randy Projektausstellungen betrachtete. Es ist ein ziemlich denkwürdiges Foto.

## P.A.R.A-Praxis basierend auf Apple Notes

Letzten Monat wechselte ich von Logseq, das ich zwei Jahre lang benutzt hatte, zu Obsidian. Nach etwa einem Monat Praxis entwickelte ich mehr Aufzeichnungsgewohnheiten im Vergleich zu der Zeit, als ich Logseq benutzte. Obwohl ich mir keine Gedanken mehr über Ordnerhierarchien und dergleichen machen muss, muss ich immer noch die mentale Belastung überwinden, die durch die Kette von "Ideen im Kopf aufzeichnen" -> "warten, bis ich am Computer bin, um eine neue Datei zu erstellen und ihr einen Titel zu geben" -> "Ideen organisieren und Tags hinzufügen" -> "den Inhalt aufschreiben" entsteht.

![apple_notes_folders_20240721](https://image.pseudoyu.com/images/apple_notes_folders_20240721.png)

Randy erzählte mir von seiner Methode, Apple Notes zu verwenden, um alle Ideen und Notizen aufzuzeichnen und sie durch die P.A.R.A-Hierarchie zu kategorisieren. Ich stellte fest, dass es mehr Lust zum Aufzeichnen gibt, wenn es keine Belastung durch Organisation gibt und man einfach jederzeit sein Telefon/Computer öffnen kann, um Ideen aufzuzeichnen, ohne sich Gedanken über Format oder Markdown-Syntax zu machen. Und in der Lage zu sein, aufzuzeichnen und zu handeln, ist der Kernzweck des Notizenmachens.

Auf dem Mac können Sie Quick Notes in der unteren rechten Ecke für schnelle Aufzeichnungen verwenden. Auf iOS können Sie Shortcuts verwenden, um flüchtige Ideen schnell im Entwurfsverzeichnis zu speichern. Später, wenn Sie mehr Ideen haben, können Sie sie in verschiedene Verzeichnisse verschieben. Es ist eine einfache, aber effektive Praxis, die nicht erfordert, verschiedene Tags und Kategorien anzugeben. Bei Bedarf können Sie einfach die Volltextsuche verwenden.

## Sonstige Angelegenheiten

### Wandmalerei

![car_painting_wall](https://image.pseudoyu.com/images/car_painting_wall.jpg)

Nachdem ich Ölmalerei gelernt und letztes Mal ein Porträt gemalt hatte, fand ich es sehr interessant. Kürzlich beschloss ich, mich wieder mit etwas Lustigem herauszufordern. Gemeinsam mit meinem Senior planen wir, eine ganze Zementwand in der Autowerkstatt meines Vaters mit Acrylfarbe zu bemalen (ich werde der Assistent sein).

Wir schickten die Ideen meines Vaters und Referenzbilder, die wir auf Instagram gefunden hatten, an DALL-E, und der generierte Effekt ist ziemlich gut. Ich hoffe, wir können das fertige Produkt im August haben 🤩.

### Apple Vision Pro

![apple_vision_pro_experience](https://image.pseudoyu.com/images/apple_vision_pro_experience.jpg)

Am Donnerstag dieser Woche ging ich zu Apple West Lake, um das Vision Pro zu erleben. Tatsächlich hatte ich sehr früh darauf geachtet und viele Rezensionen gesehen. Ich war an einem Punkt ziemlich versucht, aber nachdem ich die Erfahrung gemacht hatte, dass meine Quest 2 Staub ansetzte, war ich immer noch unentschlossen.

Zufälligerweise wurde auch die chinesische Version eingeführt, also vereinbarte ich einen halbstündigen Termin zum Ausprobieren. Von der Anpassung der Linsen, der Erklärung des Zubehörs bis hin zum Erleben verschiedener Funktionen und Anwendungen war die Erfahrung besser als ich mir vorgestellt hatte. Ich verspürte in den etwa 20 Minuten keinerlei Schwindel oder Druck durch das Gewicht.

In der tatsächlichen Erfahrung war die Interaktion flüssiger, natürlicher und genauer als ich mir vorgestellt hatte. Allerdings gab es noch recht auffälliges Rauschen im Bild, und die Auflösung reichte nicht für ein immersives Erlebnis aus, obwohl es recht beeindruckend war. Es gibt immer noch zu wenige unterstützte Anwendungen, so dass es eher eine Neuheitserfahrung ohne viele Anwendungsszenarien ist. Die Tipperfahrung ist schlecht, so dass immer noch eine externe Tastatur benötigt wird. Insgesamt ist diese Generation nicht kaufenswert. Vielleicht werden wir es in Zukunft in Betracht ziehen, wenn sowohl der Preis als auch die Systemanwendungsschicht ausgereifter sind.

### ChatGPT Plus -> Claude Pro

![claude_pro_sub](https://image.pseudoyu.com/images/claude_pro_sub.jpg)

Letzten Monat abonnierte ich aufgrund der hohen Nutzungsfrequenz erneut ChatGPT Plus, während ich Claude 3.5 Sonnet unter dem kostenlosen Kontingent nutzte. Ich stellte fest, dass Claudes kontextuelles Verständnis und die Verwendbarkeit der generierten Ergebnisse für Code deutlich besser waren als GPT4. Als es diese Woche ablief, beschloss ich daher, zum gleichen Preis für einen weiteren Monat auf ein Claude Pro-Abonnement umzusteigen, um es auszuprobieren.

### Guii-Erfahrung

![guii](https://image.pseudoyu.com/images/guii.jpg)

[Guii](https://guii.ai/) war das interessanteste Projekt, das ich bei diesem Adventure X Hackathon gesehen habe. Es ermöglicht Ihnen, direkt durch natürlichsprachlichen Dialog mit der Frontend-Seite zu interagieren, und es wird den Quellcode direkt modifizieren, um interessante Effekte zu erzielen.

Ich erstellte durch einfachen Dialog eine sehr einfache Kryptowährungswebsite, indem ich Elemente auswählte. Es gibt noch einige Fehler, aber es ist höchst spielbar.

Ich verlieh ihnen den OpenBuild Sponsor Track Preis, den sie sich wohl verdient haben. Ich hoffe, es kann bald online gehen 🔥.

## Interessante Dinge und Gegenstände

### Input

Obwohl die meisten interessanten Inputs automatisch im "Yu's Life" Telegram-Kanal synchronisiert werden, wähle ich trotzdem einige aus, um sie hier aufzulisten, was sich mehr wie ein Newsletter anfühlt.

#### Lesezeichen

- [Lakr233/NotchDrop](https://github.com/Lakr233/NotchDrop)

#### Bücher

- [**Brave New Words**](https://book.douban.com/subject/36798526/), geschrieben vom Gründer der Khan Academy über Gedanken und Praktiken zu GPT und die Zukunft der Bildung. Es bietet viele Inspirationen für die tägliche Nutzung von LLMs. Über das Werden zu einem Werkzeug wie Suchmaschinen hinaus gibt es noch viel Raum für Fantasie.
- [**The Gig Economy**](https://book.douban.com/subject/36191471/), ein Buch, an das ich aus der Diskussion über Radish Run dachte. Es erforscht die sozialen Spaltungen, die durch technologische Beschleunigung verursacht werden, aber mehr aus der Perspektive der Arbeiter. Ich las es eine Weile am Nachmittag, und der Erzählstil ist auch sehr angenehm.

#### Artikel

- [Ein gewöhnlicher Mensch in der sterblichen Welt](https://www.boyilu.com/normal-people)
- [Ausführungen zum Arbeitsrhythmus unabhängiger Schöpfer](https://limboy.me/posts/indie-creator-routine/)
- [Local-First: Eine andere Entwicklererfahrung](https://leonzhao.cn/posts/2024-07-17-local-first-developer-x)
- [Sal Khan ist Pionier der Innovation in der Bildung... wieder | Bill Gates](https://www.gatesnotes.com/Brave-New-Words)

#### Videos

- [Die beste Wahl für Anfänger-Fotografen im Jahr 2024? | SONY ZV-E10M2 Review](https://www.bilibili.com/video/BV15w4m1Y72a)
- [Wie bearbeite ich VLOG? 💻✨ | Vollständiger Postproduktionsprozess enthüllt: Farbkorrektur-Techniken, Wo man BGM findet, Schnelle Untertitelungsmethoden~](https://www.bilibili.com/video/BV1Yz421B7nV)

#### Musik

- [**Frühlingswind für Zehn Meilen**](https://open.spotify.com/track/0glre0pXcbXmVDWH5ZUKVs) von Mr. Deer Band