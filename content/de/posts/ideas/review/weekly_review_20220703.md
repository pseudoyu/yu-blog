---
title: "Wochenrückblick #02 - Arbeit, Ängste und Wachstum"
date: 2022-07-03T12:54:39+08:00
draft: false
tags: ["review", "life", "work", "responsibility", "growth"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="'Here After Us - Mayday'" >}}

## Vorwort

![raspberry_pi](https://image.pseudoyu.com/images/raspberry_pi.jpg)

Ein ganzes Jahr ist vergangen, seit ich nach meinem Praktikum in Peking zu arbeiten begonnen habe.

Ich war schon immer ein Mensch mit einem unerklärlichen Sinn für Rituale. An diesem Wendepunkt reflektiere ich häufig über meine Gedanken, Errungenschaften, Ängste und Bedauern aus diesem vergangenen Jahr. Ich frage mich oft, was sich jene nervöse, aber erwartungsvolle Version meiner selbst vor einem Jahr von dem bevorstehenden Jahr erhofft hätte.

Lasst uns also in diesem Beitrag über Arbeit, Ängste und Wachstum sprechen.

## Über die Arbeit

### Der Berufseinstieg

Ich war bei meiner Jobsuche nicht besonders fleißig, vielleicht weil es selbst in Peking nicht viele Blockchain-Unternehmen zur Auswahl gab. Während meiner Quarantäne in einem Hotel in Shenzhen nach meiner Rückkehr aus Hongkong nahm ich nur an etwa fünf oder sechs Vorstellungsgesprächen teil, obwohl einige davon durchaus einen bleibenden Eindruck hinterließen.

Ein Unternehmen hatte keinen konventionellen Prozess. In der ersten Runde teilte ich meinen Bildschirm mit einem amerikanischen Interviewer und verbrachte zwei Stunden damit, einen ERC20 Token Smart Contract zu schreiben, zu testen und zu deployen. Die zweite Runde erforderte das Schreiben einer systemweiten geplanten Aufgabe mit einem Shell-Skript. Ein anderes Unternehmen stellte viele Fragen zur EVM-Low-Level-Optimierung und wie man unendliche Schleifen in Verträgen vermeidet.

Das Unternehmen, für das ich mich letztendlich entschied, hatte zwei technische Leiter, die das Interview gemeinsam durchführten. Einer stellte Fragen zur Go-Sprache, während der andere nach Hyperledger Fabric und Ethereum fragte (ich erfuhr später, dass er ein ehemaliger Entwickler aus dem IBM Fabric-Team war). Wir diskutierten auch viele Themen im Zusammenhang mit zukünftigen Entwicklungsrichtungen, was fast eineinhalb Stunden dauerte, gefolgt von einem halbstündigen Algorithmustest.

Ich genieße und schätze wirklich die Möglichkeiten, bei Vorstellungsgesprächen neues technisches Wissen zu gewinnen oder mich relativ gleichberechtigt mit den Interviewern auszutauschen. Es ermöglicht mir, schnell zu lernen oder zumindest etwas Klarheit über Richtungen zu gewinnen.

Nach meiner Ankunft in Peking nahm ich an einem HR-Interview teil und trat offiziell als Praktikant bei, womit mein erstes formelles technisches Praktikum begann.

### Das Praktikum

Bei der ersten Begegnung mit einer technischen Position überwog die anfängliche Beklommenheit die Neuheit. Es fehlte mir an Selbstvertrauen, vom theoretischen Wissen aus der Schule zur praktischen Unternehmenstechnik überzugehen. Ich hatte die Go-Sprache nur wenige Monate lang für die Vorbereitung auf Vorstellungsgespräche studiert und noch nie an der Erstellung einer Produktionsanwendung teilgenommen.

Als Neuling in der CRUD-Welt begann ich unter der Anleitung unseres Leiters, Bruder Cheng, damit, Geschäftsschnittstellen zu schreiben, um mich mit der Arbeit vertraut zu machen. Wir entwickelten hauptsächlich eine BaaS-Plattform und schrieben in zwei Wochen sieben Schnittstellen, wobei wir komplexe SQL-Abfragen wiederholt testeten und optimierten. Ich erlebte auch vollständig die git-Commit-Standards, Code-Reviews und Code-Merge-Prozesse. Es war ein recht angenehmer Prozess, meinen Code in Produktionsprojekten laufen zu sehen und verschiedene erlernte Kenntnisse schnell in der Arbeit anzuwenden, um Echtzeit-Feedback zu erhalten, sowie ein Team, das gemeinsam auf ein gemeinsames Ziel und einen Meilenstein hinarbeitet.

Nachdem ich die Hauptentwicklungsarbeit für dieses Projekt abgeschlossen hatte, wollte ich etwas Chain-bezogene Entwicklung machen. Also bewarb ich mich um die Teilnahme an einem Projekt einer anderen Gruppe zur Optimierung der Leistung einer selbst entwickelten Chain-Smart-Contract-Ausführungs-Engine. Da ich jedoch mit Java nicht vertraut war, konnte ich nur versuchen, einige Tests zu schreiben, während ich die Theorie studierte und erforschte. Dies war der Blogbeitrag, den ich zu dieser Zeit aufzeichnete: "Ethereum MPT (Merkle Patricia Tries) Explained in Detail". In dieser Zeit wurde mir klar, wie schnell diese trockenen Algorithmenprinzipien von LeetCode tatsächlich zum Einsatz kommen würden.

Vielleicht aufgrund meines Praktikantenstatus war das Arbeitstempo nicht sehr hoch, was viel Zeit ließ, interessante Bereiche oder Technologien zu erkunden. Ich schrieb die folgenden Blogbeiträge, um meine Erkenntnisse festzuhalten:

1. [Introduction and Architecture of Blockchain-as-a-Service (BaaS) Platform](https://www.pseudoyu.com/de/2021/09/07/blockchain_baas_platform/)
2. [Distributed Systems and Blockchain Consensus Mechanisms](https://www.pseudoyu.com/de/2021/09/08/blockchain_consensus/)
3. [Cross-Chain Technology Principles and Practice](https://www.pseudoyu.com/de/2021/09/06/blockchain_crosschain/)
4. [Source Code Analysis of BitXHub Cross-Chain Plugin (Fabric)](https://www.pseudoyu.com/de/2021/09/09/blockchain_crosschain_bitxhub/)

Interessanterweise reichte ich, da das Unternehmen keine interne Plattform zur Veröffentlichung von Inhalten hatte, in dieser Zeit oft Artikel bei den Blockchain-Technologie-Blog-Plattformen unserer Konkurrenten ein und erhielt Lernfeedback von deren technischem Kernpersonal. Ich profitierte stark im Bereich Cross-Chain, was mich auch die Offenheit der Technologie spüren ließ.

Zu diesem Zeitpunkt hatte ich mich noch nicht entschieden, ob ich bleiben sollte, und ich hatte einigen Kontakt zu anderen wünschenswerten Unternehmen. Kurz darauf nahm ich jedoch an einem anderen Cross-Chain-Projekt mit einem anderen Leiter, Bruder Tao, teil. Je mehr ich mit ihm interagierte, desto mehr sah ich die Begeisterung und die unendlichen Möglichkeiten eines Technologen. Wir beide liebten es, mit verschiedenen neuartigen Werkzeugen und Technologien zu tüfteln und tauschten uns oft darüber aus. In dem Wissen, dass ich mich oft ängstlich fühlte, nicht genügend technische Erfahrung und Fähigkeiten zu haben, bezog er mich in verschiedene Projektpraktiken ein, manchmal führte er mich sogar am Wochenende beim Pair Programming an.

Er ist ein Kernentwickler von [Hyperledger Cello](https://github.com/hyperledger/cello) und ermutigte mich, an Open Source teilzunehmen. Ein Satz, den er damals sagte, ist mir noch lebhaft in Erinnerung. Der Kern war, dass man als Technologe neben dem Abschließen einer Arbeitsaufgabe nach der anderen immer mehrere Etiketten in seiner technischen Karriere haben muss, wie zum Beispiel "Kernbeitragender zu einem bestimmten Open-Source-Projekt" und so weiter. Ich muss auch kontinuierlich danach streben, meine eigenen Etiketten zu finden. Dieser Punkt beeinflusste mich tief, und in der anschließenden Arbeit und im Studium begann ich, die Open-Source-Gemeinschaft kontinuierlich zu beachten und langsam daran teilzunehmen.

Ein unersetzlicher Leiter wurde zu einem bedeutenderen Faktor, der meine Wahl beeinflusste, so dass ich ohne viel Zögern blieb.

### Die Arbeit

Kurz darauf nahm ich an dem teil, was streng genommen mein erstes vollständiges Projekt war, das auch den größten Teil meines ersten Arbeitsjahres einnahm - ein grundlegendes Cross-Chain-Projekt.

Vielleicht aufgrund meines vorherigen Studiums und Verständnisses von Cross-Chain nach der Arbeitszeit wurde ich unerklärlich zum Projektleiter, gerade als ich vom Praktikanten zum Probezeitmitarbeiter überging. Ich nahm an technischen Lösungsdiskussionen, früher Systemgestaltung, Entwicklung und Modifikation der zugrunde liegenden Chain, Standardisierung des Entwicklungsprozesses, Nutzung von DevOps-Umgebungen, Erklärungen und Demonstrationen sowie projektbezogener Dokumentation und Kommunikationsarbeit teil. Dies brachte Druck und Ängste mit sich, die ich zu Beginn meiner Arbeit nie erwartet hätte, aber es führte auch zu meinem schnellen Wachstum.

Tagsüber konnten Besprechungen einen halben Tag dauern, so dass nur die Abende blieben, um sich auf das Schreiben von Code zu konzentrieren. Spät aufbleiben oder sogar die ganze Nacht durcharbeiten wurde zur Norm, um Projektmeilensteine zu erreichen. Technische Schwierigkeiten konnten den Fortschritt tagelang aufhalten, dennoch musste ich gleichzeitig andere Entwicklungsaufgaben jonglieren. Damit einher gingen viele emotionale Unterdrückungen und der Verlust der Kontrolle über die Lebensrhythmen.

Aber als ich mit dem Team wirklich die endgültige Auslieferung dieses Projekts abschloss, war dieses Gefühl der Freude und Erfüllung beispiellos. Dies könnte für mich eine besondere Bedeutung haben. Von meinem Englischstudium im Grundstudium über das Auslandsstudium bis hin zum Wechsel zur Informatik fühlte ich mich während vieler Kursstudien oft frustriert und hinterfragte mehr als einmal, ob ich diesen Weg weitergehen könnte. Obwohl der Prozess dieses Projekts holprig war, gelang es uns letztendlich, was mir enormes Selbstvertrauen gab.

### Interaktionen

Erwähnenswert ist die Art der Interaktion zwischen Menschen nach Beginn der Arbeit. Ich scheine nie diese studentische Ausstrahlung abgelegt zu haben und kommuniziere immer recht direkt und offen, ob ich nun Führungskräften, Kollegen oder Projektpartnern gegenüberstehe. Als mein Leben im Mai einige Veränderungen erfuhr, übernahmen Teammitglieder mehr Arbeitsverantwortung, um mir Zeit zur Anpassung zu geben. Ein Kundenleiter aus einem kürzlich abgeschlossenen Projekt rief mich drei bis vier Stunden lang an, um mich zu trösten. Und ein Leiter aus einem anderen laufenden Projekt half mir, eine Dienstreise zu beantragen, um meine Stimmung ein wenig zu erleichtern. Arbeit ist tatsächlich nicht so trostlos, wie diese angsteinflößenden Artikel es beschreiben. Ich hatte immer das Gefühl, dass unabhängig von der Umgebung oder Gelegenheit Beziehungen und Interaktionen gegenseitig sind. Andere aufrichtig zu behandeln, kann in der Tat gleichermaßen etwas Vertrauen und Aufrichtigkeit zurückgewinnen.

### Errungenschaften, Herausforderungen und Veränderungen

![dev_guide](https://image.pseudoyu.com/images/dev_guide.png)

Ein Jahr ist vergangen, und das zweite Projekt steht kurz vor dem Ende. Ich habe in diesem Jahr viel gelernt und wollte der Abteilung auf meine eigene Art etwas hinterlassen, also beschloss ich, einen technischen Leitfaden zu schreiben. Neben Entwicklungsspezifikationen enthält er auch einige meiner Lernaufzeichnungen über Blockchain aus den letzten Jahren sowie einige praktische Aufzeichnungen, die ich aus der Arbeit gelernt habe. Dies sind alles Dinge, die ich zu lernen gehofft hatte, als ich diese Arbeit antrat, und ich hoffe, neuen Mitgliedern davon erzählen zu können.

![dev_guide_content](https://image.pseudoyu.com/images/dev_guide_content.png)

Obwohl erst ein Jahr in meiner Arbeit vergangen ist, mit viel Raum für Verbesserung und Wachstum in Technologie und Erfahrung, bin ich etwas verwirrt über die Richtung geworden. Ich möchte mich in die zugrunde liegende Blockchain-Technologie vertiefen, die Produkte des Unternehmens oder persönliche Produkte verfeinern und mehr an der Open-Source-Konstruktion teilnehmen. Aber die Arbeit lässt mich oft durch Projekt-Lieferfristen erschöpft zurück, was es schwierig macht, vollständige Zeit zum Lernen und Forschen zu haben. Dies ist eine Herausforderung, die ich in meiner zukünftigen Karriere überwinden und anpassen muss.

Glücklicherweise legt ein anderer Leiter, Bruder Kai, großen Wert auf Open Source und zugrunde liegende Technologie. Unser gelegentlicher Austausch hat mir einige Richtungen aufgezeigt. Es gibt noch viel zu lernen und zu verbessern; der Weg der Technologie ist lang, mit großer Verantwortung und einem langen Weg vor uns.

## Schlussfolgerung

Das oben Genannte ist meine Zusammenfassung der Arbeit zu diesem Zeitpunkt. Ich genieße es zunehmend, mein Leben, meine Arbeit und meinen Gemütszustand auf diese Weise zu organisieren und aufzuzeichnen. Ich hoffe, dass ich, wenn ich im nächsten Jahr auf dieses Jahr, das ich gerade erlebe, zurückblicke, mehr Veränderungen und Wachstum in mir selbst sehen werde. Lasst uns einander ermutigen.