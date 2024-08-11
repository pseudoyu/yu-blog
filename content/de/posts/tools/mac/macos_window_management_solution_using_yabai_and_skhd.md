---
title: "Automatisierte Fensterverwaltung: Ein macOS-Fensterverwaltungssystem basierend auf yabai+skhd"
date: 2022-06-04T13:08:33+08:00
draft: false
tags: ["macOS", "yabai", "skhd", "window management", "productivity"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《后来的我们 - 五月天》" >}}

## Vorwort

Es ist nun fünf Jahre her, seit ich begonnen habe, macOS zu nutzen, angefangen mit meinem ersten MacBook Pro, für das ich im Sommer 2017 gespart hatte. Mit wachsenden Arbeits- und Studienbedürfnissen habe ich allmählich begonnen, einen Multi-Screen-Workflow zu nutzen. Da ich ständig viele Fenster öffnen muss, wie IDEs, Textbearbeitungstools, Terminals, IM-Software, E-Mail-Clients und so weiter, kann es ohne sorgfältige Aufmerksamkeit schnell unübersichtlich werden. Ich ertappte mich dabei, wie ich ständig zwischen Fenstern wechselte, um das benötigte zu finden, was sehr umständlich war. So begann meine Reise, Lösungen für die Fensterverwaltung zu erforschen.

## Anforderungen an die Fensterverwaltungslösung

Zunächst skizzierte ich meine Bedürfnisse für die Fensterverwaltung und listete folgende Kernpunkte auf:

1. Automatische intelligente Split-Screen-Ausführung auf dem aktuellen Desktop jedes Mal, wenn ein neues Fenster geöffnet wird, wie Vollbild für ein einzelnes Fenster, Halbbildschirm für zwei Fenster und so weiter
2. Anpassung des Split-Screen-Layouts oder Wiederherstellung des ursprünglichen Layouts durch Tastenkombinationen
3. Springen zwischen verschiedenen Fenstern mittels Tastenkombinationen
4. Verschieben/Austauschen verschiedener Fensterpositionen mittels Tastenkombinationen
5. Bequeme Durchführung einiger Operationen am aktuellen Fenster durch Tastenkombinationen, wie Vollbild, Zentrieren, Senden an einen bestimmten Desktop, etc.
6. Schnelle Umschaltgeschwindigkeit

Mit diesen Anforderungen im Hinterkopf begann ich, einige beliebte Fensterverwaltungstools zu recherchieren, die derzeit verfügbar sind.

## Fensterverwaltungstools

Es gibt bereits viele relativ ausgereifte Fensterverwaltungstool-Lösungen auf dem Markt, wie [Magnet](https://magnet.crowdcafe.com), [BetterTouchTool's eingebaute Fenster-Snap-Funktion](https://docs.folivora.ai/docs/100_window_snapping_chapter.html), etc. Ich habe beide gekauft und verwendet, aber insgesamt hatte ich das Gefühl, dass sie nicht ganz zu meinem Workflow passten.

Magnet verlässt sich hauptsächlich auf Tastenkombinationen. Obwohl man Tastenkombinationen an die eigenen Gewohnheiten anpassen kann, sind die Gedächtniskosten hoch. Darüber hinaus müssen Sie es, wenn Sie mehrere Geräte haben, herunterladen und mit Ihrem eigenen Konto neu konfigurieren, um es weiterhin zu nutzen, was nicht bequem ist.

![magnet_keyshotcuts](https://image.pseudoyu.com/images/magnet_keyshotcuts.png)

BetterTouchTool hingegen verlässt sich darauf, die Maus zu verschiedenen Auslöseecken des Fensters zu bewegen. Der Vorteil ist, dass Sie keine Tastenkombinationen selbst einstellen müssen; Sie müssen nur die Maus an den Rand des Fensters bewegen, um Split-Screen zu erreichen. Es teilt jedoch den gleichen Nachteil wie Magnet: Jedes Mal, wenn Sie ein neues Fenster öffnen, müssen Sie immer noch manuell Split-Screen implementieren, was oft vergessen wird, wenn Sie beschäftigt sind oder viele Fenster geöffnet haben, was die Verwaltung unbequem macht.

![bettertouchtool_setting](https://image.pseudoyu.com/images/bettertouchtool_setting.png)

Da vorhandene Software meine Bedürfnisse nicht vollständig erfüllen konnte, wandte ich mich als Programmierer, der gerne bastelt, einigen hochgradig anpassbaren Lösungen aus der Open-Source-Community zu.

## Open-Source-Lösungen

### Hammerspoon

[Hammerspoon](https://www.hammerspoon.org) ist ein leistungsfähiges macOS-Automatisierungstool, das Fensterverwaltungsfunktionen durch das Schreiben einiger Lua-Skripte implementieren und Tastenkombinationen anpassen kann. Neben der Fensterverwaltung kann es auch umfangreiche Funktionen wie Schlafsteuerung und Zwischenablagetools implementieren. Nachdem ich es konfiguriert und eine Weile benutzt hatte, stellte ich fest, dass es ähnlich wie Magnet keine effektive Implementierung des intelligenten Split-Screens ermöglichte (vielleicht gibt es fertige Skripte, aber es ist mühsam, viele Anwendungen einzeln zu konfigurieren), also verwarf ich es ebenfalls.

### yabai + skhd

Nach einiger Recherche fand ich eine Lösung aus dem Video <[Blazing Fast Window Management on macOS](https://www.youtube.com/watch?v=fYsCAOfGjxE)> des YouTubers [Josh Medeski](https://www.youtube.com/c/JoshMedeski). Es ist Open-Source, kostenlos, hochgradig anpassbar und erfordert nur eine Konfigurationsdatei, um alle meine Bedürfnisse perfekt zu erfüllen.

#### yabai

[yabai](https://github.com/koekeishiya/yabai) ist eine Open-Source-Erweiterung des in macOS eingebauten Fensterverwaltungstools, die die freie Steuerung von Fenstern und mehreren Displays durch Befehlszeilentools ermöglicht. Seine Hauptfunktion ist die Verwendung des `binary space partitioning`-Algorithmus zur automatischen Modifikation des Fensterlayouts, was uns erlaubt, uns auf den Fensterinhalt zu konzentrieren, ohne aktives Management zu benötigen. Wir müssen nur das entsprechende Anwendungsfenster öffnen, um eine automatische Anordnung zu erreichen, ohne unseren Workflow zu stören.

#### skhd

[skhd](https://github.com/koekeishiya/skhd) ist ein macOS-Tastenkombinationsverwaltungstool, das andere Programme/Befehle durch Konfigurationsdateien aufrufen und binden kann, wie z.B. yabai's Fensterverwaltungsbefehle, um hochgradig angepasste Fensteroperationen zu erreichen. skhd's Implementierung ist sehr leistungsorientiert, mit schnellen Reaktionszeiten.

## Meine Fensterverwaltungskonfiguration

### yabai

#### Installation und Grundkonfiguration

yabai ist einfach zu installieren, folgen Sie einfach den Anweisungen in seinem [offiziellen Wiki](https://github.com/koekeishiya/yabai/wiki/Installing-yabai-(latest-release)).

Ich persönlich empfehle die Installation durch [brew](https://brew.sh). Wenn Sie `brew` noch nicht installiert haben, können Sie es zuerst über das offizielle Ein-Klick-Skript installieren.

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Nach der Installation von `brew` können Sie mit der Installation und Grundkonfiguration durch Befehle fortfahren. Öffnen Sie das Terminal und geben Sie die folgenden Befehle ein:

```sh
brew install koekeishiya/formulae/yabai
```

Installieren Sie das Skript-Plugin:

```sh
sudo yabai --install-sa
sudo yabai --load-sa
```

Starten Sie den yabai-Dienst:

```sh
brew services start yabai
```

Hinweis: Für macOS Big Sur oder Monterey-Systeme müssen Sie, da API-Injektion benötigt wird, um Skripte aufzurufen, `root`-Berechtigungen und den Start beim Booten konfigurieren. Die offizielle Anleitung bietet detaillierte Vorgehensweisen:

Bearbeiten Sie die Datei `/private/etc/sudoers.d/yabai`:

```sh
sudo visudo -f /private/etc/sudoers.d/yabai
```

Fügen Sie den folgenden Inhalt zur geöffneten Datei hinzu:

```sh
<user> ALL = (root) NOPASSWD: <path> --load-sa
```

Der `user` und `path` innerhalb der `<>` oben können durch die Befehle `whoami` und `which yabai` erhalten werden.

![see_user_and_config_yabai_sudo](https://image.pseudoyu.com/images/see_user_and_config_yabai_sudo.png)

Nach Abschluss der obigen Konfiguration fügen Sie die folgenden zwei Zeilen zur `.yabairc`-Konfigurationsdatei von yabai hinzu:

```plaintext
sudo yabai --load-sa
yabai -m signal --add event=dock_did_restart action="sudo yabai --load-sa"
```

#### Benutzerdefinierte Konfiguration

yabai's Konfigurationsdatei wird durch die `.yabairc`-Datei im `$HOME`-Verzeichnis des Benutzers verwaltet, die über einen Editor oder ein Befehlszeilentool bearbeitet werden kann:

```sh
vi ~/.yabairc
```

Das Folgende ist meine persönliche Konfiguration, die Sie kopieren und anpassen können. Ich habe meine persönliche Konfiguration auf der GitHub-Code-Hosting-Plattform platziert, die Sie [hier](https://github.com/pseudoyu/dotfiles/blob/master/yabai/yabairc) einsehen können.

```plaintext
# !/usr/bin/env sh

sudo yabai --load-sa
yabai -m signal --add event=dock_did_restart action="sudo yabai --load-sa"

# Globale Konfiguration
yabai -m config mouse_follows_focus          off
yabai -m config focus_follows_mouse          off
yabai -m config window_origin_display        default
yabai -m config window_placement             second_child
yabai -m config window_topmost               off
yabai -m config window_shadow                on
yabai -m config window_opacity               off
yabai -m config active_window_opacity        1.0
yabai -m config normal_window_opacity        0.90
yabai -m config window_border                off
yabai -m config window_border_width          6
yabai -m config active_window_border_color   0xff775759
yabai -m config normal_window_border_color   0xff555555
yabai -m config insert_feedback_color        0xffd75f5f
yabai -m config split_ratio                  0.50
yabai -m config auto_balance                 off
yabai -m config mouse_modifier               fn
yabai -m config mouse_action1                move
yabai -m config mouse_action2                resize
yabai -m config mouse_drop_action            swap

# Space-Konfiguration
yabai -m config layout                       bsp
yabai -m config top_padding                  15
yabai -m config bottom_padding               15
yabai -m config left_padding                 15
yabai -m config right_padding                15
yabai -m config window_gap                   15

# Ignorierte Apps
yabai -m rule --add app="^System Preferences$" manage=off
yabai -m rule --add app="^Archive Utility$" manage=off
yabai -m rule --add app="^Logi Options+$" manage=off
yabai -m rule --add app="^Alfred Preferences$" manage=off
```

Meine Konfiguration ist im Grunde nur teilweise modifiziert basierend auf dem offiziell bereitgestellten Beispiel, verwendet den `bsp`-Algorithmus für intelligenten Split-Screen und passt den Abstand auf 15 an, was ein komfortablerer Abstand ist.

Ich habe auch einige benutzerdefinierte Regeln hinzugefügt, um Anwendungen zu ignorieren, die keine Fenster anpassen können, wenn Systemkonfigurationen, Entpackungstools usw. geöffnet werden.

Die Gesamtpräsentation sieht wie folgt aus (der folgende Effekt ist der Algorithmus, der automatisch anordnet, nachdem Anwendungsfenster geöffnet wurden, und neue Fenster werden automatisch neu angeordnet):

![my_layout_1](https://image.pseudoyu.com/images/my_layout_1.png)

### skhd

Nach der Konfiguration von yabai haben wir intelligenten Split-Screen erreicht, aber manchmal entsprechen die vom Algorithmus bereitgestellten Fensterpositionen nicht unseren Bedürfnissen, oder wir müssen häufig zwischen verschiedenen Fenstern wechseln/anpassen. Hier kommt das skhd-Tool ins Spiel, um einige Tastenkombinationen anzupassen.

#### Installation

skhd kann auch über das `brew`-Paketverwaltungstool installiert werden, was sehr bequem ist:

```sh
brew install koekeishiya/formulae/skhd
```

Starten Sie es nach der Installation:

```sh
brew services start skhd
```

#### Benutzerdefinierte Konfiguration

Ähnlich wie yabai wird skhd's Konfiguration durch die `$HOME/.skhdrc`-Konfigurationsdatei verwaltet, die über einen Editor oder ein Befehlszeilentool bearbeitet werden kann.

```sh
vi ~/.skhdrc
```

Das Folgende ist meine persönliche Konfiguration, die Sie kopieren und anpassen können. Ich habe meine persönliche Konfiguration auf der GitHub-Code-Hosting-Plattform platziert, die Sie [hier](https://github.com/pseudoyu/dotfiles/blob/master/skhd/skhdrc) einsehen können.

```plaintext
# Fensterfokus
alt - h : yabai -m window --focus west
alt - j : yabai -m window --focus south
alt - k : yabai -m window --focus north
alt - l : yabai -m window --focus east

# Fenster tauschen
shift + alt - h : yabai -m window --swap west
shift + alt - j : yabai -m window --swap south
shift + alt - k : yabai -m window --swap north
shift + alt - l : yabai -m window --swap east

# Fenster verschieben
shift + alt + ctrl - h : yabai -m window --warp west
shift + alt+ ctrl - j : yabai -m window --warp south
shift + alt + ctrl - k : yabai -m window --warp north
shift + alt + ctrl - l : yabai -m window --warp east

# Fensterlayout rotieren
alt - r : yabai -m space --rotate 90

# Vollbild
alt -f : yabai -m window --toggle zoom-fullscreen

# Fensterbereich ein-/ausschalten
alt - g : yabai -m space --toggle padding; yabai -m space --toggle gap

# Fenster in Bildschirmmitte schweben lassen / entfernen
alt - t : yabai -m window --toggle float;\
          yabai -m window --grid 4:4:1:1:2:2

# Fenster-Split-Methode ändern
alt - e : yabai -m window --toggle split

# Fensterlayout zurücksetzen
shift + alt - 0 : yabai -m space --balance

# Fenster auf bestimmten Desktop verschieben
shift + alt - 1 : yabai -m window --space 1; yabai -m space --focus 1
shift + alt - 2 : yabai -m window --space 2; yabai -m space --focus 2
shift + alt - 3 : yabai -m window --space 3; yabai -m space --focus 3
shift + alt - 4 : yabai -m window --space 4; yabai -m space --focus 4
shift + alt - 5 : yabai -m window --space 5; yabai -m space --focus 5
shift + alt - 6 : yabai -m window --space 6; yabai -m space --focus 6
shift + alt - 7 : yabai -m window --space 7; yabai -m space --focus 7
shift + alt - 8 : yabai -m window --space 8; yabai -m space --focus 8
shift + alt - 9 : yabai -m window --space 9; yabai -m space --focus 9

# Fenstergröße vergrößern
shift + alt - w : yabai -m window --resize top:0:-20
shift + alt - d : yabai -m window --resize left:-20:0

# Fenstergröße verkleinern
shift + alt - s : yabai -m window --resize bottom:0:-20
shift + alt - a : yabai -m window --resize top:0:20
```

Vereinfacht gesagt, habe ich eine Einrichtung ähnlich der vim-Tastenkombinationslogik konfiguriert und folgende gängige Funktionen implementiert:

- `<Option> + hjkl` zum Fokussieren zwischen verschiedenen Fenstern
- `<Option> + <Shift> + hjkl` zum Tauschen verschiedener Fenster
- `<Option> + <Shift> + 0` zum Zurücksetzen des Fensterlayouts
- `<Option> + <Shift> + <1~9>` zum schnellen Verschieben des aktuellen Fensters auf einen bestimmten Desktop
- `<Option> + f` für Vollbild
- `<Option> + t` zum Schweben lassen des Fensters in der Bildschirmmitte / Entfernen des Schwebens
- `<Option> + g` zum Ein-/Ausschalten des Fensterbereichs
- `<Option> + r` zum Rotieren des Fensterlayouts
- `<Option> + e` zum Ändern der Fenster-Split-Methode

Unter diesen sind `hjkl` häufig verwendete Operationen im vim-Editor. Sie können sie auch in Hoch, Runter, Links, Rechts oder andere Tasten Ihrer Wahl ändern.

Nach Abschluss der obigen Konfiguration haben wir die intelligente Fensterverwaltung von yabai und Fensteroperationen durch einfache Tastenkombinationen erreicht. Als Nächstes nehmen wir einige Konfigurationen am macOS-System vor, um unser Fensterverwaltungssystem zu optimieren.

### macOS Desktop-Verwaltung

macOS bietet leistungsstarke Multi-Desktop-Verwaltungsfunktionen. Jeder Desktop-Bereich kann als Arbeitsbereich verstanden werden, in dem verschiedene Fenster unabhängig platziert werden können, wie im folgenden Bild gezeigt:

![macos_desktop_management](https://image.pseudoyu.com/images/macos_desktop_management.png)

Wir können Desktops verwenden, um unsere Arbeitsbereiche zu unterscheiden, z.B. Desktop 1 für Entwicklungs-IDEs und Terminals, Desktop 2 für Browser-Abfragen und Dokumentenerstellung, Desktop 3 für die Bearbeitung von WeChat, E-Mail und anderen Kommunikationstools und Desktop 4 für Freizeit und Unterhaltung, Videowiedergabe usw. Auf diese Weise müssen wir nur zwischen einigen wenigen Desktops wechseln, um unsere Workflow-Logik zu implementieren, ohne uns um Fokusprobleme kümmern zu müssen.

Um weiter zu optimieren und schneller zwischen Desktops zu wechseln, können wir Launcher wie [Alfred](https://www.alfredapp.com) oder [Raycast](https://www.raycast.com) verwenden, um Anwendungen schnell zu starten/zu fokussieren, oder Tastenkombinationen von Fensterwechsel-Software wie [AltTab](https://alt-tab-macos.netlify.app) oder [Manico](https://manico.im) nutzen, um schnell zwischen geöffneten Anwendungen zu wechseln.

Darüber hinaus bieten die macOS-Systemeinstellungen auch anpassbare Umschalttastenkombinationen. Ich habe `<Option> + <1~9>` für bestimmte Desktops geändert, sodass ich, wenn ich arbeite, schnell zum entsprechenden Arbeitsbereich gelangen kann, indem ich die entsprechende Tastenkombination drücke, was schnell zur Muskelgedächtnis wird.

Öffnen Sie **Systemeinstellungen - Tastatur - Kurzbefehle - Mission Control**, wo wir entsprechende Tastenkombinationen für verschiedene Desktops einstellen können. Wenn sie nicht angezeigt werden, können Sie zuerst 9 leere Desktops öffnen, um sie zu konfigurieren, und die Konfiguration wird auch nach dem Schließen der Desktops beibehalten.

![keyboardshortcut_to_change_desktop](https://image.pseudoyu.com/images/keyboardshortcut_to_change_desktop.png)

Zusätzlich gibt es eine weitere kleine Einstellung, die ich mag. Öffnen Sie **Systemeinstellungen - Bedienungshilfen - Anzeige - Anzeige - Bewegung reduzieren**. Dies reduziert den Animationseffekt beim Wechsel zwischen verschiedenen Desktops und erhöht die Umschaltgeschwindigkeit. In Kombination mit unserem automatischen Split-Screen und Tastenkombinationen erreicht dies einen schnellen und leistungsstarken Multi-Workspace-Wechsel. Ich priorisiere Geschwindigkeit und Effizienz, aber wenn Sie macOS-Animationen mögen, können Sie diesen Schritt überspringen.

![reduce_display_effect](https://image.pseudoyu.com/images/reduce_display_effect.png)

## Fazit

Das oben Genannte ist meine aktuelle macOS-Fensterverwaltungslösung. Ich bin jemand, der es liebt, an Software und verschiedenen Konfigurationen zu basteln, oft mehrere Tage damit verbringt, eine kleine Anforderung zu beheben, und immer nach meinen Best Practices strebt.

Vielleicht werden mir viele Konfigurationen in meiner anschließenden Arbeit nicht viel Zeit sparen, wobei sich die Fensterorganisation und der Wechsel nur um wenige Sekunden unterscheiden. Aber wenn ich das System, das ich einmal mit viel Überlegung erforscht und optimiert habe, in meiner täglichen Arbeit und meinem Studium nutze, oder wenn ein plötzlicher Bedarf eine Software/Konfiguration verwendet, an der ich zuvor gebastelt habe, fühle ich mich unerklärlich glücklich und erfüllt. Das ist wahrscheinlich der Sinn des Bastelns, und ich hoffe, dass jeder solches Glück genießen kann.

Ich pflege ein Toolbox-Projekt auf GitHub 『[GitHub - pseudoyu/yu-tools](https://github.com/pseudoyu/yu-tools)』, das viele andere Software- und Hardware-Entscheidungen aufzeichnet und ständig aktualisiert und optimiert wird. Wenn Sie interessiert sind, können Sie gerne kommunizieren, und ich werde nach und nach entsprechende Konfigurations-/Nutzungstutorials erstellen.

> Hinweis: Dieser Artikel wurde von mir zuerst auf 『[少数派](https://sspai.com)』 mit Genehmigung veröffentlicht. Die Adresse des Originalartikels lautet: 『[让窗口管理也能自动化，基于 yabai+skhd 的 macOS 窗口管理系统](https://sspai.com/post/73620)』.

## Referenzen

> 1. [Blazing Fast Window Management on macOS](https://www.youtube.com/watch?v=fYsCAOfGjxE)
> 2. [yabai Projektadresse](https://github.com/koekeishiya/yabai)
> 3. [skhd Projektadresse](https://github.com/koekeishiya/skhd)
> 4. [pseudoyu/yu-tools Persönliche Toolbox-Projektadresse](https://github.com/pseudoyu/yu-tools)