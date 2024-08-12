---
title: "Implementierung von Two-Phase Commit in Solidity Smart Contracts unter Verwendung von State Locks"
date: 2022-07-01T10:54:57+08:00
draft: false
tags: ["blockchain", "ethereum", "solidity", "smart contract", "web3"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《后来的我们 - 五月天》" >}}

## Vorwort

In Smart-Contract-Anwendungen, die Interaktionen zwischen mehreren Systemen oder Verträgen beinhalten, insbesondere in Geschäftsbereichen, in denen die Genauigkeit von Vermögenswerten oder Daten sensibel ist, müssen wir die Datenatomizität während des gesamten Geschäftsprozesses sicherstellen. Daher müssen wir auf Vertragsebene einen Mechanismus implementieren, der dem mehrstufigen Commit ähnelt und den Zustandsänderungsprozess im Vertrag in zwei Phasen zerlegt: Vor-Commit und formaler Commit.

Dieser Artikel implementiert ein minimalistisches Zwei-Phasen-Commit-Modell unter Verwendung eines Zustandssperrmechanismus. Der vollständige Vertragscode ist unter [TwoPhaseCommit.sol](https://github.com/pseudoyu/learn-solidity/blob/master/practice/two_phase_commit/TwoPhaseCommit.sol) zu finden. Im Folgenden wird die Kernlogik dieses Vertrags erläutert und es wird angestrebt, Stilrichtlinien und Best Practices zu befolgen.

> Hinweis: Dieser Vertrag wurde hauptsächlich für den geschäftlichen Einsatz in Konsortialketten konzipiert und wurde nicht speziell für Gasgebühren optimiert. Er dient nur zu Lernzwecken.

## Vertragslogik

### Vertragsstruktur

Das Zwei-Phasen-Commit-Szenario umfasst die folgenden Methoden:
1. set: Zwei-Phasen - Vor-Commit
2. commit: Zwei-Phasen - Formaler Commit
3. rollback: Zwei-Phasen - Rollback

Aufgrund der Einschränkungen der Solidity-Sprache bei der Beurteilung und dem Vergleich von Zeichenkettenlängen bietet dieser Vertrag zur Verbesserung der Lesbarkeit des Vertragscodes einige Hilfsmethoden, hauptsächlich einschließlich:
1. isValidKey: Überprüft, ob der Schlüssel gültig ist
2. isValidValue: Überprüft, ob der Wert gültig ist
3. isEqualString: Vergleicht, ob zwei Zeichenketten gleich sind

### Zwei-Phasen-Commit Kernlogik

Im Zwei-Phasen-Commit-Szenario bietet dieser Vertrag einen einfachen Satz von `set`, `commit` und `rollback` Methoden, um Schlüssel-Wert-Paare, die in Vertragsaufrufen übergeben werden, in der Kette zu speichern. Wir verwenden einen Zustandssperrmechanismus, um die Atomizität von kettenübergreifenden Transaktionen zu erreichen. Wir definieren die folgenden Datenstrukturen:

```solidity
enum State {
    UNLOCKED,
    LOCKED
}

struct Payload {
    State state;
    string value;
    string lockValue;
}
```

Hier ist `State` ein Aufzählungstyp, der den Sperrstatus des Schlüssels in der Kette aufzeichnet, während die `Payload`-Struktur den Sperrstatus, den aktuellen Wert und den gesperrten Wert speichert. Sie ist durch die folgende `mapping`-Struktur an den Schlüssel gebunden:

```solidity
mapping (string => Payload) keyToPayload;
```

So können wir den Zustand jedes Schlüssels im Vertragsaufruf basierend auf `keyToPayload` verfolgen und den Zustand des Schlüssels in den folgenden `set`, `commit` und `rollback` Methoden zur Ausnahmebehandlung überprüfen.

#### set()

In der `set()`-Methode überprüfen wir den Zustand des Schlüssels. Wenn er `State.LOCKED` ist, wird keine Speicherung durchgeführt und eine Ausnahme wird ausgelöst:

```solidity
if (keyToPayload[_key].state == State.LOCKED) {
    revert TwoPhaseCommit__DataIsLocked();
}
```

Wenn er `State.UNLOCKED` ist, wird der im Vertragsaufruf übergebene Wert in lockValue gespeichert und sein Zustand wird auf `LOCKED` gesetzt, um auf anschließendes `commit` oder `rollback` zur Entsperrung zu warten.

```solidity
keyToPayload[_key].state = State.LOCKED;
keyToPayload[_key].lockValue = _value;
```

#### commit()

In der `commit()`-Methode überprüfen wir den Zustand des Schlüssels. Wenn er `State.UNLOCKED` ist, wird für diesen Schlüssel keine Operation durchgeführt und eine Ausnahme wird ausgelöst:

```solidity
if (keyToPayload[_key].state == State.UNLOCKED) {
    revert TwoPhaseCommit__DataIsNotLocked();
}
```

Wenn er `State.LOCKED` ist, überprüfen wir, ob der im Vertragsaufruf übergebene Wert gleich lockValue ist. Wenn nicht gleich, wird eine Ausnahme ausgelöst:

```solidity
if (!isEqualString(keyToPayload[_key].lockValue, _value)) {
    revert TwoPhaseCommit__DataIsInconsistent();
}
```

Wenn die Werte gleich sind, wird der diesem Schlüssel entsprechende Wert in der Kette gespeichert, der Zustand des Schlüssels wird auf `UNLOCKED` gesetzt, der aktuelle Wert `value` wird aktualisiert und `lockValue` wird geleert:

```solidity
store[_key] = _value;
keyToPayload[_key].state = State.UNLOCKED;
keyToPayload[_key].value = _value;
keyToPayload[_key].lockValue = "";
```

#### rollback()

In der `rollback()`-Methode überprüfen wir den Zustand des Schlüssels. Wenn er `State.UNLOCKED` ist, wird für diesen Schlüssel keine Operation durchgeführt und eine Ausnahme wird ausgelöst:

```solidity
if (keyToPayload[_key].state == State.UNLOCKED) {
    revert TwoPhaseCommit__DataIsNotLocked();
}
```

Wenn er `State.LOCKED` ist, überprüfen wir, ob der im Vertragsaufruf übergebene Wert gleich lockValue ist. Wenn nicht gleich, wird eine Ausnahme ausgelöst:

```solidity
if (!isEqualString(keyToPayload[_key].lockValue, _value)) {
    revert TwoPhaseCommit__DataIsInconsistent();
}
```

Wenn die Werte gleich sind, wird der Zustand des Schlüssels auf `UNLOCKED` gesetzt und `lockValue` wird geleert:

```solidity
keyToPayload[_key].state = State.UNLOCKED;
keyToPayload[_key].lockValue = "";
```

### Fehlerbehandlungslogik

In Ausnahmeszenarien der Vertragsausführung werfen wir Fehler und führen Rollbacks durch. Um die Lesbarkeit der Fehlermeldungen zu verbessern und die Fehlererfassung und -behandlung durch Anwendungspersonal der oberen Ebene zu erleichtern, haben wir den Ansatz der Fehlertypdefinition gewählt und verschiedene Ausnahmeszenarien definiert. Da ich bereits die meisten Informationen in der Fehlerbenennung einbezogen habe, wurden keine zusätzlichen Parameterwerte für Fehlertypen definiert, die nach Bedarf angepasst werden können.

```solidity
error TwoPhaseCommit__DataKeyIsNull();
error TwoPhaseCommit__DataValueIsNull();
error TwoPhaseCommit__DataIsNotExist();
error TwoPhaseCommit__DataIsLocked();
error TwoPhaseCommit__DataIsNotLocked();
error TwoPhaseCommit__DataIsInconsistent();
```

In der spezifischen Vertragslogik werfen wir Ausnahmen mit der `revert`-Methode, wie zum Beispiel:

```solidity
if (!isValidKey(bytes(_key))) {
    revert TwoPhaseCommit__DataKeyIsNull();
}

if (!isValidValue(bytes(_value))) {
    revert TwoPhaseCommit__DataValueIsNull();
}

if (keyToPayload[_key].state == State.UNLOCKED) {
    revert TwoPhaseCommit__DataIsNotLocked();
}

if (!isEqualString(keyToPayload[_key].lockValue, _value)) {
    revert TwoPhaseCommit__DataIsInconsistent();
}
```

### Generische Parametervalidierung

Wir führen einige Gültigkeitsprüfungen für Eingabeparameter durch. Um Erweiterbarkeit zu bieten, verwenden wir die Methoden `isValidKey()` und `isValidValue()`, um Schlüssel und Werte unabhängig zu validieren:

```solidity
/**
 * @notice Daten-Schlüssel-Format-Validierung
 * @param _key Daten - Schlüssel
 */
function isValidKey(bytes memory _key) private pure returns (bool)
{
    bytes memory key = _key;

    if (key.length == 0) {
        return false;
    }
    return true;
}

/**
 * @notice Daten-Wert-Format-Validierung
 * @param _value Daten - Wert
 */
function isValidValue(bytes memory _value) private pure returns (bool)
{
    bytes memory value = _value;

    if (value.length == 0) {
        return false;
    }
    return true;
}
```

Dieser Vertrag führt nur Nicht-Null-Überprüfungen durch. Sie können die Geschäftslogik nach Geschäftsanforderungen anpassen und sie dort aufrufen, wo eine Validierung erforderlich ist, wie zum Beispiel:

```solidity
if (!isValidKey(bytes(_key))) {
    revert TwoPhaseCommit__DataKeyIsNull();
}

if (!isValidValue(bytes(_value))) {
    revert TwoPhaseCommit__DataValueIsNull();
}

if (!isValidValue(bytes(store[_key]))) {
    revert TwoPhaseCommit__DataIsNotExist();
}
```

### Ereignismechanismus

Zusätzlich haben wir Ereignisse definiert, die den Kernmethoden entsprechen, und für Ereignisse indiziert sind, um die Überwachung und Verarbeitung durch Anwendungen der oberen Ebene zu erleichtern.

```solidity
event setEvent(string indexed key, string indexed value);
event getEvent(string indexed key, string indexed value);
event commitEvent(string indexed key, string indexed value);
event rollbackEvent(string indexed key, string indexed value);
```

Ereignisse werden in Vertragsmethoden mit der `emit()`-Methode ausgelöst, wie zum Beispiel:

```solidity
emit setEvent(_key, _value);
emit getEvent(_key, _value);
emit commitEvent(_key, _value);
emit rollbackEvent(_key, _value);
```

## Fazit

Das oben Genannte ist eine Best Practice für meinen Zwei-Phasen-Commit-Vertrag. Für grundlegende Solidity-Syntax verweise ich auf "[Solidity Smart Contract Entwicklung - Grundlagen](https://www.pseudoyu.com/de/2022/05/25/learn_solidity_from_scratch_basic/)". Ich werde in Zukunft weiterhin üben und mehr Vertragsszenarien erklären, also bleiben Sie dran.

## Referenzen

> 1. [TwoPhaseCommit.sol Vertragsquellcode](https://github.com/pseudoyu/learn-solidity/blob/master/practice/two_phase_commit/TwoPhaseCommit.sol)
> 2. [Solidity Smart Contract Entwicklung - Grundlagen](https://www.pseudoyu.com/de/2022/05/25/learn_solidity_from_scratch_basic/)
> 3. [Solidity Offizielle Dokumentation](https://docs.soliditylang.org/en/v0.8.15/)