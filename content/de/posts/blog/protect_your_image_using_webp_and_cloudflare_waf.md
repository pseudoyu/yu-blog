---
title: "Hinzufügen von Datenschutz und Urheberrechtsschutz zu Ihrem Bild-Hosting mit WebP Cloud und Cloudflare WAF"
date: 2024-07-02T06:12:47+08:00
draft: false
tags: ["image-hosting", "cloudflare", "waf", "webp cloud", "serverless", "blog"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

## Vorwort

In dem Artikel "Aufbau eines kostenlosen Bild-Hosting-Systems von Grund auf (Cloudflare R2 + WebP Cloud + PicGo)" habe ich ein kostenloses Bild-Hosting-System mit Cloudflare R2 erstellt und Bilder durch [WebP Cloud](https://webp.se/) optimiert.

Bei der Nutzung von WebP Cloud entdeckte ich, dass es Funktionen wie benutzerdefinierte Proxy User Agents und Wasserzeichen anbot. Dies brachte mich auf eine Idee: Könnte ich WebP Cloud nutzen, um die Quelllinks meines Bild-Hostings zu schützen, sodass WebP Clouds Proxy-Links der einzige Zugangspunkt für alle meine Bilder werden, während ich gleichzeitig einheitlich mein exklusives Urheberrechts-Wasserzeichen hinzufüge?

Dieser Artikel dokumentiert diese Praxis und dient als ergänzendes Kapitel zur Einrichtung des Bild-Hostings.

## Anforderungsanalyse

![webp_proxy_info](https://image.pseudoyu.com/images/webp_proxy_info.png)

Meine aktuelle Bild-Hosting-Lösung beinhaltet das Hosten von Bildern auf Cloudflare R2 und den Zugriff darauf über WebP Cloud, einem leistungsstarken Bild-Proxy-Tool zur Optimierung. Allerdings können sowohl der Proxy-Link `image.pseudoyu.com` als auch der Quelllink `images.pseudoyu.com` auf meine Bilder zugreifen, wobei ersterer optimiert ist und letzterer das ursprüngliche von mir gespeicherte Bild darstellt.

### Datenschutz

Tatsächlich tragen Fotos, die mit unseren Smartphones, Digitalkameras und anderen Geräten aufgenommen werden, EXIF-Informationen (EXchangeable Image File Format), die in der Regel sensible Daten wie das Aufnahmegerät, die Zeit und den Standort enthalten. Wir können diese Metadaten manuell durch einige technische Mittel entfernen, aber der Prozess ist umständlich und anfällig für Übersehen.

![webp_exif_remove](https://image.pseudoyu.com/images/webp_exif_remove.png)

Nach Konsultation der Dokumentation von WebP Cloud stellte ich fest, dass es tatsächlich eine automatische Löschung der EXIF-Informationen ohne zusätzliche Konfiguration bietet. Besucher können jedoch immer noch über den von Cloudflare R2 exponierten Quelllink auf das Originalbild zugreifen. Um dies zu verhindern, muss ich die Benutzer darauf beschränken, nur über WebP Cloud Proxy-Links anzufragen, um sicherzustellen, dass sie keine nützlichen Informationen erhalten können, wenn sie auf die Cloudflare R2 Quelllinks zugreifen.

### Urheberrechtsschutz

![randy_pic_copyright](https://image.pseudoyu.com/images/randy_pic_copyright.png)

Ich habe zuvor Randys Erfahrung auf Twitter gesehen, bei der sein eigenes Schreibtisch-Setup-Foto missbraucht wurde.

Als jemand, der selbst in der Fotografie dilettiert, mag meine Arbeit zwar keinen besonderen kommerziellen Wert haben, aber es ist trotzdem meine Kreation und verdient Urheberrechtsschutz. Daher möchte ich einheitlich mein eigenes Urheberrechts-Wasserzeichen zu den Bildern hinzufügen, um eine unbefugte Nutzung durch andere zu verhindern.

## Umsetzungsplan

Mit klaren Anforderungen teilt sich die Aufgabe im Wesentlichen in zwei Teile:

1. Sicherstellen, dass Benutzer nur über WebP Cloud Proxy-Links auf meine Bilder zugreifen können, und den direkten Zugriff auf die Original-Bildlinks verhindern.
2. Automatisches Hinzufügen meines Urheberrechts-Wasserzeichens zu allen Bildern auf der Ebene des WebP Cloud Proxys, ohne manuelle Intervention.

Nachfolgend ist mein Umsetzungsplan mit detaillierten Schritten.

### WebP Benutzerdefinierter User Agent + Cloudflare WAF

Nach einem Gespräch mit [Nova Kwok](https://x.com/n0vad3v), dem Entwickler von [WebP Cloud](https://webp.se/), entdeckte ich, dass WebP Cloud eine benutzerdefinierte "Proxy User Agent"-Funktion bietet. Er empfahl, entsprechende Regeln in Cloudflare WAF zu konfigurieren, um die Bildsicherheit zu schützen, wie in der Dokumentation detailliert beschrieben -- "[Security | WebP Cloud Services Docs](https://docs.webp.se/webp-cloud/security/#cloudflare)".

#### WebP Cloud Konfiguration

Wenn wir im Internet auf Webseiten oder Bildlinks zugreifen, enthält die Anfrage normalerweise ein User Agent-Feld, das in der Regel Informationen wie die Browserversion enthält. Websites können für verschiedene User Agents spezifische Logikverarbeitungen durchführen.

WebP Cloud verwendet standardmäßig `WebP Cloud Services/1.0` als Wert, was bedeutet, dass unabhängig davon, welches Endgerät oder welchen Browser der Benutzer zum Zugriff auf das Bild verwendet, die Anfrage an Cloudflare R2 vereinheitlicht als der vom Benutzer definierte User Agent-Wert erscheint.

![webp_custom_user_agent](https://image.pseudoyu.com/images/webp_custom_user_agent.png)

Daher melden wir uns in der WebP Cloud-Konsole an und setzen das Feld "Proxy User Agent" auf einen benutzerdefinierten Wert, beispielsweise `pseudoyu.com/1.0`.

#### Cloudflare WAF Konfiguration

![cloudflare_waf_intro](https://image.pseudoyu.com/images/cloudflare_waf_intro.png)

[WAF (Web Application Firewall)](https://developers.cloudflare.com/waf) ist ein von Cloudflare bereitgestellter Firewall-Dienst, der es ermöglicht, benutzerdefinierte Regeln zur Einschränkung spezifischer Anfragen für die Website-Sicherheit festzulegen. Nach der Anmeldung bei Cloudflare klicken Sie in der linken Seitenleiste auf "Websites", geben den zu schützenden Domainnamen ein, wählen "Security" - "WAF" in der Seitenleiste, um es kostenlos zu nutzen (Hinweis: Dies ist nicht das kontoweite WAF auf der äußersten Ebene). Kostenlose Konten können bis zu fünf benutzerdefinierte Regeln festlegen.

![waf_create_rule](https://image.pseudoyu.com/images/waf_create_rule.png)

Klicken Sie auf "Create Rule", um zur Einstellungsseite zu gelangen.

![user_agent_protection_waf](https://image.pseudoyu.com/images/user_agent_protection_waf.png)

Klicken Sie rechts neben "Expression Preview" auf "Edit Expression" und geben Sie die folgende Regel ein:

```plaintext
(http.user_agent ne "pseudoyu.com/1.0") and (http.host eq "images.pseudoyu.com")
```

Zunächst müssen Sie `pseudoyu.com/1.0` durch den benutzerdefinierten User Agent-Wert ersetzen, den Sie zuvor in WebP Cloud festgelegt haben. Um zu verhindern, dass Bilder von anderen selbst bereitgestellten Diensten auf derselben Domain betroffen sind, habe ich die Bedingung `(http.host eq "images.pseudoyu.com")` hinzugefügt, die nur für den Zugriffs-Link des Bild-Hostings gilt. Dieser Teil muss durch Ihre eigene Bild-Hosting-Domain ersetzt werden.

Wählen Sie "Block" aus dem Dropdown-Menü "Select Action". Dies wird unsere Regel abgleichen und spezifische Netzwerkanfragen blockieren. Klicken Sie nach der Bearbeitung auf "Deploy/Save".

Ich verwende derzeit die [empfohlene Regel](https://docs.webp.se/webp-cloud/security/#cloudflare), die in der offiziellen WebP Cloud-Dokumentation bereitgestellt wird. Sie kann in Zukunft für neue Funktionen angepasst werden, daher können Sie sich direkt auf die Dokumentation beziehen.

![block_by_waf_example](https://image.pseudoyu.com/images/block_by_waf_example.png)

Nach Abschluss der Konfiguration werden Versuche, auf Quelllinks zuzugreifen, die mit `images.pseudoyu.com` beginnen, von WAF blockiert, zum Beispiel:

[images.pseudoyu.com/images/new_mbp_setup.jpg](https://images.pseudoyu.com/images/new_mbp_setup.jpg)

Links, die über WebP Cloud weitergeleitet werden, können jedoch normal aufgerufen werden, zum Beispiel:

[image.pseudoyu.com/images/new_mbp_setup.jpg](https://image.pseudoyu.com/images/new_mbp_setup.jpg)

Dies erfüllt perfekt unsere Anforderungen.

### Hinzufügen von Urheberrechts-Wasserzeichen zu Bildern mit WebP Cloud

Nach den obigen Operationen haben wir sichergestellt, dass Benutzer nur über WebP Cloud Proxy-Links auf unsere Bilder zugreifen können. Der nächste Schritt besteht darin, Urheberrechts-Wasserzeichen zu den Bildern hinzuzufügen.

![webp_watermark_feature](https://image.pseudoyu.com/images/webp_watermark_feature.png)

Erneut stellte ich bei der Konsultation der WebP Cloud-Dokumentation fest, dass es im Modul "Visual Effects" eine "Watermark"-Funktion bietet, die benutzerdefinierte Wasserzeichen zu Bildern hinzufügen kann. Es verwendet die `Fabric.js`-Bibliothek für die Implementierung und bietet einige visuelle Bearbeitungsoptionen. Sie haben sogar einen interessanten Blogbeitrag geschrieben -- "[Implementierung einer Echtzeit-Wasserzeichen-Vorschau mit Fabric.js](https://blog.webp.se/dashboard-fabric-zh/)".

![watermark_list_webp](https://image.pseudoyu.com/images/watermark_list_webp.png)

Rufen Sie die WebP-Konsole auf, wählen Sie links "Visual Effects" und klicken Sie oben rechts auf "Create Watermark", um einige benutzerdefinierte Wasserzeichenstile zu konfigurieren.

![pseudoyu_copyright](https://image.pseudoyu.com/images/pseudoyu_copyright.png)

Dies ist meine Konfiguration, die einen hellgrauen `@pseudoyu`-Text unten in der Mitte des Bildes hinzufügt.

![webp_purge_all_cache](https://image.pseudoyu.com/images/webp_purge_all_cache.png)

Beachten Sie, dass WebP Cloud Bilddaten für Benutzer zwischenspeichert. Wenn Sie möchten, dass zuvor hochgeladene Bilder das Wasserzeichen anwenden oder auf ein neues Wasserzeichen aktualisiert werden, müssen Sie in der Proxy-Konfiguration auf "Purge All Cache" klicken, um den Cache zu leeren.

![apply_watermark_webp](https://image.pseudoyu.com/images/apply_watermark_webp.png)

Nach der Bearbeitung des Wasserzeichens gehen Sie zur detaillierten Konfigurationsseite des Proxys, scrollen Sie zum Modul "Watermark Setting", wählen Sie das gerade erstellte Wasserzeichen aus und klicken Sie oben rechts auf "Save".

Ich werde den Effekt nicht separat demonstrieren, da alle Bilder in diesem Artikel auf diese Weise mit Wasserzeichen versehen wurden.

## Fazit

![webp_thoughts](https://image.pseudoyu.com/images/webp_thoughts.png)

Es ist erst drei Tage her, seit ich begonnen habe, [WebP Cloud](https://webp.se/) zu nutzen, und anfänglich dachte ich, es sei nur ein CDN-ähnliches Tool zur Beschleunigung des Bildzugriffs. Nach einigem Herumprobieren entdeckte ich viele interessante Aspekte. Das kostenlose Kontingent für individuelle kostenlose Benutzer reicht aus, um jedem eine bessere Bilderfahrung zu bieten, was ihrem Prinzip des "Das Richtige tun" entspricht.

Das Team konzentriert sich mehr auf technische Akkumulation und Praxis und schreibt zahlreiche Blogbeiträge -- "[WebP Cloud Services Blog](https://blog.webp.se/)". Wenn man diese in der Freizeit liest, kann man ihre Begeisterung spüren. Kürzlich habe ich aufgrund einer Erfahrung, die in "Wöchentlicher Rückblick #63 - Eine unangenehme Blumenbestellerfahrung, Händler und Verbraucher und die zunehmend KI-gesteuerte Welt" geteilt wurde, über das Thema "schlechtes Geld verdrängt gutes" nachgedacht. Ich glaube, dass Teams, die darauf bestehen, das Richtige zu tun, ohne zu viele Kompromisse bei der Kommerzialisierung einzugehen, es verdienen, von mehr Menschen gesehen zu werden und es verdienen, besser abzuschneiden. Obwohl mein Einfluss begrenzt ist, hoffe ich, dass diese Tutorials mehr Menschen helfen können, sie kennenzulernen.