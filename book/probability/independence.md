# Indipendenza

## Spazio di probabilità prodotto

Siano \\( (\Omega\_1, \mathbb{P}\_1) \\) e \\( (\Omega\_2, \mathbb{P}\_2) \\) due schemi probabilistici _(Es. lancio di una moneta e misura della temperatura a Rio)_. Ora si considera l'esperimento congiunto 

$$ \Omega = \Omega\_1 \times \Omega\_2 = \\{ (\omega\_1, \omega\_2) \mid \omega\_1 \in \Omega\_1, \omega\_2 \in \Omega\_2 \\} $$

La scelta naturale per la probabilità \\( \mathbb{P} \\) è la probabilità **prodotto** 

$$ \mathbb{P}(\\{\omega\_1, \omega\_2\\}) = \mathbb{P}\_1(\\{\omega\_1\\}) \cdot \mathbb{P}\_2(\\{\omega\_2\\}) $$ 

Si può osservare che:

> Se \\( \mathbb{P}\_1, \mathbb{P}\_2 \\) sono le probabilità uniformi su \\( \Omega\_1, \Omega\_2 \\) allora \\( \mathbb{P} \\), probabilità prodotto, è la **probabilità uniforme** su \\( \Omega \\).

Infatti

$$ \mathbb{P}(\\{\omega\_1, \omega\_2\\}) = \frac{1}{|\Omega\_1|} \cdot \frac{1}{|\Omega\_2|} = \frac{1}{| \Omega\_1 \times \Omega\_2 |} = \frac{1}{| \Omega |} $$ 

\\( \mathbb{P} \\) soddisfa le seguenti condizioni di compatibilità:

- Sia \\( A \subseteq \Omega \\) un evento che posso decidere osservando l'esperimento descritto solo da \\( (\Omega\_1, \mathbb{P}\_1) \\), osservo che \\( A = A\_1 \times \Omega\_2 \\) con \\( A\_1 \subseteq \Omega\_1 \\), allora

$$ 
\mathbb{P}(A) = \sum\_{(\omega\_1, \omega\_2)\in A\_1 \times \Omega\_2} \mathbb{P}\_1(\\{\omega\_1\\}) \cdot \mathbb{P}\_2(\\{\omega\_2\\}) =\\\\
= \sum\_{\omega\_1 \in A\_1} \mathbb{P}(\\{\omega\_1\\}) \cdot \sum\_{\omega\_2 \in \Omega\_2} \mathbb{P}(\\{\omega\_2\\}) =\\\\
= \sum\_{\omega\_1 \in A\_1} \mathbb{P}(\\{\omega\_1\\}) \cdot 1 = \mathbb{P}\_1(A\_1) 
$$

- Allo stesso modo, se \\(B\\) è un evento deciso osservando solo \\(\Omega\_2\\), ovvero \\(B = \\Omega\_1 \times B\_2\\) con \\(B\_2 \subseteq \Omega\_2 \\), si ha \\( \mathbb{P}(B) = \mathbb{P}\_2(B\_2) \\)

Nello schema di **probabilità prodotto**, se \\(A\\) è deciso solo da \\(\Omega\_1\\) e \\(B\\) è deciso solo da \\(\Omega\_2\\), allora  \\( \mathbb{P}(A \cap B) = \mathbb{P}(A) \cdot \mathbb{P}(B) \\)

$$
A\_1 \subseteq \Omega\_1, A = A\_1 \times \Omega\_2\\\\
B\_2 \subseteq \Omega\_2, B = \Omega\_1 \times B\_2\\\\
\mathbb{P}(A \cap B) = \mathbb{P}((A\_1 \times \Omega\_2) \cap (\Omega\_1 \times B\_2)) =\\\\ 
= \mathbb{P}(A\_1 \times B\_2) = \mathbb{P}\_1(A\_1) \cdot \mathbb{P}\_2(B\_2) =\\\\
= \mathbb{P}(A) \cdot \mathbb{P}(B)
$$

> In generale, dato lo schema probabilistico \\((\Omega, \mathbb{P})\\), due eventi \\(A,B \subseteq \Omega\\) sono **indipendenti** quando \\( \mathbb{P}(A \cap B) = \mathbb{P}(A) \cdot \mathbb{P}(B) \\)

<!-- TODO: esempio 1 estrazione da mazzo di 40, il fatto che sia 7 è indipendente dal fatto che sia "denari" -->

## Indipendenza di 3 eventi

Dato lo schema probabilistico \\((\Omega, \mathbb{P})\\), siano \\(A,B,C \subseteq \Omega\\) ci sono almeno due modi di definire l'indipendenza di 3 eventi:

1. Indipendenza a coppie, per cui 
    - \\( \mathbb{P}(A \cap B) = \mathbb{P}(A) \cdot \mathbb{P}(B) \\)
    - \\( \mathbb{P}(A \cap C) = \mathbb{P}(A) \cdot \mathbb{P}(C) \\)
    - \\( \mathbb{P}(B \cap C) = \mathbb{P}(B) \cdot \mathbb{P}(C) \\)

2. Indipendenza a terna, per cui
    - \\( \mathbb{P}(A \cap B \cap C) = \mathbb{P}(A) \cdot \mathbb{P}(B) \cdot \mathbb{P}(C) \\)

Si dimostra che l'indipendenza di tipo \\(1\\) **non implica** \\(2\\) e l'indipendenza di tipo \\(2\\) **non implica** \\(1\\), per questo, quando si darà per assunta l'**ipotesi di indipendenza** si considerano sia l'indipendenza a coppie sia l'indipendenza a terna come vere.

###

<!-- TODO: esempio dado 4 facce, VRB 2 !-> 1 -->

## Indipendenza di \\(n\\) eventi

Sia \\( (\Omega, \mathbb{P}) \\) uno schema probabilistico, \\( A\_1, A\_2, ..., A\_n \subseteq \Omega \\) sono **indipendenti** quando presa una qualunque sottofamiglia di \\(A\_1, ..., A\_n\\) la probabilità 
\\( \mathbb{P}(A\_1 \cap ... \cap A\_n) = \mathbb{P}(A\_1) \cdot ... \cdot \mathbb{P}(A\_n) \\)

$$
\forall k, \forall (1 \leq i\_1 \lt i\_2 \lt ... \lt i\_k \leq n)\\\\
\mathbb{P}(A\_{i\_1} \cap A\_{i\_2} \cap ... \cap A\_{i\_k}) =\\\\
= \mathbb{P}(A\_{i\_1}) \cdot \mathbb{P}(A\_{i\_2}) \cdot ... \cdot \mathbb{P}(A\_{i\_k})
$$
