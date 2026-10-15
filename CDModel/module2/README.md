# Module 2 – Syntax Analyzer (Parser)

Checks whether the input follows the grammar for declarations (`int`, `float`, `char`),
assignments, `if` / `if-else`, `while`, and blocks `{ ... }` with arithmetic, relational and
logical (`&&`, `||`, `!`) conditions. Prints `Successfully parsed` or a syntax error.

## Files

| File             | Written by hand? | How it is produced                        |
|------------------|------------------|-------------------------------------------|
| `lexer.l`        | Yes              | Flex specification (source)               |
| `parser.y`       | Yes              | Bison grammar (source)                    |
| `parser.tab.c`   | No (generated)   | `bison -d -v parser.y`                    |
| `parser.tab.h`   | No (generated)   | `bison -d -v parser.y` (`-d` flag)        |
| `parser.output`  | No (generated)   | `bison -d -v parser.y` (`-v` flag, parser states/conflicts report – optional) |
| `lex.yy.c`       | No (generated)   | `flex lexer.l`                            |
| `parser`         | No (generated)   | `gcc parser.tab.c lex.yy.c -o parser`     |

## How to run

Run bison first, since `lexer.l` includes `parser.tab.h`.

```bash
bison -d -v parser.y
flex lexer.l
gcc parser.tab.c lex.yy.c -o parser
./parser < input.txt
```

Or run `./parser`, type the code, and end input with `Ctrl+D` (Linux) /
`Ctrl+Z` then Enter (Windows).

### Example input

```c
int a, b;
a = 5;
if (a < 10 && b != 0) { b = a * 2; } else b = 0;
while (a > 0) a = a - 1;
```
