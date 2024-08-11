---
title: "Häufig verwendete Datenstrukturen für LeetCode-Problemlösung (Java-Edition)"
date: 2021-01-01T00:12:17+08:00
draft: false
tags: ["java","algorithm", "leetcode"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Vorwort

Kürzlich habe ich begonnen, Algorithmusprobleme auf LeetCode zu lösen. Bei der berufsbezogenen Algorithmuspraxis liegt der Schwerpunkt auf der Verfeinerung von Problemlösungsansätzen und Programmierfähigkeiten, anstatt komplexe Datenstrukturen wie in Algorithmuswettbewerben zu verwenden. Daher sind die häufig verwendeten Datenstrukturen und Operationen nicht zahlreich. Der versierte Umgang mit diesen kann die Codequalität erheblich verbessern. Ich habe diese Zusammenfassung für eine einfache Referenz erstellt.

## Datenstrukturen

### Array []

#### Initialisierung

```java
// Initialisiere ein Array der Größe 10 mit Standardwert 0
int[] nums = new int[10];

// Initialisiere ein 2D-Boolean-Array
boolean[][] visited = new boolean[5][10];
```

#### Gängige Methoden

```java
// Im Allgemeinen wird zu Beginn einer Funktion eine Nicht-Leer-Prüfung durchgeführt, dann werden Elemente über den Index zugegriffen
if (nums.length == 0) {
    return;
}

for (int i = 0; i < nums.length; i++) {
    // Zugriff auf num[i]
}
```

### String

#### Initialisierung

```java
String s1 = "hallo welt";
```

#### Zugriff auf String

```java
// String unterstützt keinen direkten Zugriff auf Zeichen mit []
char c = s1.charAt(2);
```

#### Modifizierung von String

```java
// String unterstützt keine direkte Modifikation, er muss für Änderungen in char[] umgewandelt werden
char[] chars = s1.toCharArray();
chars[1] = 'a';
String s2 = new String(chars);
```

#### Vergleich von Strings

```java
// Verwenden Sie immer die equals-Methode zum Vergleichen, nicht ==
if (s1.equals(s2)) {
    // Gleich
} else {
    // Nicht gleich
}
```

#### Verkettung von Strings

```java
// Direkte Verkettung mit + wird unterstützt, ist aber nicht effizient
String s3 = s1 + "!";
```

#### Verwendung von StringBuilder für häufige String-Verkettung zur Effizienzsteigerung

```java
StringBuilder sb = new StringBuilder();

for (char c = 'a'; c <= 'f'; c++) {
    // Die append-Methode unterstützt das Verketten von Zeichen, Strings, Zahlen usw.
    sb.append(c);
    String result = sb.toString();
}
```

### ArrayList

#### Initialisierung

```java
// Initialisiere ein dynamisches Array für die Speicherung von String-Typen
ArrayList<String> strings = new ArrayList<>();

// Initialisiere ein dynamisches Array für die Speicherung von int-Typen
ArrayList<Integer> nums = new ArrayList<>();
```

#### Gängige Methoden

```java
// Überprüfe, ob leer
boolean isEmpty()

// Gib die Anzahl der Elemente zurück
int size()

// Greife auf Element über Index zu
E get(int index)

// Füge Element am Ende hinzu
boolean add(E e)
```

### LinkedList

#### Initialisierung

```java
// Initialisiere eine doppelt verkettete Liste für die Speicherung von String-Typen
LinkedList<String> strings = new LinkedList<>();

// Initialisiere eine doppelt verkettete Liste für die Speicherung von int-Typen
LinkedList<Integer> nums = new LinkedList<>();
```

#### Gängige Methoden

```java
// Überprüfe, ob leer
boolean isEmpty()

// Gib die Anzahl der Elemente zurück
int size()

// Füge Element am Ende hinzu
boolean add(E e)

// Entferne und gib das letzte Element zurück
E removeLast()

// Füge Element am Anfang hinzu
void addFirst(E e)

// Entferne und gib das erste Element zurück
E removeFirst()
```

### HashMap

#### Initialisierung

```java
// Initialisiere eine Hashtabelle, die Integer auf Strings abbildet
HashMap<Integer, String> map = new HashMap<>();

// Initialisiere eine Hashtabelle, die Strings auf Integer-Arrays abbildet
HashMap<String, int[]> map = new HashMap<>();
```

#### Gängige Methoden

```java
// Überprüfe, ob ein Schlüssel existiert
boolean containsKey(Object key)

// Hole den zum Schlüssel gehörenden Wert, gib null zurück, wenn nicht vorhanden
V get(Object key)

// Hole den zum Schlüssel gehörenden Wert, gib defaultValue zurück, wenn nicht vorhanden
V getOrDefault(Object key, V defaultValue)

// Speichere Schlüssel-Wert-Paar in der Hashtabelle
V put(K key, V value)

// Speichere Schlüssel-Wert-Paar in der Hashtabelle, wenn nicht vorhanden
V putIfAbsent(K key, V value)

// Entferne Schlüssel-Wert-Paar und gib den Wert zurück
V remove(Object key)

// Hole alle Schlüssel in der Hashtabelle
Set<K> keySet()
```

### Queue

#### Initialisierung

```java
// Queue ist ein Interface in Java
// Initialisiere eine Warteschlange für die Speicherung von String
Queue<String> q = new LinkedList<>();
```

#### Gängige Methoden

```java
// Überprüfe, ob leer
boolean isEmpty()

// Gib die Anzahl der Elemente zurück
int size()

// Gib das Element am Anfang der Warteschlange zurück
E peek()

// Entferne und gib das Element am Anfang der Warteschlange zurück
E poll()

// Füge Element am Ende der Warteschlange ein
boolean offer(E e)
```

### Stack

#### Initialisierung

```java
// Initialisiere einen Stack vom Typ int
Stack<Integer> s = new Stack<>();
```

#### Gängige Methoden

```java
// Überprüfe, ob leer
boolean isEmpty()

// Gib die Anzahl der Elemente zurück
int size()

// Lege Element oben auf den Stack
E push(E e)

// Gib das Element oben auf dem Stack zurück
E peek()

// Entferne und gib das Element oben auf dem Stack zurück
E pop()
```

## Fazit

Der Weg des Problemlösens ist lang... Bleib dran!

## Referenzen

> 1. [LeetCode Offizielle Website](https://leetcode.com)
> 2. [labuladongs Algorithmus-Spickzettel](https://github.com/labuladong/fucking-algorithm)