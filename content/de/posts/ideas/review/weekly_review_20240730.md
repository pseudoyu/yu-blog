---
title: "Wochenrückblick #66 - 10x-Ingenieure, technische Leidenschaft und persönliche Werkzeuge"
date: 2024-07-30T20:30:00+08:00
draft: false
tags: ["review", "life", "tools", "epubkit", "work", "painting", "programming"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/photograph.mp3" caption="'Photograph - Ed Sheeran'" >}}

## Vorwort

![weekly_review_20240730](https://image.pseudoyu.com/images/weekly_review_20240730.png)

Dieser Beitrag dokumentiert und reflektiert mein Leben vom `22.07.2024` bis zum `30.07.2024`.

Nach einer außergewöhnlich erlebnisreichen Woche voller Adventure X-Aktivitäten bin ich zur täglichen Routine des fokussierten Programmierens zurückgekehrt. Ich war beschäftigt mit Arbeitsanforderungen; der Weiterentwicklung des API-Teils von EpubKit mit Cloudflare Worker; der Umstrukturierung des Backends eines Nebenprojekts, das ich vor über einem Jahr begonnen, aber nie vollständig realisiert hatte, unter Verwendung von Go; dem Versuch, einen API-Server in Rust zu schreiben; der Erstellung eines Astro-Webprojekts "[tools.pseudoyu.com](https://tools.pseudoyu.com/)" für mein persönliches Toolkit-Projekt "[GitHub - yu-tools](https://github.com/pseudoyu/yu-tools)"; dem Verfassen eines Tutorial-Blogs zur Remark42-Bereitstellung, der von einem Leser im Prozess der Einrichtung eines Blogsystems validiert wurde; einem Ausflug mit meiner Familie in einen Wasserpark am Qiandao-See, wobei ich das Gefühl hatte, ein recht erfülltes Leben zu führen; dem Ausprobieren von Aquarellmalerei und dem Beginn eines Garagenwand-Malprojekts; und vielen anderen interessanten Ereignissen.

## 10x-Ingenieure

![randy_10x](https://image.pseudoyu.com/images/randy_10x.png)

Randy hat kürzlich ein Projekt namens "[Ask Hackers](https://askhackers.com/)" gestartet, ein Suchwerkzeug basierend auf Hacker News-Kommentaren. Es scheint, dass von der Entstehung der Idee bis zur Umsetzung und Promotion nur etwa ein oder zwei Tage vergingen. Das erinnerte mich an das Konzept eines "10x-Ingenieurs" - jemand, der seine Ideen schnell entwickeln und umsetzen kann. Ich bewundere diese Fähigkeit.

Ich habe tatsächlich an ziemlich vielen Projekten gearbeitet, sowohl beruflich als auch privat, und ich muss beschämt zugeben, dass ich zwar viele Technologie-Stacks berührt habe und in jedem ein bisschen schreiben kann, aber in keinem besonders tief bin. Meine Fähigkeit, ein Produkt schnell umzusetzen und zu iterieren, ist immer noch recht schwach. Es scheint bei mir eine fehlende Verbindung zwischen Idee und Demo/Produkt zu geben. Ich habe dieses Thema mit Randy diskutiert, und er meint, es sei eine Frage der technischen Erfahrung. Wenn er einen bestimmten Effekt auf einer Website oder App sieht, kann er im Allgemeinen erraten, wie er implementiert wurde, und ihn reproduzieren, während ich vielleicht immer noch den Quellcode anschauen oder KI konsultieren müsste, um es gerade so zu bewältigen.

## Technische Leidenschaft

Darüber hinaus habe ich festgestellt, dass Leidenschaft und Motivation auch mein Verhalten beeinflussen. Vielleicht, weil ich meine eigene Produktidee und -richtung noch nicht gefunden habe, hatte ich immer das Gefühl, dass ich bei meinen früheren Nebenprojekten lediglich "implementierte" oder technische Übungen machte. Was mich anzog, war nicht die Gestaltung des Produkts selbst, sondern das Lernen und die Verbesserung technischer Fähigkeiten im Implementierungsprozess. Das ist in Ordnung für die persönliche Entwicklung, aber für ein Produkt scheint es an Seele zu mangeln. Es ist wie damals, als ich Randy zum ersten Mal traf und ihn neugierig fragte, warum er Cusdis nicht mehr aktualisierte, das doch recht viele Sterne hatte und von vielen selbst eingesetzt wurde, einschließlich mir. Soweit ich mich erinnere, sagte er, dass es neben wirtschaftlichen Faktoren mehr daran lag, dass er keine Motivation mehr dafür hatte und keine weitere Begeisterung für ein Produkt aufbringen konnte, das er selbst nicht nutzen oder für das er nicht zahlen würde.

Mein eigenes Dilemma liegt auch darin. Es scheint, als hätte ich noch keine Idee gefunden, die mich so begeistern würde, dass ich nicht schlafen könnte. Im Gegenteil, bei der gemeinsamen Entwicklung von EpubKit, da ich selbst seit langem E-Book-Nutzer bin, habe ich aus der Perspektive eines Nutzers mehr Ideen und Enthusiasmus für die Produktiteration, und es fühlt sich erfüllender an.

Man muss der erste Nutzer seines eigenen Produkts sein.

## Persönliches Toolkit-Projekt

![yu_tools_website](https://image.pseudoyu.com/images/yu_tools_website.png)

Ich war schon immer ein eifriger Tüftler verschiedener Software und Hardware. Ich verbringe viel Zeit damit, das am besten geeignete Werkzeug für fast jeden speziellen Bedarf auszuwählen, selbst wenn die Zeit für die Recherche die Nutzungszeit bei weitem übersteigt. Ich genieße es trotzdem immens. Seit dem College bis heute haben mich unzählige Menschen in meinem Umfeld Fragen gestellt wie "Hast du Empfehlungen für Kamera/Tastatur/Mikrofon/xxx?" oder "Ich möchte xxx auf meinem Handy machen, gibt es empfohlene Apps dafür?" Also hatte ich vor über zwei Jahren die Idee, eine persönliche Toolkit-Liste zu erstellen - "[GitHub - yu-tools](https://github.com/pseudoyu/yu-tools)".

Anfangs war es nur ein einfaches GitHub-Projekt mit einer `README.md`-Datei. Später fügte ich nach und nach einige Kategorien und eine kurze Beschreibung für jedes Element hinzu. Ich aktualisierte es über zwei Jahre hinweg periodisch, und überraschenderweise wurde es zu meinem Repo mit den meisten Sternen.

Ich hatte zuvor eine Toolkit-Website gesehen, die von einem Entwickler erstellt wurde, den ich sehr schätze, "[devaslife/Takuya Matsuyama](https://www.craftz.dog/)" - "[A curated list of the tech I use](https://uses.craftz.dog/)". Er fotografiert jedes Werkzeug und fügt seine Nutzungserfahrung hinzu, was ich sehr wertvoll fand. Also verbrachte ich einen Abend damit, mit Astro eine Website basierend auf seiner Vorlage zu erstellen - "[tools.pseudoyu.com](https://tools.pseudoyu.com/)". Sie wird sich mehr auf Software und Dienste konzentrieren, und mit zunehmender Anzahl von Einträgen möchte ich auch eine konversationelle Suchfunktion ähnlich wie "[Ask Hackers](https://askhackers.com/)" hinzufügen.

Das Fotografieren, Screenshotten und Vorstellen von Software und Hardware ist ein großes Projekt und wird kontinuierlich aktualisiert. Wer interessiert ist, kann es im Auge behalten.

## Persönliche Lebensschnipsel

### Aquarell

![rust_painting](https://image.pseudoyu.com/images/rust_painting.jpg)

Einmal nach dem Abendessen versuchten wir uns gemeinsam als Familie an Aquarellmalerei auf Fächern. Es war eine völlig neue Erfahrung. Ich wählte die kleine Rust-Krabbe und vollendete mit etwas Anleitung meiner Seniorin dieses Werk. Ich bin sehr glücklich!!!

### Garagenwandmalerei

![wall_painting](https://image.pseudoyu.com/images/wall_painting.jpg)

Seit der Generierung des Bildes, das ich auf die Werkstattwand malen wollte, mit DALL-E, fanden wir endlich Zeit, mit der Arbeit zu beginnen. Der Fortschritt liegt bei 30%, aber aufgrund eines Team-Meetings am Montagabend waren es meine Seniorin und meine Schwester, die malten. Obwohl ich meine Kamera mitgebracht hatte, hatte ich keine Zeit, den vollständigen Prozess aufzuzeichnen, was ein wenig bedauerlich ist. Nächstes Mal werde ich mehr Fotos vom Prozess und den Details machen. Ich freue mich auf den endgültigen Effekt.

### Nini

![nienie_on_desktop](https://image.pseudoyu.com/images/nienie_on_desktop.jpg)

In letzter Zeit, vielleicht meine Geschäftigkeit spürend, sind beide Kätzchen anhänglicher geworden. Jedes Mal, wenn ich programmiere, liegt Nini still auf dem Schreibtisch, streckt sich gelegentlich faul oder macht ein kokettes Geräusch, entspannend und heilend.

## Interessante Dinge und Objekte

### Input

Obwohl die meisten interessanten Inputs automatisch mit dem Telegram-Kanal "[Yu's Life](https://t.me/pseudoyulife)" synchronisiert werden, werde ich hier trotzdem einige auflisten. Es fühlt sich jetzt mehr wie ein Newsletter an.

#### Sammlungen

- [Hono - Ultraschnelles Web-Framework für die Edges](https://hono.dev/docs/)
- [Ask Hackers](https://askhackers.com/)
- [OpenMoji](https://openmoji.org/)
- [Vercel AI SDK](https://sdk.vercel.ai/)
- [Open Source Alternativen zu proprietärer Software](https://www.opensourcealternative.to/)

#### Bücher

- [**Shape Up**](https://book.douban.com/subject/34945817/), geschrieben vom Gründer der Khan Academy über Gedanken und Praktiken zu GPT und die Zukunft der Bildung. Es bietet einige Inspirationen für den täglichen Gebrauch von LLMs. Neben der Entwicklung zu einem Werkzeug wie Suchmaschinen gibt es noch viel Raum für Fantasie.

#### Artikel

- [Abonnementbasierte Suchmaschine: Kagi](https://anotherdayu.com/2024/5837/)
- [Erstellen Sie Ihr kostenloses Blog-Kommentarsystem von Grund auf (Remark42 + fly.io)](https://www.pseudoyu.com/de/2024/07/22/free_commenting_system_using_remark42_and_flyio/)

#### Videos

- [Traf den Top-Spieler-Kid auf der Straße, er wollte mir auf der Stelle Geld geben!?](https://www.bilibili.com/video/BV1J4421S7hA)
- [Du hast die Fähigkeit, glücklich zu sein | Buchempfehlung "Beratung für Kröten"](https://www.bilibili.com/video/BV1s8vKegE66)

#### Fernsehserien

- [**Geh an den windigen Ort**](http://movie.douban.com/subject/35662223/), beim Essen geschaut.