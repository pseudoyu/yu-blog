---
title: "Wochenrückblick #31 - Open Source, Front-end-Entwicklung und ChatGPT-Praxis"
date: 2023-02-20T21:51:11+08:00
draft: false
tags: ["review", "life", "home", "cat", "beer", "programing", "chatgpt", "open-source", "ai", "front-end", "nextjs", "prisma"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/christmas_song_english_version.mp3" caption="'Christmas Song (English Cover) - Matt Cab'" >}}

## Vorwort

Dieser Beitrag ist eine Aufzeichnung und Reflexion meines Lebens vom 13. Februar 2023 bis zum 20. Februar 2023.

Diese Woche war außergewöhnlich erfüllt mit Arbeit und verschiedenen persönlichen Projekten. Obwohl ich nicht wirklich so beschäftigt war, dass ich keine Zeit zum Schlafen hatte, entwickelte ich ein unerklärliches Gefühl von Angst und niedergeschlagener Stimmung, was oft zu einer Tendenz zur Rache-Schlafprokrastination führte. Ein Blick auf die Schlafaufzeichnungen meines Smartphones zeigt, dass ich durchschnittlich weniger als 3 Stunden pro Tag schlief.

Diese Woche löste der Valentinstag durch den Douban-Filmkalender einige Emotionen aus und erinnerte mich an vergangene Ereignisse. Ich fasste den Entschluss, ein wenig zu basteln und kaufte ChatGPT Plus, was in Kombination mit GitHub Copilot viel repetitive Arbeit ersparte. Da ich in letzter Zeit damit herumexperimentiert habe, ging ich sogar in BoYis Finanz-Livestream, um eine Stunde lang AIGC und ChatGPT zu popularisieren - mein Livestream-Debüt, eine ganz neue Erfahrung. Am Wochenende fühlte ich mich zu deprimiert und ging mit Freunden in die Sea Dive Bar, um etwas zu trinken, ein seltener Moment der Entspannung. Mein vorheriges Nebenprojekt verzögerte sich erheblich, was zu fast zwei schlaflosen Nächten am Wochenende führte, in denen ich wie verrückt Front-end-Code schrieb. Ich trat dem Entwicklungsteam für Cusdis v2 bei und schrieb mein erstes Feature. Seltsamerweise erwies sich mein erster PR für ein relativ großes Open-Source-Projekt als Backend-Entwickler als einer für Next.js, was recht unerwartet war. Es gab noch viele andere interessante Dinge.

## Open Source und Front-end-Lernen

Obwohl ich auf GitHub, Twitter und meinem Blog recht aktiv zu sein scheine, habe ich aufgrund meiner relativ kurzen Berufserfahrung und meiner derzeitigen Arbeit, die nicht open-source ist, in Bezug auf Code-Beiträge noch nicht wirklich an großen Open-Source-Projekten teilgenommen. Stattdessen habe ich für einige Markdown- und Kursaufgaben-Projekte ziemlich viele Sterne erhalten, was mich oft ein wenig verlegen macht.

Deshalb habe ich mir zu Beginn dieses Jahres einige Ziele gesetzt, um an verschiedenen Formen von Open-Source-Projekten teilzunehmen, die mich interessieren. Dazu gehörte auch, dass ich mir letzte Woche ein Open-Source-Budget festgelegt habe (siehe "Wochenrückblick #30 - Open-Source-Budget, Schreibambitionen und Demut gegenüber der Technologie"). Ich habe auch einige Issues für RSS3 aufgeworfen, was ein guter Anfang ist.

Eine interessante Sache geschah, als ich Randy auf Twitter sah, der nach Partnern für die Entwicklung von Cusdis v2 suchte. Ich benutze Cusdis jetzt seit fast zwei Jahren (d.h. das Kommentarsystem für diesen Blog) und mag dieses einfache, aber leistungsfähige System wirklich sehr. Ich habe auch einigen Freunden geholfen, einige Bereitstellungs- und Nutzungsprobleme zu lösen oder zu erstellen, und wurde fast zu einer wandelnden Werbung dafür.

Obwohl ich kein Front-end-Entwickler bin, war ich so interessiert, dass ich dem TG-Chat beitrat. Randy ist wirklich ein reiner Technologe und sehr freundlich. Nachdem ich kurz meine Situation und meine Gedanken dargelegt hatte, bat er mich, zuerst den neuesten Code zu ziehen und zum Laufen zu bringen, bevor wir weiter sprachen (plötzlich fühlte es sich wie ein Vorstellungsgespräch an).

Ich sah mir kurz die Codestruktur und die Befehle an. Da ich das JavaScript-basierte Hardhat-Framework für das Schreiben von Solidity verwendet und beim späteren Studium des Front-ends etwas über TypeScript gelernt hatte, war ich mit der Paketverwaltung und einigen grundlegenden Befehlen recht vertraut. Der einzige Unterschied bestand darin, von yarn zu pnpm zu wechseln. Nachdem ich ein wenig an der Umgebung herumgebastelt und eine PostgreSQL-Instanz auf dem Server mit Docker gestartet hatte, brachte ich es zum Laufen (später stellte ich fest, dass lokales SQLite ausgereicht hätte, kein Grund für einen solchen Umweg).

Dann bat er mich, mir die aktuellen Grundfunktionen anzusehen und zu schauen, welcher Teil mich mehr interessierte. Also begann ich langsam, den Code zu lesen, und wies ihn sogar auf einige Fehler der Version v1 hin (die schnell behoben wurden, was eine starke Ausführung zeigte). Dann wurde es bei den Arbeitsprojekten hektisch, so dass ich nicht mit dem Schreiben begann, aber in dieser Zeit las ich ein kleines Buch über Next.js-Entwicklung, das Randy geschrieben hatte:

- [Next.js Application Development Practice](https://nextjs-in-action-cn.taonan.lu/)

Dieses Buch ist wirklich super gut. Es ist die klarste Erklärung zu Code-Praktiken, die ich gesehen habe, seit ich begonnen habe, Next.js zu schreiben. Es behandelt Best Practices wie Query, Mutation und die Verwendung von Query Invalidation zur erzwungenen Datenaktualisierung und empfiehlt auch Prisma, eine sehr nützliche ORM-Bibliothek. Die theoretischen Erklärungen am Anfang sind sehr klar und leicht verständlich, und am Ende sind zwei Beispielprojekte angehängt, die sehr lesenswert sind.

![side_project_api_structure](https://image.pseudoyu.com/images/side_project_api_structure.png)

Nach der Lektüre dieses Buches verwarf ich das Go-Backend meines halbfertigen Nebenprojekts und verbrachte ein ganzes Wochenende damit, den Teil der Backend-Logikimplementierung im Next.js-API-Modul unter Verwendung von Prisma zur Verbindung mit der PostgreSQL-Datenbank umzustrukturieren. Anfangs fühlte ich mich etwas unwohl, als ich den Code in diesem kleinen Buch betrachtete und entsprechend für Benutzerverwaltung und Authentifizierung modifizierte. Später wurden die anderen Funktionen handlicher, und es war auch eine relativ vollständige Übung. Ich muss die Kombination von Next.js + TailwindCSS + Prisma loben, die eine sehr gute Entwicklungserfahrung bietet und sehr gut für die eigenständige Entwicklung einiger Projekte geeignet ist.

Nach zwei Tagen intensiven Codierens am Wochenende wuchs auch mein Selbstvertrauen in die Front-end-Implementierung beträchtlich. Also ging ich zu Randy, um eine Entwicklungsaufgabe zu übernehmen. Die Funktion war nicht kompliziert, es ging nur darum, mit Mutation die Logik für Benutzer zu implementieren, um die für Kommentarbenachrichtigungen benötigte Webhook-Verbindungskonfiguration zu speichern und einige Ladezustände und Toast-Benachrichtigungen hinzuzufügen. Aber es war trotzdem ein guter Anfang.

![chat_with_randy_01](https://image.pseudoyu.com/images/chat_with_randy_01.png)

Bei der Umsetzung stieß ich auf einige Probleme und konsultierte ihn, und er gab geduldige Antworten. Schließlich schloss ich diesen PR am Abend ab.

- [feat: save webhook settings logic \(with loading and toast\) by pseudoyu · Pull Request \#241 · djyde/cusdis](https://github.com/djyde/cusdis/pull/241/commits/914888031bc69628f061fd55a76d8c07402173a5)

![chat_with_randy_02](https://image.pseudoyu.com/images/chat_with_randy_02.png)

Diese Art von Erfahrung ist recht interessant. Der Versuch, an Open Source teilzunehmen, als ich kaum Front-end-Projekte geschrieben hatte, brachte mir Hilfe und Anleitung von Entwicklern ein, die ich sehr bewundere. Manchmal kann Proaktivität zu unerwarteten Gewinnen führen. Wenn ich jedoch daran denke, dass als Blockchain-Backend-Entwickler mein erster Beitrag zu einem relativ großen Open-Source-Projekt und mein erster funktionaler PR sich als Front-end herausstellte, ist das eine ziemlich eigenartige Erfahrung.

Wenn Sie interessiert sind, können Sie [Cusdis](https://cusdis.co) ausprobieren. Ich habe auch schon einmal einen Artikel über die Bereitstellung geschrieben, auf den Sie sich beziehen können:

- [Leichtgewichtige Open-Source-Lösung für kostenlose Blog-Kommentarsysteme (Cusdis + Railway) · Pseudoyu](https://www.pseudoyu.com/en/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/)

## ChatGPT

Ich war einer der frühen Beta-Tester für GitHub Copilot und war beim ersten Mal, als ich es benutzte, erstaunt. Ich konnte nicht glauben, dass KI in Bezug auf Code bereits so viel leisten konnte. Seitdem benutze ich es ununterbrochen, seit etwa eineinhalb Jahren. Später habe ich auch häufig DeepLs maschinelle Übersetzung verwendet, die meiner Meinung nach von viel besserer Qualität ist als Google Translate, und sie hat mir bei vielen Open-Source-Übersetzungsprojekten geholfen. Danach kam Notion AI, aber weil ich später komplett von Notion zu Logseq gewechselt bin, habe ich es nur ausprobiert und dann beiseite gelegt. Ähnlich dazu ist Craft, eine Online-Notiz-Software, die ich am Black Friday gekauft habe und die auch einen eingebauten Assistenten zur Textoptimierung hat. Aber das schwergewichtigste von allem ist zweifellos ChatGPT, das Ende letzten Jahres gestartet wurde.

Ich erinnere mich, dass es Ende November gestartet wurde, und ich begann Anfang Dezember damit zu experimentieren, nachdem ich von Ni in Australien einen Telefonverifizierungscode erhalten hatte. Damals benutzte ich es oft, um Code-Fragen zu stellen, und es konnte im Grunde ziemlich genaue Antworten geben. Aber weil ich eigentlich den nahtloseren Ansatz von GitHub Copilot bevorzuge und nicht jedes Mal eine Menge Sprache organisieren wollte, um Fragen zu stellen und dann den Code zum Bearbeiten zurückzukopieren, spielte ich eine Weile damit herum und legte es dann beiseite, öffnete es nur gelegentlich, um mir einige neue Technologien anzusehen.

![chatgpt_assistant_usage](https://image.pseudoyu.com/images/chatgpt_assistant_usage.png)

Letzte Woche sah ich zufällig [Zili](https://twitter.com/hzlzh) ChatGPT als Assistent benutzen, was sehr verlockend war. Nach einigem Herumbasteln mit virtuellen Kreditkarten und dergleichen bekam ich schließlich die Plus-Mitgliedschaft. Die nicht gerade billigen Kosten von 20 Dollar pro Monat brachten mich dazu, meine täglichen Nutzungsbedürfnisse zu sortieren. Am Ende teilte ich Programmiercode-Fragen, Japanisch-Lernen, Chinesisch-Englisch-Übersetzung, Suchmaschine, Copywriting-Optimierung und andere Bedürfnisse in mehrere Dialogfelder zur Nutzung auf. Jeden Tag ist es, als hätte man eine Reihe kleiner Assistenten, ziemlich lebendig.

In letzter Zeit hatte ich viel Front-end-Arbeit zu erledigen. Obwohl ich vorher Kurse besucht und studiert habe, gibt es immer noch viele Details, über die ich mir nicht sehr im Klaren bin. In dieser Situation ist es tatsächlich recht effektiv, Fragen an ChatGPT zu stellen und die richtigen Antworten aus seinen Antworten zu filtern und sie in mein eigenes Wissen zu verdauen. Es ist auch sehr praktisch und schlägt oft neuartige Implementierungsideen vor. Beim Sprachenlernen sollte es nach dem gleichen Prinzip funktionieren, aber ich hatte noch keine Zeit, die Wirkung des Japanischlernens richtig zu testen. Wenn es später interessant ist, könnte ich einige Dialoge aufzeichnen.

## Interessante Dinge und Objekte

### Input

Obwohl die meisten interessanten Inputs automatisch im Telegram-Kanal "Yu's Life" synchronisiert werden, wähle ich trotzdem einige aus, um sie hier aufzulisten, was sich mehr wie ein Newsletter anfühlt.

#### Artikel

- [Next.js Application Development Practice](https://nextjs-in-action-cn.taonan.lu/)
- [Nach 14 Jahren in der Branche finde ich das Programmieren immer noch schwierig | Piglei](https://www.piglei.com/articles/programming-is-still-hard-after-14-years/)
- [Großunternehmen-Krankheit in der Toilette - hayami's blog](https://hayami.typlog.io/bullshitjobs)
- [Re:Play Ausgabe 25 - Romantisch bis zum Tod](https://newsletter.replay.cafe/re-play-25-lang-man-zhi-si/)
- [Die 4 Ebenen des persönlichen Wissensmanagements - Forte Labs](https://fortelabs.com/blog/the-4-levels-of-personal-knowledge-management/)
- [Reale technische Herausforderungen #8: Aufbrechen eines Monolithen](https://newsletter.pragmaticengineer.com/p/real-world-eng-8)
- [Readme Driven Development](https://tom.preston-werner.com/2010/08/23/readme-driven-development.html)

#### Podcasts

Hier sind einige Podcasts, die ich gehört habe:

- [ep.2 Sea Dive Bar: Die Welt versinkt, wir müssen bauen - Paipai Zuo | Little Universe](https://www.xiaoyuzhoufm.com/episode/63146f53e50e37575adb1cbe)
- [Vol. 84 Digitale Litschi: Ökosystem lizenzierter Software, unabhängige Entwicklung und Fernarbeit - Maple Words (Podcast) | Listen Notes](https://www.listennotes.com/zh-hans/podcasts/%E6%9E%AB%E8%A8%80%E6%9E%AB%E8%AF%AD/vol-84-%E6%95%B0%E7%A0%81%E8%8D%94%E6%9E%9D-%E6%AD%A3%E7%89%88%E8%BD%AF%E4%BB%B6%E7%94%9F%E6%80%81%E7%8B%AC%E7%AB%8B%E5%BC%80%E5%8F%91%E4%B8%8E%E8%BF%9C%E7%A8%8B%E5%8A%9E%E5%85%AC-Y-Uq0g5CrZM/)
- [ChatGPTs Durchbruch und die Ängste der Großen - Tech Stew (Podcast) | Listen Notes](https://www.listennotes.com/zh-hans/podcasts/%E7%A7%91%E6%8A%80%E4%B9%B1%E7%82%96/chatgpt%E7%9A%84%E5%87%BA%E5%9C%88%E4%B8%8E%E5%A4%A7%E4%BD%AC%E4%BB%AC%E7%9A%84%E7%84%A6%E8%99%91-WgOpJNm435Z/)
- [#20 Jährliche Verschwendungsepisode 2022 - Binary Radio (podcast) | Listen Notes](https://www.listennotes.com/podcasts/%E4%BA%8C%E5%88%86%E7%94%B5%E5%8F%B0/20-%E4%B8%80%E5%B9%B4%E4%B8%80%E5%BA%A6%E8%B4%A5%E5%AE%B6%E8%8A%82%E7%9B%AE-2022-Wz84cHdvN-u/)

#### Videos

Ebenso habe ich einige interessante Videos aufgezeichnet, die ich gesehen habe:

- [Valentinstag 8.0 | Musik, der universellste Liebesbrief der Welt](https://www.bilibili.com/video/BV1PG4y1P7vm/)
- [Du bist nur einen flirtenden Satz von der Liebe entfernt, ich lehre dich, wie man Liebes-Anmachsprüche richtig einsetzt](https://www.bilibili.com/video/BV1JA411z7KM/)
- [Wie ich eine ganze Website mit ChatGPT programmiert habe - YouTube](https://www.youtube.com/watch?v=ng438SIXyW4)

## Persönliche Lebensmomente

### Sea Dive Bar

![sea_bar_outside](https://image.pseudoyu.com/images/sea_bar_outside.jpg)

![sea_bar_wine](https://image.pseudoyu.com/images/sea_bar_wine.jpg)

Am Wochenende ging ich mit Freunden in die Sea Dive Bar. Es ist eine kleine Bar in einer Hutong, überfüllt, aber nicht laut, mit ihrer eigenen Art von Lebendigkeit. Drinnen hängt ein großes Schild mit der Aufschrift "Jemand taucht". Ich hatte ein langes Gespräch mit einem Freund, der zufällig geschäftlich in Peking war, was einige der düsteren Emotionen linderte, die ich diese Woche mit mir herumgetragen hatte. Ich muss mich für die neue Woche gut anpassen.

### Nie Nie

![my_lovely_nie_nie_01](https://image.pseudoyu.com/images/my_lovely_nie_nie_01.png)

> Ich hatte einige Drinks in der "Sea Dive Bar" und kam gegen 1 Uhr morgens nach Hause, schlief bald darauf ein. Ich öffnete gerade benommen meine Augen und fand Nie Nie, die anscheinend intensiv an meinem Gesicht schnüffelte und mich gelegentlich vorsichtig mit ihrer kleinen Pfote berührte. Es dauerte eine Weile, bis mein Gehirn (nach dem Neustart) realisierte, dass sie sich Sorgen machte, ob ich noch am Leben war. Ich öffnete hastig mein Handy im Dunkeln, um ein Foto zu machen, und spürte plötzlich ein wenig lang vermisste Wärme und Abhängigkeit.

![my_lovely_nie_nie_02](https://image.pseudoyu.com/images/my_lovely_nie_nie_02.png)

> Sie muss wissen, dass sie bezaubernd ist!

### Valentinstag

![valentine_douban](https://image.pseudoyu.com/images/valentine_douban.png)

Ich muss sagen, die Person, die die Filme für den Douban-Filmkalender auswählt, ist sehr aufmerksam. Sie haben "Liebe wie ein Blumenstrauß" am Valentinstag platziert, mit der Bildunterschrift:

> Liebe ist wie eine Party, sie wird eines Tages enden.