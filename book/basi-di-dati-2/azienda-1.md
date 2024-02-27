Si vuole sviluppare un sistema informativo per la gestione dei dati sul personale di una
certa azienda costituita da diversi dipartimenti. Durante la fase di raccolta dei requisiti
è stata prodotta la specifica dei requisiti mostrata di seguito.
Si chiede di iniziare la fase di Analisi dei requisiti ed in particolare di:
1. raffinare la specifica dei requisiti eliminando inconsistenze, omissioni o ridondanze
e produrre un elenco numerato di requisiti il meno ambiguo possibile
2. produrre un diagramma UML delle classi concettuale che modelli i dati di interesse,
utilizzando solo i costrutti di classe, associazione, attributo.

I dati di interesse per il sistema sono impiegati, dipartimenti, direttori dei dipartimenti e progetti aziendali.

Di ogni impiegato interessa conoscere il nome, il cognome, la data di nascita e lo stipendio attuale, il dipartimento (esattamente uno) al quale afferisce.

Di ogni dipartimento interessa conoscere il nome, il numero di telefono del centralino, e la data di afferenza di ognuno degli impiegati che vi lavorano.

Di ogni dipartimento interessa conoscere inoltre il direttore, che è uno degli impiegati dell’azienda.

Il sistema deve permettere di rappresentare i progetti aziendali nei quali sono coinvolti i diversi impiegati.

Di ogni progetto interessa il nome ed il budget.

Ogni impiegato può partecipare ad un numero qualsiasi di progetti.

```mermaid
classDiagram
	namespace Diagramma {
		class Progetto {
			nome: Stringa
			budget: Reale
			string nome
			double budget
		}

		class Impiegato {
			nome: Stringa
			cognome: Stringa
			data_di_nascita: Data
			stipendio: Reale
		}

		class Afferenza {
			data: Data
		}

		class Dipartimento {
			nome: Stringa
			telefono: Stringa
		}
	}

	namespace Tipi {
		class Color{
			<<enumeration>>
			RED
			BLUE
			GREEN
			WHITE
			BLACK
		}
	}


	namespace Istanze {
		class luigi {
			nome = Luigi
			cognome = Spada
			data_di_nascita = 1989-06-05
			stipendio = 1350.00€"
		}
		class luigi["luigi_1: Impiegato"]

		class aff {
			data = 2003-08-02
		}
		class aff["afferenza_1: Afferenza"]

		class dip {
			nome = "grafica"
			telefono = "+61 892187581"
		}
		class dip["grafica: Dipartimento"]

		class prog {
			nome = "TeslaX"
			budget = 2_000_000_069€
		}
		class prog["tesla: Progetto"]
	}


	Afferenza "1..1" <|-- "1..1" Impiegato : impiegato_afferenza
	Afferenza "1..1" --|> "1..1" Dipartimento : dipartimento_afferenza
	Impiegato "1..1" --|> "0..1" Dipartimento : dirige
	Impiegato "0..*" --|> "0..*" Progetto : partecipa a

	luigi ..|> Impiegato : <i><< istanza di >></i>
	aff ..|> Afferenza : <i><< istanza di >></i>
	dip ..|> Dipartimento : <i><< istanza di >></i>
	prog ..|> Progetto : <i><< istanza di >></i>
```

<style>
	.er.relationshipLine{
		marker-start: none;
		marker-end: none;
	}
	.er.attributeBoxEven {
		/* 	The box containing attributes on even-numbered rows  */ 
	}
	.er.attributeBoxOdd {
		/* 	The box containing attributes on odd-numbered rows  */ 
	}
	.er.entityBox {
		/* 	The box representing an entity  */ 
	}
	.er.entityLabel {
		/* 	The label for an entity  */ 
	}
	.er.relationshipLabel {
		/* 	The label for a relationship  */ 
	}
	.er.relationshipLabelBox {
		/* 	The box surrounding a relationship label  */ 
	}
	.er.relationshipLine {
		/* 	The line representing a relationship between entities  */ 
	}
</style>
