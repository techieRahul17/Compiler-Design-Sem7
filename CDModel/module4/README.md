# Module 4 – Code Optimizer

Reads three-address code and applies:
- **Constant folding** – `t1 = 2 + 3` → `t1=5`
- **Algebraic simplification** – `x + 0`, `x - 0`, `x * 1`, `x / 1`, `x * 0`
- **Strength reduction** – `x * 2` → `x+x`, `x * 4` → `x<<2`, `x * 8` → `x<<3`
- **Dead code elimination** – removes temporaries (`t1`, `t2`, ...) that are never used

## Files

| File          | Written by hand? | How it is produced                  |
|---------------|------------------|-------------------------------------|
| `optimizer.c` | Yes              | C source                            |
| `optimizer`   | No (generated)   | `gcc optimizer.c -o optimizer`      |

## How to run

```bash
gcc optimizer.c -o optimizer
./optimizer
```

Enter one TAC instruction per line and type `END` to finish. Put spaces around the operator
(`dest = left op right`) so each instruction is recognised.

### Example input

```
t1 = 2 * 3
t2 = a + 0
t3 = b * 4
t4 = c - d
x = t1 + t3
END
```

Here `t2` and `t4` are never used, so they are removed as dead code.
