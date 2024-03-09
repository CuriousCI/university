# Accademia 1

## Requisiti

I dati di interesse per il sistema sono i docenti universitari, i progetti di ricerca e le attività dei docenti.

Di ogni docente interessa conoscere il nome, il cognome, la data di nascita, la matricola, la posizione universitaria (ricercatore, professore associato, professore ordinario) e i progetti ai quali partecipa.

Dei progetti interessa il nome, un acronimo, la data di inizio, la data di fine e i docenti che vi partecipano.

Un progetto è composto da molti Work Package (WP). Oltre al progetto a cui fa riferimento, del WP interessa sapere il nome, la data di inizio e la data di fine.

Il sistema deve permettere ai docenti di registrare impegni di diverso tipo. 

Degli impegni interessa sapere il giorno in cui avvengono, la durata in ore e la tipologia di impegno con relativa motivazione.


### 1. Docenti
    1.1 nome
    1.2 cognome
    1.3 data di nascita

### 2. Progetti di ricerca

### 3. Attività dei docenti

## UML

```mermaid
classDiagram
    class Studente {
        nome: Stringa
        codice_fiscale: [A-Z]3[A-Z]3[0-9]2[A-Z][0-9]2[A-Z][0-9]3[A-Z]
        matricola: Stringa [0-9]7
        data_di_nascita: Data
    }

    class Citta {
        nome: Stringa
    }
    class Citta["Città"]

    class Regione {
        nome: Stringa
        codice: [A-Z]2 
    }

    class Corso {
        nome: Stringa
    }

    class Insegnamento {
        codice: (codice_insegnamento: 100000..999999)
        nome: Stringa
        ore_di_lezione: intero >= 1
    }

    class Facolta {
        nome: Stringa
    }
    class Facolta["Facoltà"]

    class Professore {
        nome: Stringa
        data_di_nascita: Data
        codice_fiscale: [A-Z]3[A-Z]3[0-9]2[A-Z][0-9]2[A-Z][0-9]3[A-Z]
    }

    Citta "0..*" -- "1..1" Regione : sta in
    Studente "0..*" -- "1..1" Citta : nato a
    Studente "0..*" -- "0..2" Corso : iscritto a
    Studente "" -- "" Insegnamento : superato (voto 18..30, e la lode?)
    Insegnamento "0..*" -- "0..*" Corso : in (potrei considerare 21..* a sinistra? Nah, la magistrale ne avra' di meno)
    Corso "0..*" -- "1..1" Facolta : appartiene a
    Professore "1..1" -- "0..*" Insegnamento : insegna
```
