---
title: "Baue dein kostenloses Bildhosting-System von Grund auf (Cloudflare R2 + WebP Cloud + PicGo)"
date: 2024-06-30T14:12:47+08:00
draft: false
tags: ["image-hosting", "cloudflare", "r2", "webp cloud", "serverless", "s3", "blog", "picgo"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

## Vorwort

Im Artikel "Was sich 2024 in meinem Blog geändert hat" habe ich das Blogsystem vorgestellt, das ich mit Serverless-Plattformen und einigen Open-Source-Projekten aufgebaut habe, und auch diese Tutorialreihe begonnen, um den gesamten Aufbau- und Bereitstellungsprozess zu dokumentieren.

Dieser Artikel befasst sich mit der Lösung für das Bildhosting-System.

**[2024-07-02 Update]**

Ich habe ein neues Tutorial geschrieben, das Datenschutz und Urheberrechtsschutz für das Bildhosting-System implementiert, was als zusätzliches Kapitel betrachtet werden kann.

- [Füge Datenschutz und Urheberrechtsschutz zu deinem Bildhosting mit WebP Cloud und Cloudflare WAF hinzu](https://www.pseudoyu.com/de/2024/07/02/protect_your_image_using_webp_and_cloudflare_waf/)

## Iterationen der Bildhosting-Lösung

Zu Beginn meines Blog-Aufbaus wurden aufgrund des begrenzten Inhalts und weniger Illustrationen die meisten Bilder direkt im `static`-Verzeichnis meines Hugo-Blog-Repositories platziert. Ich spürte keine Unannehmlichkeiten, bis ich auf mehreren Plattformen veröffentlichen musste. Nach dem Kopieren der Markdown-Quelldateien des Blogs konnten alle Bilder nicht angezeigt werden, da sie relative Pfade zum Blog verwendeten. Ich musste die Bilder einzeln neu hochladen, was sehr umständlich war.

Damals begann ich, das Konzept des Bildhostings zu verstehen - das Hochladen von Bildern auf einen dedizierten Speicherdienst und die Verwendung über öffentliche Links. Dies ermöglicht nicht nur eine einheitliche Verwaltung, sondern reduziert auch effektiv die Größe der Blog-Repository-Dateien und verbessert die Ladegeschwindigkeit der Website.

### GitHub + jsDelivr CDN + PicGo

Zunächst erstellte ich ein neues GitHub-Repository "GitHub - image-hosting", lud direkt über PicGo in das Repository hoch und änderte den von PicGo zurückgegebenen Bildpfad in den CDN-beschleunigten Link von [jsDelivr](https://www.jsdelivr.com/). Es war recht praktisch und hatte sogar Versionskontrolle.

Doch die guten Zeiten währten nicht lange. jsDelivr litt unter DNS-Verschmutzung und wurde in Festland-China blockiert, was dazu führte, dass meine Blog-Bilder für einen langen Zeitraum völlig unladbar waren. Dies ließ mich einige Bedenken über diesen rein CDN-abhängigen Ansatz haben. Zudem basiert das Hosting von Bildern auf GitHub auf Code-Repositories, und das Hochladen von Bildern hängt von Code-Commits ab, was leicht die Commit-Historie verschmutzen kann. Es ist letztendlich eine Art Missbrauch, und wenn es Probleme mit dem Konto/Repository-Zugriff gibt, ist es leicht, alle Bilder zu verlieren. Also begann ich, nach anderen Lösungen zu suchen.

### Aliyun OSS + PicGo

Die zweite Option, die mir in den Sinn kam, war der Objektspeicher, der von Cloud-Service-Anbietern bereitgestellt wird. Dienste wie Amazon S3 und Aliyun OSS bieten nicht nur öffentlich zugängliche Links, sondern auch Vorteile wie Zugriffskontrolle, Datensicherung und Skalierbarkeit. Sie bieten eine optimale Lösung für die Speicherung und Verwaltung von Dateidaten zu relativ geringen Kosten.

Da ich den Zugriff für Benutzer in Festland-China optimieren wollte, entschied ich mich letztendlich für Aliyun OSS. Die Konfiguration war nicht kompliziert, und ich verwendete weiterhin PicGo zum Hochladen und Konvertieren in Aliyun OSS-Links. Es gab eine spürbare Verbesserung der Zugriffsgeschwindigkeit.

![aliyunoss_invoice](https://image.pseudoyu.com/images/aliyunoss_invoice.jpeg)

Aufgrund des verbrauchsabhängigen Abrechnungsmodells waren die kontinuierlich steigenden Kosten jedoch eine Überlegung für einen nicht-kommerziellen persönlichen Blog. Anfang 2023 gab es eine Zeit, in der der Traffic meines Blogs recht hoch war, und die monatlichen Rechnungen stiegen weiter an. Zudem musste ich, wenn ich eine benutzerdefinierte Zugriffsdomain für Aliyun OSS verwenden wollte, den Anmeldeprozess durchlaufen. Da meine Domain über Cloudflare gehostet wird, zog ich eine Anmeldung nicht in Betracht. Also überlegte ich nach ein paar Monaten Nutzung, die Bildhosting-Lösung erneut zu ändern.

### Chevereto + PicGo

Nach einiger Recherche implementierte ich die kostenlose selbstgehostete Version von [Chevereto](https://github.com/rodber/chevereto-free) mit einem Docker-Image auf meinem Bandwagon-Server (mit guter Konnektivität, CN2GIA DC6 Rechenzentrum) und montierte die Bilder als Docker-Volume auf dem Host.

Ehrlich gesagt ist der Interfacestil von Chevereto etwas veraltet und verwendet immer noch den alten PHP-Dienst. Die kostenlose Version wurde seit langem nicht mehr gewartet oder aktualisiert, aber sie ist umfassend in der Funktionalität. Man kann immer noch PicGo verwenden, um mit Cheveretos API für Bildupload und andere Operationen zu interagieren, und die Stabilität ist gut. Also nutzte ich es anderthalb Jahre lang.

Aber ich war zu sorglos in Bezug auf die Stabilität selbstgehosteter Dienste und die Kostbarkeit von Daten. Vor einigen Tagen fiel der Server plötzlich aus, mit einem Kernelfehler, der einen Neustart verhinderte. Der Ausfall des Dienstes war das eine, aber ich konnte meine Bilddaten aus den letzten eineinhalb Jahren nicht exportieren. Ich kontaktierte den technischen Support über ein Ticket, aber sie antworteten nur zweimal an einem Tag, einmal mit der Aufforderung neu zu starten und einmal mit dem Vorschlag, einen Netzwerkadministrator zur Untersuchung anzuheuern.

Ich musste mich selbst helfen. Nach der Suche nach verschiedenen Lösungen online und einem Tag des Kämpfens gelang es mir schließlich, das Problem zu lösen. Aber diese Lektion gab mir ein ganz neues Verständnis für die Sicherung und Stabilität selbstgehosteter Dienste mit wichtigen Daten. Zusätzlich stellte ich fest, als ich neu implementieren wollte, dass die kostenlosen Versionsbilder offline genommen worden waren und nur noch eine jährlich bezahlte Lizenzversion übrig war. Also gab ich die ursprüngliche Lösung auf.

### Cloudflare R2 + WebP Cloud + PicGo

![cloudflare_r2_free_tier](https://image.pseudoyu.com/images/cloudflare_r2_free_tier.png)

Also wandte ich mich wieder dem Objektspeicher von Cloud-Service-Anbietern zu und entdeckte den R2-Objektspeicherdienst, der vom Cyber-Bodhisattva Cloudflare bereitgestellt wird. Der kostenlose Plan umfasst 10 GB Speicherkapazität pro Monat, was für den persönlichen Gebrauch völlig ausreicht. Die Dienste und Datensicherheit eines großen Unternehmens bieten auch Sicherheit.

Um den Benutzerzugriff zu optimieren, verwendete ich auch einen "WebP Cloud"-Dienst, um die Bilder von R2 zu proxyen und die Bildgröße auf Proxy-Ebene weiter zu reduzieren. Obwohl die Geschwindigkeit für inländische Benutzer sicherlich nicht mit dem Netzwerk von Aliyun OSS vergleichbar ist, ist dies unter den umfassenden Bedingungen der Anmeldefreiheit, Stabilität und Kostenlosigkeit die beste Lösung, die ich mir vorstellen konnte.

Auf der Computerseite ist es immer noch fast ein Ein-Klick-Upload über den PicGo-Client und generiert Markdown-Bildlinks, die direkt im Blog verwendet werden können. Einmal konfiguriert, ist es sehr einfach zu bedienen.

## Anleitung zur Einrichtung des Bildhostings

Obwohl die Cloudflare R2 + WebP Cloud + PicGo-Lösung mehrere Komponenten und Plattformen umfasst, sind alle Operationen innerhalb des kostenlosen Plans. Dies ist die Lösung, für die ich mich letztendlich entschieden habe, und im Folgenden werde ich erläutern, wie man dieses kostenlose Bildhosting-System von Grund auf aufbaut.

### Cloudflare R2

R2 ist ein kostenloser Objektspeicherdienst, der von Cloudflare eingeführt wurde. Sie müssen ein kostenloses [Cloudflare-Konto](https://www.cloudflare.com/de-de/) registrieren, um es zu nutzen. Nach der Registrierung und Anmeldung klicken Sie in der linken Seitenleiste auf R2, um auf den Dienst zuzugreifen. Es ist jedoch zu beachten, dass für die Aktivierung des R2-Dienstes eine Kreditkarte gebunden werden muss (große inländische und internationale Kreditkarten werden akzeptiert), aber es werden keine Gebühren erhoben. Es dient hauptsächlich zur Überprüfung der Benutzeridentität.

#### Erstellen eines Bildhosting-Buckets

![cloudflare_r2_interview](https://image.pseudoyu.com/images/cloudflare_r2_interview.png)

Nach der Aktivierung des R2-Dienstes klicken Sie auf die Schaltfläche "Bucket erstellen" in der oberen rechten Ecke, um einen neuen Bucket zu erstellen.

![cloudflare_r2_create_bucket](https://image.pseudoyu.com/images/cloudflare_r2_create_bucket.png)

Auf der Erstellungskonfigurationsseite müssen Sie den Bucket-Namen eingeben. Es wird empfohlen, etwas Identifizierbares zu verwenden, da es später bei der Konfiguration von Uploads verwendet wird.

Wählen Sie für den Standort "Automatisch", aber Sie können zusätzlich einen Standorthinweis konfigurieren. Da ich später den "WebP Cloud"-Dienst des US-West-Rechenzentrums für die Bildproxyoptimierung verwenden werde, habe ich hier "North America West (WNAM)" gewählt. Sie können basierend auf Ihren Bedürfnissen andere Regionen wählen, aber Cloudflare garantiert nicht, dass Sie definitiv der angegebenen Region zugewiesen werden.

![cloudflare_r2_create_done](https://image.pseudoyu.com/images/cloudflare_r2_create_done.png)

Klicken Sie auf die Schaltfläche "Bucket erstellen", um die Erstellung abzuschließen. An diesem Punkt können wir bereits Dateien in unseren "yu-r2-test" Bucket hochladen. Sie können wählen, Dateien oder Ordner direkt auf der Webseite hochzuladen.

Sie können auch die S3 API für das Hochladen verwenden. Wir werden uns später auf diese Methode für das Hochladen mit dem PicGo-Client verlassen, aber es erfordert einige zusätzliche Konfigurationen. Klicken Sie auf die Option "Einstellungen" in der Navigationsleiste, um zu konfigurieren.

![cloudflare_r2_config](https://image.pseudoyu.com/images/cloudflare_r2_config.png)

Zunächst müssen wir die "R2.dev Subdomain" aktivieren. Dies ist für die öffentliche Adresse erforderlich, die später für den Zugriff auf die Bilder benötigt wird. Klicken Sie auf "Zugriff erlauben" und geben Sie "allow" ein, wie aufgefordert, um es zu aktivieren.

![r2_dev_domain_allow](https://image.pseudoyu.com/images/r2_dev_domain_allow.png)

Nach Abschluss wird eine öffentliche Webadresse angezeigt, die mit `r2.dev` endet. Dies ist die Adresse, die wir später für den Zugriff auf Bilder verwenden werden.

#### Benutzerdefinierte Bildhosting-Domain (Optional)

Die zugewiesene Adresse ist jedoch ziemlich lang und nicht leicht zu merken. Wir können eine "Benutzerdefinierte Domain" verwenden, um unseren exklusiven Domainnamen zu binden. Klicken Sie auf die Schaltfläche "Domain verbinden".

![r2_custom_domain_setup](https://image.pseudoyu.com/images/r2_custom_domain_setup.png)

Geben Sie den Domainnamen ein, den Sie binden möchten, z.B. `yu-r2-test.pseudoyu.com`, und klicken Sie auf Weiter.

![cloudflare_r2_custom_domain](https://image.pseudoyu.com/images/cloudflare_r2_custom_domain.png)

![r2_custom_domain_dns_wait](https://image.pseudoyu.com/images/r2_custom_domain_dns_wait.png)

Verbinden Sie die Domain und warten Sie, bis die DNS-Auflösung wirksam wird.

![r2_bucket_status](https://image.pseudoyu.com/images/r2_bucket_status.png)

Nach Abschluss sollte der Bucket-Status "Erlaubt" für "Öffentlicher URL-Zugriff" anzeigen, und "Domain" sollte den benutzerdefinierten Domainnamen anzeigen, den wir gerade eingerichtet haben, was auf eine erfolgreiche Konfiguration hinweist.

#### Konfigurieren der Bucket-Zugriffs-API

![yu_bucket_preview](https://image.pseudoyu.com/images/yu_bucket_preview.png)

Wenn wir die obige Konfiguration abgeschlossen haben, können wir zur Bucket "Objekte"-Oberfläche zurückkehren, ein Beispielbild hochladen und auf die Details klicken, um die Zugriffsadresse für dieses Bild anzuzeigen. An diesem Punkt haben wir einen zugänglichen Bildhosting-Dienst.

Das manuelle Hochladen von Bildern über die Cloudflare-Seite jedes Mal ist offensichtlich nicht praktisch genug. R2 bietet eine S3-kompatible API, die eine einfache Verwendung einiger Client/Kommandozeilen-Tools für Operationen wie Hochladen und Löschen ermöglicht.

![create_r2_api_token](https://image.pseudoyu.com/images/create_r2_api_token.png)

![create_r2_api_key](https://image.pseudoyu.com/images/create_r2_api_key.png)

Kehren Sie zur R2-Hauptseite zurück, klicken Sie auf "R2 API-Token verwalten" in der oberen rechten Ecke, dann klicken Sie nach dem Eintreten auf "API-Token erstellen".

![r2_apikey_conifg](https://image.pseudoyu.com/images/r2_apikey_conifg.png)

Geben Sie einen Token-Namen ein, wählen Sie "Objekt lesen und schreiben" für "Berechtigungen" und weisen Sie diese API dem zuvor erstellten Bucket zu. Dies minimiert die Berechtigungen und gewährleistet die Datensicherheit. Andere Optionen können als Standard belassen werden.

![api_key_config_details](https://image.pseudoyu.com/images/api_key_config_details.png)

Nach Abschluss der Erstellung werden alle Schlüssel angezeigt. Wir benötigen die folgenden drei Informationen für PicGo. Da sie jedoch nur einmal angezeigt werden, ist es ratsam, diese Parameterinformationen sicher in einem Passwort-Manager oder anderswo aufzubewahren.

An diesem Punkt haben wir den Konfigurationsteil auf Cloudflare R2 abgeschlossen. Als Nächstes müssen wir den PicGo-Client konfigurieren.

### PicGo

PicGo ist eine Werkzeugsoftware zum schnellen Hochladen und Erhalten von Bild-URLs, mit einem relativ reichen Plugin-Ökosystem, das mehrere Bildhosting-Dienste unterstützt. Sein GitHub-Repository ist "GitHub - Molunerfinn/PicGo", und Sie können den entsprechenden Plattform-Client zur Verwendung herunterladen.

#### Konfigurieren des R2-Bildhostings

PicGo selbst enthält kein S3-Bildhosting, aber es kann durch das Plugin "GitHub - wayjam/picgo-plugin-s3" unterstützt werden.

![picgo_s3_plugin](https://image.pseudoyu.com/images/picgo_s3_plugin.png)

Wählen Sie in den "Plugin-Einstellungen" die Installation aus, und eine neue Amazon S3-Option wird in den "Bildhosting-Einstellungen" erscheinen. Klicken Sie darauf, um die Konfigurationsoptionen aufzurufen.

![r2_picgo_s3_config](https://image.pseudoyu.com/images/r2_picgo_s3_config.png)

Es gibt mehrere Konfigurationselemente, die besondere Aufmerksamkeit erfordern:

- **Application Key ID**, füllen Sie die Access Key ID aus der R2 API aus
- **Application Key**, füllen Sie den Secret Access Key aus der R2 API aus
- **Bucket Name**, füllen Sie den in R2 erstellten Bucket-Namen aus, wie `yu-r2-test` in meinem obigen Beispiel
- **File Path**, der Dateipfad, der in R2 hochgeladen wird, ich habe mich für `{fileName}.{extName}` entschieden, um den ursprünglichen Dateinamen und die Erweiterung beizubehalten
- **Custom Node**, füllen Sie den "Jurisdiction-specific endpoint for S3 clients" aus der R2 API aus, d.h. den S3 Endpoint im Format `xxx.r2.cloudflarestorage.com`
- **Custom Domain Name**, füllen Sie die zuvor generierte Domain im Format `xxx.r2.dev` oder den benutzerdefinierten Domainnamen aus, wie `yu-r2-test.pseudoyu.com`, den ich konfiguriert habe

Andere Konfigurationen können als Standard belassen werden. Nachdem Sie sich vergewissert haben, dass die Parameter korrekt sind, klicken Sie auf "Bestätigen" und "Als Standard-Bildhosting festlegen".

#### Bild-Upload

![upload_r2_with_picgo](https://image.pseudoyu.com/images/upload_r2_with_picgo.png)

Nach Abschluss der obigen Konfiguration können wir Dateien direkt in den "Upload-Bereich" ziehen, um Bilder hochzuladen. Wenn es nach dem Hochladen korrekt angezeigt wird, ist die Konfiguration erfolgreich. Der generierte Link wird automatisch in der Systemzwischenablage sein, und Sie können ihn direkt dort einfügen, wo er benötigt wird.

![picgo_custom_url_format](https://image.pseudoyu.com/images/picgo_custom_url_format.png)

Und Sie können das entsprechende Format im Link-Format auswählen, wie URL- oder Markdown-Format-Links, die in Blogs verwendet werden können. Hier habe ich eine kleine Konfiguration vorgenommen: In den linken "PicGo-Einstellungen" - "Benutzerdefiniertes Link-Format" habe ich es zu `![$fileName]($url)` geändert und "Benutzerdefiniert" im Link-Format des Upload-Bereichs ausgewählt. Auf diese Weise wird nach dem Hochladen ein Markdown-Bildlink mit dem Dateinamen als Alt-Text basierend auf dem Dateinamen generiert.

### WebP Cloud Bildoptimierung

An diesem Punkt haben wir den gesamten Bildhosting-Aufbau, die Konfiguration und den Upload-Prozess abgeschlossen. Normalerweise sind jedoch die Bilder, die wir lokal screenshot oder mit Kameras aufnehmen, ziemlich groß, was für Besucher lange zum Laden dauern würde und nicht direkt für die Internetveröffentlichung geeignet ist.

![tiny_png_compress](https://image.pseudoyu.com/images/tiny_png_compress.png)

Lange Zeit verwendete ich eine sehr umständliche Methode: die API der Online-Website "TinyPNG" kombiniert mit einer Open-Source-macOS-Client-Anwendung. Ich würde Bilder zur Komprimierung hineinziehen, bevor ich sie über PicGo zum Bildhosting hochlud. Dies konnte normalerweise die Bildgröße um mehr als 50% reduzieren, mit minimalem Verlust der Bildqualität. Es war umständlich, aber effektiv.

Nachdem ich diesmal die Bildhosting-Lösung geändert hatte, begann ich auch, nach intelligenteren Bildoptimierungsdiensten zu suchen, und dachte an "WebP Cloud".

Ich habe tatsächlich letztes Jahr an einem Abend von diesem Dienst erfahren, als ich mit [STRRL](https://x.com/strrlthedev) in einer Spielhalle in einem Einkaufszentrum in Hangzhou Leute beim Rhythmusspiele spielen beobachtete. Er zeigte mir die Nachricht, dass ein Blogbeitrag von [Nova Kwok](https://x.com/n0vad3v) die Hacker News-Rangliste anführte, und wir verbrachten eine halbe Stunde damit, ihn gemeinsam anzuschauen. Damals wusste ich nur, dass es ein Dienst zur Optimierung von Bildern war, verstand ihn aber nicht im Detail.

Also öffnete ich die offizielle Website "webp.se" erneut, um eine detailliertere Einführung zu sehen.

![webp_se_intro](https://image.pseudoyu.com/images/webp_se_intro.png)

Einfach ausgedrückt, ist dies ein CDN-ähnlicher Bild-Proxy-SaaS-Dienst, der die Bildgröße erheblich reduzieren kann, während er fast die gleiche Bildqualität beibehält, und so die gesamte Site-Ladegeschwindigkeit beschleunigt. Mit seiner Entwicklung bietet er jetzt neben der Reduzierung der Bildgröße mehr praktische Funktionen wie Caching, Hinzufügen von Wasserzeichen, Bildfilter und bietet benutzerdefinierte Header-Konfigurationsoptionen.

Nach einem Rundgang fühlte ich, dass es meine Bildoptimierungsanforderungen für den Blog gut erfüllen könnte, also begann ich, mit der Konfiguration zu spielen.

#### Konfigurieren von WebP Cloud

![webp_cloud_login](https://image.pseudoyu.com/images/webp_cloud_login.png)

Melden Sie sich zunächst über die GitHub-Autorisierung bei der [WebP Cloud](https://dashboard.webp.se/) Plattform an.

![webp_cloud_overview](https://image.pseudoyu.com/images/webp_cloud_overview.png)

Die Seite ist sehr intuitiv und zeigt hauptsächlich das kostenlose Kontingent und zusätzliche Kontingentdaten unter dem aktuellen Plan sowie einige Nutzungsstatistiken an.

Klicken Sie auf die Schaltfläche "Proxy erstellen", um eine Konfiguration hinzuzufügen.

![webp_cloud_config](https://image.pseudoyu.com/images/webp_cloud_config.png)

- Um den Zugriff für Benutzer in China zu optimieren, habe ich für "Proxy Region" die US-West-Region "Hillsboro, OR" gewählt
- Füllen Sie einen benutzerdefinierten Namen für "Proxy Name" aus
- "Proxy Origin URL" ist wichtig, Sie müssen den benutzerdefinierten R2-Domainnamen ausfüllen, den wir zuvor konfiguriert haben, wie `yu-r2-test.pseudoyu.com` in meinem Fall. Wenn Sie keinen benutzerdefinierten Domainnamen konfiguriert haben, füllen Sie die von R2 bereitgestellte Domain im Format `xxx.r2.dev` aus

![yu_webp_test](https://image.pseudoyu.com/images/yu_webp_test.png)

Das unter "Visitor" im Abschnitt Basic info des Bildes gezeigte Format `xxx.webp.li` ist unsere Proxy-Adresse.

Zum Beispiel kann auf die Datei [yu-r2-test.pseudoyu.com/new_mbp_setup.jpg](https://yu-r2-test.pseudoyu.com/new_mbp_setup.jpg), die wir zuvor über PicGo in R2 hochgeladen haben, mit diesem Link zugegriffen werden: [dc84642.webp.li/new_mbp_setup.jpg](https://dc84642.webp.li/new_mbp_setup.jpg).

~~Wenn Ihnen die Standard-Proxy-Adresse nicht gefällt, können Sie den Entwickler über den Chat in der unteren rechten Ecke oder per E-Mail kontaktieren, um den Domainnamen anzupassen. In Zukunft könnte es einen automatisierteren Konfigurationsprozess geben.~~

**[2024-07-06 Update]**

Die Konfiguration benutzerdefinierter Domains wird jetzt unterstützt. Für detaillierte Anweisungen beachten Sie bitte "Custom Domain | WebP Cloud Services Docs".

#### Ändern der PicGo-Konfiguration

![change_pic_go_config](https://image.pseudoyu.com/images/change_pic_go_config.png)

Es ist wichtig zu beachten, dass wir, da die Bilder, die wir letztendlich im Blog platzieren müssen, Links sind, die durch WebP Cloud geproxyt wurden, zu den "Bildhosting-Einstellungen" von PicGo zurückkehren und die "Benutzerdefinierte Domain" in die WebP Cloud-Proxy-Adresse ändern müssen, die wir gerade konfiguriert haben, die im Format `xxx.webp.li` oder andere benutzerdefinierte Domainnamen vorliegt.

#### Verwendung von WebP Cloud

Kostenlose Benutzer haben 2000 Free Quota pro Tag, was bedeutet, dass sie 2000 Bildzugriffsanfragen proxyen können und 100M Bild-Cache bereitstellen. Dies ist für allgemeine Benutzer völlig ausreichend. Wenn es einige spezifische Perioden mit höherem Traffic gibt, können Sie auch zusätzliches Kontingent kaufen, was sehr günstig ist.

Wenn das Kontingent überschritten wird, wird der Zugriff 301 zur Quellbildadresse umgeleitet, ohne Komprimierung durch den WebP Cloud-Dienst, aber es wird immer noch nutzbar sein. Wenn der Cache 100M überschreitet, wird er nach dem LRU-Algorithmus gelöscht, so dass immer noch sichergestellt werden kann, dass einige häufig angeforderte Bilder eine gute Zugriffserfahrung haben können.

![yu_webp_uasge](https://image.pseudoyu.com/images/yu_webp_uasge.png)

Die täglichen Besuche meines Blogs liegen bei etwa 300-500 Besuchen. Wenn man einige RSS-Abonnements und Crawler-Traffic hinzufügt, liegen laut WebP Cloud-Statistiken die täglichen Anfragen bei etwa 4000-5000, mit 10000+ an Tagen, an denen ich neue Beiträge veröffentliche.

![webp_cloud_price](https://image.pseudoyu.com/images/webp_cloud_price.png)

Also habe ich mich vorerst für den Lite-Plan entschieden, kombiniert mit einiger zusätzlicher Nutzung, um Spitzenverkehr abzudecken. Ich plane, noch eine Weile zu beobachten, um zu sehen, wie es läuft.

## Fazit

Das oben Genannte ist meine Lösung für den Aufbau des Bildhosting-Systems. Alle Bilder in diesem Artikel wurden ebenfalls mit PicGo hochgeladen, in Cloudflare R2 gespeichert und durch WebP Cloud-Proxy optimiert.

Dies ist eines meiner Blog-Setup- und Deployment-Serien-Tutorials. Wenn Sie daran interessiert sind, Kommentarsysteme, Datenstatistiksysteme usw. einzurichten, bleiben Sie dran. Ich hoffe, dies kann für alle als Referenz dienen.