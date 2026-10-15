# Final – Boolean Compiler (Declarations + Arithmetic + Boolean)

Everything in `basic`, plus relational operators (`< > <= >= == !=`) and the logical
operators `and` / `or`. Relations are translated into TAC with `if ... goto` jumps and labels.

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

./tacgen < input.txt                                # three-address code only
./tacgen < input.txt | ./optimizer                  # optimized TAC
./tacgen < input.txt | ./optimizer | ./codegen      # final target code
```

### Example input (`input.txt`)

```c
int a,b,c,d,x,y;
a = 10;
b = 20;
c = a + b * 2;
x = a < b;
y = a < b or b > c and a != d;
```
