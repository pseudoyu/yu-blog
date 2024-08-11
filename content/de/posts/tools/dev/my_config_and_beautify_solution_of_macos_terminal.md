---
title: "Warp, iTerm2 oder Alacritty? Meine Terminal-Tüftler-Reise"
date: 2022-07-10T11:18:29+08:00
draft: false
tags: ["dev-environment", "terminal", "macos", "iterm2", "tmux", "alacritty", "zsh", "starship", "warp", "neovim", "tools"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《Here After Us - Mayday》" >}}

## Vorwort

Als Entwickler können wir nicht ohne das Terminal auskommen, das in dem Bild unten zu sehen ist - jenes schwarze Fenster, das oft in Science-Fiction-Filmen auftaucht. Sei es, um Code lokal auszuführen und zu debuggen oder um Projekte auf entfernten Servern zu deployen und zu warten.

![my_terminal_tools](https://image.pseudoyu.com/images/my_terminal_tools.png)

Betriebssysteme haben im Allgemeinen ihre Standard-Shells, wie "Powershell" unter Windows und bash oder zsh auf macOS- und Linux-Systemen. Systeme mit grafischen Benutzeroberflächen kommen auch mit vorinstallierten Terminal-Emulatoren, wie "Terminal.app" auf macOS und verschiedenen Terminal-Programmen, die mit Linux-Distributionen gebündelt sind.

Als Produktivitäts-Tool-Enthusiast und Ästhet hat meine Bastelei an der Terminal-Konfiguration und -Anpassung nie aufgehört und durchlief mehrere Iterationen. Vielleicht bin ich anders als die meisten Entwickler, da ich kein Anhänger einer bestimmten Lösung bin. Stattdessen probiere ich verschiedene Tools aus und konfiguriere sie nach meinen Gewohnheiten, um die operativen Unterschiede zwischen verschiedenen Lösungen zu reduzieren. In der täglichen Entwicklung wechsle ich nahtlos zwischen ihnen basierend auf dem Zweck, manchmal wähle ich sogar zufällig eines aus, um als Stimmungswechsler zu dienen.

Dieser Artikel beschreibt hauptsächlich meine Terminal-Lösungsauswahl und Konfigurationsdetails.

## Anforderungen an die Terminal-Konfiguration

Die Terminal-Konfiguration besteht aus mehreren Aspekten:

1. **Tool-Konfiguration**. Bei der Entwicklung auf macOS- oder Windows-Systemen benötigen wir oft einen Terminal-Emulator, um uns mit der lokalen Entwicklungsumgebung oder entfernten Servern zu verbinden. Dies ist in der Regel eine dauerhafte Anwendung in unserem Entwicklungsprozess, und ihre Ästhetik, Reaktionsgeschwindigkeit und Shortcuts beeinflussen unsere Entwicklungserfahrung stark, was sie zum Schwerpunkt unserer Konfiguration und Anpassung macht.

2. **Funktionale Konfiguration**. Bei der Verwendung der Kommandozeile zur Durchführung von Operationen an Systemdiensten/Dateien müssen wir Shells wie bash oder zsh verwenden. Die Konfiguration von Befehlsaufforderungen, Auto-Vervollständigung und anderen Funktionen kann unsere Benutzererfahrung effektiv verbessern.

3. **Integrationskonfiguration**. Neben der Ausführung gängiger Kommandozeilen-Tools wie git müssen Terminals oft fortgeschrittene Bedürfnisse wie Textbearbeitung und Multi-Task-Management erfüllen. Daher ist die tiefe Integration von Tools wie vim und tmux durch Terminal-Konfiguration ebenfalls ein wichtiger Aspekt zur Optimierung unserer Entwicklungserfahrung.

Ich habe meine Terminal-Nutzungsanforderungen umrissen und die folgenden Kernpunkte aufgelistet:

1. **Minimalistischer Stil**. Als Software, der ich täglich über lange Zeiträume gegenüberstehe, können selbst die ausgefallensten Themen ermüdend werden und sogar meine Konzentration beeinträchtigen. Daher ist mein grundlegender Ansatz zur Konfiguration des Erscheinungsbildes und der Betriebslogik von Terminal-Tools Minimal Distraction - einfach, aber nicht monoton.

2. **Schnelle Reaktion**. Anfangs konzentrierte ich mich bei der Terminal-Konfiguration auf Ästhetik und Funktionalität und installierte viele Plugins und Konfigurationen, was jedoch auch zu der unangenehmen Erfahrung von mehreren Sekunden Verzögerung bei jedem Softwarestart führte. Daher ist die Reaktionsgeschwindigkeit während der Nutzung ebenfalls ein Schwerpunkt meiner Lösungsauswahl und -optimierung.

3. **Anpassbarkeit**. Da ich das spezielle Vim "HJKL"-Tastaturlayout für meinen Code-Editor und die Fensterverwaltung verwende, hoffe ich auch, flexible Shortcuts konfigurieren zu können, um die Kosten für den Wechsel zwischen verschiedenen Softwares zu reduzieren.

4. **Portabilität**. Ich muss oft auf verschiedenen Geräten arbeiten, und gelegentlich gibt es Gerätewechsel. Ich hoffe, dass meine Konfigurationen bequem auf neue Geräte/Server portiert werden können, vorzugsweise unter Wiederverwendung derselben Konfigurationsdatei.

5. **Erweiterbarkeit**. Ich hoffe, einige Funktionen und Plugins nach meinen Bedürfnissen erweitern zu können, wie zum Beispiel die Verwendung von fzf zur Suche nach Dateien oder Befehlsverläufen, das Springen zu bestimmten Verzeichnissen über Befehle, die Verwendung von waka-time zur Aufzeichnung meiner Programmierzeit usw.

## Erklärung meiner Terminal-Konfiguration

Selbst mit relativ klaren Anforderungen ist es immer noch eine herausfordernde, aber angenehme Aufgabe, geeignete Tools und Konfigurationslösungen zu finden. Als Nächstes werde ich die Lösungen beschreiben, die ich immer noch verwende und mit denen ich recht zufrieden bin, und meine Konfigurationsdateien als Referenz bereitstellen.

Da ich die meiste Zeit auf macOS entwickle, basieren meine Terminal-Tool-Konfigurationen hauptsächlich auf der macOS-Plattform. Einige Tools oder Plugins (wie Alacritty, ohmyzsh, Neovim usw.) sind jedoch plattformübergreifend, mit ähnlichen Konfigurationsmethoden, die je nach tatsächlicher Situation referenziert und konfiguriert werden können.

### Warp

![warp_interface](https://image.pseudoyu.com/images/warp_interface.png)

Ich habe von Natur aus eine Neigung zum Basteln und hoffe, genügend Anpassungsraum für verschiedene Konfigurationen zu haben. Wenn ich jedoch nur ein Tool für Neueinsteiger empfehlen müsste, die gerade erst mit der Nutzung von Terminals beginnen, würde ich ohne zu zögern "[Warp](https://www.warp.dev)" wählen.

Warp ist ein modernes Terminal-Tool, das auf Rust basiert und extrem schnell, leistungsfähig und sofort einsatzbereit ist. Es unterstützt intelligente Eingabeaufforderungen, KI-Befehlssuche, Abfrage des Befehlsverlaufs, benutzerdefinierte Workflows und andere Funktionen ohne zusätzliche Konfiguration.

Ich gehörte zu den ersten Nutzern, die an Warps internem Test teilnahmen. Selbst in den frühen Stadien, als die Funktionen noch unvollständig waren, war ich von seinem exquisiten Erscheinungsbild und der reibungslosen Benutzererfahrung beeindruckt. Da es in der Rust-Sprache entwickelt wurde, sind Warps Befehlsausführung und Reaktionsgeschwindigkeit sehr schnell. Darüber hinaus hat es viele gängige Funktionen eingebaut, sodass wir leistungsstarke funktionale Unterstützung erhalten, ohne Plugins wie Verlaufssuche und Befehlsaufforderungen auf der Shell-Ebene konfigurieren zu müssen.

![warp_code_block](https://image.pseudoyu.com/images/warp_code_block.png)

Es hat auch viele einzigartige Funktionen, die herkömmliche Terminals nicht besitzen, wie das Konzept der "Blöcke". Jede Befehlsausführung wird in Form eines "Befehlsblocks" präsentiert, was die Bewegung zwischen Blöcken mit den Pfeiltasten ermöglicht und das ständige Ziehen der Scrollleiste zum Lesen vermeidet, wenn einige Befehlsausgaben zu lang sind. Wir können auch bestimmte Blöcke über die obere rechte Ecke mit Lesezeichen versehen, Befehle kopieren, Inhalte suchen oder sogar online teilen.

![edit_command_in_warp](https://image.pseudoyu.com/images/edit_command_in_warp.png)

Anders als bei herkömmlichen Terminal-Tools ist Warps Befehlseingabefenster dauerhaft am unteren Rand fixiert (ähnlich einer IDE) und trennt visuell unsere Befehlseingabe von der Ergebnisrückmeldung. Darüber hinaus ähnelt sein Eingabemodus eher einem Texteditor - wir können den Cursor frei mit der Maus oder Tastatur bewegen, um Befehle zu bearbeiten, zu modifizieren oder mehrzeilige Befehle zur sequentiellen Ausführung einzugeben. Das betrachte ich als Warps Killer-Feature.

![warp_other_feature](https://image.pseudoyu.com/images/warp_other_feature.png)

Wir müssen nur die entsprechenden Shortcuts im Eingabefeld verwenden, um Funktionen wie Verlaufssuche und benutzerdefinierte Workflows aufzurufen, und können mit dem Mausrad oder den Richtungstasten zur Auswahl navigieren, was sehr flexibel ist. Noch leistungsfähiger ist, dass diese Shortcuts auch wirksam sind, wenn wir Warp verwenden, um über SSH eine Verbindung zu einem entfernten Terminal herzustellen, wie zum Beispiel die Verlaufssuche, ohne dass eine Konfiguration auf dem Zielserver erforderlich ist.

Erwähnenswert ist auch, dass wir die eingebauten Shortcuts `Command+D` und `Command+Shift+D` verwenden können, um das Terminal horizontal oder vertikal zu teilen, ohne dass andere Tools integriert oder zusätzliche Konfigurationen vorgenommen werden müssen.

Mit der Entwicklung der Technologie wurden Texteditoren kontinuierlich aktualisiert, um reichhaltige Funktionen hinzuzufügen und bessere Benutzererfahrungen zu bieten. Das Terminal jedoch, mit dem wir Entwickler Tag und Nacht arbeiten, hat sich nur langsam weiterentwickelt. Warp wurde in diesem Kontext geboren, ganz wie es seine offizielle Website beschreibt:

> The terminal for the 21st century.

### iTerm2

Bevor ich Warp benutzte, war mein Haupt-Terminal-Tool [iTerm2](https://iterm2.com), das meiner Meinung nach auch eine Muss-Installation für viele Entwickler ist, wenn sie zum ersten Mal einen Mac bekommen (immerhin sind Ästhetik und Spielbarkeit des Standard-Terminals nicht großartig). iTerm2 ist ein langjähriges Terminal-Tool, das Ästhetik und Funktionalität kombiniert, und selbst seine Standardkonfiguration erfüllt unsere Bedürfnisse bereits sehr gut.

#### Erscheinungsbild und Farbschema

![iterm2_interface](https://image.pseudoyu.com/images/iterm2_interface.png)

Ich habe die Konfiguration eines YouTubers namens "[Takuya Matsuyama](https://www.craftz.dog)" modifiziert, um ein minimalistisches Erscheinungsbild-Schema anzupassen.

Zuerst konfigurieren wir das Thema, die Registerkartenleiste und die Statusleiste im Bereich **Preferences** - **Appearance** wie folgt, um ein relativ einfaches Layout beizubehalten.

![iterm2_theme_config](https://image.pseudoyu.com/images/iterm2_theme_config.png)

Nach Abschluss der Themenkonfiguration klicken wir mit der rechten Maustaste auf die untere Statusleiste für die detaillierte Konfiguration. Ich habe einige Statusleisten-Komponenten ausgewählt, um den Gerätestatus in Echtzeit anzuzeigen. Dieser Teil kann nach Ihren Vorlieben gewählt werden.

![iterm2_status_components](https://image.pseudoyu.com/images/iterm2_status_components.png)

Wählen Sie Ihr Themen-Farbschema oder importieren Sie andere Farbschemata im Panel **Profile** - **Colors**. Sie können [hier](https://github.com/pseudoyu/dotfiles/tree/master/iterm2) klicken, um meine Konfigurationsdatei herunterzuladen, sie importieren und nach Ihren Bedürfnissen anpassen.

![iterm2_window_blur_setting](https://image.pseudoyu.com/images/iterm2_window_blur_setting.png)

Nach der Auswahl des Farbschemas habe ich einen transparenten Hintergrund und einen Milchglaseffekt (Fensterunschärfe) erreicht, indem ich Transparency und Blur angepasst habe. Dies kann entsprechend dem visuellen Effekt des spezifischen Geräts angepasst werden.

Nach der Konfiguration des Terminal-Tools müssen wir immer noch die Shell konfigurieren, um einige benutzerdefinierte Themen, intelligente Eingabeaufforderungen, Suchverlaufsaufzeichnungen und andere Erweiterungsmodule zu integrieren. Ich verwende die zsh + ohmyzsh + starship Lösung. Da diese Konfigurationen für verschiedene Lösungen üblich sind, finden Sie Details im Abschnitt zur Alacritty-Konfigurationsbeschreibung unten.

#### Multi-Server-Management

![iterm2_profile_settings](https://image.pseudoyu.com/images/iterm2_profile_settings.png)

Derzeit verwende ich iTerm2 hauptsächlich, um mich mit meinen verschiedenen Remote-Hosts/Servern zu verbinden. Es bietet eine bequeme Multi-Konfigurations-Management-Funktionalität, die einen schnellen Wechsel zwischen verschiedenen Servern oder Konfigurationsumgebungen durch das Einstellen verschiedener Profile ermöglicht und auffällige Badges als Identifikatoren verwenden kann.

![iterm2_multiple_servers_management](https://image.pseudoyu.com/images/iterm2_multiple_servers_management.png)

Wenn wir uns für die Arbeit oder den persönlichen Gebrauch mit mehreren Entwicklungsmaschinen verbinden müssen, können wir den Server öffnen, indem wir `Command+O` drücken oder mit der rechten Maustaste auf das iTerm2-Symbol in der Dock-Leiste klicken, um das entsprechende Profil auszuwählen. Wir können auch die eingebauten Shortcuts `Command+D` und `Command+Shift+D` verwenden, um das Terminal horizontal oder vertikal zu teilen, was die gleichzeitige Bedienung mehrerer Server erleichtert, ohne ständig Fenster wechseln zu müssen.

### Alacritty

iTerm2 ist bereits ein Terminal-Tool mit einer sehr ausgewogenen Ästhetik und Funktionalität auf der macOS-Plattform, aber seine Gesamtreaktionsgeschwindigkeit und Konfigurationsfreiheit sind nicht ganz perfekt. Daher verwende ich es jetzt hauptsächlich, um mich mit entfernten Servern zu verbinden, und bin für mein häufig genutztes lokales Terminal zu [Alacritty](https://alacritty.org) gewechselt.

Alacritty ist ebenfalls ein plattformübergreifendes Terminal-Tool, das in Rust geschrieben wurde und einige grundlegende Standardkonfigurationen bereitstellt sowie verschiedene Einstellungen über die Datei `~/.config/alacritty/alacritty.yml` anpasst. Sie können [hier](https://github.com/pseudoyu/dotfiles/tree/master/alacritty) auf meine vollständige Konfiguration zugreifen.

#### Erscheinungsbild-Konfiguration

![alacritty_interface](https://image.pseudoyu.com/images/alacritty_interface.png)

Für den Erscheinungsbild-Teil verwende ich hauptsächlich die folgende Konfiguration für Fenster- und Schriftarteinstellungen, um eine halbtransparente minimalistische Konfiguration ohne Rahmen oder Schaltflächen zu erreichen. Andere Konfigurationen können Sie selbst einsehen, wie zum Beispiel select-to-copy und andere häufig verwendete Funktionen in iTerm2, die durch einige einfache Konfigurationseinträge implementiert werden können.

```yaml
window:
  opacity: 0.85
  padding:
    x: 18
    y: 16
  dynamic_padding: false
  decorations: buttonless

font:
  normal:
    family: "MesloLGSDZ Nerd Font Mono"
    style: Regular
  size: 13.0
  use_thin_strokes: true
```

#### ohmyzsh + starship

![alacritty_starship_config](https://image.pseudoyu.com/images/alacritty_starship_config.png)

Ich verwende zsh als Standard-Terminal und nutze ohmyzsh, um die Plugin-Funktionalität zu erweitern. zsh + ohmyzsh ist derzeit eine sehr beliebte Shell-Konfigurationslösung mit einem reichen Plugin-System, das verschiedene erweiterte Funktionen durch ein paar Zeilen Konfiguration einfach implementieren kann. Zunächst installieren wir gemäß den [offiziellen Anweisungen](https://ohmyz.sh/#install).

```bash
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

Nach der Installation aktivieren wir ohmyzsh, indem wir die folgende Konfiguration zu `~/.zshrc` hinzufügen:

```plaintext
export ZSH="$HOME/.oh-my-zsh"
source $ZSH/oh-my-zsh.sh
```

Ich habe starship konfiguriert, um die Shell-Eingabeaufforderung zu verschönern. Ähnlich installieren und konfigurieren wir gemäß den [offiziellen Anweisungen](https://starship.rs/guide/#🚀-installation):

```bash
curl -sS https://starship.rs/install.sh | sh
```

Nach Abschluss fügen wir die folgende Konfiguration zu `~/.zshrc` hinzu:

```plaintext
eval "$(starship init zsh)"
```

Darüber hinaus können wir Plugin-Konfigurationen im Plugin-Abschnitt von `~/.zshrc` hinzufügen. Zum Beispiel habe ich die folgenden Plugins konfiguriert, um intelligente Eingabeaufforderungen, Syntaxhervorhebung, `Ctrl + R` zur Suche im Befehlsverlauf und `j + <Pfad>` für schnelle Sprünge zu unterstützen.

```plaintext
plugins=(
  git
  zsh-autosuggestions
  zsh-syntax-highlighting
  zsh-history-substring-search
  autojump
  zsh-wakatime
  fzf-zsh-plugin
)
```

Klicken Sie [hier](https://github.com/pseudoyu/dotfiles/tree/master/zsh), um meine vollständige Konfiguration anzusehen. Installationsanweisungen für jedes Plugin finden Sie in der offiziellen Dokumentation.

#### tmux

![acacritty_tmux_demo](https://image.pseudoyu.com/images/acacritty_tmux_demo.png)

Da Alacritty selbst keine Funktionen wie Fensterteilung und Sitzungsverwaltung bietet, müssen wir [tmux](https://github.com/tmux/tmux/wiki) integrieren, ein leistungsstarkes plattformübergreifendes Fensterverwaltungstool.

Benutzer der macOS-Plattform können es über `brew install tmux` installieren, während andere Plattformen es gemäß den [offiziellen Anweisungen](https://github.com/tmux/tmux/wiki/Installing) installieren können.

Es wird über `~/.tmux.conf` konfiguriert. Klicken Sie [hier](https://github.com/pseudoyu/dotfiles/tree/master/tmux), um meine Konfiguration anzusehen. Da seine Konfiguration und Verwendung einige Lern- und Gedächtniskosten erfordern, wird dieser Artikel es nicht im Detail beschreiben. Es wird empfohlen, es durch die offizielle Dokumentation oder andere vollständige Tutorials zu erlernen.

#### Neovim

Für unsere tägliche Entwicklung schreiben wir in der Regel Code in VS Code oder Jetbrains' IDEs, während das Debugging die Verwendung eines Terminals erfordert. Wenn Sie nicht häufig zwischen verschiedenen Softwares wechseln möchten, können wir vim wählen, ein Bearbeitungstool, das in der Kommandozeile verwendet werden kann.

Das native vim ist jedoch nur ein einfaches Fenster, das mit unserem gut konfigurierten Terminal fehl am Platz erscheint. Daher werden wir auch vim verschönern und konfigurieren. Aufgrund von Platzbeschränkungen wird dieser Artikel keine spezifischen Konfigurations- und Nutzungsinhalte in Bezug auf vim abdecken, sondern nur meine Konfigurationslösung beschreiben.

![vi_homepage](https://image.pseudoyu.com/images/vi_homepage.png)

Ich verwende neovim, eine Abwandlung von vim, deren hohe Version lua für die Konfiguration und Plugin-Verwaltung verwendet. Ich verwende ein Schema, das von meinem Freund [Cluas](https://github.com/Cluas) angepasst wurde, und habe darauf basierend einige Änderungen und Anpassungen vorgenommen. Sie können [hier](https://github.com/pseudoyu/nvim/tree/pseudoyu) darauf zugreifen. Sie müssen nur das `nvim/`-Verzeichnis klonen oder herunterladen und es nach `~/.config` kopieren.

Sein Anzeigeeffekt ist wie folgt:

![neovim_file_preview](https://image.pseudoyu.com/images/neovim_file_preview.png)

![neovim_edit_file](https://image.pseudoyu.com/images/neovim_edit_file.png)

#### Shortcut-Konfiguration

tmux ist ein leistungsstarkes Fensterverwaltungstool, aber es ist sehr umständlich, jedes Mal `<Ctrl+b> + %` oder `<Ctrl+b> + :` für horizontale oder vertikale Bildschirmteilung oder `<Ctrl+b> + c` zur Erstellung eines neuen Fensters zu verwenden.

Gibt es also eine Möglichkeit, Bildschirmteilung oder das Erstellen neuer Fenster durch macOS' eingebaute Shortcuts wie `Command+D`, `Command+Shift+D` oder `Command+T`, die von anderen Terminal-Editoren verwendet werden, zu erreichen?

Nach einiger Recherche und Bastelei habe ich diese Anforderung perfekt umgesetzt, indem ich mich auf [Josh Medeskis](https://www.joshmedeski.com) Artikel "[macOS Keyboard Shortcuts for tmux](https://www.joshmedeski.com/posts/macos-keyboard-shortcuts-for-tmux)" bezog.

Die grundlegende Implementierungsmethode besteht darin, den Befehl `xxd -psd` im Terminal einzugeben, dann den tmux-Shortcut einzugeben, den Sie zuordnen möchten, wie zum Beispiel `<Ctrl+b> + c`. Es wird die Hexcodes für diese Eingabe anzeigen als:

```bash
^Bc
02630a
```

Hier repräsentiert `02` `<Ctrl+b>`, `63` repräsentiert `c`, und `0a` repräsentiert die Eingabetaste. Daher ist der Hexcode, der dem Shortcut für die Erstellung eines neuen Fensters in tmux entspricht, `\x02\x63`. Wir können die folgende Option im Abschnitt key_bindings von `~/.config/alacritty/alacritty.yml` konfigurieren:

```yaml
key_bindings:
  - { key: T, mods: Command, chars: "\x02\x63" }
```

Das Implementierungsprinzip für andere Shortcut-Konfigurationen ist dasselbe. Sie können [hier](https://github.com/pseudoyu/dotfiles/tree/master/alacritty) auf alle meine Shortcut-Konfigurationen zugreifen und sie bei Bedarf modifizieren.

## Fazit

Bis zu diesem Punkt habe ich die drei Terminal-Tools, die ich derzeit verwende, vorgestellt und erklärt. Das sofort einsatzbereite Warp hat seine Stärken, iTerm2 erreicht ein schönes Gleichgewicht zwischen Benutzerfreundlichkeit und Anpassbarkeit, und Alacritty hat seine eigene Freude am Basteln.

Wie ich bereits erwähnt habe, ist der Wechsel zu einem anderen Terminal manchmal eine völlig neue Stimmung, und die ständige Optimierung und das Basteln in der Freizeit ist auch eine Form der Entspannung. Natürlich hat jedes Terminal-Setup seine eigenen Präferenzen und Eigenschaften. Dieser Artikel stellte nur meine Lösung vor, die größtenteils meinem ästhetischen Streben und funktionalen Bedürfnissen entspricht. Ich hoffe, er kann als Referenz für Ihre Terminal-Konfiguration dienen. Wenn Sie bei der Konfiguration auf Probleme stoßen oder bessere Optimierungsvorschläge haben, zögern Sie nicht, sich auszutauschen.

## Referenzen

> 1. [GitHub - pseudoyu/dotfiles](https://github.com/pseudoyu/dotfiles)
> 2. [GitHub - Cluas/nvim](https://github.com/Cluas/nvim)
> 3. [Warp Offizielle Website](https://www.warp.dev)
> 4. [iTerm2 Offizielle Website](https://www.iterm2.com)
> 5. [Alacritty Offizielle Website](https://alacritty.org)
> 6. [ohmyzsh Offizielle Website](https://ohmyz.sh)
> 7. [starship Offizielle Website](https://starship.rs)
> 8. [Neovim Offizielle Website](https://neovim.io)
> 9. [GitHub - tmux/tmux](https://github.com/tmux/tmux)
> 10. [macOS Keyboard Shortcuts for tmux](https://www.joshmedeski.com/posts/macos-keyboard-shortcuts-for-tmux)