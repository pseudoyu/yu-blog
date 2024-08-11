---
title: "Baue dein kostenloses Blog-Kommentarsystem von Grund auf (Remark42 + fly.io)"
date: 2024-07-22T01:10:42+08:00
draft: false
tags: ["commenting-system", "serverless", "fly.io", "blog"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

## Vorwort

In dem Artikel "Was hat sich 2024 in meinem Blog verändert" habe ich das Blog-System vorgestellt, das ich mit Serverless-Plattformen und einigen Open-Source-Projekten aufgebaut habe, und auch diese Tutorialreihe begonnen, um den gesamten Prozess des Aufbaus und der Bereitstellung zu dokumentieren.

Dieser Artikel behandelt die Lösung für das Kommentarsystem.

## Evolution der Kommentarsysteme

![remark42_comments](https://image.pseudoyu.com/images/remark42_comments.png)

Ich habe oft das Gefühl, dass Kommentare nicht nur Kommunikation zwischen Lesern und Autoren sind, sondern der Inhalt selbst auch Teil des Artikels ist. Manchmal können die Gedanken und Diskussionen in Kommentaren wertvoller sein als der Artikel selbst. Daher habe ich dem Kommentarsystem schon immer große Bedeutung beigemessen. Ich bin nicht bereit, einigen von Drittanbietern gehosteten Diensten zu vertrauen, möchte keine Zensur und wünsche mir einen möglichst minimalistischen Stil, der mit meinem Blog-Stil übereinstimmt.

Während der Entwicklung meines Blogs hat die Lösung für das Kommentarsystem mehrere Iterationen durchlaufen. Bezüglich der Arten und Auswahl von Kommentarsystemen gefällt mir die detaillierte Einführung des Entwicklers [reorx](https://reorx.com/) in "Changing Blog Commenting Systems" sehr gut. Ich werde hier nicht weiter darauf eingehen; dieser Artikel konzentriert sich mehr auf persönliche Erfahrungen und den detaillierten Einrichtungsprozess.

### Disqus

Das erste Blog-Kommentarsystem, das ich verwendete, war das berüchtigte Disqus, ein umständliches und die Privatsphäre der Nutzer sammelndes bekanntes Kommentarsystem. Weil es langsam lädt und die kostenlose Version oft mit einigen Anzeigen daherkommt, war es wirklich unerträglich. Außerdem gab es zu diesem Zeitpunkt praktisch keine Kommentare, sodass es keine Migrationslast gab. Ich habe es nach kurzer Nutzung aufgegeben.

### Utterances

Also wechselte ich zu einem anderen Kommentarsystem namens utterances, das auf GitHub Issues basiert. Es generiert für jeden Artikel ein Issue, und Benutzer kommentieren das Issue, indem sie die GitHub-Anmeldung autorisieren. Der Vorteil dieser Methode ist, dass sie nur die Autorisierung eines utterances-bots für die Verwaltung benötigt, ohne dass man selbst Dienste bereitstellen und Datenbanken warten muss. Nach einiger Zeit der Nutzung bemerkte ich jedoch mehrere Nachteile:

- Es ist auf die GitHub-API für die Kommentarverwaltung angewiesen. Wenn sich die Schnittstelle später ändert oder Einschränkungen für diese Art von Kommentarmethode mit Issues eingeführt werden, wäre es instabil.
- Leser müssen die GitHub-Anmeldung autorisieren, was für Nicht-Techniker oder Leser auf mobilen Geräten sehr unbequem ist.
- Es verschmutzt die Issues-Aufzeichnung des GitHub-Repositories und ist auch für die spätere Migration zu anderen Systemen unbequem.

### Cusdis + Supabase + Vercel

Cusdis ist ein Open-Source-Kommentarsystem mit Fokus auf Datenschutz, entwickelt von [Randy](https://lutaonan.com/). Es ist sehr leichtgewichtig, nur etwa 5kb nach der Gzip-Komprimierung. Am Namen kann man erkennen, dass es schwer zu ertragen ist, Disqus zu benutzen, also hat er eine alternative Version erstellt. Daher unterstützt es auch den Import historischer Daten aus Disqus, was sehr durchdacht ist.

Ich benutze es seit Mitte 2021, also genau drei Jahre. Abgesehen von den anfänglichen Schwierigkeiten mit Bereitstellungsplattformen aufgrund der Gebühren von Heroku und Railway, läuft es stetig. Allerdings bin ich auch auf einige Probleme bei der Nutzung gestoßen:

- Wahrscheinlich aufgrund einiger Modifikationen durch den eingebauten Browser von WeChat kann die Kommentarkomponente nicht gesehen werden, wenn der Blog aus dem WeChat-Chat/Dialog geöffnet wird.
- Obwohl man eine E-Mail-Adresse eingeben kann, unterstützt es nicht das Abonnieren von Kommentarantworten.
- Der Administrator muss Kommentare manuell überprüfen, aber der TG-Bot für Kommentarbenachrichtigungen fällt oft aus, was zu verpassten Kommentaren führt.

Insgesamt ist es jedoch auch heute noch eine sehr empfehlenswerte Lösung. Es ist leichtgewichtig, einfach selbst zu implementieren und hat einen minimalistischen und gut aussehenden Stil. Für Einrichtungsanweisungen siehe "Lightweight Open Source Free Blog Comment System Solution (Cusdis + Railway)".

Da Railway seinen Free Plan seit August letzten Jahres eingestellt hat, können Sie, wenn Sie es immer noch völlig kostenlos nutzen möchten, Vercel/Netlify/Zeabur verwenden, um das Hauptprojekt kostenlos bereitzustellen, und eine kostenlose PostgreSQL-Datenbankinstanz auf [Supabase](https://supabase.com) bereitstellen, wobei Sie den Link als Umgebungsvariable an den Cusdis-Dienst übergeben. Andere Verfahren sind ähnlich.

Auch weil seine Kernfunktionen seit langem nicht aktualisiert wurden, wirkt es im Vergleich zu anderen ausgereifteren Kommentarsystemen etwas rudimentär. Da ich jedoch auch dem Prinzip "gut genug ist gut genug" folge, hatte ich nie die Idee einer Migration/Aktualisierung. Ich habe nur eine Weile an der Entwicklung der Cusdis V2-Version teilgenommen, als ich Frontend lernte, aber ich habe es nicht lange gemacht.

Aufgrund des ständigen Scheiterns der Vercel-Bereitstellungs-Upgrades im April, was dazu führte, dass ich fast ein paar Wochen lang keine Kommentare erhielt, plus ich tatsächlich einige funktionale Anforderungen hatte, entschloss ich mich zur Migration und erforschte neue Lösungen.

### Remark42 + fly.io

Nach einigen Recherchen wählte ich [Remark42](https://remark42.com/), das [reorx](https://reorx.com/) schließlich in dem Artikel "Changing Blog Commenting Systems" auswählte.

Allein in Bezug auf die Konfigurationsoptionen ist es viel umfangreicher als Cusdis. Derzeit habe ich mehrere gängige Social-Account-Logins konfiguriert (GitHub, Twitter, Telegram, E-Mail), anonymes Kommentieren ist erlaubt, es unterstützt E-Mail-Abonnements für Antwortbenachrichtigungen, und ich habe auch TG-Bot-Benachrichtigungen eingerichtet. Es ist auf [fly.io](https://fly.io) bereitgestellt, mit Go-Single-Binary + Single-File-Datenbank, eine sehr komfortable Lösung. Für eine detailliertere Einführung und die Vorteile von Remark42 können Sie den oben erwähnten Artikel konsultieren.

Obwohl Remark42 einige Migrationslösungen anbietet, unterstützt es von Haus aus nicht Cusdis, das ich verwendete. Da es jedoch in Golang geschrieben ist, habe ich selbst Migrationslogik hinzugefügt und die über diese Jahre angesammelten 438 Kommentardaten nahtlos migriert.

## Remark42 + fly.io Bereitstellungsanweisungen

Die Remark42 + fly.io-Lösung umfasst nur einen einzigen Dienst, wobei die Datenbank boltdb in einem Volume gemountet wird, aber alle Operationen innerhalb des Free Plans von fly.io stattfinden.

Im Folgenden werde ich erklären, wie man dieses kostenlose Kommentarsystem von Grund auf aufbaut.

Der Remark42-Code selbst ist Open Source - "GitHub - umputun/remark42", und es stellt ein offiziell gepflegtes Image bereit. Die Dokumentation ist klar und leicht zu lesen, und Sie können es nach Ihren tatsächlichen Bedürfnissen konfigurieren.

### Installation des `flyctl` Kommandozeilentools

[fly.io](https://fly.io) unterscheidet sich stark von Railway, Zeabur usw., die ich zuvor verwendet habe, da die meisten Operationen auf der Kommandozeile und Konfigurationsdateien basieren, anstatt in einem Web-Management-Backend zu arbeiten. Daher müssen Sie zunächst das `flyctl` Kommandozeilentool gemäß der [Dokumentation](https://fly.io/docs/flyctl/install/) installieren.

Am Beispiel von macOS verwende ich `brew` für die Installation:

```bash
brew install flyctl
```

### Autorisierte Anmeldung

Öffnen Sie das Terminal-Tool und verwenden Sie den folgenden Befehl für die autorisierte Anmeldung:

```bash
flyctl auth login
```

![fly_auth_login](https://image.pseudoyu.com/images/fly_auth_login.png)

![fly_auth_web](https://image.pseudoyu.com/images/fly_auth_web.png)

Melden Sie sich auf der Webseite bei Ihrem Konto an oder erstellen Sie ein neues Konto. Nach Abschluss klicken Sie auf "Continue as xxx", um die autorisierte Anmeldung der `flyctl` Kommandozeile abzuschließen.

### Anwendungsverzeichnis erstellen

![create_fly_config](https://image.pseudoyu.com/images/create_fly_config.png)

Da ich normalerweise Konfigurationen manuell verwalte, anstatt ihre offiziellen Vorlagen zu verwenden, erstelle ich ein Verzeichnis wie `remark42-on-fly` und lege alle Konfigurationsdateien, Umgebungsvariablen usw. in diesem Pfad ab.

Und ich verwende VS Code zum Bearbeiten (Sie können auch vim oder andere Editoren/IDEs verwenden).

### Konfigurationsdatei

fly.io verwendet hauptsächlich Konfigurationsdateien im `.toml`-Format zur Dienstverwaltung. Hier ist die Konfigurationsdatei, die dem von mir bereitgestellten Dienst entspricht:

```toml
app = 'yu-remark42-01'
primary_region = 'hkg'

[build]
  image = 'umputun/remark42:latest'

[[mounts]]
  source = 'remark42_data_01'
  destination = '/srv/var'

[http_service]
  internal_port = 8080
  force_https = true
  auto_stop_machines = false
  auto_start_machines = true
  min_machines_running = 1
  processes = ['app']

[env]
  REMARK_URL = 'https://yu-remark42-01.fly.dev/'
  SECRET = 'remark42-secret'
  SITE= 'remark42-demo'
  ADMIN_SHARED_ID= ''

[[vm]]
  cpu_kind = 'shared'
  cpus = 1
  memory_mb = 256
```

Hier ist eine detaillierte Konfigurationserklärung:

- `app`: Anwendungsname, ich habe hier `yu-remark42-01` verwendet, Sie können ihn nach Ihrer tatsächlichen Situation ändern
- `primary_region`: Bereitstellungsregion, Sie können die Region, in der Sie bereitstellen möchten, aus dieser [Liste](https://fly.io/docs/reference/regions/#fly-io-regions) auswählen, ich habe Hongkong gewählt
- `[Build]`, dieser Teil betrifft hauptsächlich die Service-Image-Konfiguration
  - `image`: Service-Image, verwendet das offiziell bereitgestellte `umputun/remark42:latest`, Sie können bei Bedarf die Tag-Version angeben
- `[[mounts]]`, dieser Teil betrifft hauptsächlich die Konfiguration der Datenvolumeeinbindung, da Remark42 die boltdb-Datenbank verwendet, benötigt es persistenten Speicher
  - `source`: Name des Datenvolumes, ich habe hier `remark42_data_01` verwendet
  - `destination`: Einbindungsverzeichnis, ich habe es unter `/srv/var` eingebunden, was Remark42's Standard-Datenspeicherverzeichnis ist
- `[http_service]`, dieser Teil betrifft hauptsächlich dienstbezogene Konfigurationen
  - `internal_port`: Interner Dienstport, verwendet 8080
  - `force_https`: Erzwingt die Verwendung von HTTPS
  - `auto_stop_machines`: Auf `false` gesetzt
  - `auto_start_machines`: Auf `true` gesetzt, d.h. automatischer Start
  - `min_machines_running`: Minimale Anzahl laufender Maschinen, auf 1 gesetzt
  - `processes`: Dienstprozess, auf `app` gesetzt
- `[env]`, konfiguriert Umgebungsvariablen
  - `REMARK_URL`: URL des Remark42-Dienstes, ich habe hier `https://yu-remark42-demo.fly.dev/` verwendet, die automatisch von fly.io generiert wird, sie muss später geändert werden, wenn Sie eine benutzerdefinierte Domain haben
  - `SITE`: Seitenname, ich habe hier `remark42-demo` verwendet
  - `SECRET`: Benutzerdefinierter JWT-Token, ich habe hier `remark42-secret` verwendet
  - `ADMIN_SHARED_ID`: Administrator-ID, ich habe hier einen leeren String verwendet, d.h. kein Administrator, kann später ergänzt werden
- `[[vm]]`, dieser Teil betrifft hauptsächlich maschinenbezogene Konfigurationen
  - `cpu_kind`: CPU-Typ, auf `shared` gesetzt
  - `cpus`: Anzahl der CPUs, auf 1 gesetzt
  - `memory_mb`: Speicher, auf 256MB gesetzt

### Dienst erstellen

Nach Abschluss und Überprüfung der Konfiguration führen Sie den folgenden Befehl aus, um den Dienst zu erstellen:

```bash
flyctl launch
```

![fly_launch_remark42](https://image.pseudoyu.com/images/fly_launch_remark42.png)

### Konfiguration der Umgebungsvariablen

Derzeit haben wir nur den Dienst bereitgestellt und keine Umgebungsvariablen gesetzt, sodass der Dienst Probleme beim Starten haben wird. Als Nächstes setzen wir Umgebungsvariablen, legen Sie diese in der Datei `prod.env` ab:

```plaintext
AUTH_GITHUB_CID=<your_github_cid>
AUTH_GITHUB_CSEC=<your_github_csec>
AUTH_TWITTER_CID=<your_twitter_cid>
AUTH_TWITTER_CSEC=<your_twitter_csec>
AUTH_ANON=true
AUTH_TELEGRAM=true
TELEGRAM_TOKEN=<your_telegram_token>
NOTIFY_ADMINS=telegram
NOTIFY_TELEGRAM_CHAN=<your_telegram_group>
NOTIFY_USERS=email
AUTH_EMAIL_ENABLE=true
SMTP_HOST=smtp.gmail.com
SMTP_PORT=465
SMTP_TLS=true
SMTP_USERNAME=xxx@gmail.com
SMTP_PASSWORD=<your_password>
AUTH_EMAIL_FROM=xxx@gmail.com
NOTIFY_EMAIL_FROM=xxx@gmail.com
```

Der Teil der Umgebungsvariablen ist relativ komplex, beziehen Sie sich für spezifische Parameter auf die [Dokumentation](https://remark42.com/docs/configuration/authorization/).

#### Anmelde-/Autorisierungskonfiguration

Ich habe anonymes Kommentieren, GitHub, Twitter und Telegram-Methoden konfiguriert, Sie können andere Anmeldemethoden entsprechend Ihrer Situation konfigurieren.

- Anonyme Anmeldung
  - `AUTH_ANON`: Ob anonyme Kommentare erlaubt sind, ich habe mich dafür entschieden, es zu erlauben, d.h. Benutzer können kommentieren, ohne sich anzumelden
- GitHub-Anmeldung
  - `AUTH_GITHUB_CID` und `AUTH_GITHUB_CSEC`: Client ID und Client Secret der GitHub OAuth App
- Twitter-Anmeldung
  - `AUTH_TWITTER_CID` und `AUTH_TWITTER_CSEC`: Client ID und Client Secret der Twitter OAuth App
- Telegram-Anmeldung
  - `AUTH_TELEGRAM`: Ob Telegram-Anmeldung erlaubt ist
  - `TELEGRAM_TOKEN`: Telegram Bot Token, erstellt durch `botfather`
- E-Mail-Anmeldung
  - `AUTH_EMAIL_ENABLE`: Ob E-Mail-Anmeldung erlaubt ist
  - `AUTH_EMAIL_FROM`: Absende-E-Mail für E-Mail-Anmeldung

#### Benachrichtigungskonfiguration

- Telegram-Benachrichtigung für Administratoren, siehe [diesen Teil der Dokumentation](https://remark42.com/docs/configuration/telegram/) für die Erstellung und Konfiguration des Telegram-Bots
  - `NOTIFY_ADMINS`: Methode zur Benachrichtigung von Administratoren, wählen Sie telegram
  - `NOTIFY_TELEGRAM_CHAN`: Wenn Sie Telegram-Benachrichtigungen für Administratoren aktivieren, müssen Sie die entsprechende Channel-ID konfigurieren, füllen Sie einfach den ID-Teil nach `t.me/xxx` aus, wie z.B. `pseudoyuchat`
- E-Mail-Benachrichtigung für Benutzer, siehe [diesen Teil der Dokumentation](https://remark42.com/docs/configuration/email/) für die Konfiguration von E-Mail-SMTP usw.
  - `NOTIFY_USERS`: Methode zur Benachrichtigung von Benutzern, ich habe E-Mail gewählt, d.h. E-Mail-Benachrichtigung, daher müssen Sie das SMTP unten konfigurieren
  - `NOTIFY_EMAIL_FROM`: Absende-Adresse für E-Mail-Benachrichtigungen

#### E-Mail-SMTP-Konfiguration

Die oben erwähnte E-Mail-Anmeldung und E-Mail-Benachrichtigung benötigen beide die Konfiguration eines SMTP-Servers, dieser Teil kann auch entsprechend Ihrem E-Mail-Dienstanbieter [gemäß der Dokumentation](https://remark42.com/docs/configuration/email/) konfiguriert werden.

- `SMTP_HOST`: SMTP-Server-Adresse
- `SMTP_PORT`: SMTP-Server-Port
- `SMTP_TLS`: Ob TLS aktiviert werden soll
- `SMTP_USERNAME`: SMTP-Benutzername
- `SMTP_PASSWORD`: SMTP-Passwort

### Importieren von Umgebungsvariablen in den Dienst

Nachdem Sie die Umgebungsvariablen gemäß den obigen Anweisungen konfiguriert haben, führen Sie den folgenden Befehl im Verzeichnis aus, in dem sich die Konfigurationsdatei und die Umgebungsvariablendatei befinden, um die Umgebungsvariablen zu importieren:

```bash
fly secrets import < prod.env
```

![fly_secret_import](https://image.pseudoyu.com/images/fly_secret_import.png)

![deploy_status_remark42](https://image.pseudoyu.com/images/deploy_status_remark42.png)

Überprüfen Sie nach der Ausführung den Dienststatus in der fly.io-Konsole. Wenn der Status `Deployed` ist, zeigt dies eine erfolgreiche Bereitstellung an.

### Konfigurieren einer benutzerdefinierten Domain (Optional)

Wenn Sie die von fly.io bereitgestellte Standarddomain nicht verwenden möchten, können Sie eine benutzerdefinierte Domain konfigurieren.

![custom_domain_flyio](https://image.pseudoyu.com/images/custom_domain_flyio.png)

Gehen Sie in die fly.io-Konsole, wählen Sie den gerade bereitgestellten `yu-remark42-01`-Dienst aus, klicken Sie auf die Option `Certificates` auf der linken Seite, dann auf `Add a Certificate` in der oberen rechten Ecke und folgen Sie den Anweisungen, um eine benutzerdefinierte Domain hinzuzufügen.

![custom_domain_dns_in_fly](https://image.pseudoyu.com/images/custom_domain_dns_in_fly.png)

Nach dem Klick auf `Create Certificate` erscheint eine Seite mit den DNS-Einträgen, die Sie hinzufügen müssen. Folgen Sie den Anweisungen, um diese hinzuzufügen.

![cloudflare_dns_remark42](https://image.pseudoyu.com/images/cloudflare_dns_remark42.png)

![flyio_certificate_success](https://image.pseudoyu.com/images/flyio_certificate_success.png)

Zum Beispiel wird meine Domain bei Cloudflare gehostet, ich habe zwei DNS-Einträge gemäß den Anweisungen hinzugefügt. Kehren Sie zur Seite zurück und klicken Sie auf `Check again` oder warten Sie eine Weile und aktualisieren Sie, um zu sehen. Wenn alles grün angezeigt wird, war die Konfiguration erfolgreich.

![change_remark_url](https://image.pseudoyu.com/images/change_remark_url.png)

An diesem Punkt können wir `REMARK_URL` in `fly.toml` auf die benutzerdefinierte Domain ändern und dann den folgenden Befehl ausführen, um den Dienst neu bereitzustellen. Alle nachfolgenden Änderungen an der Konfigurationsdatei können mit diesem Befehl aktualisiert werden:

```bash
fly deploy
```

## Konfigurieren von Remark42 in Ihrem Blog

Nachdem wir die Bereitstellung des Remark42-Dienstes abgeschlossen haben, müssen wir die Remark42-Kommentarkomponente zu unseren Blogbeiträgen hinzufügen. Ich werde meinen Hugo-Blog als Beispiel verwenden.

### Definieren der Hugo-Theme-Kommentarkomponente

Ich habe eine neue Datei `comments.html` im Verzeichnis `layouts/partials` meines Hugo-Blogs erstellt, um die Remark42-Kommentarkomponente zu definieren:

```html
<div class="comments">
  <div class="title">
    <span>Kommentare</span>
    <span class="counter"><span class="remark42__counter" data-url="{{ .Permalink }}"></span></span>
  </div>
  <div id="remark42">
  </div>
</div>

<script>
  var remark_config = {
    host: 'https://comments.pseudoyu.com',
    site_id: 'pseudoyu.com',
    components: ['embed', 'counter'],
    max_shown_comments: 20,
    simple_view: true,
    theme: 'light',
  }
</script>

<script>
    (function () {
      // init or reset remark42
      const remark42 = window.REMARK42
      if (remark42) {
        remark42.destroy()
        remark42.createInstance(remark_config)
      } else {
        for (const component of remark_config.components) {
          var d = document, s = d.createElement('script');
          s.src = `${remark_config.host}/web/${component}.mjs`;
          s.type = 'module';
          s.defer = true;
          // prevent the <script> from loading mutiple times by InstantClick
          s.setAttribute('data-no-instant', '')
          d.head.appendChild(s);
        }
      }
    })();
</script>
```

Der `host` und `site_id` in `remark_config` müssen entsprechend Ihrer tatsächlichen Konfiguration geändert werden. Andere Teile der Konfiguration können unverändert bleiben oder gemäß der Dokumentation angepasst werden.

Nachdem Sie die `comments`-Komponente konfiguriert haben, fügen Sie sie am Ende des Artikels in `layouts/posts/single.html` ein:

```html
{{ partial "comments.html" . }}
```

![add_comments_code_in_hugo](https://image.pseudoyu.com/images/add_comments_code_in_hugo.png)

Die allgemeine Position ist wie im Bild gezeigt. Wenn Sie ein anderes Theme oder Blogsystem verwenden, müssen Sie die entsprechende Vorlagendatei für Ihre Artikel finden und modifizieren.

### Lokale Vorschau/Bereitstellung der Website

![test_remark42_embedded](https://image.pseudoyu.com/images/test_remark42_embedded.png)

An diesem Punkt können Sie lokal eine Vorschau anzeigen oder die Website bereitstellen, um zu überprüfen, ob das Kommentarsystem korrekt angezeigt wird. Damit ist unsere Dienstbereitstellung abgeschlossen.

### Benutzer-ID erhalten und Admin konfigurieren

![get_user_id_remark42](https://image.pseudoyu.com/images/get_user_id_remark42.png)

Nachdem Sie sich angemeldet, autorisiert und Kommentare getestet haben, können Sie auf das Avatar in Remark42 klicken, um die Verwaltungsseite zu öffnen. Doppelklicken Sie und dann `CMD/Ctrl+C`, um die Benutzer-ID zu erhalten, die mit `github_` oder anderen Plattformen beginnt. Sie können dies in `ADMIN_SHARED_ID` konfigurieren (ändern Sie die `fly.toml`-Konfigurationsdatei und führen Sie `fly deploy` aus, um neu bereitzustellen). Dies macht Sie zum Administrator, und Administratoren haben die Berechtigung, Kommentare anderer Benutzer zu löschen und zu verwalten.

## Weitere Überlegungen

Ich habe die Kommentardaten aus Cusdis im JSON-Format gemäß bestimmten Bedingungen exportiert und das Format durch ein Go-Programm konvertiert und migriert, wodurch alle vorherigen Kommentare erhalten blieben.

Da Cusdis selbst keine Exportfunktion bietet und der Migrationsbedarf zu nischenhaft ist, habe ich den Code nicht direkt zum Upstream beigetragen oder in ein vollständiges Skript geschrieben. Freunde mit ähnlichen Bedürfnissen können sich für die Verarbeitung auf diesen PR beziehen - "feat: add cusdis to remark42 migrator support by pseudoyu · Pull Request #1 · pseudoyu/remark42".

## Fazit

Das oben Genannte ist der Prozess des Aufbaus meines Blog-Kommentarsystems. Die Einrichtung und Konfiguration eines Kommentarsystems sind relativ komplex, und die Konfigurationsmethode in diesem Artikel kann im Laufe der Zeit veralten. Wenn Sie auf Probleme stoßen, beziehen Sie sich mehr auf die [offizielle Dokumentation](https://remark42.com/docs/getting-started/installation/).

Dies ist eines meiner Blog-Aufbau- und Bereitstellungs-Tutorialreihen. Wenn Sie daran interessiert sind, Datenstatistiksysteme, In-Blog-Suche usw. aufzubauen, bleiben Sie dran. Ich hoffe, dies kann allen als Referenz dienen.