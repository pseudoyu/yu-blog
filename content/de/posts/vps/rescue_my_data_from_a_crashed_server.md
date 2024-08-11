---
title: "Wie ich kritische Daten rettete, als mein Cloud-Server abstürzte"
date: 2024-07-01T15:30:00+08:00
draft: false
tags: ["vps", "server", "vps", "linux", "serverless", "self-hosting"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Vorwort

Am Freitag meldete mein bei BandwagonHost gekaufter 2C2G-Server plötzlich einen Kernel-Fehler, wodurch eine Verbindung über SSH oder ein Neustart unmöglich wurde. Nach einer Reihe von umständlichen Rettungsversuchen gelang es mir schließlich, über tausend Bilder von meinem Bildhosting-Dienst zu bergen. Noch immer erschüttert von dieser Erfahrung, möchte ich den Rettungsprozess dokumentieren und nebenbei die neue Bildhosting-Lösung erörtern, die ich eingerichtet habe.

## Server-Rettung

Dieser Server lief seit etwa eineinhalb Jahren stabil und beherbergte viele meiner kritischen Dienste, darunter über tausend unersetzliche Bilder für den Bildhosting-Dienst meines Blogs, die über Docker Volume persistent auf dem Host gespeichert waren.

### Server-Ausfall

Bis heute bin ich mir nicht sicher, was genau schiefgelaufen ist. An jenem Morgen musste ich die Bildversion meiner RSSHub-Instanz auf dem Server aktualisieren. Ich dachte, ich könnte gleich alle Dienste auf ihre neuesten Versionen bringen. Also führte ich eine Reihe von `docker pull` und `docker-compose` Neustart-Operationen durch. Alles schien in Ordnung, bis der letzte Dienst plötzlich seinen Container nicht starten konnte und einen Fehler ähnlich `not enough space` meldete. Ich nahm an, dass das Herunterladen zu vieler Bilder möglicherweise die Festplatte gefüllt hatte, also führte ich eine Reihe von `docker image prune --all`, `docker volume prune` und `docker system prune` Befehlen aus, wodurch fast 10 GB Speicherplatz freigegeben wurden. Ich versuchte es erneut, aber es funktionierte immer noch nicht.

Als Entwickler mit nur einem Hauch von Erfahrung in der Serverwartung war mein erster Instinkt, neu zu starten. Ich ahnte nicht, dass dies der Beginn eines tagelangen Albtraums sein würde.

![uptime_kuma_status](https://image.pseudoyu.com/images/uptime_kuma_status.png)

Nach dem Neustart alarmierte mich mein Uptime Kuma, dass alle Dienste offline waren, und ich konnte keine Verbindung mehr über SSH zur Maschine herstellen.

![bwg_kernel_panic](https://image.pseudoyu.com/images/bwg_kernel_panic.jpg)

Ich meldete mich schnell in der Online-Konsole von BandwagonHost an, nur um einen Kernel-Fehler zu entdecken, der den Start verhinderte. Selbst ein erzwungener Neustart erwies sich als wirkungslos. Ich reichte sofort ein Support-Ticket ein und wandte mich an meine DevOps-Freunde um Hilfe.

### Datenrettung

![ask_strrl_about_vps](https://image.pseudoyu.com/images/ask_strrl_about_vps.png)

STRRL vermutete, dass es ein Problem mit dem `rootfs` geben könnte. Da dieser kleine Cloud-Anbieter jedoch keine erweiterten Boot-Optionen oder andere zusätzliche Funktionen anbietet, konnten wir nur auf den offiziellen technischen Support warten. Dennoch machte mich der Gedanke, eineinhalb Jahre ungesicherte Bildhosting-Daten zu verlieren, nervös, also begann ich nach Möglichkeiten zu suchen, die Daten zu retten.

![bwg_vps_snapshot](https://image.pseudoyu.com/images/bwg_vps_snapshot.png)

Nach einer Untersuchung der BandwagonHost-Konsole stellte ich fest, dass sie wöchentliche Backups anbieten, die sofort in Snapshots umgewandelt werden können. Das neueste war vom 22. Juni, was glücklich war. Mein erster Gedanke war, die Maschine direkt aus dem Snapshot wiederherzustellen. Wenn die heutigen Operationen ein Konfigurationsproblem verursacht hätten, dann sollte ein Snapshot von vor einer Woche normal booten. Voller Hoffnung wartete ich etwa zehn Minuten auf die Snapshot-Wiederherstellung, nur um auf den gleichen Fehler zu stoßen. Immer noch nicht aufgebend, versuchte ich auch das Backup vom 15. Juni wiederherzustellen, aber vergeblich.

An diesem Punkt wurde mir der Ernst der Lage bewusst, und ich bereitete mich sogar auf das Worst-Case-Szenario vor, alle Daten zu verlieren. Während ich auf eine Antwort auf mein Support-Ticket wartete, begann ich nach ähnlichen Fällen zu suchen und entdeckte schließlich, dass die Snapshot-Images von BandwagonHost heruntergeladen werden können. Ich fand einen Artikel mit dem Titel "Anleitung zum Herunterladen, Entpacken und Betrachten von Daten aus BandwagonHost-Backup-Snapshot-Image-Dateien .tar.gz und .disk-Dateien."

Also lud ich das Snapshot-Image herunter und erhielt eine `.disk`-Datei. Diese Datei schien in einem proprietären Format zu sein. Laut der Anleitung kann sie mit dem Kommandozeilen-Tool `vboxmanage convertfromraw` von Virtual Box konvertiert werden. Nach dem Download von der offiziellen Website stellte ich jedoch fest, dass es M-Chip Macs nicht unterstützt. Also installierte und führte ich die Konvertierung auf meinem alten Intel Mac von 2019 aus, was zu einer `.vmdk`-Datei führte.

Nach der Konvertierung montierte ich diese `.vmdk` als Festplatte auf einer Virtual Box CentOS virtuellen Maschine, nur um auf den gleichen Fehler zu stoßen.

![7zip_format](https://image.pseudoyu.com/images/7zip_format.png)

Also versuchte ich einen anderen Ansatz und fand heraus, dass die [7-Zip](https://arc.net/l/quote/tirhqejc) Software das Extrahieren gängiger virtueller Maschinenformate unterstützt, aber der Client nur für Windows verfügbar ist.

![x7z_vmdk_x](https://image.pseudoyu.com/images/x7z_vmdk_x.jpg)

Obwohl ich theoretisch die Kommandozeilen-Version [p7zip](https://github.com/p7zip-project/p7zip) auf macOS hätte verwenden können, stieß ich beim Extrahieren auf Fehler. Also war auch dieser Weg blockiert. Ich kam auf eine umständliche Lösung: Ich lud eine Win11 virtuelle Maschine herunter, installierte die 7-Zip Software und extrahierte die Dateien erfolgreich.

![fuse_load_img](https://image.pseudoyu.com/images/fuse_load_img.png)

Ein weiteres Problem trat auf: Die resultierenden Dateien waren Linux-Disk-Image-Dateien im Format `1.img`, `2.img`, die auf macOS nicht geladen werden konnten. Ich fragte mein Unternehmensbetriebsteam, versuchte an fuse herumzubasteln, konnte sie aber immer noch nicht laden.

![ufs_load_img_log](https://image.pseudoyu.com/images/ufs_load_img_log.jpg)

Es gab in dieser Zeit auch gute Nachrichten. Bei meiner Suche im Internet entdeckte ich eine Datenrettungssoftware namens UFS Explorer. Ich probierte sie aus und stellte fest, dass sie die Dateien normal laden konnte, außer dass Dateien über 768k eine kostenpflichtige Version erforderten. Natürlich hatte ich nicht vor zu bezahlen, aber zu sehen, dass die Dateien tatsächlich lesbar waren, beruhigte mich. Zumindest waren die Daten da; der Rest war nur ein technisches Problem.

![bwg_reply](https://image.pseudoyu.com/images/bwg_reply.png)

Inzwischen antwortete BandwagonHost auf mein Ticket und schlug vor, ich solle einen Neustart oder eine Neuinstallation versuchen... 🤣

![str_orbstack_img](https://image.pseudoyu.com/images/str_orbstack_img.png)

Ich gab die Ticket-Kommunikation auf und versuchte weiterhin, meine Daten aus der `img`-Datei zu retten. Der stets einfallsreiche STRRL teilte mir mit, dass OrbStack eine Linux-Maschine starten kann, und ich diese `img` als Linux-Festplatte mounten könnte.

```bash
sudo losetup -fP 1.img
mkdir /mnt/bwg
sudo mount /dev/loop0 /mnt/bwg
```

Mit diesen Befehlen gelang es mir, mein `img`-Disk-Image erfolgreich auf der OrbStack Ubuntu-Maschine zu mounten.

![rescue_image_from_bwg_img](https://image.pseudoyu.com/images/rescue_image_from_bwg_img.png)

Als ich meine Bilder in der Kommandozeilenausgabe erscheinen sah, war ich fast zu Tränen gerührt 😭.

```bash
tar -czvf cheverto_chevereto_images.tar.gz cheverto_chevereto_images/
rsync -acvP ./cheverto_chevereto_images.tar.gz pseudoyu@[yu-mac-studio]:~/Downloads/
```

![rsync_service](https://image.pseudoyu.com/images/rsync_service.jpg)

Ich erstellte schnell ein `tar`-Paket und übertrug es mit `rsync` auf meinen lokalen Mac. Nach dem lokalen Entpacken sah ich endlich alle meine Bilder.

### Migration des Bildhosting-Systems zu r2

Aufgrund dieser Erfahrung vertraue ich jedoch nicht mehr auf die Stabilität von serverbasiertem Bildhosting. Ich verbrachte einen halben Tag damit, ein neues kostenloses Bildhosting-System einzurichten — "Aufbau Ihres kostenlosen Bildhosting-Systems von Grund auf (Cloudflare R2 + WebP Cloud + PicGo)".

![rclone_service](https://image.pseudoyu.com/images/rclone_service.jpg)

Um die vorhandenen Daten auf `r2` hochzuladen, verwendete ich `rclone`, um die Migration abzuschließen. Mission erfüllt!

## Fazit

Ich habe begonnen, Fragen der Dienstbereitstellung und Datensicherheit zu überdenken. Ich plane, einige wichtige Daten in die Cloud zu verlagern, anstatt mich auf einzelne Maschinen zu verlassen, und einige Dienste weiterhin auf serverlose Plattformen wie [fly.io](https://fly.io) und [Zeabur](https://zeabur.com/) zu migrieren.