# Impiegati e Studenti 

## Requisiti

I dati di interesse per il sistema sono i dati anagrafici di alcune tipologie di persone.

Di ogni persona interessa mantenere nome, cognome, codice fiscale e data di nascita.

Degli uomini interessa mantenere anche la posizione militare, mentre delle donne si vuole mantenere anche il numero di maternità.

Alcune persone sono impiegati. Di questi interessa rappresentare lo stipendio e il ruolo, che può essere di segretario, direttore, oppure di progettista. Alcuni progettisti sono responsabili di progetto.

Di questi interessa mantenere la collezione dei progetti di cui sono responsabili. Di tali progetti interessa il nome.

Alcune persone sono studenti. 

Di questi interessa rappresentare anche il numero di matricola.

Nel dominio di interesse gli studenti non sono mai impiegati, ma esistono persone che non sono né impiegati né studenti.

### Persona

- nome
- cognome
- codice_fiscale
- data_di_nascita

### Uomini

- posizione_militare (un'eventuale classe)

### Donne

- numero_di_maternita' (codice univoco) [0..1]

<!-- - attributo: Stringa che rispetta la regex ^.{5}$ [1..5] -->
<!-- - attributo: Stringa con regex ^.{5}$ [1..5] -->
<!-- StringaSpeciale = Stringa che rispetta la regex ^.{5}$ -->

### Impiegati

- stipendio
- ruolo (classe a se)
    - segretario
    - direttore
    - progettista (specifica a se)

### Progettista

- responsabile di progetto

### Progetto

- nome

### Studenti

- matricola

