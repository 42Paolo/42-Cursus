# Struttura Professionale per push_swap

## Organizzazione Consigliata

```
push_swap/
├── includes/          # Tutti gli header files (.h)
│   ├── push_swap.h    # Header principale con tutte le inclusioni
│   ├── stack.h        # Strutture dati e prototipi per le stack
│   ├── operations.h   # Prototipi delle operazioni (push, swap, rotate, etc.)
│   ├── parser.h       # Prototipi per parsing e validazione input
│   ├── solver.h       # Prototipi per algoritmi di risoluzione
│   └── utils.h        # Prototipi per funzioni utility
│
├── src/               # Tutto il codice sorgente (.c)
│   ├── main.c         # Entry point del programma
│   │
│   ├── stack/         # Gestione delle stack
│   │   ├── stack_init.c      # Inizializzazione stack
│   │   ├── stack_operations.c # Operazioni base (push, pop, peek)
│   │   └── stack_utils.c     # Utility per stack (size, is_empty, etc.)
│   │
│   ├── operations/    # Operazioni sulle stack (norme del progetto)
│   │   ├── push.c     # pa, pb
│   │   ├── swap.c     # sa, sb, ss
│   │   ├── rotate.c   # ra, rb, rr
│   │   └── reverse_rotate.c # rra, rrb, rrr
│   │
│   ├── parser/        # Parsing e validazione
│   │   ├── parse_input.c     # Parsing degli argomenti
│   │   ├── validate.c        # Validazione numeri e duplicati
│   │   └── convert.c         # Conversioni stringa-numero
│   │
│   ├── solver/        # Algoritmi di risoluzione
│   │   ├── small_sort.c      # Ordinamento per stack piccole (2-5 elementi)
│   │   ├── large_sort.c      # Ordinamento per stack grandi
│   │   ├── chunk_sort.c      # Ordinamento a chunk (se usato)
│   │   └── optimize_moves.c  # Ottimizzazione delle mosse
│   │
│   └── utils/         # Funzioni utility
│       ├── errors.c    # Gestione errori
│       ├── memory.c    # Gestione memoria (malloc, free)
│       └── print.c     # Funzioni di output
│
├── libft/             # Libreria personale (se permessa/richiesta)
│   ├── includes/
│   └── src/
│
├── Makefile           # Build system
├── .gitignore
└── README.md
```

## Spiegazione Dettagliata

### 1. **includes/** - Header Files
**Perché separare gli header?**
- **Modularità**: Ogni modulo ha il suo header, facilitando la comprensione
- **Compilazione**: Include solo ciò che serve, riducendo tempi di compilazione
- **Manutenibilità**: Modifiche a un modulo non richiedono di toccare altri header

**push_swap.h**: Header principale che include tutti gli altri. Contiene:
- Inclusioni standard (stdlib.h, unistd.h, etc.)
- Definizioni comuni (costanti, macro)
- Include di tutti gli altri header del progetto

### 2. **src/** - Codice Sorgente
**Organizzazione per funzionalità** (non per tipo di file):
- Ogni cartella rappresenta un **concetto logico** del programma
- Facilita la navigazione: se cerchi operazioni sulle stack, vai in `operations/`
- Rende il codice **auto-documentante**

#### **stack/** - Gestione Strutture Dati
- **stack_init.c**: Creazione, inizializzazione e distruzione delle stack
- **stack_operations.c**: Operazioni base (push, pop, peek) - NON le operazioni del progetto (pa, pb, etc.)
- **stack_utils.c**: Funzioni helper (dimensione, vuota/piena, etc.)

#### **operations/** - Operazioni del Progetto
**Separazione per tipo di operazione**:
- **push.c**: `pa` (push da b ad a), `pb` (push da a a b)
- **swap.c**: `sa`, `sb`, `ss` (swap top di stack)
- **rotate.c**: `ra`, `rb`, `rr` (rotazione normale)
- **reverse_rotate.c**: `rra`, `rrb`, `rrr` (rotazione inversa)

**Perché separare?**
- Ogni operazione è indipendente
- Facile testare singole operazioni
- Rispetta il principio di **Single Responsibility**

#### **parser/** - Input e Validazione
- **parse_input.c**: Converte argv in array di numeri
- **validate.c**: Controlla duplicati, overflow, caratteri non validi
- **convert.c**: Conversioni sicure stringa → intero (con gestione errori)

**Separazione importante**: Parsing e validazione sono concetti diversi:
- Parsing = "come leggo l'input?"
- Validazione = "l'input è corretto?"

#### **solver/** - Algoritmi di Risoluzione
- **small_sort.c**: Algoritmi ottimizzati per 2-5 elementi (hardcoded)
- **large_sort.c**: Algoritmo principale per stack grandi (es. turkish sort, chunk sort)
- **chunk_sort.c**: Se usi algoritmo a chunk, separalo qui
- **optimize_moves.c**: Rimuove mosse ridondanti (es. ra + rra = niente)

**Perché separare small e large?**
- Algoritmi completamente diversi
- Small sort può essere hardcoded (più veloce)
- Large sort richiede logica complessa

#### **utils/** - Funzioni di Supporto
- **errors.c**: Gestione errori centralizzata (stderr, exit codes)
- **memory.c**: Wrapper per malloc/free con gestione errori
- **print.c**: Output formattato (se necessario)

### 3. **libft/** - Libreria Personale
Se la 42 permette/richiede l'uso di libft:
- Mantieni separata la tua libreria
- Non mescolare codice del progetto con codice della libreria

## Vantaggi di Questa Struttura

### ✅ **Manutenibilità**
- Modifiche isolate: cambiare un'operazione non tocca altro codice
- Facile trovare codice: struttura logica intuitiva

### ✅ **Scalabilità**
- Aggiungere nuove operazioni? Aggiungi file in `operations/`
- Nuovo algoritmo? Aggiungi file in `solver/`
- Nessuna modifica a file esistenti

### ✅ **Testabilità**
- Ogni modulo può essere testato indipendentemente
- Facile creare test unitari per singole funzioni

### ✅ **Collaborazione**
- Team può lavorare su moduli diversi senza conflitti
- Code review più semplice (cambiamenti localizzati)

### ✅ **Rispetto Norme 42**
- File non troppo lunghi (ogni file ha responsabilità chiara)
- Funzioni piccole e focalizzate
- Struttura chiara per i correttori

## Best Practices da Seguire

1. **Nomi File**: Usa snake_case, nomi descrittivi
2. **Nomi Funzioni**: Prefisso con modulo (es. `stack_push`, `op_swap`)
3. **Header Guards**: Sempre `#ifndef` negli header
4. **Makefile**: Organizza obiettivi per cartella
5. **Documentazione**: Commenti solo dove necessario (norme 42)

## Esempio Makefile Structure

```makefile
SRC_DIR = src
OBJ_DIR = obj
INC_DIR = includes

# Organizza per cartella
STACK_SRCS = $(SRC_DIR)/stack/*.c
OPS_SRCS = $(SRC_DIR)/operations/*.c
PARSER_SRCS = $(SRC_DIR)/parser/*.c
SOLVER_SRCS = $(SRC_DIR)/solver/*.c
UTILS_SRCS = $(SRC_DIR)/utils/*.c
MAIN_SRC = $(SRC_DIR)/main.c

# Compila mantenendo struttura cartelle in obj/
```

## Conclusione

Questa struttura bilancia:
- **Semplicità**: Non troppo complessa per un progetto 42
- **Professionalità**: Standard dell'industria
- **Norme 42**: Rispetta limitazioni e stile richiesto
- **Manutenibilità**: Facile da capire e modificare
