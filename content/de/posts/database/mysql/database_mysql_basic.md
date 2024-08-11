---
title: "MySQL-Grundlagen und Praxis"
date: 2021-03-29T00:12:17+08:00
draft: false
tags: ["database", "mysql", "programming", "work practice series", "work", "practice", "backend"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Vorwort

Datenbanken werden sowohl in grundlegenden Lernszenarien als auch in realen Unternehmensanwendungen häufig eingesetzt. Es gibt oft den Scherz, dass die tägliche Arbeit immer um CRUD-Operationen kreist. Die Beherrschung der Verwendung gängiger relationaler Datenbanken ist eine grundlegende Fähigkeit für Entwickler. Dieser Artikel bietet einen Überblick über die grundlegenden Kenntnisse und zugehörigen Operationen von MySQL, einer beliebten relationalen Datenbank, auf dem MacOS-System zur einfachen Referenz.

## Überblick über Daten und Datenbanken

### Daten

Grundsätzlich sind Daten eine Art von Fakten oder beobachteten Ergebnissen, eine logische Zusammenfassung objektiver Sachverhalte und eine Form und ein Träger von Informationen. Menschen haben seit der Antike Daten verwaltet (noch bevor der Begriff existierte), zunächst durch manuelle Verwaltung, später durch Dateisysteme (wie Bibliotheken, die verschiedene Informationen nach Kategorien verwalten) und schließlich mit der Entwicklung der Computertechnologie die bequemere und effizientere Form der Datenbankverwaltung gebildet.

### Datenbank

Eine Datenbank ist ein Repository, das Daten nach einer bestimmten Datenstruktur organisiert, speichert und verwaltet. Ihre Hauptmerkmale sind:

- Strukturiert
- Teilbar
- Geringe Redundanz
- Hohe Unabhängigkeit
- Leicht erweiterbar

Es ist leicht zu verstehen, dass Daten, die nach verschiedenen Beziehungen/Strukturen organisiert sind, unterschiedliche Eigenschaften haben und für verschiedene Anwendungsszenarien geeignet sind. Derzeit gibt es hauptsächlich drei Typen: hierarchische Datenbanken, Netzwerkdatenbanken und relationale Datenbanken. MySQL, auf das wir uns konzentrieren werden, ist eine relationale Datenbank.

### Datenbankmanagementsystem (DBMS)

Ein Datenbankmanagementsystem (DBMS) ist ein System, das verschiedene Operationen an Datenbanken durchführt. Es hat Kernfunktionen wie das Erstellen und Warten von Datenbanken, das Organisieren und Verwalten der Datenspeicherung, die Kontrolle von Datenbanken, das Definieren von Daten, die Manipulation von Daten und die Verwaltung der Kommunikation zwischen Daten. Verschiedene Datenbankmanagementsysteme behandeln Datenbanken und Daten unterschiedlich, und die Methoden der Datenpräsentation variieren ebenfalls. Die Wahl des Datenbankmanagementsystems muss oft auf der Grundlage von Datenumfang, Geschäftsanforderungen und anderen Szenarien getroffen werden. Beispielsweise kann bei massiven Daten und hochparallelen Datenles- und -schreibvorgängen die Leistung relationaler Datenbanken erheblich nachlassen.

## Relationales Datenbankmanagementsystem (RDBMS)

### Hauptmerkmale

Relationale Datenbanken präsentieren Daten hauptsächlich in Form von Tabellen, wobei jede Zeile ein Datensatz ist und jede Spalte das dem Datensatznamen entsprechende Datenfeld. Viele Zeilen und Spalten bilden eine einzelne Tabelle, und mehrere einzelne Tabellen bilden eine Datenbank. Benutzer/Systeme fragen die Datenbank über SQL (Structured Query Language) ab.

Einige relationale Datenbankoperationen haben transaktionale Eigenschaften, nämlich die ACID-Regeln:

- Atomarität
- Konsistenz
- Isolation
- Dauerhaftigkeit

Atomarität bedeutet, dass eine Reihe von Transaktionsoperationen entweder alle abgeschlossen werden oder alle fehlschlagen; es gibt keine Situation, in der nur ein Teil abgeschlossen wird. Zum Beispiel würde in einem Banküberweisungsszenario, nachdem die Überweisung erfolgt ist, der Saldo des Absenders abnehmen, und wenn ein Datenbankoperationsfehler auftritt und der Saldo des Empfängers nicht zunimmt, würde dies ernsthafte Probleme verursachen.

Konsistenz bedeutet, dass nach Abschluss einer Transaktion die Daten in der gesamten Datenbank konsistent sind und es keine Situationen geben sollte, in denen dieselben Daten innerhalb der Datenbank nicht synchronisiert sind.

Isolation bedeutet, dass verschiedene Transaktionen unabhängig und ohne Störungen ablaufen sollten. Dies opfert natürlich etwas Effizienz, bietet aber bessere Garantien für die Datengenauigkeit.

Dauerhaftigkeit bedeutet, dass die Änderungen einer Transaktion an der Datenbank und ihre Auswirkungen auf das System dauerhaft sind, wenn sie abgeschlossen ist.

### Datenintegrität

Datenintegrität ist eine entscheidende Anforderung und Eigenschaft von Datenbanken und bezieht sich auf die Konsistenz und Zuverlässigkeit der in der Datenbank gespeicherten Daten. Sie wird hauptsächlich in vier Typen unterteilt:

- Entitätsintegrität
- Domänenintegrität
- Referenzielle Integrität
- Benutzerdefinierte Integrität

Entitätsintegrität erfordert, dass jede Datentabelle einen eindeutigen Identifikator hat und das Primärschlüsselfeld in jeder Tabelle weder null noch doppelt sein darf, was hauptsächlich bedeutet, dass alle Daten in der Tabelle eindeutig unterschieden werden können.

Domänenintegrität besteht darin, einige zusätzliche Einschränkungen für die Spalten in der Tabelle vorzunehmen, wie die Einschränkung von Datentypen, Prüfbedingungen, Festlegung von Standardwerten, ob Nullwerte erlaubt sind und Wertebereich usw.

```sql
--- Einschränkung der Feldeinzigartigkeit bei der Tabellenerstellung
create table person (
    id int not null auto_increment primary key,
    name varchar(30),
    id_number varchar(18) unique
);
```

Referenzielle Integrität bedeutet, dass die Datenbank nicht zulässt, dass auf nicht existierende Entitäten verwiesen wird. Tabellen in der Datenbank haben oft einige Assoziationen mit anderen Tabellen, und die referenzielle Integrität kann durch Fremdschlüsselbeschränkungen sichergestellt werden.

Benutzerdefinierte Integrität besteht darin, einige semantische Beschränkungen für Daten gemäß spezifischen Anwendungsszenarien und beteiligten Daten festzulegen, wie zum Beispiel, dass der Kontostand nicht negativ sein kann usw. Sie wird im Allgemeinen durch die Festlegung von Regeln, gespeicherten Prozeduren und Triggern eingeschränkt und beschränkt.

### Gängige RDBMS

Derzeit umfassen die gängigen relationalen Datenbankmanagementsysteme:

- SQL Server
- Sybase
- DB2
- Oracle
- MySQL

Oracle und MySQL sind die beiden am häufigsten von Unternehmen und Einzelpersonen verwendeten. Im Folgenden wird eine detaillierte Erklärung der Operationen am Beispiel von MySQL gegeben.

## MySQL

### Installation und Start

MySQL ist ein beliebtes kleines Datenbanksystem, das von Sun Microsystems (später von Oracle Corporation übernommen) entwickelt und gewartet wird. Aufgrund seiner geringen Größe und schnellen Datenoperationen wird es von vielen kleinen und mittleren Unternehmen/Websites übernommen und verfügt über ein relativ vollständiges Entwicklungs- und Wartungsökosystem.

Für einzelne Benutzer, die lernen möchten, es zu verwenden, können Sie die Community-Version (Open Source) herunterladen, um eine lokale Umgebung einzurichten. Sie können je nach System verschiedene Versionen wählen, und es gibt auch eine bequeme grafische Benutzeroberfläche zum Starten, Stoppen, Neustarten des Dienstes und zum Vornehmen verwandter Konfigurationen. Dieser Artikel nimmt `MySQL 8.0.21` auf dem MacOS-System als Beispiel. Nach der Installation und grundlegenden Einrichtung können Sie den lokalen MySQL-Dienst verwalten. Die Version kann leicht unterschiedlich sein, aber die Kernfunktionalitäten unterscheiden sich nicht wesentlich.

#### Grafische Benutzeroberfläche

Öffnen Sie die Systemeinstellungen, und Sie sehen die folgende Oberfläche

![mac_mysql_manage](https://image.pseudoyu.com/images/mac_mysql_manage.png)

Klicken Sie auf das MySQL-Symbol, um in die detaillierte Verwaltungsoberfläche zu gelangen

![mac_mysql_service](https://image.pseudoyu.com/images/mac_mysql_service.png)

In dieser Verwaltungsoberfläche können Sie den MySQL-Dienst bequem starten und stoppen und auch einstellen, dass er beim Systemstart automatisch gestartet wird usw. Sie können auch weitere Einstellungen in `Konfiguration` vornehmen, aber es wird empfohlen, dies in der Befehlszeile zu tun.

#### Befehlszeilenschnittstelle

Natürlich können Sie es auch in der Befehlszeile starten

```sh
//MySQL starten
sudo /usr/local/mysql/support-files/mysql.server start

//MySQL stoppen
sudo /usr/local/mysql/support-files/mysql.server stop
```

Die Wirkung ist wie folgt

![mac_mysql_cli](https://image.pseudoyu.com/images/mac_mysql_cli.png)

Natürlich können Sie auch einige Aliase setzen, um Befehle zu vereinfachen, aber da es eine bequeme Verwaltungsoberfläche gibt, muss man sich nicht damit abmühen. Wenn Sie in einer Linux-Umgebung ohne grafische Oberfläche arbeiten, müssen Sie Befehlszeilenoperationen verwenden.

### Verbindung zu MySQL herstellen

Nach der Installation und dem Start können Sie sich über die Befehlszeile mit MySQL verbinden und einige grundlegende Operationen durchführen

```sh
mysql -h localhost -u root -p

//Geben Sie das bei der Installation festgelegte Passwort ein

//Status anzeigen
status;
```

![mysql_connect](https://image.pseudoyu.com/images/mysql_connect.png)

Neben der Verbindung über die Befehlszeile gibt es auf der MacOS-Plattform auch einen sehr nützlichen Client `Sequel Pro`, der die meisten benötigten Funktionen bietet. Aufgrund von Absturzproblemen in der offiziellen Version und da sie nicht mehr gewartet wird, wird empfohlen, die Testversion [Sequel Pro Testversion](https://sequelpro.com/test-builds) herunterzuladen, die bequem eine Verbindung zu lokalen/entfernten Server-MySQL-Diensten herstellen kann

![sequel_pro_connect](https://image.pseudoyu.com/images/sequel_pro_connect.png)

Und die Struktur und den Inhalt der Datenbank abfragen und SQL-Befehle ausführen

![sequel_pro_manage](https://image.pseudoyu.com/images/sequel_pro_manage.png)

Dies ist ein sehr leistungsfähiger und leichtgewichtiger Client, den ich bisher verwendet habe, und ich empfehle allen, ihn zu benutzen!

### SQL-Befehle

Nach der lokalen MySQL-Konfiguration und -Verbindung können wir einige Operationen an der Datenbank durchführen. Die SQL-Sprache ist hauptsächlich in die folgenden vier Kategorien unterteilt:

- DDL Datendefinitionssprache
- DML Datenmanipulationssprache
- DQL Datenabfragesprache
- DCL Datenkontrollsprache

Als Nächstes werden wir eine Reihe von Operationen durch Praxis abschließen

#### DDL-Operationen

```sql
--- Datenbank erstellen
create database learn_test;

--- Alle Datenbanken anzeigen
show databases;

--- Datenbank löschen
drop database mydb;
```

![mysql_ddl](https://image.pseudoyu.com/images/mysql_ddl.png)

```sql
--- In eine bestimmte Datenbank wechseln
use learn_test;

--- Eine einfache Datentabelle erstellen
create table contacts (
    id int not null auto_increment primary key,
    name varchar(30),
    phone varchar(20)
);

--- Feld hinzufügen
alter table contacts add sex varchar(1);

--- Feld modifizieren
alter table contacts modify sex tinyint;

--- Feld löschen
alter table contacts drop column sex;

--- Gesamte Tabelle löschen
drop table contacts;
```

Der Einfachheit halber werden diese Operationen im `Sequel Pro`-Client durchgeführt. Nach der Operation sieht unsere Tabellenstruktur wie folgt aus

![mysql_learn_test_ddl](https://image.pseudoyu.com/images/mysql_learn_test_ddl.png)

#### DML-Operationen

```sql
--- Mehrere Daten einfügen
insert into contacts (name, phone, sex) values('Zhang San', '13100000000', 1), ('Li Si', '13100000001', 1), ('Wang Wu', '13100000002', 2);

--- Dateninhalt modifizieren
update contacts set sex = 1 where name = 'Wang Wu';

--- Dateninhalt löschen
delete * from contacts where id = 3;
```

#### DQL-Operationen

MySQL kann die Tabelle durch den `select`-Befehl abfragen. Der am häufigsten verwendete Befehl zum Anzeigen der gesamten Tabelle ist

```sql
--- Alle Daten in der Tabelle anzeigen
select * from contacts;
```

Sie können auch das Schlüsselwort `where` für bedingte Abfragen und kombinierte Abfragen mit mehreren Bedingungen verwenden

```sql
--- Kombinierte Bedingungsabfrage
select * from contacts where id = 1 or name = "Li Si";
```

![mysql_contacts_dql](https://image.pseudoyu.com/images/mysql_contacts_dql.png)

`IN` und `LIKE` sind auch zwei Schlüsselwörter, die flexibel für Abfragen verwendet werden können.

`IN` kann uns helfen, mehrere Werte eines bestimmten Feldes zu filtern

```sql
--- Daten mit id in (1,3) abfragen
select * from contacts where id in(1,3);
```

![mysql_contacts_![mysql_contacts_dql_in](https://image.pseudoyu.com/images/mysql_contacts_dql_in.png)

Außerdem können `IN` und `EXISTS` für Unterabfragen verwendet werden

```sql
--- Unterabfrage IN
select A.*
from student A
where A.stu_no in(
        select B.stu_no from score B
);

--- Unterabfrage EXISTS
select A.*
from student A
where exists(
        select * from score B
        where A.stu_no = B.stu.no
);
```

`LIKE` kann uns bei einigen unscharfen Suchen nach Enthaltensbeziehungen helfen, `%` kann jedes Zeichen abgleichen, `_` kann ein einzelnes Zeichen abgleichen

```sql
--- Alle Kontakte mit Nachnamen Zhang abfragen
select * from contacts where name like 'Zhang%';
```

![mysql_contacts_dql_like_2](https://image.pseudoyu.com/images/mysql_contacts_dql_like_2.png)

```sql
--- Alle Kontakte abfragen, deren Namen mit 'Si' enden und zwei Zeichen haben
select * from contacts where name like '_Si';
```

![mysql_contacts_dql_like](https://image.pseudoyu.com/images/mysql_contacts_dql_like.png)

In praktischen Anwendungen ist das Datenvolumen von Datentabellen oft sehr groß, und Daten müssen entsprechend den entsprechenden Bedingungen gruppiert werden. Dies erfordert die Verwendung des Schlüsselworts `GROUP BY` und `HAVING` für weitere Filterbedingungen. `GROUP BY` muss in Verbindung mit Aggregatfunktionen verwendet werden.

```sql
--- Anzahl der männlichen Kontakte zählen
select case sex
            when 1 then "Männlich"
            when 2 then "Weiblich"
            else "Unbekannt" end as Geschlecht,
        count(*) as Anzahl
from contacts
group by sex
having sex = 1;
```

![mysql_contacts_dql_group_by](https://image.pseudoyu.com/images/mysql_contacts_dql_group_by.png)

Und Sie können auch `GROUP_CONCAT` verwenden, um einige spezifische Daten zu kombinieren

```sql
--- Liste und Gesamtzahl der Kontakte nach Geschlecht anzeigen
select case sex
            when 1 then "Männlich"
            when 2 then "Weiblich"
            else "Unbekannt" end as Geschlecht,
        group_concat(name order by name desc separator ' | '),
        count(*) as Anzahl
from contacts
group by sex;
```

![mysql_contacts_dql_group_concat](https://image.pseudoyu.com/images/mysql_contacts_dql_group_concat.png)

Manchmal müssen wir nur eindeutige Werte zurückgeben und doppelte Daten entfernen, dann können wir das Schlüsselwort `DISTINCT` verwenden

```sql
--- Duplikate bei der Abfrage von Feldern entfernen
select distinct sex from contacts;
```

In praktischen Anwendungen kann es auch notwendig sein, bestimmte Produkttransaktionsvolumen zu rangieren, einige Werte anzuordnen oder Blogbeiträge in chronologischer Reihenfolge anzuzeigen usw. Dies erfordert die Verwendung des Schlüsselworts `ORDER BY`, das standardmäßig aufsteigend (`ASC`) sortiert und manuell auf `DESC` gesetzt werden kann, um eine absteigende Sortierung zu erreichen.

Gleichzeitig haben einige Datenbanken eine sehr große Datenmenge, und das Zurückgeben aller Daten auf einmal ist ressourcenintensiv. Daher können Sie auch das Schlüsselwort `LIMIT` verwenden, um die Anzahl der zurückgegebenen Datensätze zu beschränken und gleichzeitig eine Paginierung zu erreichen.

```sql
select * from contacts order by id desc limit 5;
```

![mysql_dql_order_by_limit](https://image.pseudoyu.com/images/mysql_dql_order_by_limit.png)

### Eingebaute Funktionen

MySQL verfügt auch über viele gängige eingebaute Funktionen, die Benutzern helfen können, verschiedene Daten bequemer zu verarbeiten und Operationen zu vereinfachen. Die meisten Funktionen sind intuitiv und werden nicht einzeln erklärt.

![mysql_functions](https://image.pseudoyu.com/images/mysql_functions.png)

Es ist erwähnenswert, dass Aggregatfunktionen Berechnungen an einer Gruppe von Werten durchführen und einen einzelnen Wert zurückgeben.

### Flusskontrolle

MySQL verfügt über eine Flusskontrollanweisung ähnlich wie if-else oder switch in Programmiersprachen, um komplexe Anwendungslogik zu implementieren

```sql
--- Daten auswählen und Geschlecht auf Deutsch markieren
select name, phone, case sex
                        when 1 then "Männlich"
                        when 2 then "Weiblich"
                        else "Unbekannt" end
                    as sex
from contacts;
```

![mysql_contacts_flow_control](https://image.pseudoyu.com/images/mysql_contacts_flow_control.png)

### Tabellenverknüpfungen

Verschiedene Tabellen können durch bestimmte Verknüpfungsbedingungen verknüpft werden. Es gibt hauptsächlich drei Typen: Selbstverknüpfung, innere Verknüpfung und äußere Verknüpfung. Die äußere Verknüpfung wird weiter in linke äußere Verknüpfung, rechte äußere Verknüpfung und vollständige äußere Verknüpfung unterteilt. Ihre Unterschiede sind wie folgt:

![mysql_table_join](https://image.pseudoyu.com/images/mysql_table_join.png)

Selbstverknüpfung ist eine spezielle Verknüpfungsmethode, die logisch mehrere Tabellen erzeugt, um komplexe hierarchische Strukturen zu erreichen. Sie wird häufig auf Bereichstabellen, Menütabellen und Produktkategorietabellen usw. angewendet. Die Syntax lautet wie folgt:

```sql
--- Selbstverknüpfungssyntax
select A.column, B.column
from table A, table B
where A.column = B.column;
```

## Fazit

Jetzt, da wir über relationale Datenbanken gelernt haben, was ist mit nicht-relationalen Datenbanken? In Zukunft werden wir Informationen über Redis, eine weit verbreitete nicht-relationale Datenbank, organisieren. Bleiben Sie dran!

## Referenzen

> 1. [MySQL Offizielle Website](https://www.mysql.com)
> 2. [Sequel Pro Offizielle Website](https://sequelpro.com)