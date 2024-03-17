# Esercitazioni Universitarie 1

## Requisiti

I dati di interesse per il sistema sono insegnamenti universitari e le esercitazioni ivi erogate.

Di ogni insegnamento interessa sapere il nome, il relativo numero di crediti formativi universitari, i docenti (possono essere più d’uno) e l’anno accademico di riferimento. 

Dei docenti interessa matricola, nome e cognome.

Un insegnamento può prevedere diverse esercitazioni, ognuna erogata in una certa data e composta da molti esercizi, scelti tra quelli disponibili nel sistema.

Di ogni esercizio, il sistema deve rappresentare il testo e la o le relative soluzioni disponibili (anche nessuna). 

Per ogni esercizio presentato in una esercitazione, il sistema deve mantenere l’informazione circa il fatto che questo sia stato solo presentato (per essere svolto in modo autonomo dagli studenti), oppure anche risolto in aula (e, in questo caso, quale delle soluzioni disponibili è stata mostrata).

### Insegnamenti

- nome
- CFU
- anno accademico

- docenti (multipli)
- esercitazioni (multiple)

### Docenti

- matricola
- nome
- cognome

### Esercitazioni

- data
- esercizi (multipli)

### Esercizi

- testo
- soluzioni disponibili (0 o più)
- uno dei due stati
    - presentato
    - risolto in aula
        - relativa soluzione mostrata



