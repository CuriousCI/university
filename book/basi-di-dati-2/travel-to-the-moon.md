1. Requisiti sulle crociere:
  1.1. codice 
  1.2. data di inizio
  1.3. data di fine
  1.4. nave utilizzata (v. req. 2)
  1.5. itinerario (v. req. 4)
  1.6. il tipo, uno tra:
    1.6.1. luna di miele, di cui interessa:
      1.6.1.1. sottotipo, uno tra:
        1.6.1.1.1. tradizionali (se numero destinazioni romantiche > numero destinazioni divertenti)
        1.6.1.1.2. alternative (se numero destinazioni divertenti > numero destinazioni romantiche)
    1.6.2. per famiglie, di cui interessa:
      1.6.3. se adatte ai bambini (booleano)

2. Requisiti sulle navi
  2.1. nome
  2.2. comfort (3..5)
  2.3. capienza (max)

3. Requisiti sui porti:
  3.1. nome
  3.2. continente {"Africa", "Asia", "Europa", etc...}
  3.3. posti da vedere (v. req. 5)
  3.4. tipo, almeno uno tra:
    3.4.1. romantico
    3.4.2. divertente
  3.5 un insieme di posti da vedere (v. req. 5)

4. Requisiti sugli itinerari: di ogni itinerario interessa
  4.1. nome
  4.2. sequenza ordinata di elementi (tappe), di cui interessa:
    4.2.1. porto (v. req. 3)
    4.2.2. arrivo:
      4.2.2.1. il numero d'ordine del giorno (rispetto alla data di inizio della crociera) # i-esimo giorno
      4.2.2.2. ora
    4.2.3. ripartenza  
      4.2.3.1. il numero d'ordine del giorno (rispetto alla data di inizio della crociera)
      4.2.3.2. ora

5. Requisiti sui posti da vedere:
  5.1. nome
  5.2. descrizione
  5.3. orari di apertura, nella forma di una mappa che associa ad ogni giorno della settimana (lunedì, ..., domenica) un insieme di fasce orarie, dove ogni fascia oraria è definita in termini di una coppia di orari

6. Requisiti clienti
  6.1. nome
  6.2. cognome
  6.3. età
  6.3. indirizzo: (nome: Stringa, civico: numero, Città: Stringa, Regione: Stringa, Paese: Stringa)
  6.4. può prenotare crociere (v. req. 7) 

7. Requisiti prenotazioni
  6.1. istante di prenotazione (DataOra?)
  6.2. crociera prenotatata (v. req. 1)
  6.3. posti prenotati (Intero > 0)

