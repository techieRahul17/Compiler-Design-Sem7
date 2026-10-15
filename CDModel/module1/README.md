# Module 1 – Lexical Analyzer (Scanner) with Symbol Table

Tokenizes C source code (keywords, identifiers, constants, operators, comments, strings,
preprocessor directives) and prints a symbol table of declared variables with type, size,
address and initial value.

## Files

| File        | Written by hand? | How it is produced            |
|-------------|------------------|-------------------------------|
| `scanner.l` | Yes              | Flex specification (source)   |
| `lex.yy.c`  | No (generated)   | `flex scanner.l`              |
| `scanner`   | No (generated)   | `gcc lex.yy.c -o scanner`     |

## How to run

```bash
flex scanner.l
gcc lex.yy.c -o scanner
./scanner < input.c
```

You can also run `./scanner` and type code directly, then press `Ctrl+D` (Linux) /
`Ctrl+Z` then Enter (Windows) to end input and print the symbol table.

### Example input

```c
#include <stdio.h>
int a = 10, b;
float c = 2.5;
/* comment */
a = a + b;
```
