# eBuy

## Introduzione

Si vuole progettare e realizzare eBuy, un sistema informatico per la gestione di aste on-line e di attività di commercio elettronico.

Il sistema deve permettere, agli utenti registrati, di pubblicare annunci per la vendita di oggetti e di gestire aste al rialzo per la loro aggiudicazione. Il sistema deve anche consentire di mettere in vendita oggetti senza l’effettuazione di alcun’asta (formula “compralo subito”).

## Specifica dei Requisiti

Il sistema deve permettere agli utenti registrati (di cui interessa il nome scelto e la data di registrazione) di pubblicare annunci per la vendita di singoli oggetti. 

Tali annunci sono chiamati post. 

Degli oggetti in vendita va specificata una descrizione, la categoria alla quale appartiene, il prezzo di vendita, i metodi di pagamento accettati (bonifico o carta di credito), e l’informazione sul fatto che l’oggetto sia nuovo oppure usato.

Gli annunci di vendita (post) sono di due tipologie distinte, potendo prevedere o meno un’asta al rialzo per la loro aggiudicazione. Per i post che prevedono un’asta, il venditore deve specificare il prezzo iniziale d’asta, l’ammontare dei singoli rialzi (ad es., 5 euro a rialzo) e l’istante di scadenza dell’asta. 

Al contrario, per i post che non prevedono un’asta (modalità di vendita “compralo subito”), al venditore è richiesto specificare esclusivamente il prezzo di vendita dell’oggetto.

Il sistema deve consentire agli utenti (via Web) di pubblicare post per oggetti in vendita, con o senza asta.

Gli oggetti relativi a post che non prevedono asta vengono venduti al primo utente che procede con l’acquisto. 

I post che prevedono un’asta, invece, diventano oggetto di offerte di acquisto da parte di più utenti. 

Tali offerte vengono comunemente chiamate bid. 

Di ogni bid interessa l’istante in cui è stato proposto e l’utente offerente (chiamato bidder). 

Dato che i post oggetto d’asta specificano sia il prezzo iniziale che l’ammontare dei singoli rialzi, quando un bidder decide di proporre un bid per tale post, di fatto si propone di acquistare l’oggetto in questione per un prezzo che è pari all’ultimo prezzo proposto fino a quel momento, aumentato dell’ammontare del rialzo (valore deciso a priori dal venditore). 

Ad esempio, se il prezzo del bid più recente è x euro e l’ammontare del rialzo è di r euro, il nuovo bidder si propone di acquistarlo per x + r euro.

Il sistema deve consentire ad un utente (da Web) di proporre un nuovo bid per un oggetto in vendita tramite asta, oppure procedere all’acquisto di un oggetto messo in vendita con la modalità “compralo subito”.

Le aste vengono automaticamente chiuse alla data/ora specificata dal venditore. 

A questo istante, l’ultimo utente che ha effettuato un bid si aggiudica l’oggetto in vendita, al prezzo del bid. 

Di ogni asta conclusa è di interesse conoscere il bid che si è aggiudicato l’oggetto in vendita (se esiste), con il prezzo relativo. 

Per motivi legali, i venditori di oggetti nuovi devono prevedere una garanzia di almeno due anni (minimo di legge), mentre per quelli usati non c’è alcun obbligo di garanzia (che però può essere ugualmente prevista). 

L’informazione circa la durata della garanzia (se presente) deve essere dichiarata dal venditore e mantenuta dal sistema. 

Per gli oggetti usati, al venditore viene anche richiesto di dichiararne le condizioni, nella gamma di valori ottimo, buono, discreto, da sistemare.

## Raffinamento dei Requisiti

- utenti registrati
    - nome scelto
    - data di registrazione

- annunci (o post)
    - singolo oggetto
    - di due tipi
        - con l'asta
            - prezzo iniziale d'asta
            - ammontare dei singoli rialzi (5 euro al rialzo?)
            - istante di scadenza
            - più utenti (bid)
            - automaticamente chiuse alla data/ora specificata dal venditore
            - bid finale con il prezzo relativo
        - senza
            - una sola persona a cui l'ho venduto

- bid
    - istante
    - bidder
    - ammontare?
    - ultimo prezzo proposto fino a quel momento


- oggetti (in vendita)
    - descrizione
    - categoria
    - prezzo di vendita
    - metodi di pagamento accettati (bonifico / carta di credito)
    - uno di due tipi
        - nuovo
            - garanzia di almeno 2 anni
        - o usato
            - opzionalmente garanzia
            - condizioni (ottimo, buono, discreto, da sistemare)
        - garanzia dichiarata dal venditore
