---
title: "Interpretation der Bitcoin Core-Technologie"
date: 2021-02-17T12:12:17+08:00
draft: false
tags: ["blockchain", "bitcoin"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Vorwort

Im vorherigen Artikel "[Grundlagen und Schlüsseltechnologien der Blockchain](https://www.pseudoyu.com/en/2021/02/12/blockchain_basic/)" habe ich die grundlegenden Kenntnisse und Schlüsseltechnologien der Blockchain umrissen. Da Bitcoin die typischste Anwendung der Blockchain ist, wird dieser Artikel die Kerntechnologien von Bitcoin interpretieren. Falls es Fehler oder Auslassungen gibt, diskutieren und korrigieren Sie diese bitte.

## Bitcoin-System

Bitcoin ist eine digitale Währung, die 2009 von Satoshi Nakamoto erfunden wurde, hauptsächlich um dem zentralisierten Bankensystem entgegenzuwirken. Aufgrund seines genialen Systemdesigns und seiner Sicherheit ist sein Wert rasant gestiegen. Gleichzeitig wurde es wegen seiner starken Anonymität, da es nicht an Identitäten der realen Welt gebunden ist, auch für illegale Transaktionen, Geldwäsche, Erpressung und andere böswillige Aktivitäten genutzt, was zu einigen Kontroversen geführt hat.

Als dezentrales Blockchain-System kann jeder darauf zugreifen und einen Knoten lokal unterhalten, um am Bitcoin-Netzwerk teilzunehmen. Der folgende Text wird auch den Bitcoin Core-Client verwenden, um einen Knoten lokal zu unterhalten.

![bitcoin_network_nodes](https://image.pseudoyu.com/images/bitcoin_network_nodes.png)

Knoten werden in Full Nodes und Light Nodes unterteilt. In den Anfängen waren alle Knoten Full Nodes, aber mit der wachsenden Datenmenge müssen Bitcoin-Clients, die auf Geräten wie Mobiltelefonen oder Tablets laufen, keine Informationen über die gesamte Blockchain speichern. Diese werden als Simplified Payment Verification (SPV) Nodes oder Light Nodes bezeichnet.

Der Bitcoin Core-Client ist ein Full Node, der im Folgenden ausführlich besprochen wird. Full Nodes sind immer online und halten vollständige Blockchain-Informationen aufrecht. Da sie einen vollständigen Satz von UTXOs im Speicher halten, können sie die Rechtmäßigkeit von Transaktionen überprüfen, indem sie die Block- und Transaktionsinformationen der gesamten Blockchain (vom Genesis-Block bis zum neuesten Block) verifizieren. Sie entscheiden auch, welche Transaktionen in Blöcke gepackt werden. Beim Verifizieren von Transaktionen, d.h. beim Mining, können sie entscheiden, auf welcher Kette weiter gemint wird, und im Falle von gleichlangen Forks wählen, welchem Fork zu folgen ist. Sie überwachen auch die von anderen Minern geschürften Blöcke und überprüfen deren Rechtmäßigkeit.

Light Nodes müssen nicht ständig online sein und auch nicht die gesamte Blockchain (die eine große Datenmenge darstellt) speichern. Sie müssen nur die Block-Header jedes Blocks behalten und nur die Blöcke speichern, die mit ihnen selbst in Verbindung stehen, nicht alle Transaktionen auf der Kette. Da sie nicht alle Informationen speichern, können sie die Rechtmäßigkeit der meisten Transaktionen und die Korrektheit neuer online veröffentlichter Blöcke nicht überprüfen. Sie können nur die mit ihnen verbundenen Blöcke überprüfen. Sie können die Existenz einer Transaktion durch Merkle Proof verifizieren, aber nicht bestätigen, dass eine Transaktion nicht existiert. Sie können die Schwierigkeit des Minings überprüfen, da diese im Block-Header gespeichert ist.

> Lassen Sie uns die Transaktionsverifizierungsmethoden von Full Nodes und Light Nodes anhand eines Beispiels erklären.

Nehmen wir an, wir müssen eine Transaktion T verifizieren, die sich in Block 300.000 befindet. Ein Full Node würde alle 300.000 Blöcke (bis zum Genesis-Block) untersuchen und dabei eine vollständige UTXO-Datenbank aufbauen, um sicherzustellen, dass diese Transaktion nicht ausgegeben wurde. Ein Light Node hingegen würde den Merkle-Pfad nutzen, um alle mit Transaktion T verbundenen Blöcke zu verknüpfen, und dann auf die Blöcke 300.001 bis 300.006 zur Bestätigung warten, um so die Rechtmäßigkeit der Transaktion zu verifizieren.

### Blockchain-Struktur

Blockchain ist eine Datenstruktur, die aus sequentiell verknüpften Blöcken besteht und in einer einzelnen Datei oder Datenbank gespeichert werden kann. Der Bitcoin-Client verwendet Googles LevelDB-Datenbank zur Datenspeicherung. Jeder Block verweist auf den vorherigen Block. Wenn ein Block modifiziert wird, werden alle nachfolgenden Blöcke beeinflusst. Um einen Block zu manipulieren, müsste man also gleichzeitig alle nachfolgenden Blöcke manipulieren, was eine große Menge an Rechenleistung erfordert. Oft übersteigen die Kosten den Nutzen, was die Sicherheit stark gewährleistet.

Die Blockchain-Struktur umfasst mehrere Kernkomponenten: Blockgröße (4 Bytes), Block-Header, Transaktionszähler (1-9 Bytes) und Transaktionen.

Die Block-Header-Größe beträgt 80 Bytes und speichert Version (4 Bytes), Previous Block Hash (32 Bytes), Merkle Tree Root (32 Bytes), Timestamp (4 Bytes), Difficulty Target (4 Bytes) und Nonce (4 Bytes).

Der Hash-Wert jedes Blocks wird durch eine doppelte Hash-Operation am Block-Header gewonnen, d.h. SHA256(SHA256(Block Header)). Er existiert nicht in der Blockchain-Struktur, sondern wird von jedem Knoten nach Erhalt des Blocks berechnet und ist eindeutig. Zusätzlich kann auch die Block Height als Identifikator für den Block dienen.

#### Merkle-Baum

Der Merkle-Baum ist eine sehr wichtige Datenstruktur in der Blockchain, die hauptsächlich zur Verifizierung größerer Datensätze durch Hash-Algorithmen verwendet wird (ebenfalls durch eine doppelte Hash-Methode SHA256(SHA256(Block Header))). Die Struktur ist im folgenden Diagramm dargestellt:

![merkle_tree_example](https://image.pseudoyu.com/images/merkle_tree_example.png)

Mit der Merkle-Baum-Methode kann man schnell überprüfen, ob eine Transaktion in einem bestimmten Block existiert (mit einer Algorithmus-Komplexität von LogN). Um beispielsweise zu überprüfen, ob eine Transaktion K in einem Block existiert, müssen nur wenige Knoten aufgerufen werden.

![merkle_proof_example](https://image.pseudoyu.com/images/merkle_proof_example.png)

Da es im Bitcoin-Netzwerk eine große Anzahl von Transaktionen gibt, kann diese Methode die Effizienz stark verbessern, wie im folgenden Diagramm gezeigt:

![merkle_proof_efficiency](https://image.pseudoyu.com/images/merkle_proof_efficiency.png)

Da Light Nodes (wie Bitcoin-Wallets auf Mobiltelefonen) nicht die gesamten Blockchain-Daten speichern, können Transaktionen leicht über die Merkle-Baum-Struktur gefunden werden. Light Nodes konstruieren einen Bloom-Filter, um Transaktionen zu erhalten, die mit ihnen in Verbindung stehen:
1. Zuerst wird der Bloom-Filter auf einen leeren Wert initialisiert, alle Adressen in der Wallet werden abgerufen, ein Abrufmuster wird erstellt, um die Adressen zu matchen, die mit diesem Transaktionsoutput in Verbindung stehen, und das Abrufmuster wird dem Bloom-Filter hinzugefügt;
2. Dann wird der Bloom-Filter an verschiedene Knoten gesendet (über die filterload-Nachricht);
3. Nach Erhalt sendet der Knoten eine merkleblock-Nachricht, die die Block-Header enthält, die die Bedingungen erfüllen, und den Merkle-Pfad der übereinstimmenden Transaktionen, sowie eine tx-Nachricht, die die Filterergebnisse enthält.

Während des Prozesses wird der Light Node den Merkle-Pfad verwenden, um Transaktionen mit Blöcken zu verknüpfen, und Block-Header verwenden, um die Blockchain zu bilden, wodurch er überprüfen kann, dass Transaktionen in der Blockchain existieren.

Die Verwendung eines Bloom-Filters gibt Ergebnisse zurück, die die Filterbedingungen erfüllen, und es werden auch einige falsch positive Ergebnisse zurückgegeben, sodass viele irrelevante Ergebnisse zurückgegeben werden, was auch die Privatsphäre schützen kann, wenn Light Nodes relevante Adressen von anderen Knoten anfordern.

### Bitcoin-Netzwerk

Das Bitcoin-System läuft auf einem P2P-Peer-to-Peer-Netzwerk, in dem die Knoten gleichberechtigt sind, ohne Unterscheidung von Identität oder Berechtigungen; es gibt keine zentralisierten Server, und das Netzwerk hat keine hierarchischen Unterscheidungen.

Jeder Knoten muss eine Reihe von Transaktionen aufrechterhalten, die darauf warten, in die Kette aufgenommen zu werden. Jeder Block hat eine Größe von 1M, sodass es einige Sekunden dauert, bis er an die meisten Knoten weitergegeben wird. Angenommen, ein Knoten überwacht eine Transaktion von A nach B, wird er sie in den Satz schreiben. Wenn er gleichzeitig einen Double-Spending-Angriff von A nach C entdeckt, wird er diesen nicht einschreiben. Wenn er die gleiche A-zu-B-Transaktion oder eine A-zu-C-Transaktion von derselben Münzquelle überwacht, wird er die A-zu-B-Transaktion in diesem Satz löschen.

### Bitcoin-Konsensprotokoll

Als offenes System, an dem jeder teilnehmen kann, muss Bitcoin die Bedrohung durch böswillige Knoten lösen. Die Lösung ist der Proof-of-Work-Mechanismus, der auch als Rechenleistungs-Abstimmungsmechanismus bekannt ist. Wenn eine neue Transaktion auftritt, werden neue Datensätze gesendet, und das gesamte Netzwerk führt den Konsensalgorithmus aus. Miner minen, um die Aufzeichnungen zu verifizieren, d.h. sie lösen Zufallszahlen. Der Miner, der das Rätsel zuerst löst, erhält das Recht zur Aufzeichnung, generiert einen neuen Block und sendet dann den neuen Block extern. Nachdem andere Knoten verifiziert und bestätigt haben, wird er der Hauptkette hinzugefügt.

### Wallet

Als digitales Währungssystem hat Bitcoin sein eigenes Wallet-System, das hauptsächlich aus drei Teilen besteht: privater Schlüssel, öffentlicher Schlüssel und Wallet-Adresse.

> Der Prozess der Generierung einer Wallet-Adresse ist wie folgt:

1. Unter Verwendung des ECDSA (Elliptic Curve Digital Signature Algorithm) wird der entsprechende öffentliche Schlüssel mit dem privaten Schlüssel generiert.
2. Der öffentliche Schlüssel ist lang und schwer einzugeben und zu merken, daher wird ein öffentlicher Schlüssel-Hash-Wert durch SHA256- und RIPEMD160-Algorithmen gewonnen.
3. Schließlich wird er mit Base58Check verarbeitet, um eine besser lesbare Wallet-Adresse zu erhalten.

### Transaktionsprozess

Mit einer Wallet (und Vermögenswerten) kann man mit dem Handeln beginnen. Verstehen wir diesen Prozess anhand einer typischen Bitcoin-Transaktion:

A und B haben beide eine Bitcoin-Wallet-Adresse (die vom Bitcoin-Client generiert werden kann, das Prinzip ist wie oben). Angenommen, A möchte 5 BTC an B überweisen. A muss die Wallet-Adresse von B erhalten, dann mit seinem eigenen privaten Schlüssel die Transaktion "A überweist 5 BTC an B" signieren (da nur A seinen privaten Schlüssel kennt, ist der Besitz des privaten Schlüssels gleichbedeutend mit dem Besitz der Wallet-Vermögenswerte). Dann wird diese Transaktion veröffentlicht. Im Bitcoin-System erfordert das Initiieren einer Transaktion die Zahlung einer kleinen Miner-Gebühr als Transaktionsgebühr. Miner werden beginnen, die Rechtmäßigkeit dieser Transaktion zu überprüfen. Nach sechs Bestätigungen kann die Transaktion vom Bitcoin-Ledger akzeptiert werden. Der gesamte Verifizierungsprozess dauert etwa 10 Minuten.

> Warum verbrauchen Miner eine große Menge an Rechenleistung, um Transaktionen zu verifizieren?

Miner können während des Verifizierungsprozesses Block-Belohnungen und Miner-Gebühren erhalten. Block-Belohnungen werden alle vier Jahre reduziert, sodass in den späteren Phasen der Hauptanreiz die Miner-Gebühren sind.

> Warum dauert die Verifizierung 10 Minuten?

Bitcoin ist nicht absolut sicher. Neue Transaktionen sind anfällig für einige böswillige Angriffe. Indem die Mining-Schwierigkeit kontrolliert wird, um den Verifizierungsprozess auf etwa 10 Minuten zu stabilisieren, können böswillige Angriffe weitgehend verhindert werden. Dies ist nur eine probabilistische Garantie.

> Wie vermeidet das Bitcoin-System Double Spending?

Bitcoin hat ein Konzept namens UTXO (Unspent Transaction Outputs) eingeführt. Wenn ein Benutzer eine BTC-Transaktion erhält, wird sie in der UTXO aufgezeichnet.

In diesem Beispiel möchte A 5 BTC an B überweisen. Die 5 BTC von A könnten aus zwei UTXOs stammen (2 BTC + 3 BTC). Wenn A also an B überweist, muss der Miner überprüfen, ob diese beiden UTXOs vor dieser Transaktion bereits ausgegeben wurden. Wenn sie feststellen, dass sie bereits ausgegeben wurden, ist die Transaktion ungültig.

Das folgende Diagramm veranschaulicht gut den Ablauf mehrerer Transaktionen und das damit verbundene Konzept der UTXO

![btc_utxo_example](https://image.pseudoyu.com/images/btc_utxo_example.png)

Darüber hinaus hat UTXO eine sehr wichtige Eigenschaft: sie ist unteilbar. Angenommen, A hat 20 BTC und möchte 5 BTC an B überweisen. Die Transaktion wird zunächst 20 BTC als Eingabe nehmen und dann zwei Ausgaben produzieren, eine, die 5 BTC an B überweist, und eine, die die verbleibenden 15 BTC an A zurückgibt. Daher besitzt A jetzt eine UTXO im Wert von 15 BTC. Wenn eine einzelne UTXO nicht ausreicht, um zu zahlen, können mehrere UTXOs kombiniert werden, um eine Eingabe zu bilden, aber die Summe muss größer sein als der Transaktionsbetrag.

> Wie überprüfen Miner, ob der Transaktionsinitiator über ausreichendes Guthaben verfügt?

Diese Frage erscheint auf den ersten Blick einfach. Die erste Reaktion könnte sein, zu überprüfen, ob das Guthaben ausreicht, wie es Alipay tut. Bitcoin ist jedoch ein transaktionsbasiertes Ledger-Modell ohne das Konzept von Konten. Daher kann das Guthaben nicht direkt abgefragt werden. Um die verbleibenden Vermögenswerte eines Kontos zu kennen, muss man alle vorherigen Transaktionen überprüfen und alle UTXOs finden und aufaddieren.

### Transaktionsmodell

> Wir haben besprochen, wie eine Transaktion abläuft, aber aus welchen Teilen besteht eine Bitcoin-Transaktion?

![blockchain_bitcoin_script_detail](https://image.pseudoyu.com/images/blockchain_bitcoin_script_detail.png)

Wie in der Abbildung gezeigt, ist der erste Teil Version, der die Version angibt.

Dann kommen die Informationen bezüglich der Eingabe: Input Count gibt die Anzahl an, und Input Info gibt den Inhalt der Eingabe an, was das Unlocking Script ist, hauptsächlich verwendet, um die Quelle der Eingabe zu überprüfen, ob die Eingabe verfügbar ist, und andere Eingabedetails.
- Previous output hash - Alle Eingaben können auf eine Ausgabe zurückgeführt werden. Dies verweist auf die UTXO, die in dieser Eingabe ausgegeben wird. Der Hash-Wert dieser UTXO wird hier in umgekehrter Reihenfolge gespeichert.
- Previous output index - Eine Transaktion kann mehrere UTXOs haben, auf die durch ihre Indexnummern verwiesen wird. Der erste Index ist 0.
- Unlocking Script Size - Die Bytegröße des Unlocking Scripts.
- Unlocking Script - Der Hash, der das UTXO Unlocking Script erfüllt.
- Sequence Number - Standard ist ffffffff.

Als nächstes kommen die Informationen bezüglich der Ausgabe. Output Count gibt die Anzahl an, und Output Info gibt den Inhalt der Ausgabe an, was das Locking Script ist, hauptsächlich verwendet, um aufzuzeichnen, wie viele Bitcoins ausgegeben wurden, die Bedingungen für zukünftige Ausgaben und Ausgabedetails.
- Amount - Der Betrag der Bitcoin-Ausgabe, ausgedrückt in Satoshis (der kleinsten Einheit von Bitcoin). 10^8 Satoshis = 1 Bitcoin.
- Locking Script Size - Dies ist die Bytegröße des Locking Scripts.
- Locking Script - Dies ist der Hash des Locking Scripts, der die Bedingungen spezifiziert, die erfüllt sein müssen, um diese Ausgabe zu verwenden.

Schließlich gibt es Locktime, das den frühesten Zeitpunkt/Block angibt, an dem eine Transaktion der Blockchain hinzugefügt werden kann. Wenn es kleiner als 500 Millionen ist, liest es direkt die Blockhöhe, und wenn es größer als 500 Millionen ist, liest es den Zeitstempel.

### Bitcoin-Skript

In der Transaktion haben wir Unlocking Script und Locking Script erwähnt. Was ist also ein Bitcoin-Skript?

Bitcoin-Skript ist eine Liste von Anweisungen, die in jeder Transaktion aufgezeichnet sind. Wenn das Skript ausgeführt wird, kann es überprüfen, ob die Transaktion gültig ist, ob der Bitcoin verwendet werden kann, usw. Ein typisches Skript sieht so aus:

```sh
<sig> <pubKey> OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
```

Bitcoin-Skript wird von links nach rechts basierend auf einem Stack ausgeführt und verwendet Opcodes, um die Daten zu verarbeiten. In dieser Skriptsprache sind Daten, die in <> eingeschlossen sind, auf den Stack zu schieben, diejenigen ohne <> und mit dem Präfix OP_ sind Operatoren (OP kann weggelassen werden). Skripte können auch Daten einbetten, die permanent auf der Kette aufgezeichnet werden (nicht mehr als 40 Bytes), und die aufgezeichneten Daten beeinflussen UTXO nicht.

In einer Transaktion ist `<sig> <pubKey>` das Unlocking Script und `OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG` ist das Locking Script.

Im Vergleich zu den meisten Programmiersprachen ist Bitcoin-Skript nicht Turing-vollständig. Es hat keine Schleifen oder komplexe Flusssteuerung, ist einfach auszuführen, produziert deterministische Ergebnisse, egal wo es ausgeführt wird, und speichert keinen Zustand. Darüber hinaus sind Skripte voneinander unabhängig. Aufgrund dieser Eigenschaften ist Bitcoin-Skript zwar relativ sicher, kann aber keine sehr komplexe Logik handhaben, sodass es nicht geeignet ist, um einige komplexe Geschäfte zu handhaben. Ethereums Smart Contracts machten in diesem Aspekt innovative Durchbrüche und gaben so vielen dezentralen Anwendungen die Geburt.

### Mining

Wir haben das Mining in der vorherigen Diskussion des gesamten Transaktionsprozesses erwähnt. Lassen Sie uns es jetzt im Detail besprechen.

Einige Knoten werden, um Block-Belohnungen und Miner-Gebühren zu erhalten und Gewinne zu erzielen, Transaktionen verifizieren, was als Mining bezeichnet wird. Block-Belohnungen werden durch Coinbase erzeugt und verringern sich alle vier Jahre, von 25 im Jahr 2009 auf jetzt 6,5.

Mining ist eigentlich ein Prozess des ständigen Versuchs von Zufallszahlen, um einen bestimmten festgelegten Zielwert zu erreichen, wie z.B. weniger als ein bestimmter Zielwert. Diese Schwierigkeit wird künstlich festgelegt, um die Verifizierungszeit anzupassen und die Sicherheit zu erhöhen, nicht um mathematische Probleme zu lösen.

Miner werden ständig versuchen, diesen Wert zu erreichen. Die Erfolgsrate ist sehr niedrig, aber die Anzahl der Versuche kann sehr hoch sein. Daher haben Knoten mit stärkerer Rechenleistung einen proportionalen Vorteil und sind eher in der Lage, das Rätsel zu lösen.

> Warum muss die Mining-Schwierigkeit angepasst werden?

Im Bitcoin-System ist es leicht, Forks zu produzieren, wenn die Blockzeit zu kurz ist. Wenn es zu viele Forks gibt, wird es die Fähigkeit des Systems beeinträchtigen, Konsens zu erreichen, was die Systemsicherheit gefährdet. Das Bitcoin-System passt die Schwierigkeit an, um die Blockgenerierungsgeschwindigkeit bei etwa 10 Minuten zu stabilisieren und damit zu verhindern, dass Transaktionen manipuliert werden.

> Wie wird die Mining-Schwierigkeit angepasst?

Das System passt den Zielschwellenwert alle 2016 Blöcke (etwa zwei Wochen) an, der im Block-Header gespeichert wird. Alle Knoten im gesamten Netzwerk müssen der neuen Schwierigkeit beim Mining folgen. Wenn böswillige Knoten den Zielwert in ihrem Code nicht anpassen, werden ehrliche Miner ihn nicht anerkennen.

Zielschwellenwert = Zielschwellenwert * (Tatsächliche Zeit zur Produktion von 2016 Blöcken / Erwartete Zeit zur Produktion von 2016 Blöcken)

Als Bitcoin geboren wurde, gab es wenige Miner und die Mining-Schwierigkeit war relativ niedrig. Das meiste Mining wurde direkt mit Heimcomputern (CPUs) durchgeführt. Mit immer mehr Teilnehmern am Bitcoin-Ökosystem stieg die Schwierigkeit des Minings. Nach und nach begannen die Menschen, einige GPUs mit stärkerer Rechenleistung für das Mining zu verwenden. Einige spezialisierte ASIC (Application Specific Integrated Circuit) Mining-Chips und Mining-Maschinen sind auch allmählich als Reaktion auf die Marktnachfrage entstanden. Jetzt gibt es auch viele große Mining-Pools, die eine große Menge an Rechenleistung im gesamten Netzwerk für zentralisiertes Mining kombinieren.

In diesem großen Mining-Pool-System fungiert der Pool-Manager als Full Node, während die große Anzahl der gesammelten Miner gemeinsam Hash-Werte berechnen und schließlich Gewinne durch den Proof-of-Work-Mechanismus verteilen. Wenn die Rechenleistung jedoch zu konzentriert ist, kann dies leicht einige Zentralisierungsrisiken erzeugen. Zum Beispiel könnte ein großer Mining-Pool, wenn er mehr als 51% der Netzwerkrechenleistung erreicht, Transaktionen rückgängig machen oder bestimmte Transaktionen boykottieren.

### Forks

Im Bitcoin-System kann es auch Situationen geben, in denen kein Konsens erreicht wird, die als Forks bezeichnet werden. Forks werden hauptsächlich in zwei Arten unterteilt: Eine ist ein Zustandsfork, der oft absichtlich von einigen Knoten durchgeführt wird; die andere wird als Protokollfork bezeichnet, was bedeutet, dass es einige Meinungsverschiedenheiten über das Bitcoin-Protokoll gibt.

Protokollforks können weiter in zwei Typen unterteilt werden. Einer wird als harter Fork bezeichnet, was bedeutet, dass inkompatible Änderungen an Teilen des Protokolls vorgenommen wurden. Zum Beispiel die Änderung der Blockgröße von Bitcoin von 1M auf 4M. Diese Art von Fork ist permanent und bildet zwei parallele Ketten, die sich von einem bestimmten Knoten aus entwickeln, wie Bitcoin Classic, was zu zwei Arten von Münzen führt.

Die andere wird als weicher Fork bezeichnet. Zum Beispiel, immer noch die Anpassung der Blockgröße von Bitcoin, aber von 1M auf 0,5M. Nach einer solchen Anpassung wird es eine Situation geben, in der neue Knoten kleine Blöcke minen und alte Knoten große Blöcke minen. Weiche Forks sind nicht permanent. Typische Beispiele sind die Modifikation des Inhalts von Coinbase und der durch P2SH (Pay to Script Hash) erzeugte Fork.

## Bitcoin Core-Client

Bitcoin Core ist die Implementierung von Bitcoin, auch bekannt als Bitcoin-QT oder Satoshi-Client. Durch diesen Client kann man sich mit dem Bitcoin-Netzwerk verbinden, die Blockchain verifizieren, Bitcoins senden und empfangen usw. Es gibt drei Netzwerke: Mainnet, Testnet und Regnet, zwischen denen gewechselt werden kann.

Es bietet eine Debug-Konsole, um direkt mit der Bitcoin-Blockchain zu interagieren. Gängige Operationen sind wie folgt:

> Blockchain

- getblockchaininfo: Gibt verschiedene Statusinformationen über die Blockchain-Verarbeitung zurück
- getblockcount: Gibt die Anzahl der Blöcke in der Blockchain zurück
- verifychain: Überprüft die Blockchain-Datenbank

> Hash

- getblockhash: Gibt den Hash des angegebenen Blocks zurück
- getnetworkhashps: Gibt die geschätzten Netzwerk-Hashes pro Sekunde basierend auf den letzten n Blöcken zurück
- getbestblockhash: Gibt den Hash des besten (Spitzen-) Blocks in der längsten Blockchain zurück

> Blöcke

- getblock: Gibt detaillierte Informationen über einen Block zurück
- getblockheader: Gibt Informationen über den Block-Header zurück
- generate: Mint sofort die angegebene Anzahl von Blöcken an eine Wallet-Adresse

> Wallet

- getwalletinfo: Gibt ein Objekt zurück, das verschiedene Wallet-Statusinformationen enthält
- listwallets: Gibt eine Liste der aktuell geladenen Wallets zurück
- walletpassphrasechange: Ändert die Wallet-Passphrase

> Mempool

- getmempoolinfo: Gibt Details zum aktiven Zustand des TX-Speicherpools zurück
- getrawmempool: Gibt alle Transaktions-IDs im Speicherpool zurück
- getmempoolentry: Gibt Mempool-Daten für eine gegebene Transaktion zurück

> Transaktion

- getchaintxstats: Berechnet Statistiken über die Gesamtzahl und Rate der Transaktionen in der Kette
- getrawtransaction: Gibt Rohtransaktionsdaten zurück
- listtransactions: Gibt eine Liste der Transaktionen für ein gegebenes Konto zurück

> Signatur

- signrawtransaction: Signiert Eingaben für Rohtransaktion
- signmessage: Signiert eine Nachricht mit dem privaten Schlüssel einer Adresse
- dumpprivkey: Offenbart den privaten Schlüssel, der einer Adresse entspricht

> Netzwerk

- getnetworkinfo: Gibt ein Objekt zurück, das verschiedene Statusinformationen bezüglich P2P-Netzwerken enthält
- getpeerinfo: Gibt Daten über jeden verbundenen Netzwerkknoten zurück
- getconnectioncount: Gibt die Anzahl der Verbindungen zu anderen Knoten zurück

> Mining

- getmininginfo: Gibt ein Objekt zurück, das mining-bezogene Informationen enthält
- getblocktemplate: Gibt Daten zurück, die benötigt werden, um einen Block zu konstruieren, an dem gearbeitet werden soll
- prioritisetransaction: Akzeptiert oder priorisiert eine Transaktion im Mempool für das Mining

## Schlussfolgerung

Das oben Genannte ist eine Interpretation der Kerntechnologie von Bitcoin, die sich hauptsächlich auf ihre grundlegenden Prinzipien und ihr Datenmodell konzentriert. Durch das Studium von Bitcoin können wir die Designphilosophie und den Betriebsmechanismus der Blockchain besser verstehen. Als Nächstes werden wir Ethereum studieren und analysieren, das als Blockchain 2.0 bekannt ist. Bleiben Sie dran!