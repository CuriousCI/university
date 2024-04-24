# Un'occhiata veloce a GitHub Classroom 

Sarò molto sintetico, solo per dare un'idea di come funzionano gli esercizi e il feedback agli studenti

## Home 

![GitHub Classroom first page](./assets/2024-04-24_12:32:45.847.png)

## Creare una "Classroom" 

Per creare una "Classroom" bisogna selezionare l'organizzazione nella quale si vogliono mettere i repository (si quelli con le soluzioni degli studenti, sia i template con i test)

Una possibile organizzazione per il corso potrebbe essere "Metodologie di programmazione Sapienza"

![GitHub Classroom home](./assets/2024-04-24_12:33:10.080.png)

Passiamo direttamente alle informazioni importanti

## Amministratori della "Classroom"

Si può usare un link d'invito per decidere i docenti (amministratori) del corso 

![Link Invito TA e admin](./assets/2024-04-24_12:34:24.565.png)

## Assegnare esercizi

Una volta creata la "Classroom", questa è l'interfaccia di gestione dei degli esercizi 

![Specific Classroom home](./assets/2024-04-24_12:34:57.731.png)

### Individuale, di gruppo, pubblico o privato (scadenza opzionale)

Per assegnare un esercizio bisogna dare alcune informazioni di base: il nome, un'eventuale scadenza (opzionale), se si tratta di un esercizio di gruppo o individuale.

Quando lo studente "accetterà l'esercizio", verrà creato un repository (pubblico o privato) con il nome dell'esercizio e dello studente nell'organizzazione che avevamo scelto nella creazione della "Classroom"

![Creazione esercizio](./assets/2024-04-24_12:35:55.335.png)

Successivamente, si sceglie il template (il repository con i test) da usare per l'esercizio (i template con i test vengono creati una volta, e si riusano ogni anno)

### Template da usare per l'esrecizio

![Scelta Template](./assets/2024-04-24_12:37:04.544.png)

### Test

Qui si può decidere di eseguire un comando unico che fa girare tutti i test (quindi l'esercizio può essere passato / non passato), oppure si può decidere di andare più a grana fine e far girare più comandi che eseguono ciascuno un sottoinsieme dei test. 

![Test](./assets/2024-04-24_12:37:32.256.png)
![nome](./assets/2024-04-24_12:37:49.133.png)

### Riusare i test per gli anni futuri 

Gli esercizi si possono riusare, quindi non è necessario ogni volta riscrivere i test per gli esercizi dell'anno passato. Si può prendere un esercizio dell'anno passato, cliccare il tasto "riusa" e si può riproporre lo stesso esercizio con gli stessi test in un anno successivo.

### Condivisione esercizio

Una volta creato l'esercizio viene generato un link. Se gli studenti cliccano su quel link, possono accettare di fare l'esercizio, caso in cui viene creato un repository per il studente.

![Link condivisione esercizio](./assets/2024-04-24_12:38:41.963.png)

## Svolgere gli esercizi

### Accettare un homework

Questa è la schermata che vede uno studente quanto clicca un esercizio (se volete provare questo è il link di un esercizio [https://classroom.github.com/a/lWBDk-we](https://classroom.github.com/a/lWBDk-we))


![Schermata studente](./assets/2024-04-24_12:39:14.247.png)

Link del repository appena creato

![nome](./assets/2024-04-24_12:39:32.003.png)

### Testare in locale

Lo studente dovrà clonare il repository in locale (lo si può fare da CLI come preferisco io, altrimenti Eclipse ha integrate le funzionalità per lavorare con git e GitHub)

In questo esempio, per far girare i test ho eseguito il comando `gradle test`, per chi usa Eclipse, è già tutto integrato nell'editor, e possono eseguire i test cliccando sul tasto verder per eseguire il programma.

Qui un test fallisce.

![Test Fallito](./assets/2024-04-24_12:48:56.040.png)

Lo studente scrive il codice per far funzionare il test. Ora i 2 test passano enrambi.

![Codice corretto](./assets/2024-04-24_12:49:13.723.png)

### Pubblicare il codice

Una volta risolto l'esercizio (o anche parte di esso!) lo studente può fare il commit del codice al repository generato prima (usando `git` da CLI come nel mio caso, altrimenti Eclipse ha integrate le funzionalità per farlo in modo semplice)

![Git commit](./assets/2024-04-24_12:49:49.550.png)

### GitHub testa in automatico il codice

Quando lo studente fa il commit del codice, GitHub si occupa anche lui di esegure i test, per far vedere al docente quanti e quali test ha superato fino a quel momento lo studente.

![GitHub actions](./assets/2024-04-24_12:50:12.563.png)

## Esercizi dal punto di vista del doecente 

Il docente può vedere l'elenco degli studenti che hanno accettato di fare l'esercizio, se hanno passato o meno i test, e possono andare a vedere il codice che hanno scritto (e lasciare un eventuale feedback manuale sul codice)

![Studenti che hanno accettato](./assets/2024-04-24_12:40:58.785.png)

### Feedback del docente

Eventualmente, il docente può vedere il codice che ha scritto lo studente. 

![Feedback del docente](./assets/2024-04-24_12:51:05.511.png)

<!-- # TODO -->
<!-- ![nome](./assets/2024-04-24_12:33:10.080.png) -->
<!-- ![nome](./assets/2024-04-24_12:33:51.191.png) -->
<!-- ![nome](./assets/2024-04-24_12:34:24.565.png) -->
<!-- ![nome](./assets/2024-04-24_12:34:27.990.png) -->
<!-- ![nome](./assets/2024-04-24_12:34:57.880.png) -->
<!-- ![nome](./assets/2024-04-24_12:37:06.403.png) -->
<!-- ![nome](./assets/2024-04-24_12:38:14.877.png) -->
<!-- ![nome](./assets/2024-04-24_12:39:43.567.png) -->
<!-- ![nome](./assets/2024-04-24_12:41:00.875.png) -->
<!-- ![nome](./assets/2024-04-24_12:45:00.882.png) -->
<!-- ![nome](./assets/2024-04-24_12:48:22.587.png) -->
<!-- ![nome](./assets/2024-04-24_12:50:52.582.png) -->
<!-- ![nome](./assets/2024-04-24_12:51:05.511.png) -->
