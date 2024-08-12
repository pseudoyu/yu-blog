---
title: "Hugo + GitHub Action: Aufbau Ihres automatisierten Blog-Veröffentlichungssystems"
date: 2022-05-29T20:39:29+08:00
draft: false
tags: ["hugo", "github", "github action", "github pages", "cloudflare", "serverless", "self-host", "blog"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="'Here After Us - Mayday'" >}}

## Vorwort

In einem früheren Artikel, "Kostenloses Setup und Bereitstellungslösung für ein persönliches Blogsystem (Hugo + GitHub Pages + Cusdis)", erwähnte ich die Verwendung von Hugo, einem statischen Site-Generator, um wirklich meinen persönlichen Blog aufzubauen. Ich nahm einige persönliche Anpassungen und Konfigurationen basierend auf dem hugo-theme-den-Theme aus der Hugo-Open-Source-Community vor, um meinen Bedürfnissen gerecht zu werden.

Meine Lösung besteht primär aus den folgenden Kernkomponenten:

1. Persönliches Blog-Quellrepository zur Versionskontrolle von Blog-Konfigurationen und allen Artikel-.md-Quelldateien, gekoppelt mit GitHub Action für automatisierte Bereitstellung, die automatisch statische Websites generiert und sie in das GitHub Pages Blog-Veröffentlichungsrepository pusht.
2. (Optional) GitHub Pages Blog-Veröffentlichungsrepository, benannt in der Form username.github.io, das GitHub Pages für die Website-Bereitstellung verwendet, welche durch CNAME-Auflösungskonfiguration benutzerdefinierte Domänennamen verwenden kann.
3. (Optional) Cloudflare-Konto und Cloudflare Pages-Projekt.
4. Hugo-Theme-Repository, forken Sie Ihr Lieblingstheme und versionieren Sie Ihre persönliche Anpassung und Konfiguration, verknüpft mit dem persönlichen Blog-Quellrepository über git submodule.
5. Andere Komponenten-Quellrepositories, wie umami Website-Datenstatistiken und Cusdis Website-Kommentarsystem, usw.

Der folgende Text wird eine detaillierte Erklärung der Einrichtungs-, lokalen Test-, automatisierten Bereitstellungs- und Wartungsprozesse liefern, was hoffentlich für alle hilfreich sein wird.

## Aufbau eines Blogs mit Hugo

![hugo_website](https://image.pseudoyu.com/images/hugo_website.png)

Hugo ist ein in Go implementiertes Blogging-Tool, das Markdown zur Artikelbearbeitung verwendet, automatisch statische Website-Dateien generiert, reiche Theme-Konfigurationen unterstützt und auch Plugins wie Kommentarsysteme durch JavaScript einbinden kann, was eine hohe Anpassbarkeit bietet. Neben Hugo gibt es andere Optionen wie Gatsby, Jekyll, Hexo, Ghost usw., die in der Implementierung und Nutzung ähnlich sind. Sie können nach Ihren Vorlieben wählen.

### Installation von Hugo

Ich benutze macOS, daher verwende ich die offiziell empfohlene homebrew-Methode zur Installation des Hugo-Programms. Der Prozess ist für andere Systeme ähnlich.

```bash
brew install hugo
```

Nach Abschluss verwenden Sie den folgenden Befehl zur Überprüfung:

```bash
hugo version
```

### Erstellung einer Hugo-Website

Nach der Installation des Hugo-Programms mit dem obigen Befehl können Sie mit dem Befehl hugo new site die Website erstellen, konfigurieren und lokal debuggen.

```bash
hugo new site blog-test
```

![hugo_new_site](https://image.pseudoyu.com/images/hugo_new_site.png)

### Konfiguration des Themes

Nachdem wir unsere Website mit dem obigen Befehl erstellt haben, müssen wir das Theme konfigurieren. Die Hugo-Community bietet eine reiche Auswahl an Themes, aus denen Sie im Themes-Menü der offiziellen Website basierend auf Ihrem bevorzugten Stil und Vorschaueffekten wählen können. Nach der Auswahl können Sie das Theme-Projektrepository betreten, das normalerweise detaillierte Installations- und Konfigurationsanweisungen enthält. Im Folgenden werde ich den Konfigurationsprozess anhand des hugo-theme-den-Themes demonstrieren, das ich derzeit verwende.

#### Verknüpfung des Theme-Repositories

Wir können das Theme-Repository direkt mit git clone zur Verwendung klonen, aber diese Methode hat einige Nachteile. Wenn Sie das Theme später modifizieren, kann es zu Konflikten mit dem ursprünglichen Theme kommen, was das Versionsmanagement und spätere Updates erschwert. Ich habe mich dafür entschieden, das ursprüngliche Theme-Repository in meinen eigenen Account zu forken und git submodule zu verwenden, um das Repository zu verknüpfen. Auf diese Weise kann ich die Theme-Modifikationen in Zukunft separat pflegen.

```bash
cd blog-test/
git init
git submodule add https://github.com/pseudoyu/hugo-theme-den themes/hugo-theme-den
```

![hugo_init_theme](https://image.pseudoyu.com/images/hugo_init_theme.png)

#### Aktualisierung des Themes

Wenn Sie das Blog-Projekt von jemand anderem geklont haben, um es zu modifizieren, müssen Sie den folgenden Befehl zur Initialisierung verwenden:

```bash
git submodule update --init --recursive
```

Wenn Sie die neuesten Änderungen aus dem Theme-Repository synchronisieren müssen, führen Sie den folgenden Befehl aus:

```bash
git submodule update --remote
```

#### Initialisierung der Theme-Konfiguration und Veröffentlichung

Jedes Theme bietet in der Regel einige Beispielkonfigurationen und initiale Seiten. Wenn Sie beginnen, ein Theme zu verwenden, können Sie die Dateien aus seinem exampleSite/-Verzeichnis in das Site-Verzeichnis kopieren und die Konfiguration darauf basierend anpassen.

```bash
cp -rf themes/hugo-theme-den/exampleSite/* ./
```

Nach der Initialisierung der grundlegenden Theme-Konfiguration können wir die Site-Details in der config.toml-Datei konfigurieren. Spezifische Konfigurationselemente finden Sie in der Dokumentation des Themes.

![hugo_theme_config](https://image.pseudoyu.com/images/hugo_theme_config.png)

Nach Abschluss können Sie neue Artikel mit dem Befehl hugo new veröffentlichen.

```bash
hugo new posts/blog-test.md
```

![hugo_new_post](https://image.pseudoyu.com/images/hugo_new_post.png)

#### Lokales Website-Debugging

Hugo generiert statische Webseiten. Beim lokalen Bearbeiten und Debuggen können wir den Befehl hugo server für Echtzeit-Vorschau-Debugging verwenden, ohne jedes Mal neu generieren zu müssen.

```bash
hugo server
```

![hugo_server](https://image.pseudoyu.com/images/hugo_server.png)

Nach dem Starten des Dienstes können wir über den Browser unter http://localhost:1313 auf unsere lokale Vorschau-Webseite zugreifen.

![hugo_server_preview](https://image.pseudoyu.com/images/hugo_server_preview.png)

### Kauf eines Domänennamens

Als extern veröffentlichte Website müssen wir einen Domänennamen kaufen und dessen Auflösung so konfigurieren, dass sie auf den Server zeigt, auf dem sich unsere Website befindet, damit die Außenwelt bequem darauf zugreifen kann. Es gibt viele Domänenkauf-Plattformen; ich habe Cloudflare, NameSilo, GoDaddy usw. verwendet. Letztendlich bevorzuge ich Cloudflare, da es auch leistungsstarke Funktionen wie CDN, Website-Datenanalyse und benutzerdefinierte Regeln bietet.

Zunächst müssen wir ein Cloudflare-Konto registrieren. Nach dem Einloggen wählen Sie "Register Domain" aus der linken Seitenleiste und suchen nach der Domäne, die Sie registrieren möchten.

![cloudflare_register_domain](https://image.pseudoyu.com/images/cloudflare_register_domain.png)

Nachdem Sie Ihre gewünschte Domäne ausgewählt haben, klicken Sie darauf und wählen Sie die Kaufdauer aus und füllen Sie Ihre persönlichen Informationen aus.

![cloudflare_register_domain_choose](https://image.pseudoyu.com/images/cloudflare_register_domain_choose.png)

Wählen Sie eine Zahlungsmethode; es wird empfohlen, die automatische Erneuerung zu wählen, um zu vermeiden, dass Sie vergessen, zu erneuern.

![cloudflare_register_domain_payment](https://image.pseudoyu.com/images/cloudflare_register_domain_payment.png)

Wählen Sie Persönlich für den Typ und klicken Sie, um den Kauf abzuschließen.

![cloudflare_register_done](https://image.pseudoyu.com/images/cloudflare_register_done.png)

Warten Sie, bis Cloudflare den Vorgang verarbeitet hat, und dann können Sie die Informationen einsehen.

![cloudflare_domain](https://image.pseudoyu.com/images/cloudflare_domain.jpg)

### Veröffentlichung des Blogs mit Cloudflare Pages (Empfohlen)

**[Aktualisiert am 2024-06-30]**

#### Einführung in Cloudflare Pages

GitHub Pages ist bereits eine kostenlose und leistungsstarke Hosting-Plattform für statische Websites, die sich nahtlos in GitHub-Code-Repositories integriert. Allerdings ist die Zugriffsgeschwindigkeit in China nicht ideal. Da meine Domäne bereits bei Cloudflare gehostet wird, habe ich Cloudflare Pages ausprobiert, einen von Cloudflare eingeführten Hosting-Dienst für statische Websites. Er ist völlig kostenlos (zumindest habe ich bisher das kostenlose Kontingent nicht überschritten) und kann direkt mit GitHub-Code-Repositories verbunden werden, wodurch die gleiche automatisierte Bereitstellungsfunktionalität wie bei GitHub Pages erreicht wird, während bessere Zugriffswege bereitgestellt werden. Es ist derzeit eine bessere Lösung.

![cloudflare_pages_create](https://image.pseudoyu.com/images/cloudflare_pages_create.png)

#### Erstellung eines Cloudflare Pages-Projekts

Zunächst müssen wir ein Cloudflare-Konto registrieren, dann das Menü "Workers & Pages" auf der linken Seite auswählen und auf die Erstellung eines Projekts klicken.

![cloudflare_pages_with_git](https://image.pseudoyu.com/images/cloudflare_pages_with_git.png)

Der nächste Schritt bietet zwei Optionen: direktes Hochladen statischer Dateien oder Verbindung mit git. Die erste Option eignet sich in der Regel für Einzelseiten- oder sehr niedrigfrequente Update-Projekte, die kein GitHub-Code-Hosting benötigen, wie z.B. Einzelseiten-HTML-Websites. Die Verbindung mit git ermöglicht eine bessere automatische Erstellung neuer Webseiten für jede Blog-Einreichung, was die Methode ist, die wir verwenden werden.

#### Aufbau mit Hugo

![yu_blog_test_build_hugo_cloudflare_pages](https://image.pseudoyu.com/images/yu_blog_test_build_hugo_cloudflare_pages.png)

Da Cloudflare Pages fast alle gängigen Website-Erstellungstools auf dem Markt bereitstellt, wie Next.js, Astro, Hugo usw., können wir zwischen zwei Methoden für die Bereitstellung wählen:

1. Direkte Verwendung der von Cloudflare Pages bereitgestellten Erstellungstools zur Generierung statischer Webseiten und deren Online-Bereitstellung basierend auf dem Repository-Code.
2. Generierung eines statischen Webseiten-Repositories oder -Zweigs ähnlich der oben erwähnten GitHub Pages-Methode und direkte Online-Bereitstellung durch Cloudflare Pages.

![cloudflare_build_site_hugo_in_progress](https://image.pseudoyu.com/images/cloudflare_build_site_hugo_in_progress.png)

![cloudflare_pages_build_done](https://image.pseudoyu.com/images/cloudflare_pages_build_done.png)

Die erste Methode kann unseren Bereitstellungsprozess erheblich vereinfachen. Alles, was wir tun müssen, ist, das oben erstellte Blog-Quellrepository zu verknüpfen (wie mein Repository pseudoyu/yu-blog). Jede Einreichung wird automatisch erstellt und bereitgestellt, wobei nur eine Wartezeit von wenigen Dutzend Sekunden bis zum Abschluss erforderlich ist, ohne dass verschiedene GitHub Actions-Build-Befehle wie bei GitHub Pages geschrieben werden müssen. Es ist sehr bequem und die am meisten empfohlene Methode.

Die zweite Methode ähnelt tatsächlich dem GitHub Pages-Ansatz und eignet sich besser für Websites mit speziellen Anforderungen an den Build-Prozess. Zum Beispiel führe ich beim Erstellen meiner persönlichen Blog-Website gleichzeitig einige Python-Befehle in GitHub Actions aus, um meine About-Seite automatisch zu aktualisieren. Diese komplexen Operationen können nicht direkt von den von Cloudflare Pages bereitgestellten Erstellungstools gehandhabt werden, daher habe ich mich für die zweite Methode entschieden.

Sie können direkt die folgenden vereinfachten GitHub Actions in Ihrem Blog-Quellrepository verwenden:

```yml
name: deploy

on:
    push:
    workflow_dispatch:
    schedule:
        # Läuft jeden Tag um 8:00 Uhr
        - cron: "0 0 * * *"

jobs:
    build:
        runs-on: ubuntu-latest
        steps:
            - name: Checkout
              uses: actions/checkout@v2
              with:
                  submodules: true
                  fetch-depth: 0

            // Andere Schritte, die Sie hinzufügen möchten

            - name: Setup Hugo
              uses: peaceiris/actions-hugo@v2
              with:
                  hugo-version: "latest"

            - name: Build Web
              run: hugo

            - name: Deploy Web
              uses: peaceiris/actions-gh-pages@v3
              with:
                  github_token: ${{ secrets.GITHUB_TOKEN }}
                  publish_dir: ./public
                  publish_branch: cf-pages
```

on gibt die Auslösebedingungen für GitHub Action an. Ich habe drei Bedingungen festgelegt: push, workflow_dispatch und schedule:

- push: Führt GitHub Action aus, nachdem eine Push-Aktion in diesem Projektrepository aufgetreten ist
- workflow_dispatch: Kann manuell von der Action-Symbolleiste im GitHub-Projektrepository aufgerufen werden
- schedule: Führt GitHub Action nach einem Zeitplan aus, wie meine Einstellung, jeden Morgen Pekinger Zeit auszuführen, hauptsächlich um einige automatisierte statistische CI zu verwenden, um automatisch die About-Seite meines Blogs zu aktualisieren, wie zum Beispiel die Codierzeit dieser Woche, Audio- und Videoaufzeichnungen usw. Wenn Sie die Timing-Funktion nicht benötigen, können Sie diese Bedingung löschen

jobs repräsentiert die Aufgaben in GitHub Action. Wir richten eine Build-Aufgabe ein, runs-on gibt die GitHub Action-Laufzeitumgebung an, wir haben ubuntu-latest gewählt. Unsere Build-Aufgabe umfasst vier Hauptschritte: Checkout, Setup Hugo, Build Web und Deploy Web, wobei run der auszuführende Befehl ist und uses ein Plugin in GitHub Action ist. Wir verwendeten die Plugins peaceiris/actions-hugo@v2 und peaceiris/actions-gh-pages@v3. Im Checkout-Schritt kann das Setzen von submodules auf true in with die Submodule des Blog-Quellrepositories synchronisieren, was unser Theme-Modul ist.

Die obigen GitHub Actions werden die vom Blog generierten statischen Dateien in den cf-pages-Zweig pushen, da wir diesen Zweig für die Bereitstellung in Cloudflare Pages wählen. Wenn wir einige zusätzliche Schritte hinzufügen müssen, können wir vor dem Build einige benutzerdefinierte Schritte hinzufügen, was sehr flexibel ist. Für spezifische Anwendungen können Sie das Beispiel "GitHub - yu-blog/.github/workflows/deploy.yml" sehen.

#### Konfiguration einer benutzerdefinierten Domain

![custom_domain_yu_blog](https://image.pseudoyu.com/images/custom_domain_yu_blog.png)

Das Einrichten einer benutzerdefinierten Domain ist auch sehr einfach. Wählen Sie einfach benutzerdefinierte Domain in der Navigationsleiste aus und fügen Sie die Domain hinzu, die Sie binden möchten.

![cf_pages_custom_domain_dns](https://image.pseudoyu.com/images/cf_pages_custom_domain_dns.png)

Wenn es sich um eine bei Cloudflare registrierte/gehostete Domain handelt, können Sie direkt "Activate Domain" wählen, wodurch automatisch die DNS-Auflösung hinzugefügt wird. Wenn es sich um eine Domain von einer anderen Plattform handelt, fügen Sie manuell die CNAME-Auflösung hinzu.

![custom_domain_wait_dns](https://image.pseudoyu.com/images/custom_domain_wait_dns.png)

Nach der Konfiguration des DNS müssen Sie nur warten, bis es wirksam wird.

### Veröffentlichung des Blogs mit GitHub Pages

#### Erstellung eines Repositories

Das GitHub Pages-Projekt muss dem speziellen Namensformat username.github.io folgen. Nach der Einrichtung des Repositories können Sie Ihre registrierte benutzerdefinierte Domain in den Einstellungen konfigurieren, um auf die von GitHub Pages generierte URL zu verweisen. Zusätzlich müssen Sie die baseURL in der Blog-Site-Konfigurationsdatei config.toml in Ihre benutzerdefinierte Domain ändern, im Format "https://www.pseudoyu.com/". Dies ermöglicht es der Blog-Site, ordnungsgemäß auf den von GitHub Pages generierten Website-Dienst zuzugreifen.

![github_pages_repo](https://image.pseudoyu.com/images/github_pages_repo.png)

#### Domain-Auflösung

Nach der Registrierung gemäß den obigen Schritten müssen Sie die DNS-Auflösung bei Ihrem Domain-Hosting-Anbieter einrichten. Hier müssen wir CNAME wählen, das auf unsere GitHub Pages URL verweist.

![cloudflare_cname_config](https://image.pseudoyu.com/images/cloudflare_cname_config.png)

Da die CNAME-Auflösung nicht die Root-Domain setzen kann, bedeutet das, dass Sie nur www.pseudoyu.com oder andere Subdomains setzen können, nicht pseudoyu.com. Wir können Cloudflare's benutzerdefinierte Regeln verwenden, um eine Domain-Weiterleitung einzurichten. Die spezifische Konfiguration ist wie folgt, ersetzen Sie einfach meine Domain durch Ihre eigene. Selbst wenn Sie Ihre Domain über NameSilo registriert haben, können Sie eine Site über Cloudflare hinzufügen, um diese Funktionalität zu implementieren, oder andere Hosting-Plattformen haben ähnliche Funktionen, folgen Sie einfach deren Anweisungen zur Konfiguration.

![cloudflare_cname_rule_config](https://image.pseudoyu.com/images/cloudflare_cname_rule_config.png)

Nach Abschluss der obigen Vorbereitungen können wir nun über unsere benutzerdefinierte Domain auf unsere GitHub Pages zugreifen. Derzeit wird beim Besuch eine 404-Seite angezeigt, da das Projektrepository leer ist.

Wir möchten, dass die von Hugo generierte statische Website über den GitHub Pages-Dienst gehostet wird, ohne den Dienst selbst warten zu müssen, was stabiler und sicherer ist. Daher müssen wir die von Hugo generierten statischen Webseiten-Dateien in das GitHub Pages-Projektrepository hochladen.

#### Manuelle Veröffentlichung

Nach dem Bearbeiten des Blog-Inhalts und dem lokalen Debugging durch hugo server können wir statische Webseiten-Dateien mit dem hugo-Befehl generieren.

```bash
hugo
cd public/
```

![hugo_gen_pages](https://image.pseudoyu.com/images/hugo_gen_pages.png)

Hugo speichert standardmäßig generierte statische Webseiten-Dateien im Verzeichnis public/. Wir können das public/-Verzeichnis als git-Repository initialisieren und es mit unserem pseudoyu/pseudoyu.github.io Remote-Repository verknüpfen, um unsere statischen Webseiten-Dateien zu pushen.

```bash
git init
git remote add origin git@github.com:pseudoyu/pseudoyu.github.io
git add .
git commit -m "add test"
```

![hugo_public_init](https://image.pseudoyu.com/images/hugo_public_init.png)

Nach Überprüfung der Dateiänderungen können Sie mit git push origin master in das GitHub Pages-Repository pushen. Warten Sie einige Minuten, und Sie können über unsere benutzerdefinierte Domain auf unsere Blog-Site zugreifen, völlig konsistent mit unserem lokalen hugo server-Debugging.

#### Automatisierte Veröffentlichung

Durch die obigen Befehle können wir unsere statischen Dateien manuell veröffentlichen, aber es gibt immer noch einige Nachteile:

1. Die Veröffentlichungsschritte sind immer noch umständlich und erfordern nach dem lokalen Debugging den Wechsel in das public/-Verzeichnis zum Hochladen.
2. Unfähig, die Blog-.md-Quelldateien zu sichern und zu versionieren.

Daher benötigen wir eine einfache und reibungslose Möglichkeit, den Blog zu veröffentlichen. Lassen Sie uns zunächst das Repository für die Blog-Quelldateien initialisieren, wie zum Beispiel mein Repository pseudoyu/yu-blog.

Da unser Blog auf GitHub und GitHub Pages basiert, können wir die offizielle GitHub Action für CI-automatische Veröffentlichung verwenden. Ich werde dies unten ausführlich erklären. GitHub Action ist eine Plattform für kontinuierliche Integration und kontinuierliche Bereitstellung (CI/CD), die zur Automatisierung von Build-, Test- und Bereitstellungspipelines verwendet werden kann. Derzeit wurden viele Workflows entwickelt, die mit einfacher Konfiguration direkt verwendet werden können.

Die Konfiguration befindet sich im Repository-Verzeichnis .github/workflows mit der Endung .yml. Meine GitHub Action-Konfiguration ist pseudoyu/yu-blog deploy.yml, und ein Beispiel für eine Konfiguration zur automatischen Veröffentlichung sieht wie folgt aus:

```yml
name: deploy

on:
    push:
    workflow_dispatch:
    schedule:
        # Läuft jeden Tag um 8:00 Uhr
        - cron: "0 0 * * *"

jobs:
    build:
        runs-on: ubuntu-latest
        steps:
            - name: Checkout
              uses: actions/checkout@v2
              with:
                  submodules: true
                  fetch-depth: 0

            - name: Setup Hugo
              uses: peaceiris/actions-hugo@v2
              with:
                  hugo-version: "latest"

            - name: Build Web
              run: hugo

            - name: Deploy Web
              uses: peaceiris/actions-gh-pages@v3
              with:
                  PERSONAL_TOKEN: ${{ secrets.PERSONAL_TOKEN }}
                  EXTERNAL_REPOSITORY: pseudoyu/pseudoyu.github.io
                  PUBLISH_BRANCH: master
                  PUBLISH_DIR: ./public
                  commit_message: ${{ github.event.head_commit.message }}
```

Zunächst müssen Sie das EXTERNAL_REPOSITORY in der obigen deploy.yml in Ihr eigenes GitHub Pages-Repository ändern, wie zum Beispiel meine Einstellung pseudoyu/pseudoyu.github.io.

Da wir vom Blog-Repository in ein externes GitHub Pages-Repository pushen müssen, sind spezifische Berechtigungen erforderlich. Sie müssen unter den Einstellungen des GitHub-Kontos - Developer setting - Personal access tokens einen Token erstellen.

![github_psersonal_access_token](https://image.pseudoyu.com/images/github_psersonal_access_token.png)

Die Berechtigungen müssen repo und workflow aktivieren.

![yu_blog_personal_token](https://image.pseudoyu.com/images/yu_blog_personal_token.png)

Kopieren Sie nach der Konfiguration den generierten Token (Hinweis: er wird nur einmal angezeigt) und fügen Sie dann die Umgebungsvariable PERSONAL_TOKEN als den Token, den wir gerade erstellt haben, in den Einstellungen - Secrets - Actions unseres Blog-Quellrepositories hinzu. Auf diese Weise kann GitHub Action auf den Token zugreifen.

Nach Abschluss der obigen Konfiguration pushen Sie den Code in das Repository, was GitHub Action auslöst, automatisch Blog-Seiten generiert und sie in das GitHub Pages-Repository pusht.

![yu_blog_ci](https://image.pseudoyu.com/images/yu_blog_ci.png)

Wenn das GitHub Pages-Repository aktualisiert wird, löst es automatisch die offizielle Seiten-Bereitstellungs-CI aus, wodurch unsere Website-Veröffentlichung erreicht wird.

![page_build_ci](https://image.pseudoyu.com/images/page_build_ci.png)

Nach der obigen Konfiguration haben wir die lokale Hugo-Blog-Einrichtung und Versionskontrolle, GitHub Pages Website-Bereitstellung und -Veröffentlichung, Hugo-Theme-Management und -Updates sowie andere Funktionen erreicht und ein vollständiges System implementiert. Jetzt müssen wir, wann immer wir mit der lokalen Bearbeitung von Blog-Inhalten mit der vertrauten Markdown-Syntax fertig sind, nur den Code pushen und ein paar Minuten warten, um über unsere benutzerdefinierte Domain auf die aktualisierte Website zuzugreifen.

### Komponentenerweiterungen

Ein vollständiges Blogsystem erfordert auch einige Komponenten, wie Website-Datenstatistiken und Kommentarsysteme. Ich habe umfassende Serverless-Setup-Tutorials für diese beiden Kernbedürfnisse geschrieben, die Sie nach Ihren Anforderungen bereitstellen und konfigurieren können.

- [Aufbau eines kostenlosen persönlichen Blog-Datenstatistiksystems von Grund auf (umami + Vercel + Heroku)]([https://www.pseudoyu.com/de/2022/05/21/free_blog_analysis_using_umami_vercel_and_heroku/](https://www.pseudoyu.com/de/2022/05/21/free_blog_analysis_using_umami_vercel_and_heroku/))
- [Leichtgewichtige Open-Source kostenlose Blog-Kommentarsystemlösung (Cusdis + Railway)]([https://www.pseudoyu.com/de/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/](https://www.pseudoyu.com/de/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/))

## Fazit

Das oben Genannte ist das kostenlose Blog-Automatisierungssystem, das ich mit Hugo und GitHub Action implementiert habe. Mein Implementierungsrepository befindet sich im pseudoyu/yu-blog Repository, und mein angepasstes Theme-Repository ist in pseudoyu/hugo-theme-den.

Ich habe auch viele interessante automatisierte persönliche Statistikfunktionen mit GitHub Action implementiert, die automatisch mein GitHub-Profil aktualisieren. Das Projektrepository ist pseudoyu/pseudoyu. Sie können .github/workflows selbst erkunden. Diese Systeme werden kontinuierlich verbessert, und ich lade alle ein, beizutragen und sich auszutauschen.

## Referenzen

> 1. [Hugo Offizielle Website](https://gohugo.io)
> 2. [GitHub Action](https://github.com/features/actions)
> 3. [GitHub Pages](https://pages.github.com)
> 4. [Cloudflare Offizielle Website](https://www.cloudflare.com)
> 5. [Kostenlose Einrichtungs- und Bereitstellungslösung für ein persönliches Blogsystem (Hugo + GitHub Pages + Cusdis)]([https://www.pseudoyu.com/de/2022/03/24/free_blog_deploy_using_hugo_and_cusdis/](https://www.pseudoyu.com/de/2022/03/24/free_blog_deploy_using_hugo_and_cusdis/))
> 6. [Aufbau eines kostenlosen persönlichen Blog-Datenstatistiksystems von Grund auf (umami + Vercel + Heroku)]([https://www.pseudoyu.com/de/2022/05/21/free_blog_analysis_using_umami_vercel_and_heroku/](https://www.pseudoyu.com/de/2022/05/21/free_blog_analysis_using_umami_vercel_and_heroku/))
> 7. [Leichtgewichtige Open-Source kostenlose Blog-Kommentarsystemlösung (Cusdis + Railway)]([https://www.pseudoyu.com/de/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/](https://www.pseudoyu.com/de/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/))
> 8. [Mein Pseudoyu Persönlicher Blog