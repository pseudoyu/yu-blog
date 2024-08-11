---
title: "PostgreSQL Grundlagen und Praxis"
date: 2022-09-05T23:30:46+08:00
draft: false
tags: ["database", "postgres", "programming", "work practice series", "work", "practice", "backend"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《后来的我们 - 五月天》" >}}

## Vorwort

In letzter Zeit habe ich darüber nachgedacht, die in meiner Arbeit häufig verwendeten technischen Punkte und Werkzeuge zu organisieren und zusammenzufassen. Einerseits hilft mir dies, diese Wissenspunkte zu überprüfen und meine Erinnerung an deren Verwendung zu vertiefen. Andererseits kann es als Referenz für zukünftige Verwendungen dienen.

Derzeit plane ich, mehrere Kernbereiche abzudecken, darunter Datenbanken, CI/CD (GitHub Actions + GitLab CI), Container (Docker + k8s), Betrieb (Ansible etc.), sowie einige Zusammenfassungen von Sprachfunktionen, praktischen Git-Techniken und Shell-Skript-Tipps. Da ich vielen dieser Themen nur bei der Arbeit begegnet bin und einige erweiterte Lernaktivitäten auf eigene Faust unternommen habe, stimmen sie möglicherweise nicht vollständig mit spezifischen Unternehmenspraktiken überein (größtenteils basierend auf meinen eigenen Erfahrungen und meinem Verständnis). Ich hoffe, dass dies hilfreich sein kann.

Dieser Artikel ist der PostgreSQL-Teil der Datenbankserie. Ich habe zuvor MySQL zusammengefasst, auf das Sie in "MySQL Grundlagenwissen und verwandte Operationen" Bezug nehmen können.

## Überblick über Daten und Datenbanken

### Daten

Grundsätzlich sind Daten eine Art von Tatsache oder beobachtetem Ergebnis, eine logische Zusammenfassung objektiver Angelegenheiten und eine Form und ein Träger von Informationen. Menschen haben seit der Antike Daten verwaltet (selbst bevor der Begriff existierte), zunächst durch manuelle Verwaltung, dann allmählich durch Dateisysteme (wie Bibliotheken, die verschiedene Informationen nach Kategorien verwalten), und schließlich mit der Entwicklung der Computertechnologie die bequemere und effizientere Art der Datenbankverwaltung gebildet.

### Datenbank

Eine Datenbank ist ein Repository, das Daten nach einer bestimmten Datenstruktur organisiert, speichert und verwaltet. Ihre Hauptmerkmale sind:

- Strukturiert
- Teilbar
- Geringe Redundanz
- Hohe Unabhängigkeit
- Leicht erweiterbar

Es ist leicht zu verstehen, dass Daten, die nach verschiedenen Beziehungen/Strukturen organisiert sind, unterschiedliche Eigenschaften haben und für verschiedene Anwendungsszenarien geeignet sind. Derzeit gibt es hauptsächlich drei Typen: hierarchische Datenbanken, Netzwerkdatenbanken und relationale Datenbanken. PostgreSQL, auf das wir uns konzentrieren werden, ist eine relationale Datenbank.

### Datenbankmanagementsystem (DBMS)

Ein Datenbankmanagementsystem (DBMS) ist ein System, das verschiedene Operationen an Datenbanken durchführt. Es hat Kernfunktionen wie das Einrichten und Warten von Datenbanken, das Organisieren und Verwalten der Datenspeicherung, das Steuern von Datenbanken, das Definieren von Daten, das Manipulieren von Daten und das Verwalten der Kommunikation zwischen Daten. Verschiedene Datenbankmanagementsysteme behandeln Datenbanken und Daten unterschiedlich, und die Art und Weise, wie Daten präsentiert werden, variiert ebenfalls. Oft ist es erforderlich, ein geeignetes Datenbankmanagementsystem basierend auf Faktoren wie Datenumfang und Geschäftsanforderungen zu wählen. Beispielsweise kann die Leistung relationaler Datenbanken in Situationen mit massiven Daten und hochparallelen Daten-Lese-/Schreiboperationen erheblich beeinträchtigt werden.

## Relationales Datenbankmanagementsystem (RDBMS)

### Hauptmerkmale

Relationale Datenbanken präsentieren Daten hauptsächlich in Form von Datentabellen, wobei jede Zeile einen Datensatz und jede Spalte das Datenfeld des Datensatznamens darstellt. Viele Zeilen und Spalten bilden eine einzelne Tabelle, und mehrere einzelne Tabellen bilden eine Datenbank. Benutzer/Systeme fragen die Datenbank über SQL (Structured Query Language) ab.

Einige relationale Datenbankoperationen haben transaktionale Eigenschaften, nämlich die ACID-Regeln:

- Atomarität
- Konsistenz
- Isolation
- Dauerhaftigkeit

Atomarität bedeutet, dass eine Reihe von Transaktionsoperationen entweder alle abgeschlossen werden oder alle fehlschlagen müssen; es gibt keine Situation, in der nur ein Teil abgeschlossen wird. Zum Beispiel würde in einem Banküberweisung-Szenario, nachdem die Überweisung erfolgt ist, der Kontostand des Absenders abnehmen, aber wenn ein Datenbankoperationsfehler auftritt und der Kontostand des Empfängers nicht zunimmt, würde dies ernsthafte Probleme verursachen.

Konsistenz bedeutet, dass nach Abschluss einer Transaktion die Daten in der gesamten Datenbank konsistent sind; es sollte keine Situation geben, in der die gleichen Daten innerhalb der Datenbank nicht synchronisiert sind.

Isolation bedeutet, dass verschiedene Transaktionen unabhängig und ohne Störungen ablaufen sollten. Natürlich opfert dies etwas Effizienz, bietet aber bessere Garantien für die Datengenauigkeit.

Dauerhaftigkeit bedeutet, dass wenn eine Transaktion abgeschlossen ist, ihre Änderungen an der Datenbank und ihre Auswirkungen auf das System dauerhaft sind.

### Datenintegrität

Datenintegrität ist eine sehr wichtige Anforderung und Eigenschaft von Datenbanken und bezieht sich auf die Konsistenz und Zuverlässigkeit der in der Datenbank gespeicherten Daten. Sie wird hauptsächlich in vier Typen unterteilt:

- Entitätsintegrität
- Domänenintegrität
- Referenzielle Integrität
- Benutzerdefinierte Integrität

Entitätsintegrität erfordert, dass jede Datentabelle einen eindeutigen Identifikator hat, und das Primärschlüsselfeld in jeder Tabelle darf nicht leer oder doppelt sein, was hauptsächlich bedeutet, dass die Daten in der Tabelle eindeutig unterschieden werden können.

Domänenintegrität besteht darin, einige zusätzliche Einschränkungen für die Spalten in der Tabelle vorzunehmen, wie zum Beispiel die Einschränkung von Datentypen, Prüfungsbeschränkungen, Festlegung von Standardwerten, ob Nullwerte erlaubt sind und Wertebereich.

```sql
--- Einschränkung der Feldeinzigartigkeit bei der Tabellenerstellung
CREATE TABLE person (
    id INT NOT NULL auto_increment PRIMARY KEY,
    name VARCHAR(30),
    id_number VARCHAR(18) UNIQUE
);
```

Referenzielle Integrität bedeutet, dass die Datenbank nicht zulässt, dass auf nicht existierende Entitäten verwiesen wird. Tabellen in der Datenbank haben oft einige Assoziationen mit anderen Tabellen, und die referenzielle Integrität kann durch Fremdschlüsselbeschränkungen sichergestellt werden.

Benutzerdefinierte Integrität besteht darin, einige semantische Einschränkungen für Daten gemäß spezifischen Anwendungsszenarien und beteiligten Daten vorzunehmen, wie zum Beispiel, dass der Kontostand nicht negativ sein kann, usw. Sie wird im Allgemeinen durch das Festlegen von Regeln, gespeicherten Prozeduren und Triggern eingeschränkt und begrenzt.

### Mainstream RDBMS

Derzeit umfassen die Mainstream-relationalen Datenbankmanagementsysteme:

- SQL Server
- Sybase
- DB2
- Oracle
- MySQL
- PostgreSQL

Oracle, MySQL und PostgreSQL werden häufiger von Unternehmen und Einzelpersonen verwendet. Als Nächstes werden wir PostgreSQL als Beispiel für detaillierte Betriebserklärungen verwenden.

## PostgreSQL

### Installation und Konfiguration

PostgreSQL ist ein modernes Open-Source-objekt-relationales Datenbankmanagementsystem.

Für einzelne Benutzer, die lernen, es zu verwenden, können Sie direkt das Software-Installationspaket herunterladen, um eine lokale Umgebung einzurichten. Sie können je nach System verschiedene Versionen wählen, und es verfügt auch über eine praktische grafische Benutzeroberfläche zum Starten, Stoppen, Neustarten von Diensten und zum Vornehmen verwandter Konfigurationen. Dieser Artikel verwendet PostgreSQL 14 auf macOS als Beispiel. Nach der Installation und Durchführung grundlegender Einstellungen von der [offiziellen Website](https://postgresapp.com) können Sie den lokalen PostgreSQL-Dienst verwalten. Die Version kann leicht variieren, aber die Kernfunktionen unterscheiden sich nicht wesentlich.

#### Grafische Benutzeroberfläche

Öffnen Sie die PostgreSQL.app-Anwendung, und Sie sehen die folgende Oberfläche:

![mac_postgres_interface](https://image.pseudoyu.com/images/mac_postgres_interface.png)

In dieser Verwaltungsoberfläche können Sie den PostgreSQL-Dienst bequem starten und stoppen. Durch Klicken auf die entsprechende Datenbank können Sie auch in die Befehlszeilenschnittstelle gelangen.

#### Befehlszeilenschnittstelle

Zunächst fügen wir den `psql`-Pfad zu den Umgebungsvariablen für die spätere Verwendung hinzu. Ich verwende `zsh`, also füge ich den folgenden Inhalt zur `~/.zshrc`-Datei hinzu:

```bash
# postgres
export PATH=${PATH}:/Applications/Postgres.app/Contents/Versions/14/bin
```

Danach geben Sie `psql` im Terminal ein, um auf die PostgreSQL-Befehlszeilenschnittstelle zuzugreifen. Sie können den folgenden Befehl verwenden, um die psql-Befehlsliste anzuzeigen:

```bash
psql --help
```

### Verbindung zu PostgreSQL herstellen

Wir können uns mit folgendem Befehl mit der Datenbank verbinden:

```bash
# Mit der Datenbank verbinden
psql -h <host> -p <port> -U <username> <database-name>
```

Natürlich können wir auch einige Drittanbieter-Tools verwenden, um uns bequemer mit der Datenbank zu verbinden. Ich verwende derzeit [TablePlus](http://tableplus.com), das PostgreSQL-Datenbanken unterstützt, und ich empfehle es.

### Befehlszeileninteraktion

PostgreSQL bietet leistungsstarke Befehlszeileninteraktionsfunktionalität. Wir können `\` + Schlüsselwort verwenden, um Operationen durchzuführen. Wir können Befehlsdetails und Hilfeinformationen durch Konsultation der Dokumentation oder Verwendung der Befehle `\?` und `help` anzeigen. Andere häufig verwendete Befehle lauten wie folgt:

```bash
# Hilfe anzeigen
help

# psql-Befehlsdetails anzeigen
\?

# Datenbanken anzeigen (alle)
\l

# Datenbanken anzeigen (spezifisch)
\l <database-name>

# Mit einer Datenbank verbinden
\c <database-name>

# Methoden anzeigen
\df

# Tabellen anzeigen (alle)
\d

# Tabellen anzeigen (nur Tabellen)
\dt

# Tabellen anzeigen (spezifisch)
\d <table-name>

# SQL-Befehle ausführen
\i <filepath>/<filename>

# Erweiterte Ansicht öffnen
\x

# In CSV exportieren
\copy (SELECT * FROM person LEFT JOIN car ON person.car_id = car.id) TO 'path/to/output.csv' DELIMITER ',' CSV HEADER;

# Beenden
\q
```

### Kernsyntax

Nach der Konfiguration und Verbindung mit der lokalen PostgreSQL können wir einige Operationen an der Datenbank durchführen. Die SQL-Sprache ist hauptsächlich in die folgenden vier Kategorien unterteilt:

- DDL (Data Definition Language)
- DML (Data Manipulation Language)
- DQL (Data Query Language)
- DCL (Data Control Language)

#### DDL-Operationen

```sql
--- Datenbank erstellen
CREATE DATABASE <database-name>;

--- Datenbank löschen
DROP DATABASE <database-name>;
```

```bash
# In eine spezifische Datenbank eintreten
\c <database-name>;
```

```sql
--- Tabelle erstellen (Einschränkungen hinzufügen)
CREATE TABLE person (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    date_of_birth DATE NOT NULL,
    country_of_birth VARCHAR(50),
    email VARCHAR(150)
);

--- Tabelle ändern
ALTER TABLE person ADD PRIMARY KEY(id);

--- Spalte löschen
ALTER TABLE person DROP column email;

--- Gesamte Tabelle löschen
DROP TABLE person;
```

#### DML-Operationen

```sql
--- Daten einfügen
INSERT INTO person (
    first_name,
    last_name,
    gender,
    date_of_birth
) VALUES ('Yu', 'ZHANG', 'MALE', DATE '1997-06-06');

--- Dateninhalt ändern
UPDATE person SET email = 'ommar@gmail.com' WHERE id = 20;

--- Dateninhalt löschen
DELETE FROM person WHERE id = 1;
```

Sie können das Schlüsselwort `ON CONFLICT` verwenden, um Konflikte zu behandeln:

```sql
--- Nichts tun, wenn ein Konflikt auftritt
INSERT INTO person (
    first_name,
    last_name,
    gender,
    date_of_birth
) VALUES ('Yu', 'ZHANG', 'MALE', DATE '1997-06-06') ON CONFLICT (id) DO NOTHING;

--- Spezifizierte Felder aktualisieren, wenn ein Konflikt auftritt
INSERT INTO person (
    first_name,
    last_name,
    gender,
    date_of_birth
) VALUES ('Yu', 'ZHANG', 'MALE', DATE '1997-06-06') ON CONFLICT (id) DO UPDATE SET email = EXCLUDED.email;
```

#### DQL-Operationen

Sie können die Tabelle mit dem Befehl `SELECT` abfragen. Der am häufigsten verwendete Befehl zum Anzeigen der gesamten Tabelle ist:

```sql
--- Alle Daten in der Tabelle anzeigen
SELECT * FROM person;

--- Daten abfragen (spezifische Felder)
SELECT first_name, last_name FROM person;
```

Sie können das Schlüsselwort `WHERE` für bedingte Abfragen und Kombinationsabfragen mit mehreren Bedingungen verwenden:

```sql
--- Daten abfragen (Bedingungsfilterung, WHERE | AND | OR | Vergleich > | >= | < | <= | = | <>)
SELECT * FROM person WHERE gender = 'MALE' AND (country_of_birth = 'Poland' OR country_of_birth = 'China');
```

`IN`, `BETWEEN`, `LIKE` und `ILIKE` sind auch einige Schlüsselwörter, die flexibel für Abfragen verwendet werden können.

`IN` kann uns helfen, mehrere Werte eines bestimmten Feldes zu filtern.

```sql
--- Daten abfragen (mit IN-Schlüsselwort)
SELECT * FROM person WHERE country_of_birth IN ('China', 'Brazil', 'France');
```

`BETWEEN` kann uns helfen, einen Bereich eines bestimmten Feldes zu filtern.

```sql
--- Daten abfragen (mit BETWEEN-Schlüsselwort)
SELECT * FROM person WHERE date_of_birth BETWEEN DATE '2021-10-10' AND '2022-08-31';
```

`LIKE` kann uns bei einigen unscharfen Suchen nach Einschlussbeziehungen helfen. `%` kann jedes Zeichen entsprechen, `_` kann ein einzelnes Zeichen entsprechen. `ILIKE` ist die Groß-/Kleinschreibung nicht beachtende Version von `LIKE`.

```sql
--- Daten abfragen (mit LIKE/ILIKE-Schlüsselwörtern, _ | %)
SELECT * FROM person WHERE email LIKE '%@bloomberg.%';
SELECT * FROM person WHERE email LIKE '________@google.%';
SELECT * FROM person WHERE country_of_birth ILIKE 'p%';
```

In praktischen Anwendungen ist das Datenvolumen von Datentabellen oft sehr groß, und Daten müssen entsprechend den entsprechenden Bedingungen gruppiert werden. Dies erfordert die Verwendung des Schlüsselworts `GROUP BY`, und `HAVING` wird für weitere Filterbedingungen verwendet. `GROUP BY` muss in Verbindung mit Aggregatfunktionen verwendet werden.

```sql
--- Daten abfragen (mit GROUP BY-Schlüsselwort für gruppierte Abfragen, mit HAVING-Schlüsselwort zum Hinzufügen von Bedingungen, mit AS für Ergebnisaliase)
SELECT country_of_birth, COUNT(*) AS Amount FROM person GROUP BY country_of_birth HAVING Amount > 5 ORDER BY country_of_birth;
```

Manchmal müssen wir nur eindeutige Werte zurückgeben und doppelte Daten entfernen. In diesem Fall können wir das Schlüsselwort `DISTINCT` verwenden.

```sql
--- Daten abfragen (Duplikate entfernen)
SELECT DISTINCT country_of_birth FROM person;
```

In praktischen Anwendungen ist es auch sehr wahrscheinlich, dass wir bestimmte Produkttransaktionsvolumen rangieren, einige Werte anordnen oder Blogbeiträge in chronologischer Reihenfolge anzeigen müssen usw. Dies erfordert die Verwendung des Schlüsselworts `ORDER BY`, das standardmäßig auf `ASC` aufsteigend eingestellt ist und manuell auf `DESC` für absteigend eingestellt werden kann.

```sql
--- Daten abfragen (sortieren ASC | DESC)
SELECT * FROM person ORDER BY id, country_of_birth;
```

Gleichzeitig haben einige Datenbanken sehr große Datenmengen, und das Zurückgeben aller Daten auf einmal ist ressourcenintensiv. Daher können wir das Schlüsselwort `LIMIT` verwenden, um die Anzahl der zurückgegebenen Datensätze zu beschränken, und `OFFSET` verwenden, um den Versatz anzugeben.

```sql
--- Daten abfragen (Menge und Versatz angeben)
SELECT * FROM person OFFSET 5 LIMIT 10;
SELECT * FROM person OFFSET 5 FETCH FIRST 5 ROW ONLY;
```

### Kernkonzepte

#### PRIMARY KEY

Der Primärschlüssel ist der eindeutige Identitätsdatensatz in der Datentabelle, erstellt und geändert mit den folgenden Befehlen:

```sql
--- Primärschlüssel hinzufügen
CREATE TABLE person (
    id BIGSERIAL NOT NULL PRIMARY KEY
);

--- Primärschlüssel ändern
ALTER TABLE person ADD PRIMARY KEY(id);
```

Der Primärschlüssel verwendet normalerweise `SERIAL/BIGSERIAL` inkrementelle `INT`-Werte, oder `UUID` kann als Primärschlüssel verwendet werden.

```sql
CREATE TABLE person (
    id UUID NOT NULL PRIMARY KEY
);
```

#### FOREIGN KEY

Ein Fremdschlüssel ist eine spezielle Art von Primärschlüssel, der der Primärschlüssel einer anderen Tabelle ist, erstellt und geändert mit den folgenden Befehlen:

```sql
--- Fremdschlüssel hinzufügen
CREATE TABLE person (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    car_id BIGINT REFERENCES car (id),
    UNIQUE(car_id)
);

--- Fremdschlüssel ändern
CREATE TABLE car (
    id BIGSERIAL NOT NULL PRIMARY KEY
)
```

#### JOIN

Eine Verbindungsabfrage bezieht sich auf das Verbinden von Daten aus mehreren Tabellen während einer Abfrage, um mehr Informationen abzurufen. In SQL können wir das Schlüsselwort `JOIN` verwenden, um Verbindungsabfragen zu implementieren, das Schlüsselwort `LEFT JOIN` verwenden, um linke Verbindungsabfragen zu implementieren, und das Schlüsselwort `RIGHT JOIN` verwenden, um rechte Verbindungsabfragen zu implementieren.

```sql
--- JOIN-Abfrage
SELECT * FROM person
JOIN car ON person.car_id = car.id

--- LEFT JOIN-Abfrage
SELECT * FROM person
LEFT JOIN car ON person.car_id = car.id
```

Sie können das Schlüsselwort `USING` verwenden, um die Verwendung des Schlüsselworts `ON` zu vereinfachen.

```sql
SELECT * FROM person
LEFT JOIN car USING (car_id);
```

#### Einschränkungen

CONSTRAINT wird verwendet, um die Daten in der Datentabelle einzuschränken. Wir können Einschränkungen mit dem folgenden Befehl hinzufügen:

```sql
ALTER TABLE person ADD CONSTRAINT gender_constraint CHECK (gender = 'Female' OR gender = 'Male');
```

Zum Beispiel fügen Sie `UNIQUE` hinzu, um Eindeutigkeit anzuzeigen:

```sql
CREATE TABLE person (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    email VARCHAR(150) UNIQUE
);

ALTER TABLE person ADD CONTRAINT unique_email_address UNIQUE (email);
```

### Nützliche Techniken

#### Aggregatfunktionen

Viele Aggregatfunktionen sind eingebaut, wie `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` usw., die für Aggregatberechnungen von Daten verwendet werden.

#### COALESCE

Bei der Abfrage von Daten können wir `COALESCE` verwenden, um Standardwerte einzufügen:

```sql
--- COALESCE verwenden, um Standardwerte einzufügen
SELECT COALESCE(email, 'Email Not Provided') FROM person;
```

#### NULLIF

Mit dem Schlüsselwort `NULLIF` wird, wenn der zweite Parameter gleich dem ersten ist, `NULL` zurückgegeben, andernfalls wird der erste Parameter zurückgegeben. Dies wird verwendet, um Fehler wie Division durch Null zu verhindern.

```sql
SELECT COALESCE(10 / NULLIF(0, 0), 0);
```

#### Zeit

Das Anzeigeformat für Zeit ist wie folgt:

```sql
SELECT NOW();
SELECT NOW()::DATE;
SELECT NOW()::TIME;
```

Wir können Berechnungen mit der Zeit durchführen:

```sql
SELECT NOW() - INTERVAL '1 YEAR';
SELECT NOW() + INTERVAL '10 MONTHS';
SELECT (NOW() - INTERVAL '3 DAYS')::DATE;
```

Wir können `EXTRACT` verwenden, um einen bestimmten Teil der Zeit zu erhalten:

```sql
SELECT EXTRACT(YEAR FROM NOW());
SELECT EXTRACT(MONTH FROM NOW());
SELECT EXTRACT(DAY FROM NOW());
SELECT EXTRACT(DOW FROM NOW());
SELECT EXTRACT(CENTURY FROM NOW());
```

Wir können das Schlüsselwort `AGE` verwenden, um Altersunterschiede zu berechnen:

```sql
SELECT first_name, last_name, AGE(NOW(), date_of_birth) AS age FROM person;
```

### Erweiterte Unterstützung

PostgreSQL bietet viele Erweiterungen, um reichhaltigere Funktionalität zu implementieren.

#### Erweiterungen installieren

```sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
```

#### Erweiterungsmethoden anzeigen

```bash
df
```

#### Erweiterungsmethoden verwenden

```sql
SELECT uuid_generate_v4();
```

## Fazit

Das oben Genannte ist meine Erklärung des Grundlagenwissens und der praktischen Operationen von PostgreSQL. Ich hoffe, es ist für Sie hilfreich.

## Referenzen

> 1. [PostgreSQL Offizielle Website](http://www.postgresql.org)
> 2. [Postgres.app Offizielle Website](https://postgresapp.com)
> 3. [TablePlus Offizielle Website](https://tableplus.com)