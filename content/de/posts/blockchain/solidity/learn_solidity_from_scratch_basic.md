---
title: "Solidity Smart Contract Entwicklung - Grundlagen"
date: 2022-05-25T01:07:33+08:00
draft: false
tags: ["blockchain", "ethereum", "solidity", "smart contract", "web3"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="'Here After Us - Mayday'" >}}

## Vorwort

Im letzten Jahr habe ich während meines Masterstudiums den Kurs "COMP7408 Distributed Ledger and Blockchain Technology" an der HKU belegt. In diesem Kurs lernte ich über die Entwicklung von Ethereum Smart Contracts und erstellte eine einfache Bibliotheksverwaltungs-ÐApp. Für mein Abschlussprojekt entschied ich mich, eine Musik-Copyright-Anwendung basierend auf Ethereum zu entwickeln, die unter [Uright - Blockchain Music Copyright Management ÐApp](https://github.com/pseudoyu/uright) zu finden ist. Durch diese Erfahrungen gewann ich ein grundlegendes Verständnis für die Solidity-Entwicklung.

Nach Beginn meiner beruflichen Laufbahn konzentrierte ich mich hauptsächlich auf Consortium-Blockchain und Geschäftsentwicklung und hatte lange Zeit nicht mit Verträgen gearbeitet. Infolgedessen wurde mein Verständnis der Syntax und einiger zugrunde liegender Konzepte etwas vage. Kürzlich war ich an einem Projekt beteiligt, das auf einer EVM-kompatiblen Kette basiert und die Entwicklung grundlegender Verträge für Beweisspeicherung, -abruf und -migration umfasst. Das Debuggen dieser Verträge erwies sich als herausfordernd, weshalb ich beschloss, Solidity systematisch zu studieren. Indem ich meine Notizen in Artikeln organisiere, hoffe ich, mich selbst zu ermutigen, tief zu denken und effektiv zusammenzufassen.

Diese Artikelserie wird auch in mein persönliches Wissensbasis-Projekt "Blockchain Beginner's Guide" aufgenommen, das unter [https://www.pseudoyu.com/blockchain-guide/](https://www.pseudoyu.com/blockchain-guide/) zu finden ist. Ich beabsichtige, diese Ressource kontinuierlich zu verbessern, während ich lerne. Für Interessierte können Sie das [Projekt-Repository](https://github.com/pseudoyu/blockchain-guide) besuchen, um beizutragen oder Vorschläge zu machen.

Dieser Artikel ist der erste in der Serie und wird die grundlegenden Kenntnisse von Solidity behandeln.

## Smart Contracts und die Solidity-Sprache

Smart Contracts sind Programme, die auf der Blockchain laufen. Vertragsentwickler können Smart Contracts verwenden, um mit On-Chain-Assets und -Daten zu interagieren, während Benutzer Verträge über ihre On-Chain-Konten aufrufen können, um auf Assets und Daten zuzugreifen. Aufgrund der Eigenschaften der Blockchain, historische Aufzeichnungen in einer Kettenstruktur zu bewahren, Dezentralisierung und Unveränderlichkeit, bieten Smart Contracts im Vergleich zu traditionellen Anwendungen eine größere Fairness und Transparenz.

Da Smart Contracts jedoch mit der Blockchain interagieren müssen, verbrauchen Operationen wie Bereitstellung und Datenschreiben eine gewisse Menge an Gebühren. Die Kosten für Datenspeicherung und -änderung sind ebenfalls relativ hoch. Daher ist es bei der Gestaltung von Verträgen entscheidend, den Ressourcenverbrauch zu berücksichtigen. Darüber hinaus können reguläre Smart Contracts nach der Bereitstellung nicht mehr geändert werden, sodass bei der Vertragsgestaltung Sicherheit, Upgradefähigkeit und Erweiterbarkeit berücksichtigt werden müssen.

Solidity ist eine vertragsorientiertierte Hochsprache, die für die Implementierung von Smart Contracts entwickelt wurde. Sie läuft auf der EVM (Ethereum Virtual Machine) und hat eine Syntax ähnlich wie JavaScript. Sie ist derzeit die beliebteste Smart-Contract-Sprache und ist für diejenigen, die in die Blockchain- und Web3-Bereiche einsteigen, unerlässlich. Solidity bietet relativ umfassende Lösungen, um die oben genannten Probleme beim Schreiben von Verträgen anzugehen, die wir später im Detail besprechen werden.

## Entwicklungs- und Debug-Tools

Im Gegensatz zu herkömmlichen Programmiersprachen kann die Entwicklung von Solidity Smart Contracts oft nicht bequem direkt über eine IDE oder lokale Umgebung debuggt werden. Stattdessen erfordert sie eine Interaktion mit einem On-Chain-Knoten. Entwicklung und Debugging werden typischerweise nicht direkt auf dem Mainnet (der Kette, auf der echte Assets, Daten und Geschäfte residieren) durchgeführt, da dies hohe Transaktionsgebühren verursachen würde. Derzeit gibt es mehrere Hauptmethoden und Frameworks für Entwicklung und Debugging:

1. [Truffle](https://github.com/trufflesuite/truffle). Truffle ist ein sehr beliebtes JavaScript-Framework für die Solidity-Vertragsentwicklung. Es bietet eine vollständige Toolchain für Entwicklung, Test und Debugging und kann mit lokalen oder entfernten Netzwerken interagieren.

2. [Brownie](https://github.com/eth-brownie/brownie). Brownie ist ein Python-basiertes Framework für die Solidity-Vertragsentwicklung. Es bietet praktische Toolchains für Debugging und Testen mit prägnanter Python-Syntax.

3. [Hardhat](https://github.com/NomicFoundation/hardhat). Hardhat ist ein weiteres JavaScript-basiertes Entwicklungsframework, das ein sehr reichhaltiges Plugin-System bietet, geeignet für die Entwicklung komplexer Vertragsprojekte.

Zusätzlich zu Entwicklungsframeworks ist es notwendig, mit einigen Tools vertraut zu sein, um besser mit Solidity arbeiten zu können:

1. [Remix IDE](https://remix.ethereum.org). Das Debugging kann mit dem von Ethereum bereitgestellten browserbasierten Remix-Entwicklungstool durchgeführt werden. Remix bietet eine vollständige IDE, Kompilierungstools, Bereitstellungs-Debugging-Testknoten-Umgebung, Konten usw., was es sehr bequem für Tests macht. Dies ist das Tool, das ich beim Lernen am meisten verwendet habe. Remix kann auch direkt mit Testnets und Mainnets über das MetaMask-Plugin interagieren, und einige Produktionsumgebungen verwenden es auch für Kompilierung und Bereitstellung.

2. Remix IDE ist nicht perfekt für Syntaxvorschläge, daher können Sie [Visual Studio Code](https://code.visualstudio.com) mit der [Solidity](https://marketplace.visualstudio.com/items?itemName=juanblanco.solidity)-Erweiterung für eine bessere Schreiberfahrung verwenden.

3. [MetaMask](https://metamask.io). Eine häufig verwendete Wallet-Anwendung. Während der Entwicklung können Sie über das Browser-Plugin mit Testnets und Mainnets interagieren, was für Entwickler bequem zum Debuggen ist.

4. [Ganache](https://trufflesuite.com/ganache/). Ganache ist ein Open-Source virtueller lokaler Knoten, der ein virtuelles Kettennetzwerk bereitstellt. Es kann mit verschiedenen Web3.js, Remix oder einigen Framework-Tools interagieren und eignet sich für lokales Debugging und Testen von Projekten einer bestimmten Größenordnung.

5. [Infura](https://infura.io). Infura ist ein IaaS (Infrastructure as a Service) Produkt. Wir können unseren eigenen Ethereum-Knoten beantragen und über die von Infura bereitgestellte API interagieren, was für das Debugging bequem ist und näher an der Produktionsumgebung liegt.

6. [OpenZeppelin](https://www.openzeppelin.com). OpenZeppelin bietet zahlreiche Vertragsentwicklungsbibliotheken und Anwendungen, die Sicherheit und Stabilität gewährleisten und gleichzeitig Entwicklern eine bessere Entwicklungserfahrung bieten und die Kosten für die Vertragsentwicklung reduzieren.

## Vertragskompilierung und -bereitstellung

Solidity-Verträge sind Dateien mit der Erweiterung `.sol` und können nicht direkt ausgeführt werden. Sie müssen in Bytecode kompiliert werden, der von der EVM (Ethereum Virtual Machine) erkannt werden kann, um auf der Kette zu laufen.

![compile_solidity](https://image.pseudoyu.com/images/compile_solidity.png)

Nach der Kompilierung wird der Vertrag vom Vertragskonto auf die Kette bereitgestellt. Andere Konten können über Wallets mit dem Vertrag interagieren, um On-Chain-Geschäftslogik zu implementieren.

## Kernsyntax

Jetzt, da wir ein grundlegendes Verständnis für die Entwicklung, das Debugging und die Bereitstellung von Solidity haben, lassen Sie uns in die Kernsyntax von Solidity eintauchen.

### Datentypen

Wie gängige Programmiersprachen hat Solidity mehrere eingebaute Datentypen.

#### Grundlegende Datentypen

- `boolean`: Boolescher Typ hat zwei Werte, `true` und `false`. Er kann als `bool public boo = true;` definiert werden. Der Standardwert ist `false`.
- `int`: Ganzzahltyp, kann von `int8` bis `int256` spezifiziert werden, Standard ist `int256`. Er kann als `int public int = 0;` definiert werden. Der Standardwert ist `0`. Sie können auch `type(int).min` und `type(int).max` verwenden, um die Minimal- und Maximalwerte des Typs zu überprüfen.
- `uint`: Nicht-negativer Ganzzahltyp, kann als `uint8`, `uint16`, `uint256` spezifiziert werden, Standard ist `uint256`. Er kann als `uint8 public u8 = 1;` definiert werden. Der Standardwert ist `0`.
- `address`: Adresstyp, kann als `address public addr = 0xCA35b7d915458EF540aDe6068dFe2F44E8fa733c;` definiert werden. Der Standardwert ist `0x0000000000000000000000000000000000000000`.
- `bytes`: Abkürzung für `byte[]`, unterteilt in Arrays fester Größe und variable Arrays. Es kann als `bytes1 a = 0xb5;` definiert werden.

Es gibt auch einige relativ komplexe Datentypen, die wir separat besprechen werden.

#### Enum

`Enum` ist ein Aufzählungstyp, der mit der folgenden Syntax definiert werden kann:

```solidity
enum Status {
    Unknown,
    Start,
    End,
    Pause
}
```

Er kann mit der folgenden Syntax aktualisiert und initialisiert werden:

```solidity
// Enum-Typ instanziieren
Status public status;

// Enum-Wert aktualisieren
function pause() public {
    status = Status.Pause;
}

// Enum-Wert initialisieren
function reset() public {
    delete status;
}
```

#### Arrays

Arrays sind geordnete Sammlungen von Elementen des gleichen Typs. Sie können als `uint[] public arr;` definiert werden. Sie können die Array-Größe im Voraus bei der Definition angeben, wie `uint[10] public myFixedSizeArr;`.

Beachten Sie, dass wir Arrays im Speicher erstellen können (die Unterschiede zwischen `memory` und `storage` werden später im Detail besprochen), aber sie müssen von fester Größe sein, wie `uint[] memory a = new uint[](5);`.

Array-Typen haben einige grundlegende Operationsmethoden, wie folgt:

```solidity
// Array-Typ definieren
uint[7] public arr;

// Daten hinzufügen
arr.push(7);

// Letztes Datenelement löschen
arr.pop();

// Daten an einem bestimmten Index löschen
delete arr[1];

// Array-Länge abrufen
uint len = arr.length;
```

#### Mapping

`mapping` ist ein Abbildungstyp, definiert mit `mapping(keyType => valueType)`, wobei der Schlüssel ein eingebauter Typ wie `bytes`, `int`, `string` oder Vertragstyp sein muss, während der Wert jeder Typ sein kann, wie z.B. verschachtelter `mapping`-Typ. Beachten Sie, dass `mapping`-Typen nicht iteriert werden können; wenn eine Iteration benötigt wird, müssen Sie den entsprechenden Index selbst implementieren.

Hier sind einige Operationen:

```solidity
// Verschachtelten Mapping-Typ definieren
mapping(string => mapping(string => string)) nestedMap;

// Wert setzen
nestedMap[id][key] = "0707";

// Wert lesen
string value = nestedMap[id][key];

// Wert löschen
delete nestedMap[id][key];
```

#### Struct

`struct` ist ein Strukturtyp. Für komplexe Geschäfte müssen wir oft unsere eigenen Strukturen definieren, um verwandte Daten zu kombinieren. Es kann innerhalb eines Vertrags definiert werden:

```solidity
contract Struct {
    struct Data {
        string id;
        string hash;
    }

    Data public data;

    // Daten hinzufügen
    function create(string calldata _id) public {
        data = Data{id: _id, hash: "111222"};
    }

    // Daten aktualisieren
    function update(string _id) public {
        // Daten abfragen
        string id = data.id;

        // Aktualisieren
        data.hash = "222333"
    }
}
```

Sie können auch alle erforderlichen Strukturtypen in einer separaten Datei definieren und sie nach Bedarf in den Vertrag importieren:

```solidity
// 'StructDeclaration.sol'

struct Data {
    string id;
    string hash;
}
```

```solidity
// 'Struct.sol'

import "./StructDeclaration.sol"

contract Struct {
    Data public data;
}
```

### Variablen, Konstanten und `Immutable`

Variablen sind Datenstrukturen in Solidity, deren Werte sich ändern können. Es gibt drei Typen:

- `local` Variablen
- `state` Variablen
- `global` Variablen

`local` Variablen werden innerhalb von Methoden definiert und werden nicht auf der Kette gespeichert, wie `string var = "Hello";`. `state` Variablen werden außerhalb von Methoden definiert und werden auf der Kette gespeichert. Sie werden als `string public var;` definiert. Das Schreiben eines Wertes sendet eine Transaktion, während das Lesen eines Wertes dies nicht tut. `global` Variablen sind globale Variablen, die Ketteninformationen bereitstellen, wie die aktuelle Block-Timestamp-Variable `uint timestamp = block.timestamp;` und die Vertragsaufrufer-Adressvariable `address sender = msg.sender;`.

Variablen können mit verschiedenen Schlüsselwörtern deklariert werden, um verschiedene Speicherorte anzuzeigen.

- `storage`: Auf der Kette gespeichert
- `memory`: Im Speicher, existiert nur, wenn die Methode aufgerufen wird
- `calldata`: Existiert, wenn als Parameter zum Aufruf einer Methode übergeben

Konstanten sind Variablen, deren Werte nicht geändert werden können. Die Verwendung von Konstanten kann Gasgebühren sparen. Wir können sie mit `string public constant MY_CONSTANT = "0707";` definieren. `immutable` ist ein spezieller Typ, dessen Wert im `constructor` initialisiert werden kann, aber nicht wieder geändert werden kann. Flexible Verwendung dieser Typen kann effektiv Gasgebühren sparen und Datensicherheit gewährleisten.

### Funktionen

In Solidity werden Funktionen verwendet, um spezifische Geschäftslogik zu definieren.

#### Berechtigungsdeklaration

Funktionen haben unterschiedliche Sichtbarkeiten, die mit verschiedenen Schlüsselwörtern deklariert werden:

- `public`: Kann von jedem Vertrag aufgerufen werden
- `private`: Kann nur innerhalb des Vertrags aufgerufen werden, der die Methode definiert hat
- `internal`: Kann nur in geerbten Verträgen aufgerufen werden
- `external`: Kann nur von anderen Verträgen und Konten aufgerufen werden

Vertragsfunktionen, die Daten abfragen, haben auch unterschiedliche Deklarationsmethoden:

- `view` kann Variablen lesen, aber nicht modifizieren
- `pure` kann weder Variablen lesen noch modifizieren

#### Funktionsmodifikatoren

`modifier` Funktionsmodifikatoren können vor/nach dem Ausführen einer Funktion aufgerufen werden, hauptsächlich verwendet für Zugriffssteuerung, Eingabeparametervalidierung und Verhinderung von Wiedereintrittangriffen. Diese drei Arten von Modifikatoren können mit der folgenden Syntax definiert werden:

```solidity
modifier onlyOwner() {
    require(msg.sender == owner, "Not owner");
    _;
}

modifier validAddress(address _addr) {
    require(_addr != address(0), "Not valid address");
    _;
}

modifier noReentrancy() {
    require(!locked, "No reentrancy");
    locked = true;
    _;
    locked = false;
}
```

Um Funktionsmodifikatoren zu verwenden, müssen Sie den entsprechenden Modifikator bei der Deklaration der Funktion hinzufügen, wie zum Beispiel:

```solidity
function changeOwner(address _newOwner) public onlyOwner validAddress(_newOwner) {
    owner = _newOwner;
}

function decrement(uint i) public noReentrancy {
    x -= i;

    if (i > 1) {
        decrement(i - 1);
    }
}
```

#### Funktionsselektor

Wenn eine Funktion aufgerufen wird, müssen die ersten vier Bytes der `calldata` angegeben werden, um zu bestätigen, welche Funktion aufgerufen werden soll. Dies wird als Funktionsselektor bezeichnet.

```solidity
addr.call(abi.encodeWithSignature("transfer(address,uint256)", 0xSomeAddress, 123))
```

Die ersten vier Bytes des Rückgabewerts von `abi.encodeWithSignature()` im obigen Code sind der Funktionsselektor. Wenn wir den Funktionsselektor vor der Ausführung vorberechnen, können wir einige Gasgebühren sparen.

```solidity
contract FunctionSelector {
    function getSelector(string calldata _func) external pure returns (bytes4) {
        return bytes4(keccak256(bytes(_func)));
    }
}
```

### Bedingungs- und Schleifenstrukturen

#### Bedingungen

Solidity verwendet die Schlüsselwörter `if`, `else if`, `else`, um bedingte Logik zu implementieren:

```solidity
if (x < 10) {
    return 0;
} else if (x < 20) {
    return 1;
} else {
    return 2;
}
```

Eine Kurzform kann auch verwendet werden:

```solidity
x < 20 ? 1 : 2;
```

#### Schleifen

Solidity verwendet die Schlüsselwörter `for`, `while`, `do while`, um Schleifenlogik zu implementieren, aber weil die letzten beiden dazu neigen, den `gas limit` Grenzwert zu erreichen, werden sie selten verwendet.

```solidity
for (uint i = 0; i < 10; i++) {
    // Geschäftslogik
}
```

```solidity
uint j;
while (j < 10) {
    j++;
}
```

### Verträge

#### Konstruktor

Der `constructor` von Solidity kann bei der Erstellung eines Vertrags ausgeführt werden, hauptsächlich zur Initialisierung verwendet.

```solidity
constructor(string memory _name) {
    name = _name;
}
```

Wenn es eine Vererbungsbeziehung zwischen Verträgen gibt, wird der `constructor` auch der Vererbungsreihenfolge folgen.

#### Schnittstelle

`Interface` wird verwendet, um mit Verträgen zu interagieren, indem Schnittstellen deklariert werden. Es hat folgende Anforderungen:

- Kann keine Methoden implementieren
- Kann von anderen Schnittstellen erben
- Alle Methoden müssen als `external` deklariert werden
- Kann keinen Konstruktor deklarieren
- Kann keine Zustandsvariablen deklarieren

Eine Schnittstelle wird mit der folgenden Syntax definiert:

```solidity
contract Counter {
    uint public count;

    function increment() external {
        count += 1;
    }
}

interface ICounter {
    function count() external view returns (uint);
    function increment() external;
}
```

Sie kann wie folgt aufgerufen werden:

```solidity
contract MyContract {
    function incrementCounter(address _counter) external {
        ICounter(_counter).increment();
    }

    function getCount(address _counter) external view returns (uint) {
        return ICounter(_counter).count();
    }
}
```

#### Vererbung

Solidity-Verträge unterstützen Vererbung und können gleichzeitig von mehreren Verträgen erben, indem sie das Schlüsselwort `is` verwenden.

Funktionen können überschrieben werden. Methoden, die geerbt werden sollen, sollten als `virtual` deklariert werden, und überschreibende Methoden sollten das Schlüsselwort `override` verwenden.

```solidity
// Elternvertrag A definieren
contract A {
    function foo() public pure virtual returns (string memory) {
        return "A";
    }
}
// Vertrag B erbt von Vertrag A und überschreibt die Funktion
contract B is A {
    function foo() public pure virtual override returns (string memory) {
        return "B";
    }
}

// Vertrag D erbt von Verträgen B und C und überschreibt die Funktion
contract D is B, C {
    function foo() public pure override(B, C) returns (string memory) {
        return super.foo();
    }
}
```

Es gibt einige Punkte zu beachten: Die Reihenfolge der Vererbung wird die Geschäftslogik beeinflussen, und `state`-Variablen können nicht geerbt werden.

Wenn ein Kindvertrag seinen Elternvertrag aufrufen möchte, kann er neben dem direkten Aufruf auch das Schlüsselwort `super` verwenden, wie folgt:

```solidity
contract B is A {
    function foo() public virtual override {
        // Direkter Aufruf
        A.foo();
    }

    function bar() public virtual override {
        // Aufruf mit dem super Schlüsselwort
        super.bar();
    }
}
```

#### Vertragserstellung

In Solidity können Sie einen anderen Vertrag von einem Vertrag aus mit dem Schlüsselwort `new` erstellen.

```solidity
function create(address _owner, string memory _model) public {
    Car car = new Car(_owner, _model);
    cars.push(car);
}
```

Nach Solidity 0.8.0 wird die `create2`-Funktion für die Erstellung von Verträgen unterstützt:

```solidity
function create2(address _owner, string memory _model, bytes32 _salt) public {
    Car car = (new Car){salt: _salt}(_owner, _model);
    cars.push(car);
}
```

#### Importieren von Verträgen/externen Bibliotheken

In komplexen Geschäftsszenarien benötigen wir oft mehrere Verträge, die zusammenarbeiten. In diesem Fall können wir das Schlüsselwort `import` verwenden, um Verträge zu importieren. Es gibt zwei Möglichkeiten: lokaler Import `import "./Foo.sol";` und externer Import `import "https://github.com/owner/repo/blob/branch/path/to/Contract.sol";`.

Externe Bibliotheken ähneln Verträgen, können aber keine Zustandsvariablen deklarieren und keine Assets senden. Wenn alle Methoden der Bibliothek `internal` sind, werden sie in den Vertrag eingebettet. Wenn sie nicht `internal` sind, muss die Bibliothek im Voraus bereitgestellt und verknüpft werden.

```solidity
library SafeMath {
    function add(uint x, uint y) internal pure returns (uint) {
        uint z = x + y;
        require(z >= x, "uint overflow");
        return z;
    }
}
```

```solidity
contract TestSafeMath {
    using SafeMath for uint;
}
```

#### Ereignisse

Der Ereignismechanismus ist ein sehr wichtiges Design in Verträgen. Ereignisse ermöglichen es, Informationen auf der Blockchain zu protokollieren, und Anwendungen wie DApps können Geschäftslogik implementieren, indem sie Ereignisdaten abhören, mit sehr geringen Speicherkosten. Hier ist ein einfacher Protokollierungsmechanismus:

```solidity
// Ereignis definieren
event Log(address indexed sender, string message);
event AnotherLog();

// Ereignis auslösen
emit Log(msg.sender, "Hello World!");
emit Log(msg.sender, "Hello EVM!");
emit AnotherLog();
```

Bei der Definition eines Ereignisses können Sie das Attribut `indexed` übergeben, aber höchstens drei. Nach dem Hinzufügen können Sie die Parameter dieses Attributs filtern, `var event = myContract.transfer({value: ["99","100","101"]});`.

### Fehlerbehandlung

Die On-Chain-Fehlerbehandlung ist auch ein wichtiger Teil des Vertragsschreibens. Solidity kann Fehler auf folgende Weise werfen.

`require` wird verwendet, um Bedingungen vor der Ausführung zu überprüfen, und wenn sie nicht erfüllt sind, wird eine Ausnahme geworfen.

```solidity
function testRequire(uint _i) public pure {
    require(_i > 10, "Input must be greater than 10");
}
```

`revert` wird verwendet, um Fehler zu markieren und Rollbacks durchzuführen.

```solidity
function testRevert(uint _i) public pure {
    if (_i <= 10) {
        revert("Input must be greater than 10");
    }
}
```

`assert` erfordert, dass die Bedingung erfüllt sein muss.

```solidity
function testAssert() public view {
    assert(num == 0);
}
```

Beachten Sie, dass in Solidity, wenn ein Fehler auftritt, alle Zustandsänderungen, die in der Transaktion aufgetreten sind, rückgängig gemacht werden, einschließlich aller Assets, Konten, Verträge usw.

`try / catch` kann auch Fehler abfangen, kann aber nur Fehler von externen Funktionsaufrufen und Vertragserstellungen abfangen.

```solidity
event Log(string message);
event LogBytes(bytes data);

function tryCatchNewContract(address _owner) public {
    try new Foo(_owner) returns (Foo foo) {
        emit Log("Foo created");
    } catch Error(string memory reason) {
        emit Log(reason);
    } catch (bytes memory reason) {
        emit LogBytes(reason);
    }
}
```

### `payable` Schlüsselwort

Wir können Methoden so einstellen, dass sie `ether` von Verträgen empfangen, indem wir das `payable` Schlüsselwort deklarieren.

```solidity
// Adresstyp kann als payable deklariert werden
address payable public owner;

constructor() payable {
    owner = payable(msg.sender);
}

// Methode als payable deklarieren, um Ether zu empfangen
function deposit() public payable {}
```

### Interaktion mit `Ether`

Die Interaktion mit `Ether` ist ein wichtiges Anwendungsszenario für Smart Contracts, hauptsächlich in Sende- und Empfangsteile unterteilt, die jeweils durch verschiedene Methoden implementiert werden.

#### Senden

Hauptsächlich durch die Methoden `transfer`, `send` und `call` implementiert. Unter ihnen wurde `call` für die Verteidigung gegen Wiedereintrittangriffe optimiert und wird für die Verwendung in tatsächlichen Anwendungsszenarien empfohlen (wird aber im Allgemeinen nicht verwendet, um andere Funktionen aufzurufen).

```solidity
contract SendEther {
  function sendViaCall(address payable _to) public payable {
    (bool sent, bytes memory data) = _to.call{value: msg.value}("");
    require(sent, "Failed to send Ether");
  }
}
```

Wenn Sie eine andere Funktion aufrufen müssen, wird im Allgemeinen `delegatecall` verwendet.

```solidity
contract B {
    uint public num;
    address public sender;
    uint public value;

    function setVars(uint _num) public payable {
        num = _num;
        sender = msg.sender;
        value = msg.value;
    }
}

contract A {
    uint public num;
    address public sender;
    uint public value;

    function setVars(address _contract, uint _num) public payable {
        (bool success, bytes memory data) = _contract.delegatecall(
            abi.encodeWithSignature("setVars(uint256)", _num)
        );
    }
}
```

#### Empfangen

Der Empfang von `Ether` verwendet hauptsächlich zwei Methoden: `receive() external payable` und `fallback() external payable`.

Wenn eine Funktion, die keine Parameter akzeptiert und keine Parameter zurückgibt, wenn `Ether` an einen Vertrag gesendet wird, aber die `receive()` Methode nicht implementiert ist oder `msg.data` nicht leer ist, wird die `fallback()` Methode aufgerufen.

```solidity
contract ReceiveEther {

    // Wenn msg.data leer ist
    receive() external payable {}

    // Wenn msg.data nicht leer ist
    fallback() external payable {}

    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}
```

### Gasgebühren

Die Ausführung von Transaktionen in der EVM erfordert Gasgebühren. `gas spent` gibt an, wie viel Gas-Menge benötigt wird, `gas price` ist der Einheitspreis von Gas, `Ether` und `Wei` sind Preiseinheiten, 1 ether == 1e18 wei.

Verträge werden Gas begrenzen. `gas limit` wird vom Benutzer festgelegt, der die Transaktion initiiert, und gibt die maximale Menge an Gas an, die ausgegeben werden soll. `block gas limit` wird vom Blockchain-Netzwerk bestimmt und gibt die maximale Menge an Gas an, die in diesem Block erlaubt ist.

Bei der Vertragsentwicklung sollten wir besonders darauf achten, so weit wie möglich Gasgebühren zu sparen. Hier sind einige gängige Techniken:

1. Verwenden Sie `calldata` anstelle von `memory`
2. Laden Sie Zustandsvariablen in den Speicher
3. Verwenden Sie `i++` anstelle von `++i`
4. Zwischenspeichern Sie Array-Elemente

```solidity
function sumIfEvenAndLessThan99(uint[] calldata nums) external {
    uint _total = total;
    uint len = nums.length;

    for (uint i = 0; i < len; ++i) {
        uint num = nums[i];
        if (num % 2 == 0 && num < 99) {
            _total += num;
        }
    }

    total = _total;
}
```

## Fazit

Das oben Genannte ist der erste Artikel in unserer Serie, der die Grundlagen von Solidity behandelt. Nachfolgende Artikel werden sich auf das Lernen und Zusammenfassen seiner gängigen Anwendungen und praktischen Codiertechniken konzentrieren. Wir freuen uns auf Ihre weitere Aufmerksamkeit.

## Referenzen

> 1. [Solidity by Example](https://solidity-by-example.org)
> 2. [Ethereum Blockchain! Einführung in Smart Contracts und dezentrale Webanwendungen (dApps)](http://gasolin.idv.tw/learndapp/)
> 3. [Blockchain Beginner's Guide](https://www.pseudoyu.com/blockchain-guide/)
> 4. [Uright - Blockchain Music Copyright Management ÐApp](https://github.com/pseudoyu/uright)