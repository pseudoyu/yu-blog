---
title: "Ghost 5.0 ist da, lass uns es mit einem Klick auf Digital Ocean deployen"
date: 2022-05-29T14:21:12+08:00
draft: false
tags: ["blog", "ghost", "digital ocean", "vps", "self-host"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《Here After Us - Mayday》" >}}

## Vorwort

Ich bin ein Befürworter von statischen Blogs und serverloser Unterstützung. Mein [persönlicher Blog](https://www.pseudoyu.com) und einige [Wissensdatenbank-Projekte](https://www.pseudoyu.com/blockchain-guide) werden mit [hugo](https://gohugo.io) generiert und auf [GitHub Pages](https://pages.github.com) gehostet. Dieser Ansatz ist praktisch für die Versionskontrolle und Wartung, aber für nicht-technische Personen kann die Verwendung von Befehlszeilen-Git-Operationen übermäßig komplex sein, und es ist nicht besonders bequem für Szenarien mit mehreren Mitwirkenden.

Letzte Woche bat mich ein ehemaliger Kollege (nicht-technisch) um Hilfe beim Einrichten einer Portal-Website, hauptsächlich zur Präsentation von Unternehmensinformationen und zur Veröffentlichung von Nachrichten, Funktionen, Tools usw. In Anbetracht der Benutzerfreundlichkeit und anderer Faktoren, und nachdem ich gerade die offizielle Veröffentlichung von [Ghost](https://ghost.org) Version 5.0 gesehen hatte, die viele leistungsfähige Funktionen wie E-Mail-Abonnements und Datenanalyse unterstützt und selbst gehostet werden kann, zog ich diese Lösung in Betracht. Der folgende Text dokumentiert den Installations- und Bereitstellungsprozess.

## Ghost 5.0

![ghost_5_intro](https://image.pseudoyu.com/images/ghost_5_intro.jpg)

Ghost ist ein eher altmodisches Blogging-Tool, das sich seit der Veröffentlichung seines Prototyps im Jahr 2013 neun Jahre lang entwickelt und verbessert hat. Die kürzlich gestartete Version 5.0 ist sehr gut für Einzelpersonen und unabhängige Publishing-Plattformen geeignet. Die Version 5.0 umfasst folgende Funktionsaktualisierungen:

* Unterstützung für leistungsfähigere Abonnementfunktionen, wie z.B. gestaffelte Abonnements
* Unterstützung für mehrere E-Mail-Abonnements, wodurch Designänderungen bequemer werden
* Unterstützung für die Veröffentlichung von Werbeaktionen, mit einem leistungsfähigeren Benutzeranalysedashboard
* Native Unterstützung für Videos, Blogs, GIFs, E-Commerce-Produkte, NFTs usw.
* Veröffentlichung von mehr neuen Themes
* Leistungsoptimierung von 20%+
* ...

Ghost unterstützt offiziell verschiedene Bereitstellungsmethoden, wie Ghost(Pro)-Hosting, Docker-Images, Server-Installation usw. Da die Produktionsumgebung von Ghost jedoch von Ubuntu, Node, MySQL und anderen Umgebungen abhängt, kann es ziemlich mühsam sein, sie eigenständig einzurichten, und die Wartungskosten sind ebenfalls relativ hoch. Nach einigen Recherchen bietet Digital Ocean gemäß den Installationsanweisungen in der offiziellen Dokumentation als offizieller Cloud-Hosting-Partner von Ghost eine Ein-Klick-Bereitstellungs- und Installationsmethode, die einfach und bequem ist.

## Installations- und Bereitstellungsanleitung

### Domainkauf

Als öffentlich zugängliche Website müssen wir einen Domainnamen kaufen und die DNS-Auflösung konfigurieren, um auf den Server zu verweisen, auf dem unsere Website gehostet ist, damit die Öffentlichkeit bequem darauf zugreifen kann. Es gibt viele Domain-Kaufplattformen; ich habe [Cloudflare](https://www.cloudflare.com), [NameSilo](https://www.namesilo.com), [GoDaddy](https://www.godaddy.com) usw. verwendet. Letztendlich nutze ich regelmäßig Cloudflare, da es auch leistungsstarke Funktionen wie CDN, Website-Datenanalyse und benutzerdefinierte Regeln bietet.

Zunächst müssen wir ein Cloudflare-Konto registrieren. Nach Abschluss und Anmeldung wählen Sie in der linken Seitenleiste "Domain registrieren" aus und suchen Sie nach dem gewünschten Domainnamen.

![cloudflare_register_domain](https://image.pseudoyu.com/images/cloudflare_register_domain.png)

Nachdem Sie Ihren gewünschten Domainnamen ausgewählt haben, klicken Sie darauf und wählen Sie die Kaufdauer aus und füllen Sie Ihre persönlichen Informationen aus.

![cloudflare_register_domain_choose](https://image.pseudoyu.com/images/cloudflare_register_domain_choose.png)

Wählen Sie die Zahlungsmethode. Es ist ratsam, die automatische Verlängerung zu wählen, um zu vermeiden, dass Sie vergessen, die Verlängerung durchzuführen.

![cloudflare_register_domain_payment](https://image.pseudoyu.com/images/cloudflare_register_domain_payment.png)

Wählen Sie 'Persönlich' für den Typ und klicken Sie, um den Kauf abzuschließen.

![cloudflare_register_done](https://image.pseudoyu.com/images/cloudflare_register_done.png)

Warten Sie, bis Cloudflare die Verarbeitung abgeschlossen hat, und dann können Sie die Informationen einsehen.

![cloudflare_domain](https://image.pseudoyu.com/images/cloudflare_domain.jpg)

### Digital Ocean SSH-Konfiguration

Da wir später auf den Digital Ocean-Host zugreifen müssen, müssen wir zunächst ein Konto registrieren und unseren SSH-Schlüssel für die passwortlose Anmeldung konfigurieren.

![digital_ocean_add_key](https://image.pseudoyu.com/images/digital_ocean_add_key.png)

Geben Sie unseren SSH-Schlüssel ein und klicken Sie auf Hinzufügen.

![digital_ocean_ssh_config](https://image.pseudoyu.com/images/digital_ocean_ssh_config.png)

### Ein-Klick-Erstellung des Ghost Droplet

Wie bereits erwähnt, bietet Ghost Unterstützung für die Ein-Klick-Droplet-Erstellung auf Digital Ocean. Wir können das [Installationsanleitungsdokument](https://ghost.org/docs/install/) besuchen und auf das Digital Ocean-Symbol klicken, um weitergeleitet zu werden.

![ghost_use_digital_ocean](https://image.pseudoyu.com/images/ghost_use_digital_ocean.png)

Wir können auch im Digital Ocean Image Marketplace suchen und auswählen, dann in der oberen rechten Ecke auf Erstellen klicken.

![digital_ocean_market_ghost](https://image.pseudoyu.com/images/digital_ocean_market_ghost.png)

Laut den offiziellen Anweisungen ist die Konfiguration für 5 $/Monat bereits ausreichend. Sie können auch mit einem Klick erweitern, wenn Sie später höhere Anforderungen haben (Hinweis: Wenn Sie zuerst eine hohe Konfiguration wählen, können Sie nicht herunterstufen).

![digital_ocean_ghost_config](https://image.pseudoyu.com/images/digital_ocean_ghost_config.png)

Wählen Sie die Host-Instanzregion. Ich habe die US-Region gewählt, aber Sie können je nach Ihren Bedürfnissen wählen. Wählen Sie auch die SSH-Konfiguration aus, die wir zuvor hinzugefügt haben, um später bequem darauf zugreifen zu können.

![digital_ocean_ghost_region](https://image.pseudoyu.com/images/digital_ocean_ghost_region.png)

Nachdem wir die Konfigurationsauswahl abgeschlossen haben, wählen wir die Menge, den Namen und klicken auf Droplet erstellen.

![digital_ocean_ghost_create](https://image.pseudoyu.com/images/digital_ocean_ghost_create.png)

Warten Sie, bis Digital Ocean den Host vorbereitet hat, was etwa ein paar Minuten dauert, um abgeschlossen zu sein.

![digital_ocean_ghost_done_hide](https://image.pseudoyu.com/images/digital_ocean_ghost_done_hide.jpg)

### Konfiguration der Domainnamensauflösung

Da Ghost HTTPS konfigurieren muss und für die Bequemlichkeit der Benutzer beim Zugriff, müssen wir die DNS-Auflösung für den neu erstellten Server einrichten.

Melden Sie sich bei Cloudflare an, wählen Sie die Domain aus, die wir gerade registriert haben, wählen Sie den DNS-Tab auf der linken Seite und konfigurieren Sie die A-Record-Auflösung (im Allgemeinen müssen Root-Auflösung und www-Auflösung konfiguriert werden). Der Vorgang ist für andere Domain-Hosting-Websites ähnlich.

![cloudflare_dns_config](https://image.pseudoyu.com/images/cloudflare_dns_config.jpg)

### Domain SSL/TLS-Konfiguration (Optional)

Wenn Sie Cloudflare für das Hosting verwenden, können Sie den SSL/TLS-Verschlüsselungsmodus auf Vollständig einstellen, um die Sicherheit zu erhöhen.

![cloudflare_ssl_config](https://image.pseudoyu.com/images/cloudflare_ssl_config.png)

### Ein-Klick-Installation des Ghost-Dienstes

Nachdem die Domain-Auflösung abgeschlossen ist, können wir uns über die Digital Ocean-Konsole oder andere Terminal-Tools mit dem Host verbinden, um die Ein-Klick-Installation durchzuführen.

![ghost_one_key_install](https://image.pseudoyu.com/images/ghost_one_key_install.jpg)

Nachdem Sie die Eingabetaste gedrückt haben, beginnt das Skript automatisch mit der Installation des Dienstes und verschiedener Abhängigkeiten.

![ghost_start_install](https://image.pseudoyu.com/images/ghost_start_install.png)

Die Installation ist interaktiv über die Befehlszeile. Wir müssen nur zwei benutzerdefinierte Konfigurationen eingeben:

- Geben Sie Ihre Blog-URL ein
- Geben Sie Ihre E-Mail-Adresse ein (für das SSL-Zertifikat)

Geben Sie an diesen beiden Stellen Ihren Domainnamen und Ihre E-Mail-Adresse ein, dann warten Sie, bis die Installation abgeschlossen ist.

![ghost_install_config](https://image.pseudoyu.com/images/ghost_install_config.jpg)

### Zugriff auf die Website

Nachdem die Skriptausführung abgeschlossen ist, können wir auf die Ghost-Website zugreifen.

- https://`{Ihre Domain}`/ghost, Admin-Oberfläche
- https://`{Ihre Domain}`, Website-Adresse

Beim ersten Login ist die Registrierung eines Admin-Kontos erforderlich. Melden Sie sich nach der Registrierung an.

![ghost_login](https://image.pseudoyu.com/images/ghost_login.png)

Nach der Anmeldung sehen Sie die sehr attraktive Ghost-Admin-Seite.

![ghost_dashboard](https://image.pseudoyu.com/images/ghost_dashboard.png)

Ghost bietet viele anpassbare Konfigurationsoptionen, die gemäß den Anforderungen Ihrer Website angepasst werden können.

![ghost_setting](https://image.pseudoyu.com/images/ghost_setting.png)

## Fazit

Das oben Genannte ist meine Erfahrung mit der Verwendung der offiziell empfohlenen Digital Ocean-Hosting-Methode von Ghost zur Bereitstellung meiner eigenen Ghost-Website. Nach dem Upgrade auf 5.0 kann Ghost die Bedürfnisse der meisten Websites erfüllen und bietet eine bessere Unterstützung für Kommerzialisierung und Datenverarbeitung. Es ist eine gute Wahl für persönliche Blogs und kleine Teams. Ich hoffe, dies hilft allen.

## Referenzen

> 1. [Ghost Offizielle Website](https://ghost.org)
> 2. [Digital Ocean Offizielle Website](https://www.digitalocean.com)
> 3. [Kostenlose Einrichtung und Bereitstellungslösung für persönliche Blogsysteme (Hugo + GitHub Pages + Cusdis)](https://www.pseudoyu.com/en/2022/03/24/free_blog_deploy_using_hugo_and_cusdis/)
> 4. [Aufbau eines kostenlosen persönlichen Blog-Datenstatistiksystems von Grund auf (umami + Vercel + Heroku)](https://www.pseudoyu.com/en/2022/05/21/free_blog_analysis_using_umami_vercel_and_heroku/)
> 5. [Leichtgewichtige Open-Source-Lösung für kostenlose Blog-Kommentarsysteme (Cusdis + Railway)](https://www.pseudoyu.com/en/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/)