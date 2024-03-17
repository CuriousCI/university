# Go

## Requisiti

I dati di interesse per il sistema sono i giocatori, i tornei e le partite.

Di un giocatore interessa conoscere il nick-name (univoco), il nome, il cognome, l’indirizzo e il rank dichiarato (un intero positivo).

Due giocatori si possono sfidare in una partita. Di una partita interessa sapere la data e il luogo in cui è giocata, le regole di conteggio usate (giapponesi o cinesi), quale giocatore gioca con le pietre bianche e quale con le pietre nere, il fattore di deficit chiamato komi (numero reale non negativo, tra 0 e 10) e l’esito. 

L’esito può essere rappresentato da una rinuncia di uno dei due giocatori, oppure da una coppia di punteggi di bianco e di nero (interi non negativi).

Le partite si possono anche riferire a un torneo.

Di un torneo interessa sapere il nome, una descrizione testuale, e l’edizione in termini dell’anno in cui si svolge.

### Giocatori

- nick-name {id}
- nome
- cognome
- indirizzo (stringa speciale etc... (via|piazza), (nome: Stringa), civico: (Int > 0) etc...)
- rank dichiarato (intero > 0)

### Tornei

- nome
- descrizione
- edizione (anno in cui si svolge, {id})

### Partite

- data
- luogo (insieme di luoghi?)
- regole (giapponesi o cinesi?)
- giocatore con pietre bianche 
- giocatore con pietre nere
- komi (0 < Reale < 10)

- si possono riferire ad un torneo

- esito
    - rinuncia di uno dei due giocatori
    - (punteggio bianco, punteggio nero): (Intero >= 0, Intero >= 0)

