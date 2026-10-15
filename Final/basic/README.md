# Final – Basic Compiler (Declarations + Arithmetic)

Compiles `int` declarations and arithmetic assignments (`+ - * /`, parentheses) through
three stages: three-address code → optimized TAC → target code.

## Files

| File             | Written by hand? | How it is produced                         |
|------------------|------------------|--------------------------------------------|
| `lexer.l`        | Yes              | Flex specification (source)                |
| `parser.y`       | Yes              | Bison grammar that generates TAC (source)  |
| `optimizer.c`    | Yes              | C source                                   |
| `gen.c`          | Yes              | C source                                   |
| `input.txt`      | Yes              | Sample input program                       |
| `parser.tab.c`   | No (generated)   | `bison -d parser.y`                        |
| `parser.tab.h`   | No (generated)   | `bison -d parser.y` (`-d` flag)            |
| `lex.yy.c`       | No (generated)   | `flex lexer.l`                             |
| `tacgen`         | No (generated)   | `gcc parser.tab.c lex.yy.c -o tacgen`      |
| `optimizer`      | No (generated)   | `gcc optimizer.c -o optimizer`             |
| `codegen`        | No (generated)   | `gcc gen.c -o codegen`                     |

## How to run

Run bison first, since `lexer.l` includes `parser.tab.h`.

```bash
bison -d parser.y
flex lexer.l
gcc parser.tab.c lex.yy.c -o tacgen
gcc optimizer.c -o optimizer
gcc gen.c -o codegen

./tacgen < input.txt          # 1. three-address code
./optimizer                   # 2. paste the TAC, then type END
./codegen                     # 3. paste the optimized TAC, end with Ctrl+D
```

Run the stages one at a time. If you pipe the optimizer into `codegen`, its two prompt lines
are also sent to `codegen` and show up as `Invalid TAC`.

### Example input (`input.txt`)

```c
int a, b, c, d;
a = 10;
b = 20;
c = a + b * 2;
d = c - 5;
```
