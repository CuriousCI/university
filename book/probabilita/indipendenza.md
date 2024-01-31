# Indipendenza

## Spazio di probabilità prodotto

Siano $ (\Omega_1, \mathbb{P}_1) $ e $ (\Omega_2, \mathbb{P}_2) $ due schemi probabilistici _(Es. lancio di una moneta e misura della temperatura a Rio)_. Ora si considera l'esperimento congiunto 

$$ \Omega = \Omega_1 \times \Omega_2 = \{ (\omega_1, \omega_2) \mid \omega_1 \in \Omega_1, \omega_2 \in \Omega_2 \} $$

La scelta naturale per la probabilità $ \mathbb{P} $ è la probabilità **prodotto** 

$$ \mathbb{P}(\{\omega_1, \omega_2\}) = \mathbb{P}_1(\{\omega_1\}) \cdot \mathbb{P}_2(\{\omega_2\}) $$ 

Si può osservare che:

> Se $ \mathbb{P}_1, \mathbb{P}_2 $ sono le probabilità uniformi su $ \Omega_1, \Omega_2 $ allora $ \mathbb{P} $, probabilità prodotto, è la **probabilità uniforme** su $ \Omega $.

Infatti

$$ \mathbb{P}(\{\omega_1, \omega_2\}) = \frac{1}{|\Omega_1|} \cdot \frac{1}{|\Omega_2|} = \frac{1}{| \Omega_1 \times \Omega_2 |} = \frac{1}{| \Omega |} $$ 

$ \mathbb{P} $ soddisfa le seguenti condizioni di compatibilità:

- Sia $ A \subseteq \Omega $ un evento che posso decidere osservando l'esperimento descritto solo da $ (\Omega_1, \mathbb{P}_1) $, osservo che $ A = A_1 \times \Omega_2 $ con $ A_1 \subseteq \Omega_1 $, allora

$$ 
\mathbb{P}(A) = \sum_{(\omega_1, \omega_2)\in A_1 \times \Omega_2} \mathbb{P}_1(\{\omega_1\}) \cdot \mathbb{P}_2(\{\omega_2\}) =\\
= \sum_{\omega_1 \in A_1} \mathbb{P}(\{\omega_1\}) \cdot \sum_{\omega_2 \in \Omega_2} \mathbb{P}(\{\omega_2\}) =\\
= \sum_{\omega_1 \in A_1} \mathbb{P}(\{\omega_1\}) \cdot 1 = \mathbb{P}_1(A_1) 
$$

- Allo stesso modo, se $B$ è un evento deciso osservando solo $\Omega_2$, ovvero $B = \Omega_1 \times B_2$ con $B_2 \subseteq \Omega_2 $, si ha $ \mathbb{P}(B) = \mathbb{P}_2(B_2) $

Nello schema di **probabilità prodotto**, se $A$ è deciso solo da $\Omega_1$ e $B$ è deciso solo da $\Omega_2$, allora  $ \mathbb{P}(A \cap B) = \mathbb{P}(A) \cdot \mathbb{P}(B) $

$$
A_1 \subseteq \Omega_1, A = A_1 \times \Omega_2\\
B_2 \subseteq \Omega_2, B = \Omega_1 \times B_2\\
\mathbb{P}(A \cap B) = \mathbb{P}((A_1 \times \Omega_2) \cap (\Omega_1 \times B_2)) =\\ 
= \mathbb{P}(A_1 \times B_2) = \mathbb{P}_1(A_1) \cdot \mathbb{P}_2(B_2) =\\
= \mathbb{P}(A) \cdot \mathbb{P}(B)
$$

> In generale, dato lo schema probabilistico $(\Omega, \mathbb{P})$, due eventi $A,B \subseteq \Omega$ sono **indipendenti** quando $ \mathbb{P}(A \cap B) = \mathbb{P}(A) \cdot \mathbb{P}(B) $

<!-- TODO: esempio 1 estrazione da mazzo di 40, il fatto che sia 7 è indipendente dal fatto che sia "denari" -->

## Indipendenza di 3 eventi

Dato lo schema probabilistico $(\Omega, \mathbb{P})$, siano $A,B,C \subseteq \Omega$ ci sono almeno due modi di definire l'indipendenza di 3 eventi:

1. Indipendenza a coppie, per cui 
    - $ \mathbb{P}(A \cap B) = \mathbb{P}(A) \cdot \mathbb{P}(B) $
    - $ \mathbb{P}(A \cap C) = \mathbb{P}(A) \cdot \mathbb{P}(C) $
    - $ \mathbb{P}(B \cap C) = \mathbb{P}(B) \cdot \mathbb{P}(C) $

2. Indipendenza a terna, per cui
    - $ \mathbb{P}(A \cap B \cap C) = \mathbb{P}(A) \cdot \mathbb{P}(B) \cdot \mathbb{P}(C) $

Si dimostra che l'indipendenza di tipo $1$ **non implica** $2$ e l'indipendenza di tipo $2$ **non implica** $1$, per questo, quando si darà per assunta l'**ipotesi di indipendenza** si considerano sia l'indipendenza a coppie sia l'indipendenza a terna come vere.

###

<!-- TODO: esempio dado 4 facce, VRB 2 !-> 1 -->

## Indipendenza di $n$ eventi

Sia $ (\Omega, \mathbb{P}) $ uno schema probabilistico, $ A_1, A_2, ..., A_n \subseteq \Omega $ sono **indipendenti** quando presa una qualunque sottofamiglia di $A_1, ..., A_n$ la probabilità 
$ \mathbb{P}(A_1 \cap ... \cap A_n) = \mathbb{P}(A_1) \cdot ... \cdot \mathbb{P}(A_n) $

$$
\forall k, \forall (1 \leq i_1 \lt i_2 \lt ... \lt i_k \leq n)\\
\mathbb{P}(A_{i_1} \cap A_{i_2} \cap ... \cap A_{i_k}) =
\mathbb{P}(A_{i_1}) \cdot \mathbb{P}(A_{i_2}) \cdot ... \cdot \mathbb{P}(A_{i_k})
$$
