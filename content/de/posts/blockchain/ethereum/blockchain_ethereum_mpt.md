---
title: "Detaillierte Erklärung des Ethereum MPT (Merkle Patricia Tries)"
date: 2021-08-16T12:12:17+08:00
draft: false
tags: ["blockchain", "ethereum"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Vorwort

Kürzlich erhielt ich eine Arbeitsaufgabe, die Datenstruktur des Zustandsbaums des Projekts-Smart-Contracts von einem Rot-Schwarz-Baum in einen Trie zu ändern und die Leistung der beiden Datenstrukturen zu vergleichen. Der Trie bezieht sich hauptsächlich auf die offizielle Java-Implementierung von Ethereum [ethereum/ethereumj](https://github.com/ethereum/ethereumj/tree/develop/ethereumj-core/src/main/java/org/ethereum/trie), während der Rot-Schwarz-Baum von mir selbst implementiert wurde. Dieser Artikel ist eine Aufzeichnung des theoretischen und praktischen Vergleichs der beiden Datenstrukturen.

## Datenstrukturen

### Rot-Schwarz-Baum

Ein Rot-Schwarz-Baum ist ein annähernd ausgewogener binärer Suchbaum, der rote und schwarze Knoten enthält und sicherstellt, dass der Höhenunterschied zwischen dem linken und rechten Teilbaum eines beliebigen Knotens weniger als das Zweifache beträgt.

![red_black_tree_2](https://image.pseudoyu.com/images/red_black_tree_2.png)

#### Eigenschaften

Er muss die folgenden fünf Eigenschaften erfüllen:

1. Knoten sind entweder rot oder schwarz
2. Der Wurzelknoten ist schwarz
3. Blattknoten (NIL) sind schwarz
4. Beide Kinder jedes roten Knotens sind schwarz
5. Jeder Pfad von einem gegebenen Knoten zu einem seiner Nachkommen-NIL-Knoten enthält die gleiche Anzahl schwarzer Knoten

Rot-Schwarz-Bäume sind nicht perfekt ausgewogen, aber die Anzahl der Schichten in den linken und rechten Teilbäumen ist gleich, daher auch als schwarz perfekt ausgewogen bekannt. Da er annähernd ausgewogen ist, wird die Häufigkeit von Rotationen reduziert, die Wartungskosten sinken und die Zeitkomplexität bleibt bei LogN.

#### Operationen

Rot-Schwarz-Bäume erhalten ihre Selbstbalance hauptsächlich durch drei Operationen:

- Linksrotation
- Rechtsrotation
- Farbänderung

#### Vergleich mit AVL-Bäumen

- AVL-Bäume bieten schnellere Suchanfragen (aufgrund perfekter Balance)
- Rot-Schwarz-Bäume bieten schnellere Einfüge- und Löschoperationen
- AVL-Bäume speichern mehr Knoteninformationen (Balancefaktor und Höhe) und belegen daher mehr Speicherplatz
- AVL-Bäume eignen sich besser, wenn Leseoperationen häufig und Schreiboperationen selten sind, oft in Datenbanken verwendet; Rot-Schwarz-Bäume werden im Allgemeinen verwendet, wenn Schreiboperationen häufiger sind, da sie prägnant und leicht zu implementieren sind, oft in Bibliotheken verschiedener Hochsprachen verwendet, wie map, set usw.

#### Code-Implementierung

Da Rot-Schwarz-Bäume relativ komplex sind, wurde der Implementierungscode zum Lernen und als Referenz auf GitHub hochgeladen.

[pseudoyu/RedBlackTree-Java](https://github.com/pseudoyu/RedBlackTree-java)

### Trie - Wörterbaumbaum

Trie, auch bekannt als Wörterbaumbaum, Präfixbaum oder Schlüsselbaum, wird häufig für Statistiken und Sortierung großer Mengen von Zeichenketten verwendet, wie z.B. Textdiskstatistiken in Suchmaschinen.

Er kann unnötige Zeichenkettenvergleiche minimieren, was zu einer hohen Abfrageeffizienz führt.

![trie_structure](https://image.pseudoyu.com/images/trie_structure.png)

#### Eigenschaften

1. Knoten speichern keine vollständigen Wörter
2. Die einem Knoten entsprechende Zeichenkette wird durch Verbinden der Zeichen gebildet, die auf dem Weg vom Wurzelknoten zu diesem Knoten durchlaufen werden
3. Die von allen Kindknoten eines Knotens dargestellten Pfadzeichen sind unterschiedlich
4. Knoten können zusätzliche Informationen speichern, wie z.B. Worthäufigkeit

#### Implementierung interner Knoten

![trie_nodes](https://image.pseudoyu.com/images/trie_nodes.png)

Die Höhe eines Trie ist relativ gering, aber er belegt mehr Speicherplatz. Die Kernidee ist, Speicher gegen Zeit einzutauschen.

Er verwendet die gemeinsamen Präfixe von Zeichenketten, um die Kosten der Abfragezeit zu reduzieren und so die Effizienz zu verbessern, was natürlich Geschäftsszenarien wie Wortassoziationen lösen kann.

#### Code-Implementierung

```java
class Trie {
    private Trie[] children;
    private boolean isEnd;

    public Trie() {
        children = new Trie[26];
        isEnd = false;
    }

    public void insert(String word) {
        Trie node = this;
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            int index = ch - 'a';
            if (node.children[index] == null) {
                node.children[index] = new Trie();
            }
            node = node.children[index];
        }
        node.isEnd = true;
    }

    public boolean search(String word) {
        Trie node = searchPrefix(word);
        return node != null && node.isEnd;
    }

    public boolean startsWith(String prefix) {
        return searchPrefix(prefix) != null;
    }

    private Trie searchPrefix(String prefix) {
        Trie node = this;
        for (int i = 0; i < prefix.length(); i++) {
            char ch = prefix.charAt(i);
            int index = ch - 'a';
            if (node.children[index] == null) {
                return null;
            }
            node = node.children[index];
        }
        return node;
    }
}
```

### Modifizierte Merkle Patricia Tries

#### Speichermethode für Ethereum-Kontostatus

1. Die Verwendung einer Key-Value-Hashtabelle für die Speicherung ist kostspielig, da bei jeder Blockerstellung neue Transaktionen in Blöcke gepackt werden, was den Merkle-Baum verändert, aber tatsächlich ändern sich nur wenige Konten.
2. Die direkte Verwendung eines Merkle-Baums zur Speicherung von Konten ist nicht praktikabel, da er keine effiziente Methode zum Suchen und Aktualisieren bietet.
3. Die Verwendung eines sortierten Merkle-Baums ist ebenfalls nicht praktikabel, da neue Kontoadressen zufällig generiert werden, was Einfügen und Neusortieren erfordert.

#### MPT-Struktur

Nutzung der Eigenschaften der Trie-Struktur:

1. Die Trie-Struktur bleibt nach dem Mischen unverändert, ist natürlich sortiert und wird nicht beeinflusst, selbst wenn neue Werte eingefügt werden, was für die kontobasierte Struktur von Ethereum geeignet ist.
2. Sie hat eine gute Aktualisierungslokalität, da beim Aktualisieren nicht der gesamte Baum durchlaufen werden muss.

Die Trie-Struktur verschwendet jedoch Speicherplatz und ist ineffizient, wenn Schlüssel-Wert-Paare spärlich verteilt sind. Ethereum-Kontoadressen sind 40-stellige Hexadezimalzahlen mit etwa 2^160 möglichen Adressen, die extrem spärlich sind (um Hash-Kollisionen zu verhindern).

Daher muss die Trie-Struktur komprimiert werden, was der Patricia Trie ist. Nach der Komprimierung wird die Höhe des Baums deutlich reduziert, was sowohl den Speicherplatz als auch die Effizienz verbessert.

![pactricia_trie](https://image.pseudoyu.com/images/pactricia_trie.png)

#### Modifizierte MPT-Struktur

Die von Ethereum tatsächlich verwendete Struktur ist die modifizierte MPT-Struktur, wie unten gezeigt:

![modified_merkle_pactricia_trie](https://image.pseudoyu.com/images/modified_merkle_pactricia_trie.png)

Wenn ein neuer Block veröffentlicht wird, ändern sich die Werte der neuen Knoten im Zustandsbaum. Anstatt den ursprünglichen Wert zu ändern, werden neue Zweige erstellt, wodurch der ursprüngliche Zustand erhalten bleibt (und somit ein Rollback ermöglicht wird).

Im Ethereum-System sind Forks häufig, und Daten in verwaisten Blöcken müssen zurückgesetzt werden. Aufgrund des Vorhandenseins von Smart Contracts in ETH müssen zur Unterstützung des Rollbacks von Smart Contracts frühere Zustände beibehalten werden.

#### Code-Implementierung

Der Code bezieht sich auf die Java-Implementierung von Ethereum.

[ethereum/ethereumj - GitHub](https://github.com/ethereum/ethereumj/tree/develop/ethereumj-core/src/main/java/org/ethereum/trie)

## Fazit

Das oben Genannte ist eine Analyse der Datenstrukturen `Ethereum MPT` und Rot-Schwarz-Baum. Als ich mich mit LeetCode abmühte, dachte ich oft, dass das Lernen dieser Dinge nutzlos sei, aber ich hatte nicht erwartet, so bald ein Anwendungsszenario zu haben. Wir müssen immer noch gut verstehen und üben!

## Referenzen

> 1. [30 Bilder, die Ihnen helfen, Rot-Schwarz-Bäume gründlich zu verstehen](https://www.jianshu.com/p/e136ec79235c)
> 2. [LeetCode-Implementierung von Trie](https://leetcode-cn.com/problems/implement-trie-prefix-tree/solution/shi-xian-trie-qian-zhui-shu-by-leetcode-ti500/)
> 3. [pseudoyu/RedBlackTree-Java](https://github.com/pseudoyu/RedBlackTree-java)
> 4. [Ethereum-Quellcode-Analyse -- MPT-Baum](https://segmentfault.com/a/1190000016050921)
> 5. [ethereum/ethereumj](https://github.com/ethereum/ethereumj/tree/develop/ethereumj-core/src/main/java/org/ethereum/trie)