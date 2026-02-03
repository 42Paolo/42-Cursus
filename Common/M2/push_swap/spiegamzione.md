# Documentazione Dettagliata del Programma Push_Swap

## Indice
1. [Panoramica Generale](#panoramica-generale)
2. [Strutture Dati](#strutture-dati)
3. [Fase 1: Parsing e Validazione degli Input](#fase-1-parsing-e-validazione-degli-input)
4. [Fase 2: Assegnazione degli Indici](#fase-2-assegnazione-degli-indici)
5. [Fase 3: Algoritmi di Ordinamento](#fase-3-algoritmi-di-ordinamento)
6. [Operazioni sullo Stack](#operazioni-sullo-stack)
7. [Gestione della Memoria ed Errori](#gestione-della-memoria-ed-errori)
8. [Flusso di Esecuzione Completo](#flusso-di-esecuzione-completo)

---

## Panoramica Generale

**Push_swap** è un programma in C che ordina una sequenza di numeri interi utilizzando due stack (A e B) e un insieme limitato di operazioni. L'obiettivo è ordinare i numeri nello stack A in ordine crescente utilizzando il minor numero possibile di operazioni.

### Obiettivo del Programma
- **Input**: Una lista di numeri interi (forniti come argomenti da riga di comando)
- **Output**: Una sequenza di operazioni che ordina i numeri
- **Vincolo**: Minimizzare il numero di operazioni utilizzate

### Perché Esiste
Questo programma è un esercizio di algoritmi e strutture dati che insegna:
- Manipolazione di liste concatenate (linked lists)
- Ottimizzazione di algoritmi
- Gestione della memoria in C
- Analisi della complessità computazionale

---

## Strutture Dati

### La Struttura `t_stack`

```c
typedef struct s_stack
{
    int             value;        // Il valore numerico effettivo
    int             index;        // Posizione relativa nell'ordinamento (1 = minimo, 2 = secondo minimo, ecc.)
    int             pos;          // Posizione attuale nello stack (0 = top)
    int             target_pos;   // Posizione target nello stack A quando viene spostato da B
    int             cost_a;       // Costo (numero di operazioni) per posizionare nello stack A
    int             cost_b;       // Costo (numero di operazioni) per portare in cima allo stack B
    struct s_stack  *next;        // Puntatore al prossimo elemento
}   t_stack;
```

#### Spiegazione dei Campi

1. **`value`**: Il numero intero inserito dall'utente
   - Esempio: Se l'input è `5 2 8`, avremo tre nodi con value = 5, 2, 8

2. **`index`**: Un numero che rappresenta la posizione relativa nell'ordinamento finale
   - Il numero più piccolo ha index = 1
   - Il secondo più piccolo ha index = 2
   - E così via...
   - Esempio: Per i valori [5, 2, 8], gli index saranno: 2->index=1, 5->index=2, 8->index=3
   - **Perché è utile**: Permette di confrontare facilmente la "grandezza" relativa dei numeri senza preoccuparsi dei valori effettivi

3. **`pos`**: La posizione fisica nello stack
   - 0 = elemento in cima (top)
   - 1 = secondo elemento
   - 2 = terzo elemento, ecc.
   - **Perché è utile**: Serve per calcolare quante rotazioni servono per portare un elemento in cima

4. **`target_pos`**: Usato durante l'algoritmo principale
   - Quando un elemento è in B, target_pos indica dove dovrebbe andare in A
   - **Perché è utile**: Permette di pianificare dove inserire ogni elemento quando lo spostiamo da B ad A

5. **`cost_a` e `cost_b`**: Costi per le operazioni
   - Numero positivo = rotazioni normali (ra/rb)
   - Numero negativo = rotazioni inverse (rra/rrb)
   - **Perché è utile**: Permette di scegliere la mossa più efficiente

6. **`next`**: Puntatore al prossimo nodo
   - NULL per l'ultimo elemento
   - **Perché è utile**: Implementa la struttura di lista concatenata dello stack

---

## Fase 1: Parsing e Validazione degli Input

### Punto di Ingresso: `main()`

```c
int main(int argc, char **argv)
{
    t_stack *stack_a;
    t_stack *stack_b;
    
    if (argc < 2)
        return (0);  // Nessun argomento = uscita silenziosa
    
    stack_a = NULL;
    stack_b = NULL;
    parse_arguments(argc, argv, &stack_a);
    // ... resto del codice
}
```

#### Cosa Fa
1. Controlla se ci sono argomenti da processare
2. Inizializza i due stack (A e B) a NULL
3. Chiama `parse_arguments()` per processare l'input

---

### Funzione `parse_arguments()`

Questa funzione gestisce due modalità di input diverse:

#### Modalità 1: Stringa Singola con Spazi
```bash
./push_swap "5 2 8 1"
```

**Come funziona:**
```c
if (argc == 2)
    parse_string(argv[1], stack_a);
```

1. Riconosce che c'è un solo argomento
2. Chiama `parse_string()` che:
   - Divide la stringa usando gli spazi come separatori (tramite `ft_split()`)
   - Crea un array di stringhe: ["5", "2", "8", "1"]
   - Processa ogni numero separatamente

**Esempio di split:**
```
Input:  "5 2 8 1"
        ↓ ft_split(str, ' ')
Array:  ["5"]["2"]["8"]["1"][NULL]
```

#### Modalità 2: Argomenti Multipli
```bash
./push_swap 5 2 8 1
```

**Come funziona:**
```c
else
    parse_multiple_args(argc, argv, stack_a);
```

1. Prende ogni argomento separatamente da argv
2. Processa direttamente i numeri (argv[1] = "5", argv[2] = "2", ecc.)

---

### Validazione dei Numeri: `process_number()`

Per ogni stringa contenente un numero, viene eseguita questa validazione:

#### Step 1: Verifica che Sia un Numero Valido (`is_number()`)

```c
int is_number(char *str)
{
    int i = 0;
    if (str[i] == '-' || str[i] == '+')
        i++;              // Il segno è opzionale all'inizio
    if (!str[i])
        return (0);       // Solo un segno senza cifre = invalido
    while (str[i])
    {
        if (str[i] < '0' || str[i] > '9')
            return (0);   // Carattere non numerico = invalido
        i++;
    }
    return (1);           // Valido
}
```

**Esempi:**
- ✅ "42" → valido
- ✅ "-42" → valido
- ✅ "+42" → valido
- ❌ "4a2" → invalido (contiene 'a')
- ❌ "- 42" → invalido (spazio dopo il segno)
- ❌ "-" → invalido (solo segno)

#### Step 2: Conversione a Numero (`ft_atol()`)

```c
long ft_atol(const char *str)
{
    long result = 0;
    int sign = 1;
    int i = 0;
    
    // Salta spazi bianchi
    while (str[i] == ' ' || (str[i] >= 9 && str[i] <= 13))
        i++;
    
    // Gestisce il segno
    if (str[i] == '-' || str[i] == '+')
    {
        if (str[i] == '-')
            sign = -1;
        i++;
    }
    
    // Converte cifra per cifra
    while (str[i] >= '0' && str[i] <= '9')
    {
        result = result * 10 + (str[i] - '0');
        i++;
    }
    
    return (result * sign);
}
```

**Come funziona la conversione:**
```
Stringa: "-123"
i=0: carattere '-' → sign = -1, i++
i=1: carattere '1' → result = 0 * 10 + 1 = 1
i=2: carattere '2' → result = 1 * 10 + 2 = 12
i=3: carattere '3' → result = 12 * 10 + 3 = 123
Ritorna: 123 * (-1) = -123
```

**Perché usa `long` invece di `int`:**
- Per rilevare overflow: se il numero è > INT_MAX o < INT_MIN, viene rilevato e genera errore

#### Step 3: Verifica dei Limiti

```c
if (num > INT_MAX || num < INT_MIN)
{
    free_split(numbers);
    free_stack(stack);
    error_exit();
}
```

**Limiti in C:**
- INT_MAX = 2147483647
- INT_MIN = -2147483648

**Esempi:**
- ✅ 2147483647 → valido
- ❌ 2147483648 → errore (troppo grande)

#### Step 4: Aggiunta allo Stack

```c
add_to_stack(stack, (int)num);
```

Crea un nuovo nodo e lo aggiunge in fondo allo stack.

---

### Rilevamento dei Duplicati

Dopo aver aggiunto tutti i numeri, controlla che non ci siano duplicati:

```c
int has_duplicates(t_stack *stack)
{
    while (stack)
    {
        t_stack *tmp = stack->next;
        while (tmp)
        {
            if (stack->value == tmp->value)
                return (1);  // Trovato duplicato!
            tmp = tmp->next;
        }
        stack = stack->next;
    }
    return (0);  // Nessun duplicato
}
```

**Come funziona:**
1. Prende ogni elemento dello stack
2. Lo confronta con tutti gli elementi successivi
3. Se trova due valori uguali, ritorna 1 (errore)

**Complessità:** O(n²) - Ogni elemento viene confrontato con tutti gli altri

**Esempio:**
```
Stack: 5 → 2 → 8 → 2
       ↓
5 confrontato con: 2, 8, 2 ✓
       ↓
2 confrontato con: 8, 2 → DUPLICATO TROVATO! ❌
```

---

### Gestione degli Errori nel Parsing

In caso di errore durante il parsing:

```c
void error_exit(void)
{
    ft_putstr("Error\n");
    exit(1);
}
```

**Quando viene chiamato:**
- Numero non valido (caratteri non numerici)
- Overflow (numero troppo grande o piccolo)
- Duplicati
- Errore di allocazione memoria

**Comportamento:**
- Stampa "Error\n" su stdout
- Esce con codice 1
- Prima di uscire, tutta la memoria allocata viene liberata

---

## Fase 2: Assegnazione degli Indici

### Perché Servono gli Indici?

Gli indici trasformano i valori arbitrari in posizioni relative, semplificando gli algoritmi di ordinamento.

**Esempio:**
```
Valori:    [42, -7, 100, 0, 58]
           ↓ Assegnazione indici
Indici:    [3,  1,  5,   2, 4]
```

**Vantaggi:**
- Non importa se i numeri sono grandi, piccoli, negativi o positivi
- Gli algoritmi possono basarsi su confronti semplici: "index < size/2"
- Diventa facile identificare min e max

---

### Funzione `assign_index()`

```c
void assign_index(t_stack *stack_a, int stack_size)
{
    t_stack *current;
    int index = 1;
    
    while (index <= stack_size)
    {
        current = get_next_min(stack_a);  // Trova il prossimo minimo
        if (current)
            current->index = index;        // Assegna l'indice
        index++;
    }
}
```

**Come funziona:**
1. Inizia con index = 1
2. Trova l'elemento con il valore più piccolo tra quelli che non hanno ancora un indice
3. Assegna index = 1 a quell'elemento
4. Ripete per index = 2, 3, 4... fino a coprire tutti gli elementi

---

### Funzione `get_next_min()`

```c
static t_stack *get_next_min(t_stack *stack)
{
    t_stack *min = NULL;
    int has_min = 0;
    
    while (stack)
    {
        // Cerca elementi con index == 0 (non ancora assegnato)
        if (stack->index == 0 && (!has_min || stack->value < min->value))
        {
            min = stack;
            has_min = 1;
        }
        stack = stack->next;
    }
    return (min);
}
```

**Procedimento dettagliato:**

```
Iterazione 1: Cerca elementi con index=0, trova il minimo
Stack: [42:0] [−7:0] [100:0] [0:0] [58:0]
              ↑ 
       Valore più piccolo = -7
       Assegna: -7->index = 1

Iterazione 2: Cerca elementi con index=0, trova il minimo
Stack: [42:0] [−7:1] [100:0] [0:0] [58:0]
                              ↑
       Valore più piccolo tra quelli con index=0 è 0
       Assegna: 0->index = 2

Iterazione 3:
Stack: [42:0] [−7:1] [100:0] [0:2] [58:0]
        ↑
       Assegna: 42->index = 3

Iterazione 4:
Stack: [42:3] [−7:1] [100:0] [0:2] [58:0]
                                     ↑
       Assegna: 58->index = 4

Iterazione 5:
Stack: [42:3] [−7:1] [100:0] [0:2] [58:4]
                      ↑
       Assegna: 100->index = 5

Risultato finale:
Stack: [42:3] [−7:1] [100:5] [0:2] [58:4]
```

**Complessità:** O(n²) - Per ogni elemento deve scorrere tutto lo stack

---

## Fase 3: Algoritmi di Ordinamento

Il programma usa algoritmi diversi in base alla dimensione dell'input:

### 1. Stack di 2 Elementi

```c
if (stack_size(stack_a) == 2)
    sa(&stack_a, 1);
```

**Logica:**
- Se ci sono solo 2 elementi, basta scambiarli se sono nel ordine sbagliato
- Operazione `sa` (swap a): scambia i primi due elementi dello stack A

**Esempio:**
```
Prima:  [5] [2]
        ↓ sa
Dopo:   [2] [5]
```

---

### 2. Stack di 3 Elementi: `sort_three()`

```c
void sort_three(t_stack **stack_a)
{
    int highest;
    
    if (is_sorted(*stack_a))
        return;

    highest = find_highest_index(*stack_a);
    
    if ((*stack_a)->index == highest)
        ra(stack_a, 1);           // Ruota se il massimo è in cima
    else if ((*stack_a)->next->index == highest)
        rra(stack_a, 1);          // Ruota indietro se il massimo è in mezzo
    
    if ((*stack_a)->index > (*stack_a)->next->index)
        sa(stack_a, 1);           // Scambia i primi due se necessario
}
```

**Logica:**
1. Se già ordinato, non fa nulla
2. Identifica l'elemento con l'indice più alto (il massimo)
3. Porta il massimo in fondo usando rotazioni
4. Se i primi due elementi sono nell'ordine sbagliato, li scambia

**Tutti i casi possibili per 3 elementi:**

```
Caso 1: [3][2][1]   → ra → [2][1][3] → sa → [1][2][3] ✓
Caso 2: [3][1][2]   → ra → [1][2][3] ✓
Caso 3: [2][3][1]   → rra → [1][2][3] ✓
Caso 4: [2][1][3]   → sa → [1][2][3] ✓
Caso 5: [1][3][2]   → rra → [2][1][3] → sa → [1][2][3] ✓
Caso 6: [1][2][3]   → già ordinato ✓
```

**Numero massimo di operazioni:** 2 (molto efficiente)

---

### 3. Stack di 4-5 Elementi: `sort_small()`

```c
void sort_small(t_stack **stack_a, t_stack **stack_b)
{
    int size = stack_size(*stack_a);
    int min_pos;
    
    while (size > 3)
    {
        min_pos = get_min_index_pos(stack_a);
        
        // Porta il minimo in cima
        if (min_pos <= size / 2)
        {
            // Il minimo è nella prima metà: usa rotazioni normali
            while (min_pos-- > 0)
                ra(stack_a, 1);
        }
        else
        {
            // Il minimo è nella seconda metà: usa rotazioni inverse
            while (min_pos++ < size)
                rra(stack_a, 1);
        }
        
        pb(stack_a, stack_b, 1);  // Sposta il minimo in B
        size--;
    }
    
    sort_three(stack_a);          // Ordina i 3 rimasti in A
    
    while (*stack_b)
        pa(stack_a, stack_b, 1);  // Riporta tutto in A
}
```

**Strategia:**
1. Trova ripetutamente il numero più piccolo
2. Portalo in cima usando la via più breve (rotazione normale o inversa)
3. Spostalo in stack B
4. Ripeti fino a lasciare solo 3 elementi in A
5. Ordina i 3 elementi rimasti
6. Riporta tutti gli elementi da B ad A (che sono già in ordine crescente)

**Esempio con 5 elementi [5, 2, 4, 1, 3]:**

```
Indici: [5:4] [2:2] [4:3] [1:1] [3:3]

Passo 1: Trova minimo (index=1, pos=3)
        pos=3 > size/2=2 → usa rra
        [3:3] [5:4] [2:2] [4:3] [1:1]
        [1:1] [3:3] [5:4] [2:2] [4:3]
        pb → B: [1:1]  A: [3:3] [5:4] [2:2] [4:3]

Passo 2: Trova minimo (index=2, pos=2)
        pos=2 > size/2=2 → usa rra
        [4:3] [3:3] [5:4] [2:2]
        [2:2] [4:3] [3:3] [5:4]
        pb → B: [2:2] [1:1]  A: [4:3] [3:3] [5:4]

Passo 3: Ordina i 3 in A
        [4:3] [3:3] [5:4] → sort_three
        [3:3] [4:3] [5:4]

Passo 4: Riporta da B ad A
        pa → [2:2] [3:3] [4:3] [5:4]
        pa → [1:1] [2:2] [3:3] [4:3] [5:4] ✓
```

**Perché la Scelta tra ra e rra:**
- Se l'elemento è nella prima metà, è più veloce ruotare in avanti
- Se è nella seconda metà, è più veloce ruotare indietro
- Questo minimizza il numero di operazioni

---

### 4. Stack di 6+ Elementi: Algoritmo Principale `sort()`

Questo è l'algoritmo più complesso, basato sul calcolo dei costi.

#### Fase 1: `push_all_but_three()`

```c
static void push_all_but_three(t_stack **stack_a, t_stack **stack_b)
{
    int size = stack_size(*stack_a);
    int pushed = 0;
    int i = 0;
    
    // Prima fase: sposta metà degli elementi (quelli più piccoli)
    while (size > 6 && i < size && pushed < size / 2)
    {
        if ((*stack_a)->index <= size / 2)
        {
            pb(stack_a, stack_b, 1);
            pushed++;
        }
        else
            ra(stack_a, 1);
        i++;
    }
    
    // Seconda fase: sposta tutto tranne 3
    while (size - pushed > 3)
    {
        pb(stack_a, stack_b, 1);
        pushed++;
    }
}
```

**Strategia in due fasi:**

**Fase 1:** Sposta prima i numeri più piccoli (index <= size/2)
- Questo crea una base ordinata in B
- Gli elementi più grandi rimangono in A
- Limita il numero di elementi spostati a size/2

**Fase 2:** Sposta tutto il resto tranne 3 elementi
- Gli ultimi 3 elementi in A saranno ordinati con sort_three()

**Esempio con 10 elementi [10, 3, 7, 1, 9, 2, 8, 4, 6, 5]:**

```
Indici: [10:9] [3:3] [7:6] [1:1] [9:8] [2:2] [8:7] [4:4] [6:5] [5:5]

Fase 1 - Sposta index <= 5 (metà inferiore):
[10:9]                → index=9 > 5 → ra
[3:3] [7:6] [1:1] ... → index=3 <= 5 → pb
[7:6]                 → index=6 > 5 → ra
[1:1]                 → index=1 <= 5 → pb
... continua fino a pushed = 5

Risultato Fase 1:
A: [10:9] [9:8] [8:7] [7:6] [6:5]  (elementi grandi)
B: [5:5] [4:4] [2:2] [1:1] [3:3]  (elementi piccoli, non ordinati)

Fase 2 - Sposta tutto tranne 3:
A: [10:9] [9:8] [8:7] [7:6] [6:5]
pb → B: [6:5] ...  A: [10:9] [9:8] [8:7] [7:6]
pb → B: [7:6] ...  A: [10:9] [9:8] [8:7]

Risultato Fase 2:
A: [10:9] [9:8] [8:7]  (solo 3 elementi)
B: [7:6] [6:5] [5:5] [4:4] [2:2] [1:1] [3:3]
```

---

#### Fase 2: Ordina i 3 Elementi Rimasti in A

```c
sort_three(stack_a);
```

Dopo questa operazione, i 3 elementi in A sono ordinati.

---

#### Fase 3: Ciclo Principale - Riporta Elementi da B ad A

```c
while (*stack_b)
{
    get_target_position(stack_a, stack_b);
    get_cost(stack_a, stack_b);
    do_cheapest_move(stack_a, stack_b);
}
```

Questo ciclo si ripete fino a svuotare B, e per ogni iterazione:

1. **Calcola le posizioni target** (`get_target_position`)
2. **Calcola i costi** (`get_cost`)
3. **Esegue la mossa più economica** (`do_cheapest_move`)

---

##### 3.1 - `get_target_position()`: Trova Dove Inserire

```c
void get_target_position(t_stack **stack_a, t_stack **stack_b)
{
    t_stack *current_b;
    int target_pos;
    
    current_b = *stack_b;
    get_position(stack_a);  // Aggiorna le posizioni in A
    get_position(stack_b);  // Aggiorna le posizioni in B
    
    while (current_b)
    {
        target_pos = get_target(*stack_a, current_b->index, INT_MAX, 0);
        current_b->target_pos = target_pos;
        current_b = current_b->next;
    }
}
```

**Primo Step: Aggiorna le Posizioni**

```c
void get_position(t_stack **stack)
{
    t_stack *current = *stack;
    int pos = 0;
    
    while (current)
    {
        current->pos = pos;
        pos++;
        current = current->next;
    }
}
```

Assegna a ogni elemento la sua posizione fisica attuale (0, 1, 2, ...).

**Secondo Step: Calcola il Target per Ogni Elemento in B**

```c
static int get_target(t_stack *stack_a, int index_b, int target_index, int target_pos)
{
    t_stack *current = stack_a;
    
    // Cerca il più piccolo elemento in A che è più grande di index_b
    while (current)
    {
        if (current->index > index_b && current->index < target_index)
        {
            target_index = current->index;
            target_pos = current->pos;
        }
        current = current->next;
    }
    
    // Se trovato, ritorna la posizione
    if (target_index != INT_MAX)
        return (target_pos);
    
    // Altrimenti, cerca il minimo in A (wrap-around)
    current = stack_a;
    while (current)
    {
        if (current->index < target_index)
        {
            target_index = current->index;
            target_pos = current->pos;
        }
        current = current->next;
    }
    return (target_pos);
}
```

**Logica del Target:**

L'elemento in B deve essere inserito:
1. **Prima dell'elemento più piccolo in A che è più grande di lui**
   - Esempio: B ha index=5, A ha [3, 7, 9] → target è pos di 7
2. **Se non esiste (B è il massimo), va prima del minimo in A**
   - Esempio: B ha index=10, A ha [3, 7, 9] → target è pos di 3

**Esempio Visivo:**

```
A: [3:pos0] [7:pos1] [9:pos2]
B: [5:pos0]

Per B->index=5:
- Cerca in A elementi > 5: trova 7 e 9
- Il più piccolo tra questi è 7 (pos=1)
- Quindi target_pos = 1

Significato: l'elemento 5 di B andrà inserito prima del 7 in A
```

---

##### 3.2 - `get_cost()`: Calcola i Costi delle Operazioni

```c
void get_cost(t_stack **stack_a, t_stack **stack_b)
{
    t_stack *current_b = *stack_b;
    int size_a = stack_size(*stack_a);
    int size_b = stack_size(*stack_b);
    
    while (current_b)
    {
        // Costo per portare l'elemento in cima a B
        current_b->cost_b = current_b->pos;
        if (current_b->pos > size_b / 2)
            current_b->cost_b = (size_b - current_b->pos) * -1;
        
        // Costo per preparare la posizione target in A
        current_b->cost_a = current_b->target_pos;
        if (current_b->target_pos > size_a / 2)
            current_b->cost_a = (size_a - current_b->target_pos) * -1;
        
        current_b = current_b->next;
    }
}
```

**Logica dei Costi:**

1. **Costo Positivo**: Rotazioni normali (ra/rb)
2. **Costo Negativo**: Rotazioni inverse (rra/rrb)

**Perché Negativo per la Seconda Metà:**
- Se un elemento è oltre la metà dello stack, è più veloce ruotare al contrario
- Esempio: Stack di 10 elementi, elemento in posizione 8
  - Rotazioni normali: 8 mosse
  - Rotazioni inverse: 10 - 8 = 2 mosse (molto più efficiente!)

**Esempio di Calcolo:**

```
Stack B (size=6): [E0] [E1] [E2] [E3] [E4] [E5]
                   pos0  pos1  pos2  pos3  pos4  pos5

E1: pos=1, size_b/2=3
    1 <= 3 → cost_b = 1 (1 rotazione normale)

E4: pos=4, size_b/2=3
    4 > 3 → cost_b = (6-4)*(-1) = -2 (2 rotazioni inverse)

Stack A (size=5): [A0:7] [A1:9] [A2:3] [A3:11] [A4:6]
E1->target_pos = 2 (va prima del 3)
    2 <= 2 → cost_a = 2

E4->target_pos = 4 (va prima del 6)
    4 > 2 → cost_a = (5-4)*(-1) = -1
```

**Costo Totale:**
- E1: |cost_a| + |cost_b| = |2| + |1| = 3 operazioni
- E4: |cost_a| + |cost_b| = |-1| + |-2| = 1 + 2 = 3 operazioni

---

##### 3.3 - `do_cheapest_move()`: Esegue la Mossa Più Economica

```c
void do_cheapest_move(t_stack **stack_a, t_stack **stack_b)
{
    t_stack *current = *stack_b;
    int cheapest = INT_MAX;
    int cost_a;
    int cost_b;
    
    // Trova l'elemento con il costo totale minimo
    while (current)
    {
        if (ft_abs(current->cost_a) + ft_abs(current->cost_b) < cheapest)
        {
            cheapest = ft_abs(current->cost_a) + ft_abs(current->cost_b);
            cost_a = current->cost_a;
            cost_b = current->cost_b;
        }
        current = current->next;
    }
    
    do_move(stack_a, stack_b, cost_a, cost_b);
}
```

**Strategia:**
1. Scorre tutti gli elementi in B
2. Calcola il costo totale per ognuno (|cost_a| + |cost_b|)
3. Sceglie quello con il costo minimo
4. Esegue le operazioni necessarie

---

##### 3.4 - `do_move()`: Esegue le Operazioni Ottimizzate

```c
static void do_move(t_stack **stack_a, t_stack **stack_b, int cost_a, int cost_b)
{
    // Fase 1: Rotazioni simultanee (ottimizzazione)
    while (cost_a > 0 && cost_b > 0)
    {
        rr(stack_a, stack_b, 1);  // Ruota entrambi insieme
        cost_a--;
        cost_b--;
    }
    
    while (cost_a < 0 && cost_b < 0)
    {
        rrr(stack_a, stack_b, 1);  // Ruota entrambi indietro insieme
        cost_a++;
        cost_b++;
    }
    
    // Fase 2: Rotazioni singole per A
    while (cost_a > 0 && cost_a--)
        ra(stack_a, 1);
    while (cost_a < 0 && cost_a++)
        rra(stack_a, 1);
    
    // Fase 3: Rotazioni singole per B
    while (cost_b > 0 && cost_b--)
        rb(stack_b, 1);
    while (cost_b < 0 && cost_b++)
        rrb(stack_b, 1);
    
    // Fase 4: Sposta l'elemento da B ad A
    pa(stack_a, stack_b, 1);
}
```

**Ottimizzazione Chiave:**

La funzione usa operazioni combinate (`rr` e `rrr`) quando possibile!

**Esempio:**
```
Scenario: cost_a = 3, cost_b = 2

Approccio NON ottimizzato (5 operazioni):
ra
ra
ra
rb
rb
pa

Approccio OTTIMIZZATO (4 operazioni):
rr  (ruota A e B insieme)
rr  (ruota A e B insieme)
ra  (ruota solo A)
pa
```

**Perché è Importante:**
- Riduce il numero totale di operazioni
- Le operazioni simultanee contano come una singola mossa

**Tutti i Casi Possibili:**

1. **Entrambi positivi** (cost_a > 0, cost_b > 0):
   - Usa `rr` fino a esaurire il più piccolo
   - Continua con rotazioni singole

2. **Entrambi negativi** (cost_a < 0, cost_b < 0):
   - Usa `rrr` fino a esaurire il più piccolo
   - Continua con rotazioni inverse singole

3. **Segni opposti**:
   - Usa solo rotazioni singole separate

**Esempio Completo di Mossa:**

```
Stato iniziale:
A: [7] [9] [3] [11]
B: [5] [2] [8]

Elemento da spostare: 5 (in cima a B)
cost_a = 2 (portare 3 in cima ad A)
cost_b = 0 (5 è già in cima)

Esecuzione:
1. cost_a=2 > 0, cost_b=0: nessuna rotazione simultanea
2. Rotazioni singole A: ra, ra
   A: [3] [11] [7] [9]
3. Nessuna rotazione B (cost_b=0)
4. pa
   A: [5] [3] [11] [7] [9]
   B: [2] [8]

Risultato: 5 inserito nella posizione corretta in A
```

---

#### Fase 4: Posizionamento Finale `shift_stack()`

Dopo aver riportato tutti gli elementi da B ad A, lo stack A è quasi ordinato ma potrebbe iniziare da un numero che non è il minimo.

```c
static void shift_stack(t_stack **stack_a)
{
    int min_pos = get_min_index_pos(stack_a);
    int size = stack_size(*stack_a);
    
    if (min_pos <= size / 2)
    {
        while (min_pos-- > 0)
            ra(stack_a, 1);
    }
    else
    {
        while (min_pos++ < size)
            rra(stack_a, 1);
    }
}
```

**Scopo:**
Porta l'elemento con l'indice minimo (il più piccolo) in cima allo stack.

**Esempio:**
```
Prima:  [7] [9] [3] [5] [6]
        L'elemento minimo (3) è in posizione 2

Dopo shift_stack:
        [3] [5] [6] [7] [9]  ✓ Completamente ordinato
```

---

## Operazioni sullo Stack

Il programma usa 11 operazioni base per manipolare gli stack:

### Operazioni di Swap (Scambio)

#### `sa` - Swap A
```c
void sa(t_stack **stack_a, int print)
{
    swap(stack_a);
    if (print)
        ft_putstr("sa\n");
}

static void swap(t_stack **stack)
{
    if (!*stack || !(*stack)->next)
        return;
    
    t_stack *first = *stack;
    t_stack *second = first->next;
    
    // Scambia value e index
    int tmp_value = first->value;
    int tmp_index = first->index;
    first->value = second->value;
    first->index = second->index;
    second->value = tmp_value;
    second->index = tmp_index;
}
```

**Cosa fa:** Scambia i primi due elementi dello stack A

**Esempio:**
```
Prima:  [5] [2] [8]
        ↓ sa
Dopo:   [2] [5] [8]
```

**Nota Implementativa:**
- Non scambia i puntatori, ma i valori contenuti
- Questo mantiene la struttura della lista intatta

#### `sb` - Swap B
Identico a `sa`, ma opera sullo stack B

#### `ss` - Swap Simultaneo
```c
void ss(t_stack **stack_a, t_stack **stack_b, int print)
{
    swap(stack_a);
    swap(stack_b);
    if (print)
        ft_putstr("ss\n");
}
```

**Cosa fa:** Esegue `sa` e `sb` contemporaneamente

---

### Operazioni di Push (Spostamento)

#### `pa` - Push to A
```c
void pa(t_stack **stack_a, t_stack **stack_b, int print)
{
    push(stack_b, stack_a);
    if (print)
        ft_putstr("pa\n");
}

static void push(t_stack **src, t_stack **dst)
{
    if (!*src)
        return;
    
    t_stack *tmp = (*src)->next;
    (*src)->next = *dst;
    *dst = *src;
    *src = tmp;
}
```

**Cosa fa:** Prende il primo elemento di B e lo mette in cima ad A

**Esempio:**
```
Prima:
A: [3] [7] [9]
B: [5] [2]

Dopo pa:
A: [5] [3] [7] [9]
B: [2]
```

**Come Funziona Internamente:**
```
1. Salva il secondo elemento di B: tmp = B->next
2. Collega B al vecchio top di A: B->next = A
3. A punta ora a B: A = B
4. B punta al vecchio secondo: B = tmp
```

#### `pb` - Push to B
Identico a `pa`, ma sposta da A a B

---

### Operazioni di Rotate (Rotazione)

#### `ra` - Rotate A
```c
void ra(t_stack **stack_a, int print)
{
    rotate(stack_a);
    if (print)
        ft_putstr("ra\n");
}

static void rotate(t_stack **stack)
{
    if (!*stack || !(*stack)->next)
        return;
    
    t_stack *first = *stack;
    t_stack *last = get_bottom(*stack);
    
    *stack = first->next;    // Il secondo diventa il primo
    first->next = NULL;      // Il primo non ha più un next
    last->next = first;      // Il primo diventa l'ultimo
}
```

**Cosa fa:** Sposta tutti gli elementi in su, il primo diventa l'ultimo

**Esempio:**
```
Prima:  [1] [2] [3] [4]
        ↓ ra
Dopo:   [2] [3] [4] [1]
```

**Visualizzazione Circolare:**
```
     [1]
    /   \
  [4]   [2]
    \   /
     [3]
     
     ↓ rotate
     
     [2]
    /   \
  [1]   [3]
    \   /
     [4]
```

#### `rb` - Rotate B
Identico a `ra`, ma opera sullo stack B

#### `rr` - Rotate Simultaneo
```c
void rr(t_stack **stack_a, t_stack **stack_b, int print)
{
    rotate(stack_a);
    rotate(stack_b);
    if (print)
        ft_putstr("rr\n");
}
```

**Cosa fa:** Esegue `ra` e `rb` contemporaneamente

---

### Operazioni di Reverse Rotate (Rotazione Inversa)

#### `rra` - Reverse Rotate A
```c
void rra(t_stack **stack_a, int print)
{
    reverse_rotate(stack_a);
    if (print)
        ft_putstr("rra\n");
}

static void reverse_rotate(t_stack **stack)
{
    if (!*stack || !(*stack)->next)
        return;
    
    t_stack *last = get_bottom(*stack);
    t_stack *before_last = get_before_bottom(*stack);
    
    last->next = *stack;        // L'ultimo punta al primo
    *stack = last;              // L'ultimo diventa il primo
    before_last->next = NULL;   // Il penultimo diventa l'ultimo
}
```

**Cosa fa:** Sposta tutti gli elementi in giù, l'ultimo diventa il primo

**Esempio:**
```
Prima:  [1] [2] [3] [4]
        ↓ rra
Dopo:   [4] [1] [2] [3]
```

**È l'Opposto di Rotate:**
```
ra:  [1] [2] [3] [4] → [2] [3] [4] [1]
rra: [2] [3] [4] [1] → [1] [2] [3] [4]
```

#### `rrb` - Reverse Rotate B
Identico a `rra`, ma opera sullo stack B

#### `rrr` - Reverse Rotate Simultaneo
```c
void rrr(t_stack **stack_a, t_stack **stack_b, int print)
{
    reverse_rotate(stack_a);
    reverse_rotate(stack_b);
    if (print)
        ft_putstr("rrr\n");
}
```

**Cosa fa:** Esegue `rra` e `rrb` contemporaneamente

---

### Riepilogo delle Operazioni

| Operazione | Descrizione | Stack A | Stack B | Simultaneo |
|------------|-------------|---------|---------|------------|
| `sa` | Scambia primi 2 | ✓ | | |
| `sb` | Scambia primi 2 | | ✓ | |
| `ss` | Scambia primi 2 | ✓ | ✓ | ✓ |
| `pa` | Push da B ad A | ✓ dst | ✓ src | |
| `pb` | Push da A a B | ✓ src | ✓ dst | |
| `ra` | Ruota in su | ✓ | | |
| `rb` | Ruota in su | | ✓ | |
| `rr` | Ruota in su | ✓ | ✓ | ✓ |
| `rra` | Ruota in giù | ✓ | | |
| `rrb` | Ruota in giù | | ✓ | |
| `rrr` | Ruota in giù | ✓ | ✓ | ✓ |

---

## Gestione della Memoria ed Errori

### Allocazione della Memoria

#### Creazione di un Nodo
```c
t_stack *stack_new(int value)
{
    t_stack *new = (t_stack *)malloc(sizeof(t_stack));
    if (!new)
        return (NULL);
    
    new->value = value;
    new->index = 0;
    new->pos = -1;
    new->target_pos = -1;
    new->cost_a = -1;
    new->cost_b = -1;
    new->next = NULL;
    
    return (new);
}
```

**Inizializzazione Sicura:**
- Tutti i campi sono inizializzati
- I valori -1 indicano "non ancora calcolato"
- Ritorna NULL in caso di errore di allocazione

#### Aggiunta di un Nodo
```c
void stack_add_bottom(t_stack **stack, t_stack *new)
{
    if (!new)
        return;
    
    if (!*stack)
    {
        *stack = new;  // Stack vuoto: il nuovo diventa il primo
        return;
    }
    
    t_stack *tail = get_bottom(*stack);
    tail->next = new;  // Aggiungi in fondo
}
```

---

### Liberazione della Memoria

#### Liberazione di uno Stack
```c
void free_stack(t_stack **stack)
{
    if (!stack || !(*stack))
        return;
    
    t_stack *tmp;
    while (*stack)
    {
        tmp = (*stack)->next;  // Salva il prossimo
        free(*stack);          // Libera il corrente
        *stack = tmp;          // Passa al prossimo
    }
    *stack = NULL;
}
```

**Perché è Importante:**
- Previene memory leaks
- Libera ogni nodo uno per uno
- Assicura che il puntatore finale sia NULL

#### Liberazione di Array di Stringhe
```c
void free_split(char **split)
{
    if (!split)
        return;
    
    int i = 0;
    while (split[i])
    {
        free(split[i]);  // Libera ogni stringa
        i++;
    }
    free(split);  // Libera l'array
}
```

**Usato per:**
- Liberare l'array creato da `ft_split()`
- Gestire gli errori durante il parsing

---

### Gestione degli Errori

#### Quando Si Verificano Errori

1. **Input non valido:**
   - Caratteri non numerici
   - Stringa vuota
   - Solo segno senza numero

2. **Overflow:**
   - Numero > INT_MAX (2147483647)
   - Numero < INT_MIN (-2147483648)

3. **Duplicati:**
   - Due o più numeri uguali

4. **Errori di memoria:**
   - malloc() fallisce

#### Come Vengono Gestiti

```c
void error_exit(void)
{
    ft_putstr("Error\n");
    exit(1);
}
```

**Processo Completo:**
1. Prima di chiamare error_exit(), viene liberata tutta la memoria allocata
2. Viene stampato "Error\n" su stdout
3. Il programma termina con codice di uscita 1

**Esempio di Flusso di Errore:**
```c
if (!is_number(str))
{
    free_split(numbers);   // Libera le stringhe
    free_stack(stack);     // Libera lo stack
    error_exit();          // Stampa errore ed esci
}
```

---

## Flusso di Esecuzione Completo

### Diagramma di Flusso Generale

```
┌─────────────────────────────────────────────┐
│            MAIN - Punto di Ingresso         │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│         Verifica Argomenti (argc < 2?)      │
│               ↓ NO                          │
│         Inizializza stack_a = NULL          │
│         Inizializza stack_b = NULL          │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│         FASE 1: PARSING E VALIDAZIONE       │
│  ┌──────────────────────────────────────┐   │
│  │ parse_arguments()                    │   │
│  │   - Divide gli input                 │   │
│  │   - Valida ogni numero               │   │
│  │   - Controlla overflow               │   │
│  │   - Rileva duplicati                 │   │
│  │   - Costruisce stack_a               │   │
│  └──────────────────────────────────────┘   │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│         Verifica se Già Ordinato            │
│         is_sorted(stack_a)?                 │
│               ↓ SÌ: esci                    │
│               ↓ NO: continua                │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│         FASE 2: ASSEGNAZIONE INDICI         │
│  ┌──────────────────────────────────────┐   │
│  │ assign_index(stack_a, size)          │   │
│  │   - Trova il minimo                  │   │
│  │   - Assegna index = 1                │   │
│  │   - Ripeti per tutti                 │   │
│  └──────────────────────────────────────┘   │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│      FASE 3: SCELTA ALGORITMO               │
│         (in base alla dimensione)           │
└──────────────────┬──────────────────────────┘
                   │
         ┌─────────┼─────────┬─────────┐
         │         │         │         │
      size=2    size=3   size≤5    size>5
         │         │         │         │
         ▼         ▼         ▼         ▼
      ┌────┐   ┌────┐   ┌────┐   ┌────────┐
      │ sa │   │sort│   │sort│   │  sort  │
      │    │   │_   │   │_   │   │        │
      │    │   │three│  │small│  │(grande)│
      └────┘   └────┘   └────┘   └────────┘
         │         │         │         │
         └─────────┴─────────┴─────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│         FASE 4: CLEANUP                     │
│  ┌──────────────────────────────────────┐   │
│  │ free_stack(&stack_a)                 │   │
│  │ free_stack(&stack_b)                 │   │
│  └──────────────────────────────────────┘   │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
              ┌────────┐
              │  FINE  │
              └────────┘
```

---

### Esempio Completo di Esecuzione

Seguiamo un esempio passo-passo con 7 numeri:

**Input:** `./push_swap 4 67 3 87 23 12 -5`

---

#### Step 1: Parsing

```
Argomenti: argc=8
argv[1]="4", argv[2]="67", argv[3]="3", ...

parse_multiple_args():
  - "4" → is_number() ✓ → ft_atol() → 4 → add_to_stack
  - "67" → is_number() ✓ → ft_atol() → 67 → add_to_stack
  - "3" → is_number() ✓ → ft_atol() → 3 → add_to_stack
  - "87" → is_number() ✓ → ft_atol() → 87 → add_to_stack
  - "23" → is_number() ✓ → ft_atol() → 23 → add_to_stack
  - "12" → is_number() ✓ → ft_atol() → 12 → add_to_stack
  - "-5" → is_number() ✓ → ft_atol() → -5 → add_to_stack

has_duplicates() → 0 (nessun duplicato)

Stack A finale:
[4] → [67] → [3] → [87] → [23] → [12] → [-5] → NULL
```

---

#### Step 2: Verifica Ordinamento

```
is_sorted(stack_a):
  4 > 67? NO
  67 > 3? SÌ → NON ORDINATO
  
Ritorna: 0 (continua con l'ordinamento)
```

---

#### Step 3: Assegnazione Indici

```
assign_index(stack_a, 7):

Iterazione 1:
  get_next_min() → trova -5 (il minimo)
  -5->index = 1

Iterazione 2:
  get_next_min() → trova 3 (tra quelli con index=0)
  3->index = 2

Iterazione 3:
  get_next_min() → trova 4
  4->index = 3

Iterazione 4:
  get_next_min() → trova 12
  12->index = 4

Iterazione 5:
  get_next_min() → trova 23
  23->index = 5

Iterazione 6:
  get_next_min() → trova 67
  67->index = 6

Iterazione 7:
  get_next_min() → trova 87
  87->index = 7

Stack A con indici:
[4:3] → [67:6] → [3:2] → [87:7] → [23:5] → [12:4] → [-5:1] → NULL
```

---

#### Step 4: Scelta Algoritmo

```
stack_size(stack_a) = 7
7 > 5 → usa sort()
```

---

#### Step 5: Algoritmo `sort()` - Fase 1

##### 5.1 - push_all_but_three()

```
Stack A iniziale: [4:3] [67:6] [3:2] [87:7] [23:5] [12:4] [-5:1]
size = 7, size/2 = 3

PRIMA FASE: Sposta elementi con index ≤ 3

i=0: top=[4:3], index=3 ≤ 3 → pb
     Operazione: pb
     A: [67:6] [3:2] [87:7] [23:5] [12:4] [-5:1]
     B: [4:3]
     pushed=1

i=1: top=[67:6], index=6 > 3 → ra
     Operazione: ra
     A: [3:2] [87:7] [23:5] [12:4] [-5:1] [67:6]
     B: [4:3]

i=2: top=[3:2], index=2 ≤ 3 → pb
     Operazione: pb
     A: [87:7] [23:5] [12:4] [-5:1] [67:6]
     B: [3:2] [4:3]
     pushed=2

i=3: top=[87:7], index=7 > 3 → ra
     Operazione: ra
     A: [23:5] [12:4] [-5:1] [67:6] [87:7]
     B: [3:2] [4:3]

i=4: top=[23:5], index=5 > 3 → ra
     Operazione: ra
     A: [12:4] [-5:1] [67:6] [87:7] [23:5]
     B: [3:2] [4:3]

i=5: top=[12:4], index=4 > 3 → ra
     Operazione: ra
     A: [-5:1] [67:6] [87:7] [23:5] [12:4]
     B: [3:2] [4:3]

i=6: top=[-5:1], index=1 ≤ 3 → pb
     Operazione: pb
     A: [67:6] [87:7] [23:5] [12:4]
     B: [-5:1] [3:2] [4:3]
     pushed=3

pushed=3 < size/2=3 → continua
Ma i=7 ≥ size=7 → esci dal primo while

SECONDA FASE: Sposta tutto tranne 3

size=7, pushed=3
size - pushed = 4 > 3

Iterazione 1:
  Operazione: pb
  A: [87:7] [23:5] [12:4]
  B: [67:6] [-5:1] [3:2] [4:3]
  pushed=4

size - pushed = 3 → esci

Risultato push_all_but_three():
A: [87:7] [23:5] [12:4]  (3 elementi)
B: [67:6] [-5:1] [3:2] [4:3]  (4 elementi)
```

---

##### 5.2 - sort_three()

```
Stack A: [87:7] [23:5] [12:4]

Trovare l'indice più alto:
  highest = 7 (elemento 87)

top->index = 7 = highest? SÌ
  Operazione: ra
  A: [23:5] [12:4] [87:7]

Ora: top->index=5, next->index=4
5 > 4? SÌ
  Operazione: sa
  A: [12:4] [23:5] [87:7]

Verifica: is_sorted([12:4] [23:5] [87:7]) → SÌ ✓

Risultato sort_three():
A: [12:4] [23:5] [87:7]  (ordinato!)
B: [67:6] [-5:1] [3:2] [4:3]
```

---

##### 5.3 - Ciclo Principale: Riportare da B ad A

**ITERAZIONE 1**

```
Stato:
A: [12:4] [23:5] [87:7]
B: [67:6] [-5:1] [3:2] [4:3]

get_position():
A: [12:4,pos0] [23:5,pos1] [87:7,pos2]
B: [67:6,pos0] [-5:1,pos1] [3:2,pos2] [4:3,pos3]

get_target_position():
Per ogni elemento in B, trova dove andrebbe in A

B[67:6]:
  Cerca in A elemento > 6: trova 87:7
  Il più piccolo tra questi: 87 (pos=2)
  target_pos = 2

B[-5:1]:
  Cerca in A elemento > 1: trova 12:4, 23:5, 87:7
  Il più piccolo: 12:4 (pos=0)
  target_pos = 0

B[3:2]:
  Cerca in A elemento > 2: trova 12:4, 23:5, 87:7
  Il più piccolo: 12:4 (pos=0)
  target_pos = 0

B[4:3]:
  Cerca in A elemento > 3: trova 12:4, 23:5, 87:7
  Il più piccolo: 12:4 (pos=0)
  target_pos = 0

Aggiornamento:
B: [67:6,pos0,target2] [-5:1,pos1,target0] [3:2,pos2,target0] [4:3,pos3,target0]

get_cost():
size_a = 3, size_b = 4

B[67:6]:
  pos=0 ≤ size_b/2=2 → cost_b = 0
  target_pos=2 ≤ size_a/2=1? NO, 2 > 1
    → cost_a = (3-2)*(-1) = -1

B[-5:1]:
  pos=1 ≤ size_b/2=2 → cost_b = 1
  target_pos=0 ≤ size_a/2=1 → cost_a = 0

B[3:2]:
  pos=2 ≤ size_b/2=2 → cost_b = 2
  target_pos=0 ≤ size_a/2=1 → cost_a = 0

B[4:3]:
  pos=3 > size_b/2=2 → cost_b = (4-3)*(-1) = -1
  target_pos=0 ≤ size_a/2=1 → cost_a = 0

Costi finali:
B: [67:6,costA=-1,costB=0]  → totale: |-1|+|0| = 1
   [-5:1,costA=0,costB=1]   → totale: |0|+|1| = 1
   [3:2,costA=0,costB=2]    → totale: |0|+|2| = 2
   [4:3,costA=0,costB=-1]   → totale: |0|+|-1| = 1

do_cheapest_move():
Tre elementi hanno costo 1, sceglie il primo: 67:6

do_move(cost_a=-1, cost_b=0):
  cost_a<0, cost_b=0: non ci sono rotazioni simultanee
  cost_a=-1: rra (1 volta)
    Operazione: rra
    A: [87:7] [12:4] [23:5]
  cost_b=0: nessuna rotazione
  Operazione: pa
    A: [67:6] [87:7] [12:4] [23:5]
    B: [-5:1] [3:2] [4:3]

Risultato Iterazione 1:
A: [67:6] [87:7] [12:4] [23:5]
B: [-5:1] [3:2] [4:3]
Operazioni: rra, pa
```

---

**ITERAZIONE 2**

```
Stato:
A: [67:6] [87:7] [12:4] [23:5]
B: [-5:1] [3:2] [4:3]

get_position():
A: [67:6,pos0] [87:7,pos1] [12:4,pos2] [23:5,pos3]
B: [-5:1,pos0] [3:2,pos1] [4:3,pos2]

get_target_position():

B[-5:1]:
  Cerca in A elemento > 1: trova tutti (4, 5, 6, 7)
  Il più piccolo: 12:4 (pos=2)
  target_pos = 2

B[3:2]:
  Cerca in A elemento > 2: trova 12:4, 23:5, 67:6, 87:7
  Il più piccolo: 12:4 (pos=2)
  target_pos = 2

B[4:3]:
  Cerca in A elemento > 3: trova 12:4, 23:5, 67:6, 87:7
  Il più piccolo: 12:4 (pos=2)
  target_pos = 2

get_cost():
size_a = 4, size_b = 3

B[-5:1]:
  pos=0, cost_b = 0
  target_pos=2 ≤ size_a/2=2 → cost_a = 2

B[3:2]:
  pos=1 ≤ size_b/2=1 → cost_b = 1
  target_pos=2 ≤ size_a/2=2 → cost_a = 2

B[4:3]:
  pos=2 > size_b/2=1 → cost_b = (3-2)*(-1) = -1
  target_pos=2 ≤ size_a/2=2 → cost_a = 2

Costi:
B: [-5:1,costA=2,costB=0]  → totale: 2
   [3:2,costA=2,costB=1]   → totale: 3
   [4:3,costA=2,costB=-1]  → totale: 3

Elemento più economico: -5:1 (costo=2)

do_move(cost_a=2, cost_b=0):
  cost_a>0, cost_b=0: nessuna rotazione simultanea
  cost_a=2: ra (2 volte)
    Operazioni: ra, ra
    A: [12:4] [23:5] [67:6] [87:7]
  cost_b=0: nessuna rotazione
  Operazione: pa
    A: [-5:1] [12:4] [23:5] [67:6] [87:7]
    B: [3:2] [4:3]

Risultato Iterazione 2:
A: [-5:1] [12:4] [23:5] [67:6] [87:7]
B: [3:2] [4:3]
Operazioni: ra, ra, pa
```

---

**ITERAZIONE 3**

```
Stato:
A: [-5:1] [12:4] [23:5] [67:6] [87:7]
B: [3:2] [4:3]

get_position():
A: [-5:1,pos0] [12:4,pos1] [23:5,pos2] [67:6,pos3] [87:7,pos4]
B: [3:2,pos0] [4:3,pos1]

get_target_position():

B[3:2]:
  Cerca in A elemento > 2: trova 12:4, 23:5, 67:6, 87:7
  Il più piccolo: 12:4 (pos=1)
  target_pos = 1

B[4:3]:
  Cerca in A elemento > 3: trova 12:4, 23:5, 67:6, 87:7
  Il più piccolo: 12:4 (pos=1)
  target_pos = 1

get_cost():
size_a = 5, size_b = 2

B[3:2]:
  pos=0, cost_b = 0
  target_pos=1 ≤ size_a/2=2 → cost_a = 1

B[4:3]:
  pos=1 ≤ size_b/2=1 → cost_b = 1
  target_pos=1 ≤ size_a/2=2 → cost_a = 1

Costi:
B: [3:2,costA=1,costB=0]  → totale: 1
   [4:3,costA=1,costB=1]  → totale: 2

Elemento più economico: 3:2 (costo=1)

do_move(cost_a=1, cost_b=0):
  Operazione: ra
  A: [12:4] [23:5] [67:6] [87:7] [-5:1]
  Operazione: pa
  A: [3:2] [12:4] [23:5] [67:6] [87:7] [-5:1]
  B: [4:3]

Risultato Iterazione 3:
A: [3:2] [12:4] [23:5] [67:6] [87:7] [-5:1]
B: [4:3]
Operazioni: ra, pa
```

---

**ITERAZIONE 4**

```
Stato:
A: [3:2] [12:4] [23:5] [67:6] [87:7] [-5:1]
B: [4:3]

get_position():
A: [3:2,pos0] [12:4,pos1] [23:5,pos2] [67:6,pos3] [87:7,pos4] [-5:1,pos5]
B: [4:3,pos0]

get_target_position():

B[4:3]:
  Cerca in A elemento > 3: trova 12:4, 23:5, 67:6, 87:7
  Il più piccolo: 12:4 (pos=1)
  target_pos = 1

get_cost():
size_a = 6, size_b = 1

B[4:3]:
  pos=0, cost_b = 0
  target_pos=1 ≤ size_a/2=3 → cost_a = 1

Elemento più economico (l'unico): 4:3 (costo=1)

do_move(cost_a=1, cost_b=0):
  Operazione: ra
  A: [12:4] [23:5] [67:6] [87:7] [-5:1] [3:2]
  Operazione: pa
  A: [4:3] [12:4] [23:5] [67:6] [87:7] [-5:1] [3:2]
  B: (vuoto)

Risultato Iterazione 4:
A: [4:3] [12:4] [23:5] [67:6] [87:7] [-5:1] [3:2]
B: (vuoto)
Operazioni: ra, pa
```

---

##### 5.4 - shift_stack()

```
Stack B è vuoto, ciclo terminato

Verifica ordinamento:
is_sorted(A) → NO (4 > 12 > 23 > 67 > 87 ma poi -5 < 3)

Chiama shift_stack():

get_min_index_pos(A):
  Cerca elemento con index minimo
  -5:1 è il minimo, posizione = 5

min_pos=5, size=7
5 > size/2=3 → usa rra

Calcola quante rra servono:
size - min_pos = 7 - 5 = 2

Operazioni: rra, rra
  rra: [3:2] [4:3] [12:4] [23:5] [67:6] [87:7] [-5:1]
  rra: [-5:1] [3:2] [4:3] [12:4] [23:5] [67:6] [87:7]

Risultato Finale:
A: [-5:1] [3:2] [4:3] [12:4] [23:5] [67:6] [87:7] ✓
```

---

#### Step 6: Verifica Finale

```
is_sorted(A) → SÌ ✓

Valori in ordine: -5, 3, 4, 12, 23, 67, 87
Indici in ordine: 1, 2, 3, 4, 5, 6, 7
```

---

#### Riepilogo Operazioni Totali

```
push_all_but_three():
1. pb
2. ra
3. pb
4. ra
5. ra
6. ra
7. pb
8. pb

sort_three():
9. ra
10. sa

Iterazione 1:
11. rra
12. pa

Iterazione 2:
13. ra
14. ra
15. pa

Iterazione 3:
16. ra
17. pa

Iterazione 4:
18. ra
19. pa

shift_stack():
20. rra
21. rra

TOTALE: 21 operazioni
```

---

## IDENTIFICAZIONE DELL'ALGORITMO UTILIZZATO

Dopo aver analizzato in dettaglio tutto il codice, posso identificare con precisione l'algoritmo di ordinamento che hai implementato:

### **Nome dell'Algoritmo: Turk Algorithm (o Cost-Based Push Swap)**

Questo è un algoritmo specifico per il problema push_swap, sviluppato dalla community di 42, particolarmente efficiente per set di dati medi e grandi.

---

### Caratteristiche Principali dell'Algoritmo

#### 1. **Strategia di Divisione (Divide)**

L'algoritmo divide il problema in parti più piccole:
- Separa gli elementi in due stack (A e B)
- Mantiene solo 3 elementi in A per l'ordinamento iniziale
- Gli altri elementi vanno in B

**Perché 3 elementi?**
- 3 elementi possono essere ordinati in massimo 2 operazioni
- È il caso base più efficiente

#### 2. **Ordinamento Basato sui Costi (Cost-Based Sorting)**

La parte più caratteristica di questo algoritmo:

```
Per ogni elemento in B:
  1. Calcola dove dovrebbe andare in A (target_position)
  2. Calcola quante operazioni servono per portarlo lì:
     - cost_a: operazioni su stack A
     - cost_b: operazioni su stack B
  3. Sceglie l'elemento con il costo totale minimo
  4. Esegue le operazioni in modo ottimizzato
```

**Formula del Costo:**
```
costo_totale = |cost_a| + |cost_b|
```

**Ottimizzazione:**
- Se cost_a e cost_b hanno lo stesso segno, usa operazioni combinate (rr/rrr)
- Questo riduce il numero totale di operazioni

#### 3. **Uso di Indici Relativi**

Invece di lavorare con i valori effettivi, l'algoritmo usa gli indici:
- Semplifica i confronti
- Rende l'algoritmo indipendente dai valori numerici
- Facilita l'identificazione di min/max

---

### Confronto con Altri Algoritmi

#### vs. Quick Sort (tradizionale)
- **Quick Sort**: Divide basandosi su pivot, ricorsivo
- **Turk**: Divide basandosi su index ≤ size/2, iterativo con calcolo dei costi
- **Vantaggio Turk**: Ottimizzato per le operazioni specifiche di push_swap

#### vs. Radix Sort (altra soluzione comune per push_swap)
- **Radix Sort**: Ordina bit per bit (base 2)
- **Turk**: Ordina basandosi sul costo di inserimento
- **Turk pro**: Meno operazioni per set piccoli e medi
- **Radix pro**: Più prevedibile per set molto grandi

#### vs. Chunk Sort (altra variante per push_swap)
- **Chunk**: Divide in gruppi (chunk) di dimensione fissa
- **Turk**: Divide in metà + calcolo dinamico dei costi
- **Turk pro**: Più adattivo e spesso più efficiente

---

### Complessità Computazionale

#### Complessità Temporale

**Caso Medio:** O(n²)
- assign_index(): O(n²)
- Ciclo principale: O(n) iterazioni
  - Ogni iterazione: get_target_position() O(n), get_cost() O(n), do_cheapest_move() O(n)
  - Totale: O(n²)

**Caso Peggiore:** O(n²)

**Caso Migliore:** O(n) - quando l'array è già ordinato o quasi

#### Complessità Spaziale

**O(n)** - spazio per i nodi dello stack

**Nota:** Non usa ricorsione, quindi nessun overhead di stack delle chiamate

---

### Numero di Operazioni (Performance Pratica)

Questo è ciò che conta davvero per push_swap:

| Dimensione | Operazioni Medie | Operazioni Massime |
|------------|------------------|-------------------|
| 3 elementi | 2-3 | 3 |
| 5 elementi | 8-12 | 12 |
| 100 elementi | 700-900 | ~1100 |
| 500 elementi | 5500-7000 | ~8500 |

**Benchmark 42:**
- **100 numeri**: < 700 operazioni (ottimo), < 900 (buono), < 1100 (ok), < 1500 (limite)
- **500 numeri**: < 5500 operazioni (ottimo), < 7000 (buono), < 8500 (ok), < 11500 (limite)

Il tuo algoritmo rientra tipicamente nelle categorie "buono"/"ottimo".

---

### Perché Questo Algoritmo è Efficace

#### 1. **Greedy Approach con Lookahead**
- Sceglie sempre la mossa localmente ottimale
- Ma considera anche il costo futuro (target_position)
- Bilancia bene efficienza locale e globale

#### 2. **Ottimizzazione delle Operazioni Combinate**
- `rr` e `rrr` riducono significativamente il contatore
- Esempio: invece di ra + rb (2 op), usa rr (1 op)

#### 3. **Adattività**
- Sceglie strategie diverse in base alla dimensione:
  - ≤2: soluzione diretta
  - =3: algoritmo specifico ottimale
  - ≤5: sposta i minimi uno per uno
  - >5: algoritmo completo con calcolo costi

#### 4. **Complessità Controllata**
- Anche se è O(n²), il coefficiente è basso
- Per n=100, fa circa 700-900 operazioni (non 10000)
- L'overhead per iterazione è minimo

---

### Varianti e Ottimizzazioni Possibili

Il tuo algoritmo è una implementazione solida del Turk Algorithm. Possibili ottimizzazioni:

#### 1. **Chunk nella Prima Fase**
Invece di dividere semplicemente in due (index ≤ size/2), potresti:
```
- Dividere in 3 chunk per n > 100
- Dividere in 5 chunk per n > 500
```

#### 2. **Pre-rotazione di B**
Dopo ogni push in B, potresti:
- Posizionare gli elementi in B in modo più ordinato
- Riduce i costi nelle iterazioni successive

#### 3. **Ottimizzazione del Target**
Invece di cercare sempre il target più vicino, potresti:
- Considerare anche il costo di altri target vicini
- Scegliere il target che minimizza il costo globale

---

### Conclusione sull'Algoritmo

**Hai implementato il "Turk Algorithm" (Cost-Based Push Swap)**, che è:

✅ **Uno degli algoritmi più popolari per push_swap**
✅ **Efficiente per dimensioni medie e grandi (50-500 elementi)**
✅ **Ben bilanciato tra semplicità e performance**
✅ **Supera facilmente i requisiti di 42**

**Punti di Forza:**
- Facile da comprendere e debuggare
- Performance consistenti
- Ottimizzazione delle operazioni combinate
- Adattivo alla dimensione dell'input

**Caratteristica Distintiva:**
- Il calcolo dei costi per ogni elemento prima di decidere quale spostare
- Questo è ciò che lo rende "Turk Algorithm" invece di altre varianti

---

## Conclusioni Finali

Questo programma è un eccellente esempio di:

### 1. **Gestione della Memoria in C**
- Allocazione e deallocazione corretta
- Prevenzione di memory leak
- Gestione degli errori

### 2. **Strutture Dati**
- Implementazione di liste concatenate
- Operazioni efficienti su stack

### 3. **Algoritmi e Ottimizzazione**
- Scelta di strategie diverse in base all'input
- Calcolo dei costi per decisioni ottimali
- Minimizzazione del numero di operazioni

### 4. **Programmazione Modulare**
- Separazione delle responsabilità
- Funzioni riutilizzabili
- Codice manutenibile

---

## Risorse Addizionali

### Documentazione Utile
- [Turk Algorithm Explanation](https://medium.com/@jamierobertdawson/push-swap-the-least-amount-of-moves-with-two-stacks-d1e76a71789a)
- [Push Swap Visualizer](https://github.com/o-reo/push_swap_visualizer)
- [42 Push Swap Tester](https://github.com/lmalki-h/push_swap_tester)

### Strumenti di Test
```bash
# Genera numeri casuali
ARG=$(shuf -i 0-5000 -n 500 | tr '\n' ' ')

# Testa il programma
./push_swap $ARG | wc -l

# Verifica correttezza
./push_swap $ARG | ./checker $ARG
```

---

**Fine della Documentazione**

Questo documento copre ogni aspetto del tuo programma push_swap, dall'input iniziale all'output finale, spiegando non solo il "cosa" ma anche il "perché" e il "come" di ogni decisione implementativa. L'algoritmo che hai implementato (Turk/Cost-Based) è uno dei più efficaci e popolari per questo problema specifico.