# Module 5 – Target Code Generator

Converts three-address code into simple assembly-like target code using register `R0`:
- `a = b op c` → `MOV R0,b` / `ADD|SUB|MUL|DIV|AND|OR R0,c` / `MOV a,R0`
- `a = b` → `MOV a,b`
- `if a relop b goto L` → `CMP a,b` + `JLT/JLE/JGT/JGE/JE/JNE L`
- `goto L` → `JMP L`
- `L:` → label

## Files

| File    | Written by hand? | How it is produced       |
|---------|------------------|--------------------------|
| `gen.c` | Yes              | C source                 |
| `gen`   | No (generated)   | `gcc gen.c -o gen`       |

## How to run

```bash
gcc gen.c -o gen
./gen < tac.txt
```

Or run `./gen`, type TAC lines, and end input with `Ctrl+D` (Linux) /
`Ctrl+Z` then Enter (Windows). Put spaces around operators (e.g. `t1 = a + b`,
`if a < b goto L1`).

### Example input

```
t1 = a + b
t2 = t1 * c
x = t2
if x > 10 goto L1
goto L2
L1:
y = x - 10
L2:
```
