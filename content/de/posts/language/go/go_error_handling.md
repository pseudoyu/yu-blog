---
title: "Zusammenfassung der Go-Fehlerbehandlung und Best Practices"
date: 2021-08-29T00:19:42+08:00
draft: false
tags: ["go", "error", "programming", "translation"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Vorwort

In letzter Zeit habe ich das Go Advanced Training Camp von Herrn Mao Jian von GeekTime überprüft und zusammengefasst. Dies ist ein Kurs, der sich stärker auf Technik und Prinzipien konzentriert und eine breite Palette von Wissenspunkten abdeckt. Daher habe ich beschlossen, eine Serie zu starten, um dies aufzuzeichnen und zusammenzufassen, was auch meine eigene Überprüfung und Referenz erleichtern wird. Dies ist der erste Artikel in der Serie, "Go-Fehlerbehandlung".

## Go-Fehlerbehandlungsmechanismus

### Eingebaute Go-Fehler

In Go ist ein `error` einfach eine reguläre Schnittstelle, die einen Wert repräsentiert:

```go
// http://golang.org/pkg/builtin/#error
// Definition der Fehlerschnittstelle

type error interface {
    Error() string
}

// http://golang.org/pkg/errors/error.go
// errors konstruieren Fehlerobjekte

type errorString struct {
    s string
}

func (e *errorString) Error() string {
    return e.s
}
```

Es gibt zahlreiche benutzerdefinierte `error`-Typen in der Standardbibliothek, wie `Error: EOF`, und `errors.New()` gibt einen Zeiger auf das interne `errorString`-Objekt zurück.

### Fehler vs. Ausnahme

Im Gegensatz zu Sprachen wie Java und C++ besteht Go's Ansatz zur Behandlung von Ausnahmen nicht darin, Ausnahmen einzuführen, sondern mehrere Rückgabeparameter zu verwenden. Daher kann ein Fehler-Schnittstellenobjekt in die Funktion eingeschlossen werden, um vom Aufrufer behandelt zu werden.

```go
func handle() (int, error) {
    return 1, nil
}

func main() {
    i, err := handle()
    if err != nil {
        return
    }
    // Andere Verarbeitungslogik
}
```

Es ist erwähnenswert, dass Go einen Panic-Mechanismus hat, der in Verbindung mit Recovery verwendet werden kann, um einen Effekt ähnlich wie `try...exception...` zu erzielen. Allerdings ist Go's Panic nicht gleichbedeutend mit Ausnahmen. Ausnahmen werden in der Regel vom Aufrufer behandelt, während Go's Panic für wirklich außergewöhnliche Situationen gedacht ist (wie Index außerhalb des Bereichs, Stacküberlauf, nicht behebbare Umgebungsprobleme usw.), was darauf hinweist, dass der Code nicht weiter ausgeführt werden kann und nicht davon ausgegangen werden sollte, dass der Aufrufer die Panic lösen wird.

Go's Ansatz der mehrfachen Rückgabewerte zur Unterstützung der Fehlerbehandlung durch den Aufrufer bietet Entwicklern große Flexibilität mit den folgenden Vorteilen:

- Einfachheit
- Planung für Fehler, nicht für Erfolg
- Kein versteckter Kontrollfluss
- Vollständige Kontrolle über die Fehlerbehandlung für den Entwickler
- Fehler ist ein Wert, bietet daher große Flexibilität bei der Behandlung

## Best Practices für die Go-Fehlerbehandlung

### Panic

Panic sollte nur in wirklich außergewöhnlichen Situationen verwendet werden, wie zum Beispiel:

- Wenn ein kritischer Dienst beim Programmstart fehlschlägt, Panic auslösen und beenden
- Wenn Konfigurationen beim Programmstart offensichtlich unangemessen sind, Panic auslösen und beenden (defensive Programmierung)
- An Programmeinstiegspunkten, wie die Verwendung von Recovery in Gin-Middleware, um zu verhindern, dass das Programm aufgrund von Panic beendet wird

Da Panic dazu führt, dass das Programm direkt beendet wird, und die Verwendung von Recovery zur Behandlung weder leistungsfähig noch kontrollierbar ist, sollte Panic in anderen Situationen nicht direkt verwendet werden, es sei denn, der Programmfehler ist nicht behebbar. Stattdessen sollte ein Fehler zurückgegeben werden, wobei es dem Entwickler überlassen bleibt, diesen zu behandeln.

### Error

In der Entwicklung verwenden wir in der Regel `github.com/pkg/errors` zur Behandlung von Anwendungsfehlern, aber es ist wichtig zu beachten, dass wir dies in der Regel nicht in öffentlichen Bibliotheken verwenden.

Bei der Verwendung von mehreren Rückgabewerten zur Überprüfung auf Fehler sollte `error` der letzte Rückgabewert der Funktion sein. Wenn `error` nicht `nil` ist, sollten andere Rückgabewerte in einem unbrauchbaren Zustand sein und nicht weiter verarbeitet werden. Bei der Behandlung von Fehlern sollten wir zuerst auf Fehler prüfen und sofort zurückkehren, wenn `if err != nil`, um übermäßige Codeverschachtelung zu vermeiden.

```go

// Falsches Beispiel

func f() error {
    ans, err := someFunc()
    if err == nil {
        // Andere Logik
    }

    return err
}

// Korrektes Beispiel

func f() error {
    ans, err := someFunc()
    if err != nil {
        return err
    }

    // Andere Logik
    return nil
}
```

Wenn im Programm ein Fehler auftritt, verwenden Sie im Allgemeinen `errors.New` oder `errors.Errorf`, um einen Fehlerwert zurückzugeben:

```go
func someFunc() error {
    res := anotherFunc()
    if res != true {
        errors.Errorf("Ergebnis inkorrekt, %d Versuche unternommen", count)
    }
    // Andere Logik
    return nil
}
```

Wenn beim Aufruf anderer Funktionen ein Problem auftritt, sollte es direkt zurückgegeben werden. Wenn zusätzliche Informationen mitgeführt werden müssen, verwenden Sie `errors.WithMessage`.

```go
func someFunc() error {
    res, err := anotherFunc()
    if err != nil {
        return errors.WithMessage(err, "andere Informationen")
    }
}
```

Wenn Fehler aus anderen Bibliotheken (Standardbibliotheken, Unternehmensbibliotheken, Open-Source-Bibliotheken von Drittanbietern usw.) erhalten werden, verwenden Sie bitte `errors.Wrap`, um Stack-Informationen hinzuzufügen. Dies muss nur verwendet werden, wenn der Fehler zum ersten Mal auftritt, und wird in der Regel nicht beim Schreiben von Basisbibliotheken und weit verbreiteten Bibliotheken von Drittanbietern verwendet, um doppelte Stack-Informationen zu vermeiden.

```go
func f() error {
    err := json.Unmashal(&a, data)
    if err != nil {
        return errors.Wrap(err, "andere Informationen")
    }

    // Andere Logik
    return nil
}
```

Wenn Fehler beurteilt werden müssen, sollte `errors.Is` für den Vergleich verwendet werden:

```go
func f() error {
    err := A()
    if errors.Is(err, io.EOF){
    	return nil
    }

    // Andere Logik
    return nil
}
```

Bei der Beurteilung von Fehlertypen verwenden Sie `errors.As` für die Zuweisung:

```go
func f() error {
    err := A()

    var errA errorA
    if errors.As(err, &errA){
    	// ...
    }

    // Andere Logik
    return nil
}
```

Für Fehler in der Geschäftslogik (wie Eingabefehler) ist es am besten, ein eigenes Fehlerwörterbuch an einem einheitlichen Ort zu erstellen, das Fehlercodes enthalten sollte und als separate Felder in Logs gedruckt werden kann. Eine klare Dokumentation ist ebenfalls erforderlich.

Wir verwenden oft Logs zur Unterstützung der Fehlerbehandlung. Fehler, die nicht zurückgegeben oder ignoriert werden müssen, müssen protokolliert werden, aber es ist verboten, an jedem Fehlerpunkt zu protokollieren. Wenn die gleiche Stelle ständig Fehler meldet, ist es am besten, die Fehlerdetails einmal zu drucken und die Anzahl der Vorkommen zu drucken.

## Fazit

Das oben Genannte ist eine Zusammenfassung der Go-Fehlerbehandlung und Best Practices. In Zukunft werde ich auch Fehlertypen, Fehlerumhüllung und häufige Fallstricke bei der Verwendung zusammenfassen.

## Referenzen

> 1. [Go Error Handling Best Practices](https://lailin.xyz/post/go-training-03.html)