---
title: "Häufig verwendete Datenstrukturen für das Lösen von LeetCode-Problemen (Go-Edition)"
date: 2021-05-29T00:12:17+08:00
draft: false
tags: ["go","algorithm", "leetcode"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Vorwort

Kürzlich habe ich wieder begonnen, LeetCode-Algorithmusprobleme mit Go zu lösen. Bei der arbeitsbezogenen Algorithmenpraxis liegt der Hauptfokus darauf, Problemlösungsansätze und Programmierfähigkeiten zu schärfen, anstatt komplexe Datenstrukturen wie in algorithmischen Wettbewerben einzusetzen. Die häufig verwendeten Datenstrukturen und Operationen sind relativ wenige, aber ihre Beherrschung kann die Codequalität erheblich verbessern. Ich habe diese Zusammenfassung für eine einfache Referenz erstellt.

## Datenstrukturen

### Arrays

#### Initialisierung

```go
// Initialisierung eines Arrays der Größe 10 mit Standardwert 0
nums := make([10]int)

// Initialisierung eines zweidimensionalen booleschen Arrays
visited := make([5][10]int)
```

#### Gängige Methoden

```go
for i := 0; i < len(nums); i++ {
    // Zugriff auf num[i]
}
```

### Strings

#### Initialisierung

```go
s1 := "hallo welt"

// Erstellung eines mehrzeiligen Strings
s2 := `Dies ist ein
mehrzeiliger
String.`
```

#### Zugriff auf Strings

```go
// Direkter Zugriff auf Bytes (nicht Zeichen) mittels Index
s1 := "hallo welt"
first := s[0]

s2 := []byte(s1)
first := s2[0]
```

#### Strings modifizieren

```go
// String-Werte sind unveränderlich, kann einen neuen String-Wert zuweisen
s := "hallo"
t := s

// String in []byte oder []rune für Modifikationen umwandeln
s1 := "hallo welt"
s2 := []byte(s1)
s2[0] = 'H'
s3 := string(s2)
```

#### Prüfen, ob Zeichen zu bestimmtem Zeichensatz gehört

```go
    // Prüfen, ob das Zeichen an Index i des Strings s ein Vokal ist
    if strings.Contains("aeiouAEIOU", string(s[i])) {
        // ...
    }
```

#### Strings vergleichen

```go
if s1 == s2 {
    // Gleich
} else {
    // Nicht gleich
}

// Compare-Funktion kann für Vergleich verwendet werden, 1 größer, 0 gleich, -1 kleiner
// EqualFold-Funktion vergleicht unter Ignorierung der Groß-/Kleinschreibung
```

#### Strings verketten

```go
// Direkte Verwendung von + für Verkettung, aber nicht effizient
s1 := "hallo "
s2 := s1 + "welt"
```

#### Effiziente String-Verkettung

```go
// bytes.Buffer kann auf einmal verketten
var b bytes.Buffer
b.WriteString("Hallo ")
b.WriteString("Welt")
b1 := b.String()

// Mehrere Strings verketten
var strs []string
strings.Join(strs, "Welt")
```

#### Integer (oder beliebigen Datentyp) in String umwandeln

```go
// Itoa-Umwandlung
i := 123
t := strconv.Itoa(i)

// Sprintf-Umwandlung
i := 123
t := fmt.Sprintf("%d", i)
```

### Slices

#### Initialisierung

```go
// Initialisierung eines Slice, der String-Typ speichert
slice := make([]string, 0)
slice := []string

// Initialisierung eines Slice, der int-Typ speichert
slice := make([]int, 0)
slice := []int
```

#### Gängige Methoden

```go
// Prüfen, ob leer
if len(slice) == 0 {
    // Leer
}

// Anzahl der Elemente zurückgeben
len()

// Element per Index zugreifen
slice[i]

// Element am Ende anfügen
slice = append(slice, 1)
```

### Simulation von Stack und Queue mit Slices

#### Stack

```go
// Stack erstellen
stack := make([]int, 0)
// Push
stack = append(stack, 10)
// Pop
v := stack[len(stack) - 1]
stack = stack[:len(stack) - 1]
// Prüfen, ob Stack leer ist
len(stack) == 0
```

#### Queue

```go
// Queue erstellen
queue := make([]int, 0)
// Enqueue
queue = append(queue, 10)
// Dequeue
v := queue[0]
queue = queue[1:]
// Länge 0 ist leer
len(queue) == 0
```

### Map

```go
// Erstellen
m := make(map[string]int)
// Schlüssel-Wert setzen
m["hallo"] = 1
// Schlüssel löschen
delete(m,"hallo")
// Iterieren
for k, v := range m{
    // Operation
}

// Map-Schlüssel müssen vergleichbar sein, können kein Slice, Map, Funktion sein
// Map-Werte haben Standardwerte, können direkt auf Standardwerte operieren, z.B. m[alter]++ Wert ändert sich von 0 auf 1
// Um zwei Maps zu vergleichen, muss man iterieren und prüfen, ob kv gleich sind, wegen Standardwertbeziehung muss man sowohl val als auch ok prüfen
```

### Standardbibliothek

#### sort

```go
// Integers sortieren
sort.Ints([]int{})
// Strings sortieren
sort.Strings([]string{})
```

#### math

```go
// int32 Max- und Min-Werte
math.MaxInt32
math.MinInt32
// int64 Max- und Min-Werte (int ist standardmäßig int64)
math.MaxInt64
math.MinInt64
```

#### copy

```go
// Um a[i] zu löschen, kann copy verwendet werden, um i bis Ende-Werte auf i zu überschreiben, dann Ende -1
copy(a[i:], a[i+1:])
a = a[:len(a)-1]

// make erstellt Länge, dann Wert per Index zuweisen
a := make([]int, n)
a[n] = x

// make Länge 0, dann Wert mit append() zuweisen
a := make([]int, 0)
a = append(a, x)
```

### Typenumwandlung

```go
// byte zu Zahl
s = "12345"  // s[0] ist vom Typ byte
num := int(s[0] - '0') // 1
str := string(s[0]) // "1"
b := byte(num + '0') // '1'
fmt.Printf("%d%s%c\n", num, str, b) // 111

// string zu Zahl
num, _ := strconv.Atoi()
str := strconv.Itoa()
```

## Schlussfolgerung

Der Weg des Problemlösens ist lang... Macht weiter!

## Referenzen

> 1. [LeetCode Offizielle Website](https://leetcode.com)
> 2. [greyireland/algorithm-pattern](https://github.com/greyireland/algorithm-pattern)