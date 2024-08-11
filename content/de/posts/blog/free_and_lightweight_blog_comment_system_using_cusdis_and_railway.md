---
title: "Leichtgewichtige Open-Source-Lösung für ein kostenloses Blog-Kommentarsystem (Cusdis + Railway)"
date: 2022-05-24T21:47:47+08:00
draft: false
tags: ["hugo", "cusdis", "railway", "serverless", "self-host", "blog"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《Here, After Us - Mayday》" >}}

## Vorwort

![cusdis_intro](https://image.pseudoyu.com/images/cusdis_intro.png)

Zuvor hatte ich einen Artikel mit dem Titel "Kostenlose Lösung für die Einrichtung und Bereitstellung eines persönlichen Blogsystems (Hugo + GitHub Pages + Cusdis)" verfasst, in dem ich mein mit Serverless und einigen Open-Source-Projekten aufgebautes Blogsystem detailliert beschrieb. Ich begann auch eine Serie, um den Einrichtungsprozess zu dokumentieren.

Dieser Artikel konzentriert sich auf die Lösung für das Blog-Kommentarsystem. Das früheste Kommentarsystem, das ich verwendete, war das ~~berüchtigte~~ [Disqus](https://disqus.com), ein schwerfälliges System, das dafür bekannt ist, Nutzer-Datenschutzdaten zu sammeln. Aufgrund seiner langsamen Ladezeiten und häufigen Werbung in der kostenlosen Version wurde es unerträglich. Daher wechselte ich zu einem anderen Kommentarsystem, das auf GitHub-Issues basiert, genannt [utterances](https://utteranc.es). Es generiert ein Issue für jeden Artikel und ermöglicht es Nutzern, durch die Autorisierung des GitHub-Logins auf das Issue zu kommentieren. Der Vorteil dieser Methode ist, dass sie nur die Autorisierung eines [utterances-bot](https://github.com/utterances-bot) zur Verwaltung erfordert, ohne dass eine eigene Bereitstellung von Diensten oder Datenbankwartung notwendig ist. Nach einiger Zeit der Nutzung stellte ich jedoch mehrere Mängel fest:

1. Es ist abhängig von der GitHub-API für die Kommentarverwaltung. Wenn es in Zukunft API-Änderungen oder Einschränkungen bei der Verwendung von Issues für Kommentare gibt, könnte es instabil werden.
2. Leser müssen den GitHub-Login autorisieren, was für nicht-technische Nutzer oder diejenigen, die auf mobilen Geräten lesen, unbequem ist.
3. Es macht das GitHub-Repository unübersichtlich und erschwert die zukünftige Migration zu anderen Systemen.

Nach einiger Recherche fiel mein Augenmerk auf [Randys](https://lutaonan.com) [Cusdis](https://cusdis.com/). Cusdis ist ein Open-Source-Kommentarsystem, das den Datenschutz priorisiert und extrem leichtgewichtig ist, mit einer gzippten Größe von nur etwa 5kb. Schon am Namen erkennt man, dass der Entwickler ebenfalls von Disqus frustriert war und eine Alternative geschaffen hat. Daher unterstützt es auch den Import historischer Daten von Disqus, was sehr durchdacht ist.

Obwohl es sich um ein Projekt in einem frühen Stadium handelt, bietet es bereits E-Mail-Benachrichtigungen und Kommentaralarme durch Webhook-Integration mit Telegram, was die Verwaltung für Nutzer erleichtert. Cusdis bietet sowohl kostenlose gehostete Dienste als auch selbst gehostete Optionen an. Wenn Sie sich nicht mit der Einrichtung beschäftigen möchten, können Sie direkt den vom Autor bereitgestellten Dienst nutzen. Selbst-Hosting erfordert einen Server und eine PostgreSQL-Instanz. Wir werden hauptsächlich den selbst gehosteten Ansatz demonstrieren.

In meinem vorherigen Artikel "Aufbau eines kostenlosen persönlichen Blog-Analysesystems von Grund auf (umami + Vercel + Heroku)" verwendete ich [Vercel](http://vercel.com/) und [Heroku](https://www.heroku.com/) für die Einrichtung. Als jemand, der gerne bastelt, werden wir [Railway](https://railway.app/) verwenden, um dieses Kommentarsystem aufzubauen und bereitzustellen.

Railway ähnelt Vercel, ist ebenfalls eine PaaS-Plattform, die die Bereitstellung von Projekten in mehreren Sprachen unterstützt. Für persönliche Projekte ist das monatliche Freikontingent von 5 $ mehr als ausreichend. Nach Tests kostet die Bereitstellung des vorherigen [umami Website-Analysesystems](https://www.pseudoyu.com/en/2022/03/24/free_blog_deploy_using_hugo_and_cusdis/) zusammen mit einer PostgreSQL-Datenbankinstanz auf der Railway-Plattform etwa 0,7 $ pro Monat, was für den persönlichen Gebrauch völlig ausreicht.

![railway_price](https://image.pseudoyu.com/images/railway_price.png)

Im Vergleich zu Vercel unterstützt es auch die Bereitstellung von Datenbankinstanzen, so dass Sie die Datenbank und die Instanz zusammen in einem einzigen Projekt bereitstellen können, was die Einrichtungs- und Wartungskosten reduziert. Im Folgenden wird der spezifische Einrichtungs- und Bereitstellungsprozess aufgezeichnet, der aufgrund der offiziellen Unterstützung für die Ein-Klick-Bereitstellung auf Railway sehr reibungslos verläuft.

**[2024-06-30 Aktualisierung]**

Da Railway seit August letzten Jahres seinen kostenlosen Plan eingestellt hat, können Sie, wenn Sie es weiterhin vollständig kostenlos nutzen möchten, Vercel/Netlify/Zeabur verwenden, um das Hauptprojekt kostenlos bereitzustellen, und eine kostenlose PostgreSQL-Datenbankinstanz auf Supabase bereitstellen, wobei die Verbindung als Umgebungsvariable an den Cusdis-Dienst übergeben wird. Der Rest des Prozesses bleibt weitgehend gleich.

## Anleitung zur Einrichtung und Bereitstellung

### Ein-Klick-Bereitstellung von Dienst und Datenbankinstanz mit Railway

Registrieren Sie sich zunächst für ein Railway-Konto. Sie können meinen [Einladungslink](https://railway.app?referralCode=J0F5LQ) verwenden. Nach der Registrierung und Anmeldung klicken Sie oben rechts auf New Project, um ein Projekt zu erstellen.

![railway_dashboard](https://image.pseudoyu.com/images/railway_dashboard.png)

Suchen Sie dann nach Cusdis und klicken Sie auf das erscheinende Projekt, um mit der Bereitstellung zu beginnen. Die ersten Schritte können auch durch Klicken auf den Button `Deploy on Railway` im [Cusdis-Projektrepository](https://github.com/djyde/cusdis) für eine Ein-Klick-Bereitstellung durchgeführt werden.

![new_cusids_starter](https://image.pseudoyu.com/images/new_cusids_starter.png)

Bevor Sie mit der Bereitstellung beginnen, müssen Sie manuell drei Umgebungsvariablen eingeben:

![deploy_cusdis_on_railway](https://image.pseudoyu.com/images/deploy_cusdis_on_railway.png)

1. USERNAME: Konto für die Anmeldung
2. PASSWORD: Passwort für die Anmeldung
3. JWT_SECRET: Eine zufällige Zeichenfolge

Andere Umgebungsvariablen wurden mit Standardwerten voreingestellt, bitte ändern Sie diese nicht:

1. NEXTAUTH_URL: `${{ RAILWAY_STATIC_URL }}`
2. DB_TYPE: `pgsql`
3. DB_URL: `${{ DATABASE_URL }}`
4. PORT: `3000`

Klicken Sie auf Bereitstellen und warten Sie auf den Abschluss. Es wird automatisch den Dienst bereitstellen und die Datenbank initialisieren.

![cusdis_deploy_done](https://image.pseudoyu.com/images/cusdis_deploy_done.jpg)

### Konfigurieren des Cusdis-Skripts für den persönlichen Blog

Nach der Bereitstellung klicken Sie auf den vom Cusdis-Dienst generierten Link, um auf das Dienst-Dashboard zuzugreifen.

![cusdis_login](https://image.pseudoyu.com/images/cusdis_login.png)

Geben Sie den vor der Bereitstellung konfigurierten Benutzernamen und das Passwort ein und klicken Sie auf Anmelden. Nach der Anmeldung klicken Sie auf Dashboard, um die Projektkonfigurationsseite aufzurufen.

Bei der ersten Anmeldung fordert Sie ein Pop-up auf, die erste Website zu konfigurieren. Geben Sie den Website-Namen ein, um die Hinzufügung abzuschließen. Wenn Sie in Zukunft eine Website hinzufügen müssen, klicken Sie in der Seitenleiste auf New Website und geben Sie den Website-Namen ein, um die Hinzufügung abzuschließen.

![add_new_website](https://image.pseudoyu.com/images/add_new_website.png)

Da ich meine eigene Website bereits konfiguriert habe, zeigt die Oberfläche frühere Kommentardatensätze an.

![cusdis_dashboard](https://image.pseudoyu.com/images/cusdis_dashboard.png)

Klicken Sie als Nächstes oben auf Embed Code und kopieren Sie den Code im Pop-up-Fenster.

![cusdis_embed_code](https://image.pseudoyu.com/images/cusdis_embed_code.jpg)

Dieser Teil des Codes muss teilweise entsprechend dem von Ihnen verwendeten Typ der Blog-Website modifiziert werden. Spezifische Konfigurationen finden Sie im Integrationsmodul der [offiziellen Dokumentation](https://cusdis.com/doc#/).

Ich verwende [Hugo](https://gohugo.io), und die Konfiguration lautet wie folgt:

```html
<div id="cusdis_thread"
  data-host="xxx"
  data-app-id="xxx"
  data-page-id="{{ .File.UniqueID }}"
  data-page-url="{{ .Permalink }}"
  data-page-title="{{ .Title }}"
>
</div>

<script defer src="https://cusdis.com/js/widget/lang/zh-cn.js"></script>
<script async defer src="xxx"></script>
```

Die `data-host`, `data-app-id` usw. müssen auf dem Inhalt des gerade kopierten Embed Code basieren. Das `<script defer src="https://cusdis.com/js/widget/lang/zh-cn.js"></script>` implementiert hauptsächlich die chinesische Lokalisierung. Für die Unterstützung verschiedener Sprachen siehe das [Dokumentations-i18n-Modul](https://cusdis.com/doc#/advanced/i18n).

Fügen Sie es nach der Modifikation an die entsprechende Position Ihres Blogs (normalerweise am Ende) hinzu. Nach der Konfiguration und Bereitstellung können Sie das Kommentarfeld sehen. Das Präsentationsergebnis sieht wie folgt aus:

![cusdis_display](https://image.pseudoyu.com/images/cusdis_display.png)

### Konfigurieren einer benutzerdefinierten Domain

Die von der Railway-Bereitstellung automatisch generierte Domain ist recht lang und enthält einige Zeichen, was sie schwer zu merken macht. Wir können eine benutzerdefinierte Domain für das Projekt in Railway konfigurieren.

![railway_custom_domain](https://image.pseudoyu.com/images/railway_custom_domain.jpg)

Nachdem Sie die gewünschte Domain/Subdomain eingegeben haben, fügen Sie die DNS-Auflösung gemäß den offiziellen Anweisungen hinzu.

![railway_domain_dns](https://image.pseudoyu.com/images/railway_domain_dns.jpg)

Zum Beispiel verwende ich eine bei [Cloudflare](https://www.cloudflare.com) gehostete Domain, daher muss ich zunächst einen CNAME-DNS-Eintrag für die Domain hinzufügen.

![cloudflare_domain_dns](https://image.pseudoyu.com/images/cloudflare_domain_dns.jpg)

An diesem Punkt ist unsere Bereitstellung abgeschlossen, und wir können über die Domain auf das Verwaltungs-Backend zugreifen, um Kommentarüberprüfungen und -verwaltung durchzuführen.

### Aktualisieren des Projekts

Wie bereits erwähnt, ist Cusdis noch ein sich entwickelndes Projekt, und wir möchten die vom Autor veröffentlichten neuen Funktionen so schnell wie möglich aktualisieren. Railway bietet eine sehr bequeme Funktion zur Verwaltung von Upstream-Branches, mit der Sie das übergeordnete Projekt für das Projekt festlegen und per Klick die neuesten Updates abrufen können, was sehr praktisch ist.

![railway_update_project](https://image.pseudoyu.com/images/railway_update_project.png)

## Fazit

Das oben Genannte ist der vollständige Prozess des Hinzufügens des Cusdis-Kommentarsystems zu unserer Website. Nach der Konfiguration ist keine nachfolgende Wartung erforderlich. Sie können Ihre Website bequem über das Dashboard verwalten und Kommentare überprüfen. Die Daten werden in einer PostgreSQL-Datenbankinstanz gespeichert, was den Export, die Sicherung und die Migration erleichtert. Dies ist eines meiner Blog-Einrichtungs- und Bereitstellungs-Tutorials. Bleiben Sie dran, und ich hoffe, es kann für jeden als Referenz dienen.

## Referenzen

> 1. [Offizielle Website des Cusdis-Projekts](https://cusdis.com)
> 2. [Offizielle Website von Railway](https://railway.app)
> 3. [Bereitstellung von umami zur Erfassung persönlicher Website-Statistiken](https://reorx.com/blog/deploy-umami-for-personal-website/)