# Voli Aerei 1

## Requisiti 

I dati di interesse per il sistema sono voli, compagnie aeree ed aeroporti.

- Dei voli interessa rappresentare codice, durata, compagnia aerea ed aeroporti di partenza e arrivo.
- Degli aeroporti interessa rappresentare codice, nome, città (con nome e numero di abitanti) e nazione.
- Delle compagnie aeree interessa rappresentare nome, anno di fondazione, e la città in cui ha sede la direzione.

> TODO: durata minima di un volo
> durata: [(ore: intero >= 1, minuti: intero >= 0), (ore: intero >= 0, minuti: intero >= 1)]
> compagnia aerea più vecchia?

## UML

```mermaid
classDiagram
    class Nazione {
        nome: Stringa
        codice: Stringa lunga 3 maiuscola?
    }

    Citta "0..*" -- "1..1" Nazione : sta in?

    class Citta {
        nome: Stringa
        numero_di_abitanti: intero >= 0
    }
    class Citta["Città"]

    Aeroporto "0..*" -- "0..*" Citta : sta in?

    class Aeroporto {
        codice: Stringa?
        nome: Stringa
    } 

    Volo "0..*" -- "1..1" Aeroporto : parte da
    Volo "0..*" -- "1..1" Aeroporto : arriva a 

    class Volo {
        codice: Stringa?
        durata: (ore: intero >= 0, minuti: intero >= 0)
        compagnia_aerea: Stringa?
    }

    class Compagnia {
        nome: Stringa
        anno_di_fondazione: intero >= 1815
    }
    class Compagnia["Compagnia aerea"]

    Compagnia "0..*" -- "1..1" Citta : ha sede in
```
