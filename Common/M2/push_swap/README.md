# Push Swap - Norminette Compliant

## Struttura del Progetto

```
push_swap_fixed/
├── include/
│   └── push_swap.h           # Header con 42 header
├── src/
│   ├── main.c               # Entry point
│   ├── operations/          # Operazioni stack
│   │   ├── push.c          # pa, pb
│   │   ├── swap.c          # sa, sb, ss
│   │   ├── rotate.c        # ra, rb, rr
│   │   └── reverse_rotate.c # rra, rrb, rrr
│   ├── sorting/             # Algoritmi di ordinamento
│   │   ├── sort.c          # Algoritmo principale
│   │   ├── sort_small.c    # Ordinamento piccoli stack
│   │   ├── cost.c          # Calcolo costi
│   │   └── position.c      # Calcolo posizioni
│   ├── parsing/             # Parsing input
│   │   ├── parse.c         # Validazione argomenti
│   │   └── ft_split.c      # Split stringhe
│   └── utils/               # Funzioni di utilità
│       ├── utils.c         # Utilità generali
│       ├── stack_utils.c   # Manipolazione stack
│       ├── error.c         # Gestione errori
│       └── index.c         # Assegnazione indici
└── Makefile                 # Con 42 header
```

## Compilazione

```bash
make        # Compila il progetto
make clean  # Rimuove i file oggetto
make fclean # Rimuove tutto
make re     # Ricompila da zero
```

## Utilizzo

```bash
# Con argomenti separati
./push_swap 3 2 1 5 4

# Con una stringa
./push_swap "3 2 1 5 4"

# Con numeri negativi
./push_swap -5 2 0 -1 3
```

## Test Effettuati

✅ Compilazione con -Wall -Wextra -Werror
✅ Test con 3 numeri: funziona
✅ Test con 5 numeri: funziona
✅ Test con numeri già ordinati: nessuna operazione
✅ Test con numeri negativi: funziona
✅ Test con stringa: funziona
✅ Test errore duplicati: Error\n
✅ Test errore input non numerico: Error\n
✅ Test errore overflow: Error\n

## Note Norminette

Tutti i file hanno:
- Header 42 corretto con nome file, autore, date
- Massimo 25 righe per funzione
- Massimo 5 funzioni per file
- Nessuna linea oltre 80 caratteri
- Indentazione corretta (tab)
- Struct typedef corretta: }	t_name;
- Nomi variabili conformi
- Nessun commento C++ (//)
- Spazi corretti attorno agli operatori

## Compilato e testato con successo!

Il progetto è pronto per la correzione.
