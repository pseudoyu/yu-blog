---
title: "Kostenlose Lösung für Einrichtung und Bereitstellung eines persönlichen Blog-Systems (Hugo + Cloudflare Pages + Cusdis)"
date: 2022-03-24T01:19:28+08:00
draft: false
tags: ["hugo", "github", "github action", "cusdis", "vercel", "cloudflare", "serverless", "self-host", "blog"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

## Vorwort

[Pseudoyu](https://www.pseudoyu.com) ist meine persönliche Blog-Website. Ursprünglich mit [WordPress](https://wordpress.com/) auf meinem Vultr VPS erstellt, wurde sie später auf einen Tencent Cloud Server migriert und für verbesserte Zugriffsgeschwindigkeit registriert. Der Veröffentlichungsprozess blieb jedoch umständlich, und die Serverwartung verursachte erhebliche langfristige Kosten.

Daher suchte ich kontinuierlich nach Lösungen, die sowohl im In- als auch im Ausland optimale Zugriffserfahrungen gewährleisten und gleichzeitig auf Plattformen gehostet werden können, die den Bereitstellungs- und Veröffentlichungsprozess vereinfachen. Ich habe mein Blog-System-Setup und meinen Veröffentlichungsworkflow ständig verfeinert. Bis heute bin ich mit meiner umfassenden Lösung sehr zufrieden. Obwohl die anfängliche Bereitstellung und Einrichtung einige Konfigurationen erfordern, sind spätere Aktualisierungen und Wartungen recht bequem. Daher wird dieser Artikel eine vollständige Aufzeichnung dieser kostenlosen, Open-Source-Lösung für die Einrichtung und Bereitstellung eines persönlichen Blog-Systems liefern, in der Hoffnung, dass sie anderen nützlich sein wird.

**[2024-06-30 Update]**

Zwei Jahre sind vergangen, und viele Lösungen in diesem Artikel sind nun veraltet (obwohl sie immer noch nutzbar sind). Ich habe eine Reihe neuer Artikel aktualisiert, die meine neueste Blog-Lösung vom Juni 2024 detailliert beschreiben, die Ihnen als Referenz dienen können.

- [Was sich 2024 in meinem Blog geändert hat](https://www.pseudoyu.com/de/2024/06/29/what_changed_in_my_blog_2024/)

## Lösung

### Blog-Plattform

Es gibt bereits viele ausgereifte Blog-Plattformen, wie das zuvor erwähnte WordPress. Obwohl leistungsfähig, ist es für persönliche Blog-Seiten etwas schwerfällig und ~~nicht cool genug~~. Nach umfangreicher Recherche entschied ich mich schließlich für [Hugo](https://gohugo.io), einen statischen Website-Generator.

Hugo ist ein in Go implementiertes Blogging-Tool. Es verwendet Markdown zur Artikelbearbeitung, generiert automatisch statische Website-Dateien, unterstützt umfangreiche Theme-Konfigurationen und ermöglicht Plug-in-Einbindungen wie Kommentarsysteme durch JavaScript, was eine hohe Anpassbarkeit bietet. Neben Hugo gibt es Optionen wie Gatsby, Jekyll, Hexo, Ghost usw. Ihre Implementierungen und Verwendungen sind recht ähnlich, sodass Sie nach Ihren Vorlieben wählen können.

![yu_blog_homepage_20240629](https://image.pseudoyu.com/images/yu_blog_homepage_20240629.png)

Da das [hugo-theme-den](https://github.com/shaform/hugo-theme-den) in Hugos Open-Source-Community perfekt zu meiner Ästhetik passte, wählte ich Hugo und nahm einige persönliche Anpassungen und Konfigurationen basierend auf diesem Theme vor, um meinen Bedürfnissen gerecht zu werden.

### Blog-Hosting

Statische Blogs müssen auf einer Plattform gehostet werden, um extern zugänglich zu sein. Dies könnte Ihr eigener VPS sein oder serverlose Plattformen wie [Cloudflare Pages](https://pages.cloudflare.com/), [GitHub Pages](https://pages.github.com) oder [Vercel](http://vercel.com), wobei die letzten beiden mit GitHub-Repositories verknüpft werden können.

Ich entschied mich für GitHub Pages. Es ist völlig kostenlos und integriert sich nahtlos mit GitHub-Code-Repositories, was meinen Bedürfnissen für Backup und Versionskontrolle von Blog-Quelldateien entspricht. Es ermöglicht auch verschiedene CI/CD-Funktionalitäten durch die leistungsfähigen und ebenfalls kostenlosen [GitHub Actions](https://github.com/features/actions), wie das automatische Erstellen und Generieren von Blog-Statikdateien und deren Pushen in das GitHub Pages-Repository zur Bereitstellung nach dem Einreichen/Aktualisieren von Blog-Quelldateien. Es kann auch mit geplanten Aufgaben kombiniert werden, um Selbstvorstellungsseiten und andere Funktionen zu aktualisieren.

**[2024-06-30 Update]**

Da meine Domain bereits bei Cloudflare gehostet ist, habe ich Cloudflare Pages ausprobiert, einen von Cloudflare gestarteten Hosting-Service für statische Websites. Es ist völlig kostenlos (zumindest habe ich das kostenlose Kontingent noch nicht überschritten) und kann direkt mit GitHub-Code-Repositories verbunden werden. Es bietet gängige Website-Erstellungstools wie Next.js, Astro, Hugo usw., ermöglicht automatisierte Bereitstellungsfunktionen wie GitHub Pages und bietet bessere Zugriffrouten. Es ist derzeit eine bessere Lösung.

### Blog-Domain

Wir können unsere eigene Domain durch Domainauflösung konfigurieren, wie meine Website, die auf [pseudoyu.com](https://www.pseudoyu.com) auflöst.

~~Meine Domain wurde auf [NameSilo](https://www.namesilo.com) gekauft und über CDN auf der [Cloudflare](https://www.cloudflare.com) Plattform beschleunigt, was die Zugriffserfahrung verbessert und Domainumleitung und andere Funktionen implementiert. Ich werde später separat auf die Optimierung des Blog-Zugriffs eingehen.~~

**[2022-05-29 Update]**

Zur einfacheren Verwaltung habe ich meine NameSilo-Domain später zu Cloudflare migriert. Sie können direkt auf Cloudflare kaufen. Das Tutorial ist in "[Stellen Sie Ihren Blog mit Hugo und GitHub Action bereit](https://www.pseudoyu.com/de/2022/05/29/deploy_your_blog_using_hugo_and_github_action/)" enthalten.

### Besucheranalyse

Als kontinuierlich aktualisierte und betriebene Blog-Plattform sind wir natürlich neugierig, welche Artikel die höchste Leserschaft haben, welche Schlüsselwörter am häufigsten gesucht werden usw., was uns hilft, uns auf die Erstellung und Weitergabe wertvollerer Inhalte zu konzentrieren. Es gibt viele ähnliche Tools. Ich wählte [splitbee](https://splitbee.io) und [Google Search Console](https://search.google.com/search-console), um meine Besucherinformationen und Suchgewichtung zu analysieren. Zusätzlich kann [Cloudflare](https://www.cloudflare.com) auch den Netzwerkverkehr analysieren, obwohl es aufgrund vieler irrelevanter Netzwerkverkehre wie Crawler weniger relevant ist als die ersten beiden.

![splitbee_statistics](https://image.pseudoyu.com/images/splitbee_statistics.png)

![google_console_performance](https://image.pseudoyu.com/images/google_console_performance.png)

![cloudflare_statistics](https://image.pseudoyu.com/images/cloudflare_statistics.png)

**[2022-05-21 Update]**

Zusätzlich zu den oben genannten direkten Serviceplattformen habe ich auch einen Open-Source-Service [umami](https://umami.is) als Alternative zu [Google Analytics](https://analytics.google.com) bereitgestellt, um Besucherdaten in Echtzeit zu überwachen. Das Tutorial lautet: "[Bauen Sie ein kostenloses persönliches Blog-Datenanalysesystem von Grund auf (umami + Vercel + Heroku)](https://www.pseudoyu.com/de/2022/05/21/free_blog_analysis_using_umami_vercel_and_heroku/)".

**[2024-06-30 Update]**

Später wechselte ich zum Self-Hosting von "[goatcounter](https://www.goatcounter.com/)", einem neuen Datenanalysedienst.

### Kommentarsystem

Ein Blog-System benötigt natürlich ein Kommentarsystem. Während Plattformen wie WordPress eingebaute Kommentar-Plugins haben, müssen statische Blogs mit einigen Kommentarsystemen integriert werden. Anfangs wählte ich das Drittanbieter-System [Disqus](https://disqus.com), das einfach zu bedienen ist, aber mit vielen Werbeanzeigen kommt und nicht minimalistisch genug ist. Später wählte ich [Randy](https://lutaonan.com)s [Cusdis](https://cusdis.com), eine leichtgewichtige Open-Source-Kommentarsystemlösung (der Name selbst scheint von der Frustration mit Disqus inspiriert zu sein). Ich habe es über Vercel selbst gehostet und mit der kostenlosen [PostgreSQL](https://www.postgresql.org)-Datenbank von [Heroku](https://www.heroku.com) für die Speicherung von Kommentardaten verbunden, wodurch ein kostenloses, stabiles Kommentarsystem erreicht wurde, das auch E-Mail-Benachrichtigungen und Telegram-Bot-Warnungen/Schnellantworten unterstützt.

![cusdis_overview](https://image.pseudoyu.com/images/cusdis_overview.png)

**[2022-05-24 Update]**

Das Tutorial für die Bereitstellung von Cusdis auf der Railway-Plattform wurde aktualisiert: "[Kostenlose und leichtgewichtige Blog-Kommentarsystemlösung (Cusdis + Railway)](https://www.pseudoyu.com/de/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/)".

**[2024-06-30 Update]**

Später wechselte ich zum Self-Hosting von "[Remark42](https://remark42.com/)", einem neuen Kommentarsystem.

### Bildverwaltung

Täglich veröffentlichte Artikel können viele Bilder beinhalten. Die Speicherung von Bildern im statischen Blog-Quellprojekt-Repository würde das Projekt zu groß und schwer wiederzuverwenden und zu verwalten machen. Daher wählte ich auch GitHub als Bild-Hosting-Tool und verwendete den [PicGo](https://molunerfinn.com/PicGo/)-Client zur Verwaltung des Bildspeichers. Vor dem Hochladen verwende ich [TinyPNG](https://tinypng.com) zur Komprimierung und den [jsDelivr](https://www.jsdelivr.com)-Dienst zur Beschleunigung des GitHub-Bildspeichers. Auf diese Weise können alle Bilder im GitHub-Bildspeicher-Repository gespeichert und als externe Links in Artikel eingebettet werden.

**[2024-06-30 Update]**

Später verwendete ich eine Reihe von Bildspeicherlösungen: Cloudflare R2 + WebP Cloud Proxy-Optimierung + PicGo.

## Veröffentlichungsprozess

Normalerweise erfordert die Veröffentlichung eines Blogs auf GitHub Pages die lokale Generierung von statischen Website-Dateiverzeichnissen mit dem `hugo`-Befehl, `cd` in das `public`-Verzeichnis und die Verwendung von Befehlen wie `git add`, `git commit`, `git push`, um sie in das GitHub Pages-Repository zu übermitteln und so die Blog-Veröffentlichung zu erreichen. Da jede Aktualisierung die Wiederholung dieser Vorgänge erfordert und Blog-Quell-Markdown-Dateien nicht gut gesichert und versionskontrolliert werden können.

Daher habe ich ein Blog-Quelldatei-Repository eingerichtet und einen automatisierten Veröffentlichungsprozess über GitHub Actions implementiert. Sie müssen nur die Hugo-Blog-Quelldateien in das GitHub-Repository hochladen, was automatisch CI auslöst, um statische Website-Dateien zu generieren und sie in das GitHub Pages-Repository zu pushen.

**[2022-05-29 Update]**

Das Tutorial für Hugo-Setup und GitHub Action-Konfiguration wurde aktualisiert: "[Stellen Sie Ihren Blog mit Hugo und GitHub Action bereit](https://www.pseudoyu.com/de/2022/05/29/deploy_your_blog_using_hugo_and_github_action/)".

**[2024-06-30 Update]**

Cloudflare Pages-Bereitstellungslösung hinzugefügt: "[Stellen Sie Ihren Blog mit Hugo und GitHub Action bereit](https://www.pseudoyu.com/de/2022/05/29/deploy_your_blog_using_hugo_and_github_action/)".

Veröffentlichungsprozess

## Fazit

Das oben Genannte ist meine persönliche Blog-Lösung. Die anfängliche Einrichtung ist etwas umständlich, aber nach einigem Tüfteln erfüllt sie perfekt meine Bedürfnisse. Bezüglich der detaillierten Schritte des gesamten Prozesses ~~werde ich in mehreren Artikeln erklären, bitte bleiben Sie dran~~, in der Hoffnung, dass es für alle hilfreich sein kann.

**[2022-06-02 Update]**

Die Kernteile der Tutorial-Reihe wurden abgeschlossen:

- [Bauen Sie ein kostenloses persönliches Blog-Datenanalysesystem von Grund auf (umami + Vercel + Heroku)](https://www.pseudoyu.com/de/2022/05/21/free_blog_analysis_using_umami_vercel_and_heroku/)
- [Kostenlose und leichtgewichtige Blog-Kommentarsystemlösung (Cusdis + Railway)](https://www.pseudoyu.com/de/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/)
- [Stellen Sie Ihren Blog mit Hugo und GitHub Action bereit](https://www.pseudoyu.com/de/2022/05/29/deploy_your_blog_using_hugo_and_github_action/)

Wenn Sie keine statischen Blogs wie Hugo verwenden möchten, können Sie auch recht einfach einen Blog mit Ghost einrichten:

- [Ghost 5.0 ist da, stellen Sie es mit einem Klick auf Digital Ocean bereit](https://www.pseudoyu.com/de/2022/05/29/deploy_ghost_5_on_digital_ocean_vps/)