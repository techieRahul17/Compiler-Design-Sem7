"""
Text of the lab records.  Edit the dates / wording here and run  python tools/build_docs.py

Each entry describes one record:
    date      : shown as  Date: ...
    title     : experiment title
    aim       : text under "Aim:"
    tools     : bullet list under "Tools Used:"
    code      : [(label, file)]          -> source files, read from the assignment folder
    inputs    : [(label, file, note)]    -> sample input files shown after the code
    commands  : commands used (shown as a code block)
    outputs   : [(image, caption)]       -> main output screenshots
    notes     : short paragraphs printed after the main output
    extra     : [(image, caption)]       -> additional test cases (optional)
    extra_notes : paragraphs printed after the additional test cases
    learning  : bullets under "Learning Outcomes:"
"""

NAME = "Rahul V S"
REG_NO = "3122235001104"

LEX_TOOLS = [
    "LEX / Flex (lexical analyzer generator)",
    "YACC / Bison (parser generator)",
    "GCC Compiler",
    "Linux terminal (Ubuntu on WSL)",
]
C_TOOLS = [
    "C programming language",
    "GCC Compiler",
    "Linux terminal (Ubuntu on WSL)",
]

RECORDS = {
    # ------------------------------------------------------------------ Exp 5
    5: dict(
        date="07-08-2026",
        title="Implementation of Syntax Checker using Lex and Yacc Tools",
        aim=("To develop a syntax checker using Lex and Yacc that recognizes assignment "
             "statements, conditional statements, looping statements and declaration "
             "statements by writing suitable grammars for each."),
        tools=LEX_TOOLS,
        code=[("syntax.l", "syntax.l"), ("syntax.y", "syntax.y")],
        inputs=[("Input (input.txt)", "input.txt", None)],
        commands=["lex syntax.l", "yacc -d syntax.y",
                  "cc lex.yy.c y.tab.c -lfl -o syncheck", "./syncheck < input.txt"],
        outputs=[("output.png", "Output for the given input")],
        notes=["The grammar is conflict free: operator precedence and associativity are declared "
               "with %left / %right, and the dangling else is resolved with %prec "
               "LOWER_THAN_ELSE, so yacc reports no shift/reduce conflicts."],
        extra=[("output2.png", "Additional test cases: one valid program and two programs with "
                               "syntax errors")],
        extra_notes=[
            "input2.txt uses every statement type: declarations with initial values, for, "
            "if / else if, do-while, logical operators and increment / decrement. It is "
            "accepted as Syntactically correct.",
            "input3.txt has a missing semicolon after i = 0 and input4.txt has a missing "
            "closing bracket in the while condition. The checker reports the line number and "
            "the token at which the statement can no longer be parsed.",
        ],
        learning=[
            "Learned to design a grammar that captures declaration, assignment, conditional "
            "(if-else) and looping (while, do-while, for) statements of a C-like language.",
            "Understood how precedence declarations (%left, %right) and %prec remove "
            "shift/reduce conflicts and how the dangling else problem is resolved.",
            "Understood how Yacc builds a parser from BNF-like productions and reports syntax "
            "errors through yyerror, using yylineno to give the line number.",
            "Gained experience integrating Lex-generated tokens with a Yacc grammar to validate "
            "the structure of a small program.",
        ],
    ),
    # ------------------------------------------------------------------ Exp 6
    6: dict(
        date="14-08-2026",
        title="Generation of Intermediate Code using Lex and Yacc Tools",
        aim=("To develop an intermediate code generator using Lex and Yacc that produces three "
             "address code for assignment statements and boolean expressions by writing "
             "suitable syntax directed translation rules."),
        tools=LEX_TOOLS,
        code=[("tac.l", "tac.l"), ("tac.y", "tac.y")],
        inputs=[("Input (input.txt)", "input.txt", None)],
        commands=["lex tac.l", "yacc -d tac.y", "cc lex.yy.c y.tab.c -lfl -o tac",
                  "./tac < input.txt"],
        outputs=[("output.png", "Three address code for the given input")],
        notes=["Temporaries t1, t2, ... start again for every statement. Statements that contain "
               "a boolean expression are numbered from 100, and a relational expression a<b is "
               "translated into four instructions: if a<b goto (n+3), t := 0, goto (n+4), "
               "t := 1. The operator priority, from lowest to highest, is or, and, not, relational, "
               "arithmetic, so in a<b or c<d and e<f the and is evaluated before the or."],
        extra=[("output2.png", "Additional test cases (the last statement has a syntax error)")],
        extra_notes=[],
        learning=[
            "Learned how syntax directed translation attaches semantic actions to grammar rules "
            "so that three address code is generated while the input is being parsed.",
            "Understood how attributes ($$, $1, $3) carry the name of the temporary that holds "
            "the value of every sub-expression and how new temporaries are created.",
            "Learned to translate relational expressions into conditional jumps with instruction "
            "numbers and to combine them with and / or / not.",
            "Used precedence declarations to give unary minus, arithmetic, relational and logical "
            "operators the correct priority, and the yacc error token to recover from a bad line.",
        ],
    ),
    # ------------------------------------------------------------------ Exp 7
    7: dict(
        date="21-08-2026",
        title="Implementation of Code Optimization Techniques",
        aim=("To implement the code optimization techniques constant folding, algebraic "
             "identities, strength reduction and dead code elimination on a sequence of three "
             "address code statements."),
        tools=C_TOOLS,
        code=[("optimizer.c", "optimizer.c")],
        inputs=[("Input (input.txt)", "input.txt",
                 "The last line lists the variables that are needed after this block of code "
                 "(live at exit). An assignment whose result is not in this list and is not used "
                 "later is dead code.")],
        commands=["gcc optimizer.c -o optimizer", "./optimizer < input.txt"],
        outputs=[("output.png", "Optimization of the given three address code")],
        notes=["t2 = a + 0 becomes t2 = a and t6 = b * d repeats t4; neither t2 nor t6 is needed "
               "after the block, so dead code elimination removes both. The statement "
               "t5 = d ** 2 is reduced to t5 = d * d."],
        extra=[("output2.png", "Additional test case: constant propagation, shifts and dead "
                               "code")],
        extra_notes=[
            "a = 4 * 8 is folded to 32 and propagated into b = a + 2, giving b = 34; a is then "
            "dead. c = x * 8 becomes c = x << 3, and the earlier c is still needed because g "
            "uses it before c is assigned again.",
        ],
        learning=[
            "Learned four local optimization techniques: constant folding (with constant "
            "propagation), algebraic identities, strength reduction and dead code elimination.",
            "Understood that dead code elimination needs liveness information: the block is "
            "scanned backwards and an assignment is removed if its result is not live.",
            "Learned that one optimization creates opportunities for another (x * 1 becomes a "
            "copy, which may then become dead), so the passes are repeated until nothing changes.",
            "Gained experience parsing three address code in C and rewriting instructions "
            "safely, for example not folding a division by zero.",
        ],
    ),
    # ------------------------------------------------------------------ Exp 8
    8: dict(
        date="28-08-2026",
        title="Implementation of Code Generation",
        aim=("To implement a code generator that converts a sequence of three address code "
             "statements containing assignments, arithmetic operators, relational operators, "
             "conditional constructs and iterative constructs into 8086 style assembly code."),
        tools=C_TOOLS,
        code=[("codegen.c", "codegen.c")],
        inputs=[("Input (input.txt) - three address code of  x=0; for(i=1;i<=10;i++) x=x+1",
                 "input.txt", None)],
        commands=["gcc codegen.c -o codegen", "./codegen < input.txt"],
        outputs=[("output.png", "Assembly code generated for the given three address code")],
        notes=["x = t1 and i = t2 "
               "need no instruction because t1 and t2 are placed in the registers of x and i, "
               "which are not needed any more. The constant 10 does not change inside the loop, "
               "so it is loaded into R2 once, before the label L3."],
        extra=[("output2.png", "Additional test case: conditional statement with arithmetic "
                               "operators")],
        extra_notes=[],
        learning=[
            "Learned how three address code is translated into target instructions "
            "(MOV, ADD, SUB, MUL, DIV, CMP and the conditional jumps JL, JLE, JG, JGE, JE, JNE).",
            "Understood live variable analysis on a program with loops: it is a backward data "
            "flow problem that is repeated until nothing changes.",
            "Learned register allocation: two names may share a register only if they are never "
            "live at the same time; a name that finds no free register is kept in memory.",
            "Learned to translate relational operators and iterative constructs into a compare "
            "followed by a conditional jump, and to load loop-invariant constants before the loop "
            "only when that is safe.",
        ],
    ),
}
