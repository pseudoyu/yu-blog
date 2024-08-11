---
title: "Aufbau eines kostenlosen persönlichen Blog-Analysesystems von Grund auf (umami + Vercel + Heroku)"
date: 2022-05-21T16:56:47+08:00
draft: false
tags: ["hugo", "umami", "heroku", "vercel", "serverless", "self-host", "blog"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="'Here After Us - Mayday'" >}}

## Vorwort

![umami_dashboard_white](https://image.pseudoyu.com/images/umami_dashboard_white.png)

Zuvor hatte ich einen Artikel mit dem Titel "Kostenlose Einrichtung und Bereitstellungslösung für persönliche Blogsysteme (Hugo + GitHub Pages + Cusdis)" verfasst, in dem ich mein mit Serverless und einigen Open-Source-Projekten erstelltes Blogsystem detailliert beschrieb. Ich begann auch eine Serie, um den Einrichtungsprozess zu dokumentieren.

Vor einigen Tagen stieß ich auf einen Artikel von [Reorx](https://reorx.com) mit dem Titel "Deploy umami for Personal Website Analytics". Er stellte das [umami](https://umami.is) Projekt vor und demonstrierte dessen serverlose Bereitstellung mit [Railway](https://railway.app).

Da ich jedoch zuvor den kostenlosen Postgres-Datenbankdienst von [Heroku](https://www.heroku.com/) genutzt und mit [Vercel](http://vercel.com/) bei der Einrichtung von [Cusdis](https://cusdis.com) bereitgestellt hatte, wollte ich diese Plattformen auch für umami weiterhin nutzen, um die Einrichtungs- und Wartungskosten zu reduzieren.

Der folgende Text wird den spezifischen Einrichtungs- und Bereitstellungsprozess dokumentieren. Dank der offiziellen Ein-Klick-Bereitstellungsmethode verlief der gesamte Einrichtungsprozess sehr reibungslos.

**[2024-06-30 Aktualisierung]**

Später, als Heroku seinen kostenlosen Plan einstellte, können Sie, wenn Sie es weiterhin vollständig kostenlos nutzen möchten, Vercel/Netlify/Zeabur für die kostenlose Bereitstellung des Hauptprojekts + Supabase für die Bereitstellung von PostgreSQL-Datenbankinstanzen verwenden. Übergeben Sie den Link als Umgebungsvariable an den Umami-Dienst. Der Rest des Prozesses bleibt anwendbar.

## Einrichtungs- und Bereitstellungsanleitung

### Erstellung einer Postgres-Datenbank mit Heroku

#### Erstellung der Postgres-Datenbank

Registrieren Sie sich zunächst für ein Heroku-Konto. Nach erfolgreicher Anmeldung klicken Sie auf den Button in der oberen rechten Ecke, um eine neue Anwendung zu erstellen.

![cretae_app_in_heroku_1](https://image.pseudoyu.com/images/cretae_app_in_heroku_1.png)

Geben Sie den Instanznamen ein und wählen Sie die Region nach Belieben. Ich habe die Vereinigten Staaten ausgewählt. Klicken Sie auf Erstellen.

![cretae_app_in_heroku_2](https://image.pseudoyu.com/images/cretae_app_in_heroku_2.png)

Suchen Sie nach der Erstellung im Abschnitt Adds-on des Resources-Tabs nach der Postgres-Datenbank und wählen Sie diese aus.

![add_heroku_postgres](https://image.pseudoyu.com/images/add_heroku_postgres.png)

Wählen Sie den kostenlosen Plan. Die Postgres-Datenbank in Heroku ist kostenlos und kann kontinuierlich genutzt werden, wodurch Einrichtungs- und Wartungskosten entfallen.

![heroku_postgres_plan](https://image.pseudoyu.com/images/heroku_postgres_plan.png)

Überprüfen Sie nach der Erstellung die `DATABASE_URL` in den Einstellungen, die später für die Bereitstellung verwendet wird.

![postgres_data_url](https://image.pseudoyu.com/images/postgres_data_url.jpg)

Klicken Sie auf das neu hinzugefügte Postgres-Add-on, um mit den Einstellungen fortzufahren.

![postgres_addon_details](https://image.pseudoyu.com/images/postgres_addon_details.png)

Wählen Sie in den Einstellungen "View Credentials" und notieren Sie die Konfigurationsparameter.

![heroku_credentials](https://image.pseudoyu.com/images/heroku_credentials.png)

![postgres_settings](https://image.pseudoyu.com/images/postgres_settings.jpg)

#### Initialisierung der Postgres-Datenbank

Da eine Datenbankinitialisierung erforderlich ist, habe ich das Datenbankverwaltungstool DataGrip für die Verbindung verwendet, was recht praktisch ist. Sie können auch über die Heroku CLI verbinden und konfigurieren.

![postgres_config](https://image.pseudoyu.com/images/postgres_config.jpg)

Umami muss mit dem offiziellen [umami/sql/schema.postgresql.sql](https://github.com/mikecao/umami/blob/master/sql/schema.postgresql.sql) Skript initialisiert werden.

![postgres_init_script](https://image.pseudoyu.com/images/postgres_init_script.png)

Nach der Ausführung wird die Datenbank fünf Tabellen mit initialisierten Daten enthalten, und Sie können mit den nachfolgenden Bereitstellungsarbeiten fortfahren.

### Ein-Klick-Bereitstellung des umami-Dienstes mit Vercel

#### Bereitstellung des umami-Dienstes

Nach der Erstellung der Datenbankinstanz können Sie den umami-Dienst mit einem Klick über Vercel bereitstellen.

Besuchen Sie das [Running on Vercel](https://umami.is/docs/running-on-vercel) Modul in der [offiziellen umami-Dokumentation](https://umami.is) für Bedienungsanweisungen und das Ein-Klick-Bereitstellungsskript.

![running_on_vercel](https://image.pseudoyu.com/images/running_on_vercel.png)

Nach dem Klick auf den Ein-Klick-Bereitstellungsbutton werden Sie zur Ein-Klick-Bereitstellungsseite von Vercel weitergeleitet, um ein Github-Repository für umami zu erstellen.

![vercel_create_umami_repo](https://image.pseudoyu.com/images/vercel_create_umami_repo.png)

Als Nächstes müssen Sie den `DATABASE_URL`-Parameteradresse eingeben, die Sie bei der Bereitstellung der Heroku Postgres-Instanz zuvor notiert haben, und Sie müssen eine benutzerdefinierte Zeichenfolge `HASH_SLAT` eingeben.

![vercel_config_umami](https://image.pseudoyu.com/images/vercel_config_umami.png)

Klicken Sie auf Bereitstellen, um die Bereitstellung zu starten. Sie wird in wenigen Minuten abgeschlossen sein.

![vercel_deploy](https://image.pseudoyu.com/images/vercel_deploy.png)

![vecel_deploy_done](https://image.pseudoyu.com/images/vecel_deploy_done.png)

#### Zugriff auf den umami-Dienst

Nach der Bereitstellung klicken Sie auf Dashboard oder die zugewiesene Vercel-Domain, um auf den Dienst zuzugreifen. Sie sehen die umami-Anmeldeoberfläche.

![umami_login](https://image.pseudoyu.com/images/umami_login.png)

Für die erste Anmeldung geben Sie den Standardbenutzernamen `admin` und das Standardpasswort `umami` ein. Nach erfolgreicher Anmeldung werden Sie zur umami-Verwaltungsseite weitergeleitet. Sie können auf das Avatar in der oberen rechten Ecke klicken, um Ihr Passwort zu ändern.

![umami_change_password](https://image.pseudoyu.com/images/umami_change_password.png)

#### Konfiguration der persönlichen Website für den umami-Dienst

Nachdem Sie die grundlegende Kontokonfiguration abgeschlossen haben, klicken Sie in der Seitenleiste auf den Tab Websites und dann auf Website hinzufügen.

![umami_add_website_1](https://image.pseudoyu.com/images/umami_add_website_1.png)

Füllen Sie die grundlegenden Website-Informationen aus. Wenn Sie den Share-Link aktivieren, wird eine öffentlich zugängliche URL generiert. Ich habe sie als Lesezeichen auf dem Startbildschirm meines iPads hinzugefügt, was auch hervorragend als Daten-Dashboard funktioniert.

![umami_add_website_2](https://image.pseudoyu.com/images/umami_add_website_2.png)

#### Konfiguration des umami-Skripts für die persönliche Blog-Website

Nach der Erstellung der Website erhalten Sie das umami-Skript.

![get_umami_script](https://image.pseudoyu.com/images/get_umami_script.jpg)

Fügen Sie nach dem Erhalt das umami-Skript zu Ihrer persönlichen Website hinzu. Ich verwende den statischen Blog Hugo und füge es innerhalb des `<head>`-Tags im Theme hinzu.

![set_umami_script](https://image.pseudoyu.com/images/set_umami_script.jpg)

Nach der Konfiguration und Bereitstellung können Sie mit der Verfolgung der Website-Daten beginnen.

![umami_dashboard_white](https://image.pseudoyu.com/images/umami_dashboard_white.png)

#### Konfiguration eines benutzerdefinierten Skriptnamens

Die Verwendung des offiziellen Skriptnamens `umami.js` könnte von einigen Filterregeln blockiert werden. Daher können wir den Skriptnamen anpassen, um eine genauere Verfolgung der Website-Daten zu erreichen.

Die offizielle Seite bietet auch eine bequeme Änderungsmethode. Sie können die Umgebungsvariable `TRACKER_SCRIPT_NAME` im bereits in Vercel bereitgestellten umami-Dienst hinzufügen und sie auf einen benutzerdefinierten Namen konfigurieren.

![umami_script_environment_varible](https://image.pseudoyu.com/images/umami_script_environment_varible.png)

Stellen Sie nach der Konfiguration erneut bereit und ändern Sie dann den Skriptnamen in Ihrem persönlichen Website-Skript.

![change_umami_script](https://image.pseudoyu.com/images/change_umami_script.jpg)

#### Konfiguration einer benutzerdefinierten Domain

Wenn Sie die von Vercel bereitgestellte `vercel.app`-Domain nicht verwenden möchten, können Sie in Vercel eine benutzerdefinierte Domain hinzufügen. Folgen Sie dem offiziellen Vercel-Leitfaden, um `CNAME` usw. für Ihren Domain-Anbieter zu konfigurieren.

![set_custom_domain](https://image.pseudoyu.com/images/set_custom_domain.png)

Ich verwende beispielsweise eine bei [Cloudflare](https://www.cloudflare.com) gehostete Domain, daher muss ich zuerst eine Domain-Auflösung hinzufügen.

![cloudflare_canme_config](https://image.pseudoyu.com/images/cloudflare_canme_config.png)

Gemäß den offiziellen Anweisungen muss Cloudflare auch eine Seitenregel hinzufügen. Nach der Konfiguration können Sie die benutzerdefinierte Domain-Konfiguration abschließen.

![cloudflare_page_rule](https://image.pseudoyu.com/images/cloudflare_page_rule.png)

## Fazit

Dies ist der vollständige Prozess zum Hinzufügen des umami-Website-Statistikdienstes zu unserer Website. Nach der Konfiguration erfordert er keine anschließende Wartung und ermöglicht eine bequeme Verfolgung der Website-Daten über das Dashboard. Dies ist eines meiner Blog-Einrichtungs- und Bereitstellungs-Serien-Tutorials. Bitte bleiben Sie dran, und ich hoffe, es kann allen als Referenz dienen.

## Referenzen

> 1. [umami](https://umami.is)
> 2. [Deploy umami for Personal Website Analytics](https://reorx.com/blog/deploy-umami-for-personal-website/)
> 3. [Vercel Official Website](http://vercel.com)
> 4. [Heroku Official Website](https://www.heroku.com)