---
title: "Wochenrückblick #26 - Blog, Custom Keyboard und neuer Server"
date: 2023-01-15T19:57:33+08:00
draft: false
tags: ["review", "life", "home", "cat", "hugo", "pagefind", "open-source"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="'Here After Us - Mayday'" >}}

## Vorwort

Dies ist eine Aufzeichnung und Reflexion meines Lebens vom 10. Januar 2023 bis zum 15. Januar 2023.

Die Ferienzeit naht, obwohl ich nicht viel Sinn für Rituale zum Neujahr habe. Letztes Jahr verbrachte ich über eine Woche damit, "Pokémon-Legenden: Arceus" durchzuspielen und "Fire Emblem: Three Houses" erneut zu besuchen. Am Neujahrstag bereitete ich Feuertopf zu und hatte einen Videoanruf mit meiner Familie, und so verging das Jahr. Da ich jedoch beschlossen habe, dieses Jahr nach Hause zu fahren, mit Vorkehrungen für die Betreuung von Nini und verschiedenen Plänen für das neue Jahr, konnte ich mich nicht wirklich entspannen. Ich versuche, viele Dinge im Voraus zu erledigen, um etwas Zeit freizumachen, die ich mit meiner Familie verbringen kann.

Arbeitsmäßig hatte ich eine durchschnittliche Woche. Die kürzlich gestarteten Anforderungen hatten einige kleinere Probleme in den Details, was meinen Vorgesetzten und mich zwang, Überstunden zu machen, um sie zu beheben. Es gibt auch eine neue Funktion, die vor dem Neujahr eingeführt werden muss, aber die Tests sind noch nicht abgeschlossen, und es bleiben nur noch zwei oder drei Tage. Das Projekt, an dem ich mit Freunden arbeite, ist ebenfalls auf einige Probleme gestoßen. Der Freund, der ursprünglich für das Frontend verantwortlich war, musste ausscheiden, so dass ich seinen Teil übernehmen musste. Der Start wird sich verzögern, und ich werde mich während des Neujahrs nicht wirklich entspannen können. Es ist eine ziemliche Umstellung.

Da Nini im Haus eines Kollegen betreut wird, brachte ich sie heute zur Sicherheit zum Tierarzt für eine Untersuchung und ließ auch ihre Krallen schneiden. Der Arzt sagte, sie sei sehr gesund, und die früheren leichten Beschwerden seien im Grunde genommen abgeklungen. Er lobte mich auch dafür, dass ich mich gut um sie kümmere, was mich glücklich machte. Wenn ich jedoch an die Betreuung denke, macht mich das immer noch widerwillig und besorgt. Ich werde nach dem Neujahr früh zurückkommen, schließlich habe ich jetzt etwas, um das ich mich sorgen muss.

Ich habe ein recht interessantes Interview angenommen, eine unglaublich süße Tastatur erhalten, meinen Blog weiter ein wenig optimiert (~~nur das Theme optimiert, anstatt Artikel zu schreiben~~), und viele andere interessante Dinge sind passiert.

## Interessante Dinge und Objekte

### Blog-Bastelei

Die aktuelle Version meines persönlichen Blogs läuft nun schon seit fast drei Jahren. Früher hatte ich Lösungen wie die Einrichtung von WordPress auf meinem eigenen Server verwendet, aber später, aufgrund mangelnder Stabilität und Schwierigkeiten bei der Datenmigration, wechselte ich zur einmaligen Lösung des Hugo-statischen Blogs + GitHub-automatische Bereitstellung + Cloudflare-Hosting. Für Details können Sie "[Warum ich 2022 immer noch blogge](https://www.pseudoyu.com/de/2022/06/12/why_i_still_write_blog_in_2022/)" und "[Stellen Sie Ihren Blog mit Hugo und GitHub Action bereit](https://www.pseudoyu.com/de/2022/05/29/deploy_your_blog_using_hugo_and_github_action/)" lesen.

Der Grund, warum ich mich für Hugo entschieden habe, abgesehen von dem etwas unerklärlichen, aber nicht besonders nützlichen Gefühl der Vertrautheit, da meine Hauptaufgabe die Go-Entwicklung ist, liegt vor allem an dem Theme, das ich derzeit verwende, "[den](https://github.com/shaform/hugo-theme-den)". Dies ist ein Theme, das von einem taiwanesischen Entwickler selbst geschrieben wurde. Damals überlegte er, aufgrund von Faktoren wie der Baugeschwindigkeit von [Pelican](https://github.com/getpelican/pelican) zu [Hugo](https://gohugo.io/) zu wechseln, aber er mochte sein ursprüngliches Theme, also hat er es selbst nachgebaut. Sie können mehr darüber in seinem Beitrag "[Migration von Pelican und WordPress zu Hugo](https://city.shaform.com/zh/2018/07/22/migrate-from-pelican-and-wordpress-to-hugo/)" lesen.

Ich begann seinem Blog um 2018 herum für technische und persönliche Gedankenoutputs zu folgen, und ich kann sagen, dass mein späterer Artikelstil und meine Denkmuster in großem Maße von ihm beeinflusst wurden. Dieses Theme, das ein wenig vom Stil des alten Internets trägt, passte perfekt zu meiner Ästhetik, also richtete ich es nach einigem Basteln ein und benutze es bis heute.

Da es hauptsächlich für den persönlichen Gebrauch gedacht ist, fehlen trotz der sehr ästhetischen und minimalistischen Gestaltung dieses Themes immer noch einige Funktionen. So habe ich es in den drei Jahren der Nutzung ständig nach meinen eigenen Bedürfnissen geflickt und modifiziert. Letztes Jahr habe ich auch PRs für meine Modifikationen an RSS-Feeds, verwandten Artikeln und Freundeslinks eingereicht. Einige davon wurden nach einiger Kommunikation in den Hauptzweig aufgenommen, während einige noch ausstehen (~~zu faul~~).

Kürzlich entdeckte ich die [Pagefind](https://pagefind.app/) Web-Suchlösung auf [P.J. Wus](https://twitter.com/WuPingJu) Blog. Nach einiger Recherche habe ich sie in meinen Blog integriert, und der Effekt ist recht gut.

![pagefind_and_hugo_2](https://image.pseudoyu.com/images/pagefind_and_hugo_2.png)

Sie verwendet den Ansatz der Vorgenerierung von Artikelindexdateien anstelle der Echtzeitabfrage, was sie sehr schnell macht und keine zusätzlichen Backend-Dienste erfordert, was sie sehr gut für statische Blog-Bereitstellungslösungen geeignet macht. Für eine Einführung in Pagefind und seine Verwendung können Sie [P.J. Wus](https://twitter.com/WuPingJu) Artikel "[Wie man eine Suchfunktion zu Zola-generierten statischen Websites über Pagefind hinzufügt](https://pinchlime.com/blog/how-to-add-a-search-function-to-zola-generated-static-websites-via-pagefind/)" lesen, obwohl es um die Integration in das Zola-Blog-Framework und die Veröffentlichung über Netlify geht, ist das Prinzip ähnlich. Was die Integrationsmethode für Hugo betrifft, werde ich einen Artikel schreiben, nachdem ich mit der Konfiguration gebastelt habe. Sie können es unter [dieser Adresse](https://www.pseudoyu.com/de/search) vorab ansehen, oder auf "Suche" in der Navigationsleiste klicken (ich habe eine Zurück-nach-oben-Funktion hinzugefügt, Sie können klicken, um direkt zurückzukehren).

Ich habe es in meinen ursprünglichen GitHub CI automatischen Veröffentlichungsworkflow integriert, und die Erfahrung ist nahtlos. Ich habe auch eine Suchseiten-UI über Hugos Shortcode-Methode zur Verwendung integriert, was sehr leistungsfähig ist. Ich werde auch einen PR an das Theme-Repository einreichen, um dies zu unterstützen, um zu sehen, ob es in diesem Bereich Nachfrage gibt.

Allerdings habe ich nach der Verwendung einige Probleme mit der chinesischen Unterstützung festgestellt. Es kann Wörter nicht sehr gut segmentieren. Zum Beispiel wird die direkte Suche nach "区块链" (Blockchain) nicht übereinstimmen, aber wenn man es zu "区块 链" (Block Kette) ändert und die Wörter manuell segmentiert, wird der gewünschte Effekt erzielt. Ich habe die Suchmethode auf der Seite notiert, ~~es ist schließlich nicht unbrauchbar~~. Wir werden sehen, ob es in Zukunft bessere Lösungen gibt.

![pagefind_and_hugo_1](https://image.pseudoyu.com/images/pagefind_and_hugo_1.png)

Interessanterweise sollte meine Blog-Bastelei für diese Woche hier enden, aber plötzlich mailte mir GitHub über einen PR und Kommentare. Ein Fremder hatte meinen Blog geforkt und einige Stilanpassungen und Modifikationen vorgenommen, einige Funktionen hinzugefügt. Später schickte er mir sogar seine verbesserte CSS-Datei zur Referenz.

![github_blog_pr](https://image.pseudoyu.com/images/github_blog_pr.png)

Ursprünglich waren dies nur einige Lösungen für den persönlichen Gebrauch, und ich fand mich oft einen Nachmittag lang glücklich mit dem Theme bastelnd, ohne ein Wort zu schreiben. Ich hätte nicht erwartet, dass einige Menschen es bemerken, schätzen und übernehmen würden, und sogar viele meiner Probleme im Gegenzug lösen würden. Es fühlt sich ziemlich wunderbar an, und ich beginne, die Freude an Open Source oder öffentlichem Arbeiten zu spüren. Es gibt immer einige unerwartete Gewinne. Also verbrachte ich letzte Nacht einige Zeit mit Basteln, behob mehrere Stilprobleme, die schon eine Weile problematisch waren, aber ich hatte sie nicht behoben oder beachtet, und fügte sogar einen Zurück-nach-oben-Button-Effekt hinzu. Ich war ziemlich glücklich darüber.

### Server

Wie in einem früheren Wochenrückblick erwähnt, habe ich, nachdem ich herausgefunden hatte, wie man einen Reverse-Proxy für meinen Server mit [Nginx Proxy Manager](https://nginxproxymanager.com/) einrichtet, mehrere häufig genutzte Dienste und Websites gestartet, wie den zuvor erwähnten [zlib.pseudoyu.com](https://zlib.pseudoyu.com/) Buchsuchdienst. Da er einige Aufmerksamkeit erhielt und in einige Gruppen und Kanäle aufgenommen wurde, wollte ich ihn weiterhin pflegen, um die Servicestabilität und Zugriffsgeschwindigkeit zu gewährleisten. Allerdings waren dies zuvor alles leistungsschwache Maschinen, die mit nur wenigen Diensten schon voll ausgelastet waren. Also habe ich mir, die Einführung eines neuen anständigen Plans von Bandwagon Host nutzend, ein paar Maschinen besorgt: 2C2G + 40G Festplatte + CN2GIA DC6 Leitung, was für den langfristigen stabilen Betrieb einiger Dienste völlig ausreichend ist.

![yu_services_vps](https://image.pseudoyu.com/images/yu_services_vps.png)

Ich hatte auch schon vorher einige andere Maschinen, auf denen einige meiner grundlegenden Dienste liefen, mit einigen kleinen Anwendungen, die für Freunde zum Gebrauch eingerichtet waren. Diesmal habe ich alles gut organisiert und alle Dienste auf eine Maschine migriert. Hier muss ich die Docker- und docker-compose-Verwaltungsmethoden loben - die Datenmigration war so nahtlos. Nachdem alles migriert war, nahm es nur etwa die Hälfte der Ressourcen in Anspruch, was großartig ist.

Da ich jetzt mehr Maschinen habe (ein glückliches Problem), habe ich auch einen Open-Source-Überwachungsdienst für die Verwaltung gefunden. Es gibt mir das Gefühl, ein Cyber-Kapitalist zu sein, der diese Maschinen beaufsichtigt, hart zu arbeiten und nicht faul zu sein.

![yu_server_status](https://image.pseudoyu.com/images/yu_server_status.png)

### Desktop-Setup und Tastatur

Vielleicht weil ich keine Spiele spiele, bin ich eigentlich kein hartgesottener Tastatur-Enthusiast. Ich kann kaum den Unterschied zwischen verschiedenen Schaltern und Tastenkappen erkennen, und ich habe bisher meistens die eingebauten Scherenschalter-Tastaturen von Mac verwendet, ohne Unbehagen zu empfinden.

Es war wahrscheinlich gegen Ende 2020, als sie mich fragte, ob es etwas gäbe, das ich mir schon immer gewünscht, aber nie wirklich gekauft hätte. Nach langem Nachdenken sagte ich HHKB. Eigentlich war es mehr aus Neugier als aus praktischem Bedarf, und das retro Design des alten Batteriefachs entsprach völlig meiner Ästhetik.

Einige Tage später erhielt ich sie. Es war die HHKB Professional Hybrid Type-S Silent-Version, mit einem alten IBM-artigen Farbschema. Das elektrostatische kapazitive Gefühl, kombiniert mit ihrer kompakten Größe, gefiel mir wirklich gut. Sie koordinierte auch sehr gut auf dem Desktop.

![keyboard_hhkb_type_s_1](https://image.pseudoyu.com/images/keyboard_hhkb_type_s_1.jpg)

Jeden Morgen, bevor ich mit dem Lernen und Arbeiten beginne, ordne ich meine Umgebung ein wenig, platziere sorgfältig die Tastatur. Diese Tastatur hat mich von Hongkong nach Peking begleitet, und ich bringe sie sogar jedes Mal mit, wenn ich in ein Café gehe. Anfangs war es vielleicht nur eine Angewohnheit, aber nach und nach wurde es zu einer Art Ritual. Es scheint dem Codieren und Schreiben etwas Freude hinzugefügt zu haben.

![keyboard_hhkb_type_s_2](https://image.pseudoyu.com/images/keyboard_hhkb_type_s_2.jpg)

Nachdem ich sie über ein Jahr lang benutzt hatte, wollte ich, weil ich das Gefühl der elektrostatischen kapazitiven Schalter wirklich mochte, die verbleibenden wenigen Klassiker ausprobieren. Also erhielt ich, ebenfalls als Geschenk, eine RealForce PFU Limited Edition 87-Tasten-Tastatur. Diese sieht auch sehr schön aus, mit einem metallischen Gefühl in Umgebungen mit wenig Licht. Allerdings fühlte ich mich, vielleicht weil ich an das spezielle Tastenlayout der HHKB gewöhnt war, beim plötzlichen Wechsel zu einem 87-Tasten-Layout oft etwas unwohl. So wurde sie letztendlich mehr von ihr zum Spielen benutzt. Wie auch immer, eine Tastatur kann meine unbeholfenen Gaming-Fähigkeiten nicht retten.

![realforce_pfu_87](https://image.pseudoyu.com/images/realforce_pfu_87.jpg)

Die RealForce blieb später unbenutzt. Und ich konnte mich wirklich nicht mehr an große Tastaturen gewöhnen, also schickte ich sie zu Ni, der in Australien war. (Wenn ich darüber nachdenke, war meine erste mechanische Tastatur auch ein Geschenk von ihm, eine Cherry, obwohl ich vergessen habe, welchen Schalter sie hatte. Ich benutzte sie fast ein Jahr lang zu Hause, als ich noch Windows benutzte, und sie war ziemlich nett.)

Obwohl HHKB und RealForce bekannter zu sein scheinen, ist meiner persönlichen Erfahrung nach die am exquisitesten gefertigte und qualitativ beste unter den drei Klassikern der elektrostatischen kapazitiven Tastaturen tatsächlich die Leopold FC660C, die ich Mitte letzten Jahres erworben habe. Das Farbschema und das Tippgefühl sind angenehmer, man genießt wirklich die Erfahrung. Sie wurde anschließend zur Haupttastatur für meinen Desktop zu Hause.

![keyboard_leopold_fc660c](https://image.pseudoyu.com/images/keyboard_leopold_fc660c.jpg)

Eigentlich waren an diesem Punkt meine Tastaturnutzungsbedürfnisse vollständig erfüllt, und ich hatte nicht viel Energie, um das Ultimative zu verfolgen oder mit Anpassungen zu spielen. Eines späten Abends stieß ich jedoch auf "[【Selbstgemacht】Ich habe eine modulare mechanische Tastatur gemacht!【Soft Core】](https://www.bilibili.com/video/BV19V4y1J7Hx)" von Zhihui Jun, eine Tastatur, die von der Schaltungshardware bis zum Firmware-Code neu gestaltet und definiert wurde, alles von ihm selbst gemacht. Wer könnte dem widerstehen?

Während des Nationalfeiertags sah ich zufällig, dass er eine Co-Branding-Tastatur mit Bilibili auf den Markt gebracht hatte. Ich bestellte sie ohne zu zögern. In der Tat ist die rosa Farbe sehr attraktiv. Dies ist auch in gewissem Sinne meine erste Custom-Tastatur.

![keyboard_hello_word_75](https://image.pseudoyu.com/images/keyboard_hello_word_75.jpg)

Dann kamen mehrere Monate des langen Wartens, und endlich kam sie diese Woche in meine Hände. Ich muss sagen, sowohl das Aussehen als auch das Gefühl sind ausgezeichnet. Ich änderte schnell mein Desktop-Layout und tippte eine Woche lang glücklich vor mich hin. Vielleicht ist das Aussehen doch die primäre Produktivität. Ich habe das Gefühl, dass mein Artikel- und Code-Output diese Woche zugenommen hat. Xiaoyu kommentierte: "Wie kommt es, dass sich deine ganze Persönlichkeit nur wegen einer neuen Tastatur geändert hat?"

![chat_with_xiaoyu_about_keyboard](https://image.pseudoyu.com/images/chat_with_xiaoyu_about_keyboard.png)

Ich habe keine Sammelgewohnheit, noch will ich das ultimative Gefühl oder kundenspezifische Lösungen verfolgen. Es ist nur so, dass ich schon immer ein großes Verlangen hatte, an Dingen herumzubasteln, mit denen ich täglich interagiere, wie Desktop-Anordnungen, Computern, Tastaturen und Software-Tools. Selbst wenn es nur ein paar Sekunden Geschwindigkeitsverbesserung oder ein bisschen Stimmungsaufhellung ist, ist es für mich etwas, das sich lohnt zu tun.

## Persönliche Lebensschnappschüsse

### Lernen

Ich habe kein Japanisch gelernt... Die erste Woche der Check-ins gescheitert!

### Output

In Bezug auf den Output habe ich einen Artikel für GoCN übersetzt: "[Go 1.20 Neue Änderungen! Teil Eins: Sprachfunktionen](https://www.pseudoyu.com/de/2023/01/12/golang_120_language_changes/)"; nachdem ich den Rückblick der letzten Woche gepostet hatte, traf ich einige neue Freunde, und diese Woche habe ich auch mehrere Tweets über Blog-Setup gepostet; ich habe einen Artikel für Sspai geplant, aber ich weiß nicht, wann ich ihn schreiben werde.

### Input

#### Bücher

- **Wovon ich rede, wenn ich vom Laufen rede**, ich begann dieses Buch im Oktober zu lesen, aber verschiedene Dinge passierten dazwischen und ich fiel mit meinem Lesefortschritt zurück. In letzter Zeit lese ich es langsam in meiner Freizeit. Ich liebe Murakamis Sprechstil wirklich, und ich möchte all seine Bücher lesen.

#### Anime

- **Mob Psycho 100**, ich habe es vor ein paar Jahren einmal gesehen und fand die Einstellung interessant, habe es aber nicht wirklich in der Tiefe gewürdigt. Kürzlich wollte ich es noch einmal sehen. Die erste Staffel hat viele Ursprünge, Bindungen und Veränderungen der Hauptcharaktere. Während es ein lustiger Alltagsanime ist, gibt er den Menschen auch viele Ideen und Gedanken. Ich habe die zweite und dritte Staffel am Stück geschaut. Wenn die erste Staffel nur einige Bindungen beschrieb, brachten mir die zweite und dritte Staffel zu viele Emotionen. Das Wachstum der Charaktere, die Veränderungen der Menschen um sie herum, trotz der Einstellung, Esper zu sein, verleugnen sie sich ständig im täglichen Leben und akzeptieren sich selbst unter dem Einfluss der Menschen um sie herum. Ich mag die Nebengesprächsszene zwischen Mob und Reigen nach der Pressekonferenz am meisten, Emotionen sind bereits unausgesprochen.
- **Bungo Stray Dogs**, ich habe schon lange davon gehört, habe gerade erst angefangen, es zu verfolgen.
- **Das Drei-Körper-Problem**, ich schätze, die Mentalität, der Dramaadaption zu folgen, ist zu sehen, welche Art von psychedelischer Operation man haben kann.