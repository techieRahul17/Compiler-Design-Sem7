# Module 3 – Intermediate Code Generation (Three Address Code)

Reads a single assignment statement and prints its three-address code (TAC) using
temporaries `t1, t2, ...`. Supports arithmetic expressions (`+ - * /`, unary `-`, parentheses)
and boolean expressions (`and`, `or`, relational operators), which are emitted with
numbered labels starting at 100.

Note: assignment uses `:=` (not `=`).

## Files

| File            | Written by hand? | How it is produced                     |
|-----------------|------------------|----------------------------------------|
| `lexer.l`       | Yes              | Flex specification (source)            |
| `parser.y`      | Yes              | Bison grammar with semantic actions    |
| `parser.tab.c`  | No (generated)   | `bison -d parser.y`                    |
| `parser.tab.h`  | No (generated)   | `bison -d parser.y` (`-d` flag)        |
| `lex.yy.c`      | No (generated)   | `flex lexer.l`                         |
| `modpar`        | No (generated)   | `gcc parser.tab.c lex.yy.c -o modpar`  |

## How to run

Run bison first, since `lexer.l` includes `parser.tab.h`.

```bash
bison -d parser.y
flex lexer.l
gcc parser.tab.c lex.yy.c -o modpar
./modpar
```

Type one statement, then end input with `Ctrl+D` (Linux) / `Ctrl+Z` then Enter (Windows).

### Example inputs

```
x := a + b * c
```

```
x := a < b and c > d
```
