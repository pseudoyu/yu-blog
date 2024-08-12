---
title: "Wochenrückblick #38 - Foundry Contract-Tests, Logseq Aufgabenverwaltung und Surge Ponte Remote-Entwicklung"
date: 2023-04-30T00:10:03+08:00
draft: false
tags: ["review", "life", "work", "foundry", "solidity", "web3", "pkm", "surge", "surge ponte", "logseq"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="'Here After Us - Mayday'" >}}

## Vorwort

Dieser Beitrag ist eine Aufzeichnung und Reflexion meines Lebens vom `2023-04-19` bis zum `2023-04-30`.

In meinem letzten Wochenrückblick erwähnte ich eine Reise durch mehrere Städte. Nach meiner Rückkehr nach Hangzhou nahm ich allmählich meinen ursprünglichen Lebensrhythmus wieder auf. Ich hatte viel mehr Zeit allein, mit reichlich Input, Reflexion und interessanten Dingen zu tun. Allerdings schien es, als hätte ich weniger Zeit, mich zu organisieren und mit mir selbst zu dialogisieren, oft bemerkte ich den Zeitablauf erst mehrere Tage später. Ich betrachte mich als jemanden, der nicht sehr auf soziale Kontakte angewiesen ist und eine starke Anpassungsfähigkeit besitzt, aber bei näherer Betrachtung könnte ich meinen Lebenszustand zu sehr der virtuellen Welt anvertraut haben und fühlte ein fast abgekoppeltes Unbehagen von der Realität.

Jetzt bin ich in einem späten Nachtflug, habe ein kurzes Nickerchen gemacht und meine Schläfrigkeit verschwindet allmählich. Also beschloss ich, meinen Laptop herauszuholen und etwas zu schreiben. Vielleicht aufgrund des fehlenden Internets und äußerer Ablenkungen scheinen meine Gedanken klarer zu sein.

## Arbeitsatmosphäre und Freiheit

Es ist über einen Monat her, seit ich dem neuen Team beigetreten bin. Vielleicht weil ich in den ersten zwei bis drei Wochen ständig unterwegs war, hatte ich oft nicht viel Realitätssinn. Jetzt passe ich mich allmählich dem Rhythmus an und komme in die Spur. Die Atmosphäre in meiner Gruppe ist sehr gut; selbst bei der Fernarbeit fühle ich keine Entfremdung. Ein Meeting geht oft von Arbeitsangelegenheiten zu der Frage über, was man zum Mitnehmen essen soll, und dann zu welche Vlog-Kamera man kaufen sollte (Sony ist der Weg). Sogar ich, normalerweise sozial ängstlich, bin allmählich gesprächiger im Gruppenchat geworden.

Interessanterweise habe ich aufgrund der intensiven Teilnahme am Shenzhen Team-Building, dem Hong Kong Web3 Festival und einer Welle von Team-Building in Hangzhou bereits fast 20 Kollegen aus dem Unternehmen getroffen, was für ein vollständig remote arbeitendes Team recht bemerkenswert ist. Ich hatte auch das Glück, am Online-Jahrestreffen teilzunehmen und viele interessante Kollegen kennenzulernen, die zuvor nur in Slack-Dialogfeldern existierten (alle Arten von Talenten). Eine Performance konnte einen Rapper enthüllen, und selbst beim Tetris-Spielen konnte man die Unterschiede zwischen den Menschen spüren.

Nach einiger Kommunikation nahm ich einige Anpassungen an meinem Arbeitsinhalt vor. Ich kann weiterhin einige Smart-Contract-Entwicklungen und kettenbezogene Forschungen und Erkundungen gleichzeitig durchführen und auch tiefer an den Produkten teilnehmen, die ich mag (schauen Sie, wer [xLog](https://xlog.app/) und [xSync](https://xsync.app/) noch nicht benutzt, speziell können Sie sich diesen Artikel ansehen "Wochenrückblick #25 - Persönliches Informationsausgabe- und Synchronisationssystem basierend auf Crossbell"). Obwohl es möglicherweise mehr Balance in Bezug auf Arbeitsbelastung und Zeit erfordert, bin ich dennoch ein wenig glücklich, diesen Grad an Wahlfreiheit zu haben.

## Foundry und Contract-Tests

Als ich begann, die Projekte einer anderen Gruppe zu verstehen, der ich für die Arbeit beigetreten bin, spürte ich ziemlich deutlich, dass es trotz meiner halbjährigen Erfahrung in der Kettenentwicklung und dem Schreiben von Verträgen noch eine erhebliche Lücke in Komplexität und Entwicklungspraktiken gab. Ich plane, diesen Bereich gut zu ergänzen, also habe ich diese Woche viele Verträge und Forschungsdokumente angesehen und plane, von Hardhat zu Foundry zu wechseln.

Tatsächlich hatten [Noy](https://twitter.com/Noy_eth) und einige andere Freunde mir schon vorher das Foundry-Framework frenetisch empfohlen, aber weil das vorherige Projekt keine so hohen Anforderungen an Contract-Unit-Tests hatte und ich mich darauf verlassen hatte, viele Tool-Skripte in js zu schreiben, hatte ich die ganze Zeit Hardhat benutzt. Erst als ich dieses Mal wirklich einige Projekte ausführte und einige Demo-Unit-Tests schrieb, spürte ich seine enormen Vorteile und wechselte sofort die Seiten. Die fast verstaubte Solidity-Vertragsentwicklungsserie wird endlich ein neues Update begrüßen (~~Ich schreibe es, schauen Sie auf das Bild, wenn Sie es nicht glauben~~

![foundry_framework_outline](https://image.pseudoyu.com/images/foundry_framework_outline.png)

Tatsächlich gibt es derzeit noch sehr wenige Unternehmenspraktiken für Verträge. Auch weil einige der Verträge, die ich später machen werde, Open Source sind, plane ich, allmählich einige Erfahrungen mit Fallstricken und Best Practices aufzuzeichnen (der Vorteil, vollzeitig Open Source zu sein).

## Logseq und Aufgabenverwaltung

Da meine persönlichen Arrangements und Arbeitsaufgaben zahlreicher und komplexer geworden sind, habe ich Logseq als mein persönliches Aufgabenverwaltungstool reaktiviert. Ich hatte tatsächlich vorher Notion als mein persönliches Kanban-Board benutzt, fühlte aber immer, dass die mentale Belastung bei der Nutzung zu hoch war. Meine schwere Zwangsstörung ließ mich auch ständig diese Aufgabenkategorien und Beschreibungsinformationen optimieren, was mir tatsächlich viel Druck bereitete. Ich hatte auch konventionellere Anwendungen wie TickTick und Todoist benutzt, aber ähnlich musste ich immer noch täglich verschiedene Aufgaben und Tags sortieren, und es war nicht sehr bequem zu überprüfen.

Später entdeckte ich die Notiz-Software Logseq. Anfangs behandelte ich sie tatsächlich nur als eine Markdown-Notiz-Software mit Blöcken als Granularität und wollte auch das Konzept der bidirektionalen Links ausprobieren, die immer erwähnt zu werden schienen. Ich gewöhnte mich ziemlich daran, also migrierte ich allmählich meine Wissensdatenbank von Notion. Später bastelte ich auch daran, SimpRead zu verwenden, um meine Webannotationen und dergleichen zu synchronisieren, aber nach einer Weile fand ich es immer noch etwas umständlich, also gab ich es auf.

Bis ich dieses Video von [Randy](https://twitter.com/randyloop) entdeckte, "How I Use Logseq to Manage My Life and Notes", erwähnte er die Verwendung von Logseqs Daily Journal, um verschiedene Notizen und TODO-Management zu machen, so dass man nicht erst einen Plan erstellen und dann präsentieren muss wie bei Software wie Notion.

![logseq_daily_journal](https://image.pseudoyu.com/images/logseq_daily_journal.png)

Wenn man also plötzlich an etwas denkt, das man tun möchte, muss man nicht separat eine neue Aufgabe im Kanban-Board oder der Aufgabenverwaltungssoftware erstellen, man muss nur ein Element in seinem Daily Journal hinzufügen, wie beim Schreiben einer Notiz, und einfache Syntax wie TODO, LATER verwenden, um einfaches Aufgabenmanagement durchzuführen.

Allerdings erstrecken sich einige Aufgaben über mehrere Tage, und unsere Aufgaben werden unter den Journalen verschiedener Daten verstreut sein, was nicht sehr förderlich für eine einheitliche Verwaltung ist. Hier kommt eine weitere leistungsstarke Funktion von Logseq ins Spiel - Query. Diese Funktion kann als eine Abfrage mit Blöcken als Granularität verstanden werden (ähnlich wie SQL eine Aufzeichnung abfragt), die durch einige Tags, Syntax und andere interne Logik filtert, um die Blöcke anzuzeigen, die wir wollen.

Für diesen Teil orientierte ich mich an Randys Praxis und erstellte eine Dashboard-Seite, die verschiedene Abfrageergebnisse anzeigt. Ich verwendete hauptsächlich die folgenden Abfragen (die Abfrageaussagen stehen in Klammern, Freunde, die sie benötigen, können sie nehmen und nach Bedarf modifizieren):

1. In Bearbeitung (`{{query (todo now)}}`)
2. Zu erledigen (`{{query (todo later)}}`)
3. Schreibplan (`{{query (and (todo later) [[writing]] )}}`)
4. Lesen (`{{query (and (todo now) [[books]] )}}`)
5. Später lesen (`{{query (and (todo later) [[books]])}}`)

Die Präsentationsergebnisse sind wie folgt:

![logseq_dashboard_in_progress](https://image.pseudoyu.com/images/logseq_dashboard_in_progress.png)

![logseq_dashboard_todo](https://image.pseudoyu.com/images/logseq_dashboard_todo.png)

![logseq_dashboard_other_queries](https://image.pseudoyu.com/images/logseq_dashboard_other_queries.png)

Da dies Randys Praxis ist, werde ich keinen separaten Blogbeitrag schreiben, um sie vorzustellen. Ich habe kurz meine eigene Nutzung im Wochenrückblick vorgestellt, Interessierte können sich sein Originalvideo ansehen.

## Surge Ponte und Remote-Entwicklung

Was das Basteln an Netzwerken, verschiedenen Hardwaregeräten und Systemen angeht, gehöre ich zur Kategorie derjenigen, die sowohl ungeschickt als auch spielfreudig sind. Ich hatte zuvor einige Best Practices für die Thin-Client-Entwicklung erkundet, Details können in diesem Artikel gesehen werden:

- [Thin-Client-Entwicklungs-Workflow basierend auf frp Intranet-Penetration](https://www.pseudoyu.com/en/2022/07/05/access_your_local_devices_using_reverse_proxy_tool_frp/)

Der wichtigste und schwierigste Punkt ist, wie man in einer externen Netzwerkumgebung auf Geräte zu Hause, wie Server, Mac-Hosts usw., zugreifen kann. In meiner vorherigen Lösung verwendete ich das frp-Tool für Intranet-Penetration. Ein halbes Jahr ist vergangen, es ist sehr stabil und ist immer noch die erste empfohlene Lösung.

Aber als ich diesen Artikel "Surge Ponte Entwicklungsnotizen" von [Yachen Liu](https://twitter.com/Blankwonder) sah, juckte es mich wieder in den Fingern zu basteln.

Ich würde während des Mai-Feiertags für ein paar Tage unterwegs sein, und da meine tägliche Entwicklung auf dem Host zu Hause erfolgt, wollte ich auch in der Lage sein, darauf zuzugreifen, wenn ich unterwegs bin. Gerade weil ich den frp-Client nach der Neuinstallation des Systems nicht konfiguriert hatte, dachte ich, ich könnte genauso gut direkt Surge Ponte ausprobieren.

Also aktualisierte ich auf Surge 5 und konfigurierte und bastelte in der Nacht vor der Abreise an Surge Ponte. Nach etwas Erkundung denke ich, dass Surge Ponte im Vergleich zu frp oder anderen ähnlichen Lösungen absolute Vorteile in der Konfigurationsbenutzerfreundlichkeit und Erweiterungsspielbarkeit hat.

Das Basteln an Surge Ponte verdient definitiv einen detaillierten Blogbeitrag, also werde ich die Prinzipien und Konfigurationsdetails in diesem Wochenrückblick nicht erklären. Ich werde nur kurz die Effekte einiger Funktionen zeigen, die ich derzeit nutze.

Als ich die Surge Ponte-Funktion sowohl auf meinem 16-Zoll MBP als auch auf dem Mac Studio zu Hause aktivierte (ich verwende den NAT-Traversal-via-Proxy-Modus, der nur eine Leitung benötigt, die UDP unterstützt, wie einen selbst gebauten Proxy mit dem Trojan-Protokoll), konnte ich sie in den registrierten Geräten sehen.

![surge_ponte_config](https://image.pseudoyu.com/images/surge_ponte_config.png)

An diesem Punkt können Sie, wenn das Gerät die Erlaubnis für die Ferneinwahl aktiviert hat, direkt per Ferneinwahl auf den Host zugreifen, wie beim Zugriff auf einen Cloud-Dienst, mit einem Befehl wie `ssh [Benutzername]@[surgepontename].sgponte`, sodass es auch die VS Code Remote-Entwicklung und ähnliches unterstützt.

![surge_ponte_ssh](https://image.pseudoyu.com/images/surge_ponte_ssh.png)

Natürlich kann dieser Punkt auch leicht durch frp und andere erreicht werden, aber ein leistungsfähigerer Punkt ist, dass einige Dienste, die wir auf dem Host zu Hause starten, auch direkt über eine URL wie `[surgepontename].sgponte:[port]` zugegriffen werden können. Zum Beispiel, nachdem ich mich per ssh aus der Ferne mit dem Mac Studio zu Hause verbunden und einen lokalen Next.js-Webdienst gestartet habe, der während der lokalen Entwicklung über `localhost:3000` aufgerufen wird, kann ich jetzt direkt auf meinem MBP über `http://yu-macstudio.sgponte:3000` darauf zugreifen (obwohl frp auch Dienste nach außen abbilden kann, erfordert es das Schreiben von Port-Mapping-Regeln auf der frp-Client-Seite).

![surge_ponte_servies](https://image.pseudoyu.com/images/surge_ponte_servies.png)

Theoretisch können Sie also durch direktes Fernverbinden mit dem Host über VS Code, um Codedateien zu modifizieren, und durch Verwendung der `[surgepontename].sgponte:[port]`-Methode eine vollständige Version der lokalen Debugging-Erfahrung erhalten, die sowohl Portabilität als auch Leistung berücksichtigt (~~In Ordnung, ich verkaufe mein MBP für ein Air~~

Ein weiteres sehr praktisches Szenario ist, dass wir oft einige Dienste haben, auf die nur im lokalen Netzwerk zu Hause zugegriffen werden kann, wie z.B. Soft-Router-Konfiguration, NAS, Raspberry Pi usw. In diesem Fall müsste bei Verwendung von frp jeder einzelne separat konfiguriert werden, während Surge Ponte durch Festlegen von DEVICE-Regeln direkt externen Zugriff ermöglichen kann. Zum Beispiel kann ich jetzt direkt `http://router.asus.com` verwenden, um von unterwegs auf meine Router-Konfigurationsseite zu Hause zuzugreifen, was sehr praktisch für die Fernverwaltung einiger dauerhafter Dienste zu Hause ist.

![surge_ponte_router](https://image.pseudoyu.com/images/surge_ponte_router.png)

Es gibt noch viele weitere interessante Anwendungen, wie z.B. den direkten Zugriff auf Dateien auf Host-Geräten zu Hause über das smb-Protokoll usw. Die späteren Blogbeiträge werden versuchen, einige interessante Anwendungsszenarien abzudecken, interessierte Freunde können den Blogbeiträgen folgen (~~Drängen auf Updates~~).

## Nie Nies jüngste Situation

![nie_nie_in_painting](https://image.pseudoyu.com/images/nie_nie_in_painting.jpg)

Ältere Schwester Bo Yi malt ein Ölgemälde für Nie Nie!!! Dies ist nur ein Entwurf, mehr Details werden hinzugefügt, aber ich kann nicht anders, als es zeigen zu wollen, es ist zu schön!!!

![nie_nie_and_new_toys_01](https://image.pseudoyu.com/images/nie_nie_and_new_toys_01.jpg)

![nie_nie_and_new_toys_02](https://image.pseudoyu.com/images/nie_nie_and_new_toys_02.jpg)

Neuer Katzenbaum, startet den Urlaubsmodus im Voraus!

Plane, sie nach dem Mai-Feiertag zur Kastration zu bringen, bin immer noch etwas nervös, hoffe, alles läuft gut.

## Interessante Dinge und Gegenstände

### Input

Obwohl die meisten interessanten Inputs automatisch im "Yu's Life" Telegram-Kanal synchronisiert werden, wähle ich hier trotzdem einige aus, um sie aufzulisten, fühlt sich mehr wie ein Newsletter an.

#### Artikel

- [Warp+ Verkehrsabstimmung mit Surge](https://pepcn.com/surge/warp-liu-liang-da-pei-surge)
- [Anwendungsspezifische Blockchains: Die Vergangenheit, Gegenwart und Zukunft](https://medium.com/1kxnetwork/application-specific-blockchains-9a36511c832)
- [KI ist hier, welche Fähigkeiten sind am wertvollsten zu lernen?](https://mp.weixin.qq.com/s/ifldCMLTSb1Ir-qcyoa5rw)

#### Videos

Ähnlich zeichne ich auch einige interessante Videos auf, die ich gesehen habe:

- [Wie man sein erstes Open-Source-Projekt startet](https://www.bilibili.com/video/BV1os4y1w78T)
- [Wieder geschimpft worden! Überlebensguide des Freundes für Disneyland](https://www.bilibili.com/video/BV1wm4y127dG)

#### Anime

- **Demon Slayer: Swordsmith Village Arc**, super aufgeregt!!! Hoffe, es enttäuscht nicht
- **Oshi no Ko**, scheint ziemlich hohe Diskussionen zu haben, aber angeblich etwas traurig, habe ein bisschen vom Anfang geschaut