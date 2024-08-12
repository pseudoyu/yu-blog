---
title: "Wochenrückblick #54 - Driftender Plan, gestohlene Brieftasche und Heimserver"
date: 2024-03-16T05:20:00+08:00
draft: false
tags: ["review", "life", "travel", "computer", "work", "love", "home assistant", "home server"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/photograph.mp3" caption="'Photograph - Ed Sheeran'" >}}

## Vorwort

![weekly_review_20240316_cover](https://image.pseudoyu.com/images/weekly_review_20240316_cover.png)

Dieser Beitrag ist eine Aufzeichnung und Reflexion meines Lebens vom `01.03.2024` bis zum `16.03.2024`.

Wie im vorherigen Wochenrückblick erwähnt, begab ich mich auf einen driftenden Plan, der mit einer fast zweiwöchigen Reise durch "Hangzhou -> Shanghai -> Huzhou -> Nanjing -> Peking" endete. Größtenteils auf Jiangsu und Zhejiang beschränkt, gab es keine außergewöhnlichen Landschaften; es ging mehr um Menschen und Ereignisse. Da meine Hauptbrieftasche ohne erkennbaren Grund gestohlen wurde, installierte ich zwei primäre Computer neu, was eine Gelegenheit bot, meine Entwicklungsumgebungskonfiguration neu zu organisieren. Ich richtete das Mac Studio zu Hause als 24/7 Heimserver ein, auf dem ständig laufende Anwendungen wie Home Assistant zur Steuerung von Smart-Home-Geräten laufen - ein Bastelvorgang, der sich als recht interessant erwies. Bei der Arbeit ging das lang erwartete Alpha-Mainnet unseres Teams live, was ein Gefühl der Aufregung zurückbrachte, das ich lange nicht mehr gespürt hatte. Es gab auch viele andere faszinierende Vorkommnisse.

## Driftender Plan

![tianmushan_view](https://image.pseudoyu.com/images/tianmushan_view.jpg)

Die erste Station meines Nach-Neujahrs-Driftplans war Shanghai. Im Laufe der Jahre war ich dutzende Male dort, von ein- oder zweimonatigen Praktika bis hin zu kurzen Zwischenstopps. Normalerweise waren diese Besuche für bestimmte Zwecke oder um Menschen zu treffen. Wirklich dort zu "leben" war eine seltene Gelegenheit. Diesmal wählte ich keine belebte Gegend oder plante besondere Ausflüge. Stattdessen buchte ich einen einwöchigen Aufenthalt in einer Mietwohnung in der Nähe eines Freundes und nahm meine normale Arbeits- und Studienroutine wieder auf.

Gelegentlich wagte ich mich in nahegelegene Geschäftsviertel, um etwas zu essen. An Wochenenden traf ich mich mit lang nicht gesehenen Mitbewohnern aus dem College zum Essen. Die restliche Zeit arbeitete ich vom Hotel aus und schaffte es sogar, die lang erwartete Serie "Westworld" zu beenden. Zufälligerweise lebte ein Kollege nur ein oder zwei Kilometer entfernt, was zu einem kleinen Treffen eines dreiköpfigen Teams führte.

Als nächstes besuchte ich Huzhou und blieb eine Woche bei meinem Freund [Xiao](https://twitter.com/gxgexiao). Unsere Begegnung entstand aus einem Tweet, den er vor einem Jahr während seiner [Wanderungen durch verschiedene Orte](https://www.gexiao.me/2023/07/01/lets-wander/) gepostet hatte und in dem er Freunde in Hangzhou einlud, sich zu treffen. Zu dieser Zeit war ich gerade nach Hangzhou zurückgekehrt, voller Unsicherheit und Erwartungen für mein zukünftiges Leben. Ich fasste Mut, organisierte ein Abendessen und einen Spaziergang am Westsee. Obwohl es unser erstes Treffen war und wir wenig gemeinsam hatten, war es aufrichtig und vertrauensvoll.

Später zog er nach Huzhou. Ich hatte geplant, ihn im August zu besuchen, konnte es aber aus verschiedenen Gründen nicht schaffen, was mich bedauern ließ. Also nutzte ich diese Driftgelegenheit, um dieses Versprechen zu erfüllen. Wir wanderten abseits der Wege im Moganshan, gingen an den Klippen von Anjis Wolkenwiese entlang und besuchten zwei digitale Nomadenkommunen. Ich fühlte mich von ihrer Gemeinschaftsatmosphäre recht angezogen. Dieses Jahr scheint es, als hätte ich ein lange verloren geglaubtes Gefühl der Entspannung im Leben wiederentdeckt und bin williger geworden, Menschen zu treffen und neue Dinge zu erleben. Das Leben dreht sich nicht mehr nur um Arbeit und Studium; Menschen und alles, was mit menschlichen Verbindungen zu tun hat, ist für mich ansprechender geworden. Aufgrund tieferer Verbindungen zu vielen "Online-Freunden" haben sich die Grenzen zwischen meinen Online- und Offline-Beziehungen allmählich verwischt.

Dank des "Work Together 1 Hour" unseres Unternehmens jeden Mittwoch empfahl ein Kollege die heißen Quellen in Tangshan und die Waldbibliothek in Moganshan. Also vereinbarte ich ein Treffen mit einem älteren Schulkameraden in Nanjing, genoss eine gemütliche Woche und begann, einige Wochenendausflugsziele zu erkunden. Das Leben ist greifbarer geworden.

## Gestohlene Brieftasche und Geräteneuinstallation

Kürzlich installierte ich die Systeme sowohl auf meinem Laptop als auch auf meinem Heim-Desktop neu. Der Auslöser war der unglückliche Diebstahl meiner Hauptbrieftasche. Basierend auf den Blockchain-Aufzeichnungen geschah es um die Mittagszeit am ersten Tag des Mondneujahrs. Alle Vermögenswerte in der Brieftasche (einschließlich einiger Airdrops aus der Teilnahme an Open-Source-Projekten) wurden in ETH und BNB umgewandelt, bevor sie übertragen wurden. Die Brieftasche enthielt immer noch meine ENS und einige NFTs (~~für die sich der Hacker anscheinend nicht interessierte~~). Der finanzielle Gesamtverlust war nicht bedeutend, aber da ich nicht genau feststellen konnte, wie der private Schlüssel durchgesickert war, hatte ich keine andere Wahl, als alle Geräteumgebungen neu zu installieren - ein Großunternehmen.

Da beide Systeme macOS waren, waren die Systemeinstellungen und Softwareaspekte ziemlich unkompliziert. Ich orientierte mich hauptsächlich an meinem persönlichen Toolbox-Projekt "[GitHub - yu-tools](https://github.com/pseudoyu/yu-tools)", nahm aber einige Subtraktionen vor und behielt nur das Wesentliche. Ich entdeckte, dass nach der Deinstallation von [Rewind](https://www.rewind.ai/) die Akkulaufzeit meines MacBook Pro deutlich verbessert wurde - ich kann jetzt fast ohne Ladegerät ausgehen.

![x-cmd_env_install](https://image.pseudoyu.com/images/x-cmd_env_install.png)

Ich nutzte diese Gelegenheit auch, um meine Softwareinstallationsquellen, Entwicklungsumgebungsverwaltung und Befehlszeilenkonfigurationen zu organisieren. Ich probierte das von der Firma eines Freundes entwickelte Projekt "[x-cmd](https://cn.x-cmd.com/)" aus.

![zshrc_config](https://image.pseudoyu.com/images/zshrc_config.png)

In Kombination mit ohmyzsh vereinfachte ich meine Befehlszeilenkonfiguration auf nur etwa ein Dutzend Zeilen. Später kann ich verschiedene Umgebungen und Befehlszeilen-Tools durch Befehle wie `x env` verwalten, was sehr benutzerfreundlich ist.

![x-cmd-env-ls](https://image.pseudoyu.com/images/x-cmd-env-ls.png)

Schließlich verwendete ich `x env`, um meine Go-, Node- und Python-Entwicklungsumgebungen zu verwalten, wodurch verschiedene Schritte wie die Installation von nvm und das Setzen von Umgebungsvariablen entfielen. Ich erlebte auch Unternehmens-Level-Kundensupport (bezogen auf das Bombardieren meines Freundes auf Telegram, um Probleme zu lösen 🤣). Es wird in Zukunft Teil meiner Standardeinrichtung sein, und ich befinde mich noch im Prozess der tiefen Erforschung.

Zusätzlich vereinheitlichte ich die Verwaltung von SSH-Schlüsseln und GPG-Signaturen zwischen den beiden Geräten. In Kombination mit Elpass für Passwort-Management und automatische Server-Anmeldung erreichte ich eine nahtlose Erfahrung beim Wechsel zwischen Pendeln und Zuhause-Bleiben.

## Heimserver & Home Assistant

~~Vielleicht weil ich älter werde~~, konnte ich den drei großen Versuchungen nicht entkommen: Router, Ladeköpfe und NAS. Für den Router verwende ich den Asus AC86U, den ich letztes Jahr von [STRRL](https://twitter.com/strrlthedev) gekauft habe, geflasht mit der neuesten Merlin-Firmware, was ziemlich ausreichend ist, sodass ich mich nicht mit Software-Routern befasst habe. Was Ladeköpfe/Ladegeräte angeht, habe ich nach der Erfahrung mit der vollständig transparenten Powerbank von Flashex, dem 100W GaN-Ladegerät und dem Mini-Ladegerät von Hard Candy Factory (~~das ich jetzt etwas vorsichtig benutze~~) auch auf dieser Front abgekühlt.

Schließlich streckte ich meine Hand nach einem NAS aus. Nach einem langen Gespräch mit Ares, unserem zuverlässigen Ops & Deep NAS DIY-Enthusiasten in unserem Team, beschloss ich, zunächst das Mac Studio zu Hause als Heimserver zu verwenden.

![yu_home_assistant_macstudio](https://image.pseudoyu.com/images/yu_home_assistant_macstudio.png)

Das Erste, was ich tat, war, alle Smart-Geräte zu Hause mit Home Assistant zu verbinden. Aufgrund des Apple M1-Chips gab es jedoch keine vorgefertigte offizielle Lösung. Nach viel Tüftelei folgte ich schließlich dem Artikel "[Home Assistant unter macOS mit einer Debian 12 Virtual Machine ausführen](https://siytek.com/home-assistant-macos-utm-debian-12/)", um eine Arm-Architektur Debian-Virtualmaschine mit UTM zu installieren. Ich ließ darin eine Vollversion von Home Assistant laufen und verwendete frp, um die Schnittstelle auf das öffentliche Netzwerk abzubilden. Schließlich bediene ich es direkt über die iOS-App und Webversion. Die aktuelle Lösung könnte Probleme mit dem Netzwerkmodus der Virtualmaschine haben, sodass ich sie noch nicht über HomeKit Bridge zur Apple Home App hinzufügen kann, aber die Möglichkeit, alle Xiaomi-, Yeelight- und Petkit-Haustiergeräte zu verbinden, ist vorerst ausreichend.

Als Heimserver läuft er 24/7 mit kaum wahrnehmbarem Geräusch und Stromverbrauch. Ich aktivierte smb-Dateifreigabe, ssh-Fernzugriff und Remote-vnc-Desktopsteuerung und stellte sicher, dass ich von außen durch Intranet-Penetration auf Heimgeräte zugreifen konnte.

Um Sicherheit und Stabilität zu gewährleisten, setzte ich gleichzeitig drei verschiedene Intranet-Penetrationslösungen ein:

1. frp
2. Surge Ponte
3. Cloudflare Argo Tunnel

Ich verwende die erste Lösung seit fast zwei Jahren, wie im Artikel "[Thin Client Development Workflow Based on frp Intranet Penetration](https://www.pseudoyu.com/en/2022/07/05/access_your_local_devices_using_reverse_proxy_tool_frp/)" beschrieben. Sie erfordert einen öffentlichen Netzwerkserver, ist aber einfach zu konfigurieren und stabil. Derzeit habe ich nur die Ports für ssh und Home Assistant beibehalten.

Die zweite Lösung erreicht eine bequeme Intranet-Penetration zwischen macOS/iOS-Geräten durch die Surge-Software. Sie können ihre detaillierte Einführung in "[Surge Ponte Guide](https://kb.nssurge.com/surge-knowledge-base/guidelines/ponte)" sehen. Sie erfordert eine Proxy-Linie, die UDP unterstützt, ist aber ansonsten fast Plug-and-Play. Ich verwende sie, um auf Dateien auf dem Mac Studio zu Hause und einige lokale Dienste zuzugreifen und kann auch direkt von außen auf Heim-Intranet-Router zugreifen und diese konfigurieren, hauptsächlich für den persönlichen Gebrauch.

Die dritte Lösung wurde kürzlich hinzugefügt, nachdem ich den Artikel "[Website mit Cloudflare Argo Tunnel (cloudflared) beschleunigen und sichern](https://nova.moe/accelerate-and-secure-with-cloudflared/)" gesehen hatte. Zuvor hatte ich es manuell mit dem cloudflared-Befehlszeilentool konfiguriert, was etwas umständlich war, sodass ich es nicht in die Praxis umgesetzt hatte. Kürzlich integrierte Cloudflare es in [Zero Trust](https://developers.cloudflare.com/cloudflare-one/), sodass fast alle Operationen über die Benutzeroberfläche konfiguriert werden können. Ich verwende es, um einige Dienste auf dem Heimserver zu betreiben, die im öffentlichen Netzwerk verfügbar sein müssen. Zum Beispiel habe ich neulich [codellama:70b](https://ollama.com/library/codellama:70b) mit [ollama](https://ollama.com/) ausgeführt und dann direkt über [ChatKit](https://chatkit.app/) darauf zugegriffen. Die Erfahrung war recht gut, nur etwas langsam in der Generierung, also war es eher ein Probelauf.

Zufälligerweise ist gerade das [Alpha-Mainnet](https://rss3.io/blog/en/introducing-rss3-alpha-mainnet) unseres Unternehmens live gegangen. Ich plane, selbst einen auf dem Heimserver zu betreiben, wenn der öffentliche Knoten verfügbar ist, kann es mir aber jetzt nicht leisten, ihn zu betreiben 🤣.

## VR-Fahrstunden

![vr_car_learn](https://image.pseudoyu.com/images/vr_car_learn.png)

Aufgrund einiger bevorstehender Selbstfahrbedürfnisse schrieb ich mich erneut in der Fahrschule ein, um mit dem Lernen zu beginnen. Diese Fahrschule verfügt über VR-Fahreinrichtungen, die ich weniger einschüchternd fand als ich mir vorgestellt hatte.

## Sonstige Angelegenheiten

Es scheint nicht viele andere interessante Dinge zu erwähnen zu geben. Ich finde mich abwechselnd in Geschäftigkeit und Angst darüber, nicht all die Dinge tun zu können, die ich tun möchte, aber alles wird langsam besser.

GitHub stellte eine kostenlose Copilot-Lizenz für Open Source zur Verfügung, sodass ich weiterhin Code-Vervollständigung und Copilot Chat kostenlos nutzen kann. In Kombination mit Claude 3 Sonnet und den kostenlosen GPT4-Tokens von "[burn.hair](https://burn.hair/register?aff=isWf)" kann ich nun all meine Coding- und verschiedenen anderen Bedürfnisse erfüllen.

Oh, und es ist mir gelungen, ein Treffen mit meinem Idol-Programmierer "[Randy](https://lutaonan.com/)" Ende des Monats in Peking zu arrangieren!!!

## Interessante Dinge und Objekte

### Input

Obwohl die meisten interessanten Inputs automatisch im Telegram-Kanal "Yu's Life" synchronisiert werden, werde ich trotzdem einige auswählen, um sie hier aufzulisten, damit es sich mehr wie ein Newsletter anfühlt.

#### Bücher

- [**Der Mönch und der Philosoph**](https://book.douban.com/subject/2228297/), einige Gedanken über Religion und Philosophie, gerade erst angefangen zu lesen, da es im Gespräch aufkam.
- [**Rot und Schwarz**](https://book.douban.com/subject/35781152/), sah eine Interpretation in einem Video, tief beeindruckt von der Beschreibung von Juliens Selbstwertgefühl und dem Hochmut, den es manifestiert, derzeit am Lesen.

#### Sammlungen

- [Million Lint ist in öffentlicher Beta | Million.js](https://million.dev/blog/lint)
- [Discover Daily von Perplexity](https://discoverdaily.ai/)
- [Ehco Relay](https://ehco-relay.cc/)
- [RSS3 Alpha Mainnet](https://rss3.io/blog/en/introducing-rss3-alpha-mainnet)
- [Velja — Sindre Sorhus](https://sindresorhus.com/velja)

#### Artikel

- [Das Integral des Glücks – Rainbow Line](https://1q43.blog/post/5322)
- [Warum ich Roadtrips liebe | Douban Pea](https://blog.douchi.space/road-trip/)
- [Software hat die Medien gefressen](https://www.wheresyoured.at/the-anti-economy/)
- [Risikofreie 360% Jahresrendite? Krypto-Arbitrage für Anfänger - TARESKY](https://taresky.com/crypto-arbitrage)
- [Wie NAT-Traversal funktioniert](https://tailscale.com/blog/how-nat-traversal-works)
- [Der Zusammenbruch und die Wiedergeburt eines sechsjährigen Open-Source-Projekts - DIYgod](https://diygod.cc/6-year-of-rsshub)
- [Baue ein effizientes tägliches Questsystem mit Notion Calendar | Douban Pea](https://blog.douchi.space/notion-calendar-daily-quest/#gsc.tab=0)
- [Home Assistant unter macOS mit einer Debian 12 Virtual Machine ausführen – Siytek](https://siytek.com/home-assistant-macos-utm-debian-12/)
- [Website mit Cloudflare Argo Tunnel (cloudflared) beschleunigen und sichern | Nova Kwok's Awesome Blog](https://nova.moe/accelerate-and-secure-with-cloudflared/)

#### Videos

- [Ich hab's, der beste Weg, dein Glück zu ändern, ist zu heiraten!](https://www.bilibili.com/video/BV1cF4m157Cy)
- [study vlog #48 | Ein Neuanfang mit 26 | Abendstudienroutine eines Programmierers | Einige kleine Geschenke Hoffe, sie gefallen dir](https://www.bilibili.com/video/BV1Lj421Z7Vz)

#### Filme

- [**Monster**](http://movie.douban.com/subject/35797709/), passt tatsächlich zu dem Thema, das Hirokazu Kore-eda beschreiben wollte, aber vielleicht mit zu vielen hinzugefügten Metaphern, es gelang nicht ganz wie beabsichtigt zu vermitteln, fühlte auch eine Diskrepanz in der Handlung und dem emotionalen Rhythmus.
- [**Das Schwein, die Schlange und die Taube**](http://movie.douban.com/subject/36151692/), Taiwan hat sicherlich einen einzigartigen Geschmack in Kriminalfilmen, das Thema und die Visuals sind in der Tat gewagt, aber es ist eher ein visuell befriedigendes Film, die Darstellung und Veränderungen in den Persönlichkeiten der Charaktere fühlen sich etwas überstürzt an.
- [**Westworld**](http://movie.douban.com/subject/35042913/), bevorzuge immer noch die Parkteile der ersten beiden Staffeln, einschließlich Williams Transformation. Die letzten beiden Staffeln fühlten sich, vielleicht aufgrund des Wunsches, ein zu großes Ausmaß des Erwachens des Bewusstseins und der Selbstwahl zu zeigen, am Ende ein bisschen wie Puppenspielen an.

#### Fernsehserien

- [**Maiko in der Küche**](http://movie.douban.com/subject/35727023/), derzeit am Schauen.

#### Musik

- [**Photograph**](https://open.spotify.com/track/1HNkqx9Ahdgi1Ixy2xkKkL) von Ed Sheeran
- [**Mild Surface**](https://open.spotify.com/track/4EP4BmTjXvMGKzhBwKzWu5) von Zhao Dengkai
- [**Different Lives**](https://open.spotify.com/track/7e7JVMegy4WBMnzuZE9Srq) von Fly By Midnight
- [**After the Love Has Gone**](https://open.spotify.com/track/7e7JVMegy4WBMn) von Earth, Wind & Fire

## Schluss

Das war's für diese Woche. Bis zum nächsten Mal!