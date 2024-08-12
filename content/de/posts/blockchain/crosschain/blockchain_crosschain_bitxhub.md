---
title: "BitXHub Cross-chain Plugin (Fabric) Quellcode-Analyse"
date: 2021-09-09T15:14:26+08:00
draft: false
tags: ["blockchain", "crosschain", "bitxhub", "hyperledger fabric", "go"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Vorwort

Ich habe zuvor erwähnt, dass die BitXHub Cross-Chain-Plattform von QulianTech eine relativ umfassende Open-Source-Cross-Chain-Lösung in der Branche ist. Sie optimiert hauptsächlich die Funktionalität, Sicherheit und Flexibilität des Cross-Chain-Prozesses durch Relay-Chain-, Gateway- und Plugin-Mechanismen.

Derzeit arbeitet unser Unternehmensteam an einem Cross-Chain-Modul für eine BaaS-Plattform. Ich bin für den Cross-Chain-Adapter-Teil verantwortlich, der dem Listening-Modul und dem Anwendungskettenmodul in der BitXHub-Plattform entspricht. Der Adapter wird Cross-Chain-Ereignisse auf der Anwendungskette überwachen und die entsprechenden Parameter an das Gateway für geschäftslogische Anforderungen im Zusammenhang mit Cross-Chain weiterleiten.

Daher plane ich, eine eingehende Analyse des Quellcodes des BitXHub [meshplus/pier-client-fabric](https://github.com/meshplus/pier-client-fabric) Plugins durchzuführen, um seine hervorragende Codestruktur und funktionalen Module zu verstehen und so meine eigene Adapter-Funktionalität besser implementieren zu können.

## Cross-Chain-Transaktionsprozess

![cross_chain_plugin](https://image.pseudoyu.com/images/cross_chain_plugin.png)

Gemäß den Anforderungen des Cross-Chain-Geschäfts ist ein typischer Cross-Chain-Aufrufprozess im obigen Diagramm dargestellt.

1. Die Unterkette, die Cross-Chain-Transaktionen durchführen muss, muss den Adapter installieren und den bereitgestellten Cross-Chain-Vertrag und Geschäftsvertrag bereitstellen
2. Wenn ein Benutzer den Geschäftsvertrag über das SDK aufruft, ruft der Vertrag den Cross-Chain-Vertrag auf und löst ein Cross-Chain-Ereignis aus
3. Der entsprechende Adapter der Unterkette wird die vom Cross-Chain-Vertrag ausgelösten Cross-Chain-Ereignisse abfragen oder abonnieren und an das Listening-Modul des Cross-Chain-Gateways senden
4. Das Cross-Chain-Gateway wird die aus dem Cross-Chain-Ereignis extrahierte Antwortvormethode und Parameter in eine für die Zielunterkette erkennbare Transaktion umwandeln
5. Das Cross-Chain-Gateway wird die konvertierte Transaktion an die Zielunterkette übermitteln und ausführen

## Adapter-Mechanismus

### Schnittstellendesign

Der Adapter ist hauptsächlich für die Interaktion zwischen Unterketten verantwortlich und nimmt durch Schnittstellenaufrufe an Cross-Chain-Interaktionen teil. Er stellt hauptsächlich die folgenden Schnittstellen bereit.

#### Chaincode aufrufen

Der Adapter empfängt vom Cross-Chain-Gateway gesendete Transaktionsparameter, kapselt sie in eine von der angepassten Unterkette akzeptierte Datenstruktur und ruft den Chaincode auf.

#### Cross-Chain-Transaktion abfragen

Die Unterkette speichert cross-chain-bezogene Details im Payload-Feld, wie zum Beispiel Vertrag, Benutzer usw. Der Adapter analysiert und kapselt diese Informationen und stellt entsprechende Schnittstellen für das Cross-Chain-Gateway zur Abfrage bereit.

#### Historische Transaktionsinformationen abfragen

Der Adapter muss eine Abfrageschnittstelle für historische Transaktionen bereitstellen, um aktiv abzufragen, wenn aufgrund von Netzwerkübertragung oder anderen Gründen keine Cross-Chain-Ereignisse empfangen werden.

#### Grundlegende Informationen der Anwendungskette abfragen

Der Adapter muss eine Abfrageschnittstelle für Informationen im Zusammenhang mit seiner angepassten Unterkette für das Cross-Chain-Gateway zur Abfrage bereitstellen, wie zum Beispiel Name, Typ usw.

## Quellcode-Analyse

Als Nächstes werden wir den Quellcode des funktionalen Kernmoduls des BitXHub Cross-Chain-Plugins (Fabric) analysieren.

### Entwurfsmuster

Das Plugin-Projekt verwendet ein typisches "Producer-Consumer"-Modell, das sehr gut für nebenläufige Szenarien geeignet ist, die Daten abfragen/abonnieren müssen. Dieses Modell nutzt die Eigenschaft, dass zu jedem Zeitpunkt nur eine Goroutine auf bestimmte Daten im Kanal zugreift.

#### Cross-Chain-Ereignisse abonnieren/abfragen

Das Plugin muss ein Producer-Objekt konstruieren, um Cross-Chain-Ereignisse seiner entsprechenden Unterkette zu abonnieren.

```go
// Produzent konstruieren
ec, err := event.New(c.channelProvider, event.WithBlockEvents())
if err != nil {
    return fmt.Errorf("failed to create fabcli, error: %v", err)
}

c.eventClient = ec

// Cross-Chain-Ereignisse abonnieren
registration, notifier, err := ec.RegisterChaincodeEvent(c.meta.CCID, c.meta.EventFilter)
if err != nil {
    return fmt.Errorf("failed to register chaincode event, error: %v", err)
}
c.registration = registration
```

Die Methode zum Abonnieren von Ereignissen besteht darin, die `RegisterChaincodeEvent()`-Methode von `fabric-sdk-go` aufzurufen. Es ist wichtig zu beachten, dass Sie die `Unregister()`-Methode aufrufen sollten, um das Abonnement zu kündigen, wenn Sie keine Ereignisse mehr abhören müssen.

Die `ccID` in der Methode ist die zu überwachende Chaincode-ID, `eventFilter` ist das zu überwachende Chaincode-Ereignis, und diese Methode gibt einen Kanal zum Empfangen von Daten zurück (wenn das Abonnement gekündigt wird, wird der Kanal geschlossen).

```go
func (c *Client) RegisterChaincodeEvent(ccID, eventFilter string) (fab.Registration, <-chan *fab.CCEvent, error) {
	return c.eventService.RegisterChaincodeEvent(ccID, eventFilter)
}
```

Platzieren Sie sowohl das Objekt, das den Cross-Chain-Vertrag abonniert hat (d.h. den Produzenten), als auch den Verbraucher in einer Endlosschleife. Wenn ein Cross-Chain-Ereignis ausgelöst wird, wird der Produzent kontinuierlich Daten in den Kanal legen, und der Verbraucher wird kontinuierlich Daten aus dem Kanal entnehmen.

```go
go func() {
    for {
        select {
        // Produzent schreibt Cross-Chain-Ereignisse in den Kanal
        case ccEvent := <-notifier:
            if ccEvent != nil {
                c.handle(ccEvent)
            }
        // Verbraucher entnimmt Cross-Chain-Ereignisdaten aus dem Kanal
        case <-c.ctx:
            return
        }
    }
}()
```

Da sich sowohl der Produzent als auch der Verbraucher in einer Endlosschleife befinden, wird die Goroutine des Produzenten nicht beendet, und der Kanal schreibt weiterhin Daten. Wenn es keine neuen Ereignisse gibt, wird der Verbraucher blockieren und darauf warten, dass der Produzent neue Daten empfängt und in den Kanal schreibt.

### Plugin-Initialisierung, Ausführung und Schließung

Nachdem wir das gesamte Entwurfsmuster betrachtet haben, werfen wir einen Blick auf den Mechanismus, wie das gesamte Plugin-Projekt vom Haupteinstiegspunkt des Programms aus läuft.

#### Initialisierung

Bei der Initialisierung des Client-Programms wird zunächst ein Verbraucher-Objekt gemäß einer benutzerdefinierten Struktur konstruiert.

```go
// Verbraucher konstruieren
mgh, err := newFabricHandler(contractmeta.EventFilter, eventC, appchainID)
if err != nil {
    return err
}

done := make(chan bool)
csm, err := NewConsumer(configPath, contractmeta, mgh, done)
if err != nil {
    return err
}
```

#### Ausführung

Der Einstiegspunkt für die Programmausführung ist einfach, es wird nur der Cross-Chain-Vertrag abgefragt und das Verbraucher-Objekt gestartet.

```go
func (c *Client) Start() error {
	logger.Info("Fabric consumer started")
	go c.polling()
	return c.consumer.Start()
}
```

#### Schließung

Das Schließen des Plugins ist ebenfalls einfach, es stoppt nur die Programmausführung und meldet sich von den Ereignissen ab.

```go
// Plugin schließen
func (c *Client) Stop() error {
	c.ticker.Stop()
	c.done <- true
	return c.consumer.Shutdown()
}
```

Abmeldung von Ereignissen im Verbraucher-Paket.

```go
func (c *Consumer) Shutdown() error {
	c.eventClient.Unregister(c.registration)
	return nil
}
```

Bei genauerer Betrachtung ruft das Abmelden von Ereignissen die `Unregister()`-Methode von `fabric-sdk-go` auf, die das Abonnement für dieses Ereignis kündigt und den entsprechenden Kanal schließt.

```go
func (c *Client) Unregister(reg fab.Registration) {
	c.eventService.Unregister(reg)
}
```

### Schnittstellenimplementierung

Neben dem Abonnieren und Überwachen von Ereignissen stellt das Plugin auch eine Reihe von Abfrageschnittstellen für den Gateway bereit, um entsprechende Cross-Chain-Operationen durchzuführen.

#### getProof()

Zum Beispiel das Abrufen von Proof-Informationen usw.

```go
func (c *Client) getProof(response channel.Response) ([]byte, error) {
	var proof []byte
	var handle = func(response channel.Response) ([]byte, error) {
		// Proof von Fabric abfragen
		l, err := ledger.New(c.consumer.channelProvider)
		if err != nil {
			return nil, err
		}

		t, err := l.QueryTransaction(response.TransactionID)
		if err != nil {
			return nil, err
		}
		pd := &common.Payload{}
		if err := proto.Unmarshal(t.TransactionEnvelope.Payload, pd); err != nil {
			return nil, err
		}

		pt := &peer.Transaction{}
		if err := proto.Unmarshal(pd.Data, pt); err != nil {
			return nil, err
		}

		return pt.Actions[0].Payload, nil
	}

	if err := retry.Retry(func(attempt uint) error {
		var err error
		proof, err = handle(response)
		if err != nil {
			logger.Error("Can't get proof", "error", err.Error())
			return err
		}
		return nil
	}, strategy.Wait(2*time.Second)); err != nil {
		logger.Error("Can't get proof", "error", err.Error())
	}

	return proof, nil
}
```

#### getChainID()

Diese Schnittstelle wird verwendet, um die Chain-ID zu erhalten

```go
func (c *Client) GetChainID() (string, string) {
	request := channel.Request{
		ChaincodeID: c.meta.CCID,
		Fcn:         GetChainId,
	}

	response, err := c.consumer.ChannelClient.Execute(request)
	if err != nil || response.Payload == nil {
		return "", ""
	}
	chainIds := strings.Split(string(response.Payload), "-")
	if len(chainIds) != 2 {
		return "", ""
	}
	return chainIds[0], chainIds[1]
}
```

#### Andere Schnittstellen

Für weitere Details zur Schnittstellenimplementierung, siehe [meshplus/pier-client-fabric/client.go](https://github.com/meshplus/pier-client-fabric/blob/master/client.go).

### Cross-Chain-Vertrag

Der Cross-Chain-Vertrag ist ein wichtiger Teil der Implementierung der Plugin-Überwachung. Wenn das Geschäft Cross-Chain benötigt, wird es einheitlich den Cross-Chain-Vertrag aufrufen und mit dem Cross-Chain-Gateway interagieren.

Der Cross-Chain-Vertrag stellt eine Reihe von Schnittstellen für Geschäftsverträge zur Implementierung bereit. Daher kann das Schreiben von Geschäftsverträgen nach bestimmten Spezifikationen die Entwicklung und Wartung von Cross-Chain-Geschäften vereinfachen. Für Details zum Schreiben von Cross-Chain-Verträgen, siehe <[Dokumentation zum Schreiben von Cross-Chain-Verträgen](https://github.com/meshplus/bitxhub/wiki/跨链合约编写文档)>.

#### Ereignisimplementierung

Wie wirft der Cross-Chain-Vertrag Cross-Chain-Ereignisse an das Plugin?

In der `Invoke()`-Methode des Cross-Chain-Vertrags erhält der Cross-Chain-Vertrag zunächst die Aufrufmethode und die entsprechenden Parameter des Vertragsaufrufers (d.h. des Geschäftsvertrags) durch die `GetFunctionAndParameters()`-Methode und ruft dann verschiedene Verträge auf, indem er den Methodennamen beurteilt.

```go
func (broker *Broker) Invoke(stub shim.ChaincodeStubInterface) pb.Response {
	function, args := stub.GetFunctionAndParameters()
    // ...
    	switch function {
            // ...
            case "getChainId":
                return broker.getChainId(stub)
            case "getInMessage":
                return broker.getInMessage(stub, args)
            case "getOutMessage":
                return broker.getOutMessage(stub, args)
            // ...
            case "EmitInterchainEvent":
                return broker.EmitInterchainEvent(stub, args)
            default:
                return shim.Error("invalid function: " + function + ", args: " + strings.Join(args, ","))
	}
}

func (broker *Broker) EmitInterchainEvent(stub shim.ChaincodeStubInterface, args []string) pb.Response {
    // Prüfen, ob die Anzahl der Eingabeparameter korrekt ist
    // Cross-Chain-Verträge müssen viele Parameter übergeben, da Aufruffehler leicht zu Sicherheitsproblemen in der Kette führen können
	if len(args) != 5 {
		return shim.Error("incorrect number of arguments, expecting 7")
	}

	// Parameter lesen und in entsprechenden Variablen speichern

	// Zielketten-ID
	dstServiceID := args[0]

	// Eigene Chaincode-ID
	cid, err := getChaincodeID(stub)
	if err != nil {
		return shim.Error(err.Error())
	}

	// bxhID und appchainID abrufen
	curFullID, err := broker.genFullServiceID(stub, cid)
	if err != nil {
		return shim.Error(err.Error())
	}

	// Aktuelle Ketten-ID und Zielketten-ID zu einer Ausgabe-Cross-Chain-Dienstgruppe kombinieren
	outServicePair := genServicePair(curFullID, dstServiceID)

	// Key-Value-Paare der Ausgabewerte abrufen
	outMeta, err := broker.getMap(stub, outterMeta)
	if err != nil {
		return shim.Error(err.Error())
	}

	// Prüfen, ob die Ausgabe-Cross-Chain-Dienstgruppe im Key-Value-Paar vorhanden ist, wenn nicht, auf 0 setzen
	if _, ok := outMeta[outServicePair]; !ok {
		outMeta[outServicePair] = 0
	}

	// Transaktionsinformationen kapseln
	tx := &Event{
		Index:     outMeta[outServicePair] + 1,
		DstFullID: dstServiceID,
		SrcFullID: curFullID,
		Func:      args[1],
		Args:      args[2],
		Argscb:    args[3],
		Argsrb:    args[4],
	}

	// Ausgabedienst selbst inkrementieren
	outMeta[outServicePair]++

	// Transaktionsinformationen in JSON-Format umwandeln
	txValue, err := json.Marshal(tx)
	if err != nil {
		return shim.Error(err.Error())
	}

	// Ausgabe-Ereignisnachricht formatieren
	key := broker.outMsgKey(outServicePair, strconv.FormatUint(tx.Index, 10))

	// Nachricht und Transaktionsinformationen in das Ledger schreiben (Persistenz)
	if err := stub.PutState(key, txValue); err != nil {
		return shim.Error(fmt.Errorf("persist event: %w", err).Error())
	}

	// Den entsprechenden Cross-Chain-Transaktionsereignisnamen setzen und die Transaktionsinformationen im Payload speichern
	if err := stub.SetEvent(interchainEventName, txValue); err != nil {
		return shim.Error(fmt.Errorf("set event: %w", err).Error())
	}

	// Metadaten-Status in das Ledger schreiben
	if err := broker.putMap(stub, outterMeta, outMeta); err != nil {
		return shim.Error(err.Error())
	}

	return shim.Success(nil)
}
```

Dies geschieht beim Aufrufen des Cross-Chain-Vertrags. Im Wesentlichen setzt er nur ein Ereignis-Trigger durch `SetEvent()` im Cross-Chain-Vertrag und abonniert und überwacht es dann im Plugin durch `RegisterChaincodeEvent()`.

```go
SetEvent(name string, payload []byte) error
```

`SetEvent()` ist eine Schnittstelle unter dem `shim`-Paket, die hauptsächlich Name und Payload-Array übergibt. Für Details zu den Prinzipien und Details der Chaincode-Ereignisüberwachung, siehe <[Hyperledger Fabric Go SDK Ereignisanalyse](https://www.pseudoyu.com/de/2021/09/01/blockchain_hyperledger_fabric_gosdk_event/)>.

### Geschäftsvertrag

Nachdem wir den Cross-Chain-Vertrag analysiert haben, lassen Sie uns sehen, wie der Geschäftsvertrag den Cross-Chain-Vertrag aufruft, wobei wir den Datenaustauschvertrag `data_swapper.go` im Beispiel als Instanz nehmen.

```go
func (s *DataSwapper) get(stub shim.ChaincodeStubInterface, args []string) pb.Response {
	switch len(args) {
	case 1:
		// args[0]: key
		value, err := stub.GetState(args[0])
		if err != nil {
			return shim.Error(err.Error())
		}

		return shim.Success(value)
	case 2:
		// args[0]: Ziel-Service-ID
		// args[1]: key
		b := util.ToChaincodeArgs(emitInterchainEventFunc, args[0], "interchainGet,interchainSet,", args[1], args[1], "")
		response := stub.InvokeChaincode(brokerContractName, b, channelID)
		if response.Status != shim.OK {
			return shim.Error(fmt.Errorf("invoke broker chaincode %s error: %s", brokerContractName, response.Message).Error())
		}

		return shim.Success(nil)
	default:
		return shim.Error("incorrect number of arguments")
	}
}
```

Um Informationen von anderen Ketten im Geschäftsvertrag `data_swapper.go` zu erhalten, beurteilt es zunächst die Länge des Eingabeparameter-Arrays `args []string` durch `switch...case...`, wenn die `get`-Methode aufgerufen wird. Wenn die Länge 1 ist, ruft es normal seinen eigenen Vertrag zur Abfrage auf, und wenn die Länge 2 ist, verwendet es zuerst die von Fabric bereitgestellte `ToChaincodeArgs()`-Methode, um die Parameter von `string` in das Chaincode-Parameter-Array-Format zu konvertieren.

```go
func ToChaincodeArgs(args ...string) [][]byte {
	bargs := make([][]byte, len(args))
	for i, arg := range args {
		bargs[i] = []byte(arg)
	}
	return bargs
}
```

Dann ruft es direkt den Cross-Chain-Vertrag durch die `InvokeChaincode()`-Methode im Geschäfts-Chaincode auf und übergibt Parameter und Kanal-ID, wodurch ein Cross-Chain-Datenabfrage-Chaincode-Aufruf abgeschlossen wird.

## Fazit

Das oben Genannte ist eine Analyse des Cross-Chain-Transaktionsprozesses und des BitXHub Cross-Chain-Plugin (Fabric) Quellcodes. Ich hoffe, dass ich durch diesen Prozess mein Verständnis für Cross-Chain-Mechanismen und verwandte Plattformen vertiefen und in Zukunft besser an deren Open-Source-Aufbau teilnehmen kann.

## Referenzen

> 1. [Cross-chain Technology Platform BitXHub](https://github.com/gocn/opentalk/tree/main/PhaseTen_BitXHub)
> 2. [BitXHub Document](https://meshplus.github.io/bitxhub/bitxhub/introduction/summary/)
> 3. [meshplus/pier-client-fabric](https://github.com/meshplus/pier-client-fabric)
> 4. [Ten Questions about BitXHub: Discussing the Architecture Design of Cross-chain Platforms](https://tech.hyperchain.cn/bitxhub-design-thinking/)
> 5. [Cross-chain Contract Writing Documentation](https://github.com/meshplus/bitxhub/wiki/跨链合约编写文档)
> 6. [Hyperledger Fabric Go SDK Event Analysis](https://www.pseudoyu.com/de/2021/09/01/blockchain_hyperledger_fabric_gosdk_event/)