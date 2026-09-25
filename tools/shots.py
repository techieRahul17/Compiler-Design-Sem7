"""
Run the assignment commands in WSL (Ubuntu) and turn the captured terminal text into
an output screenshot (output.png, output2.png ...) drawn in Windows-Terminal style.

Every command is really executed inside the assignment folder, so the generated files
(lex.yy.c, y.tab.c, the executable ...) end up in the folder exactly as after a manual run.

Usage :  python tools/shots.py            (all assignments)
         python tools/shots.py 6 7        (only Assignment6 and Assignment7)

Want a real screenshot instead?  Run the same commands in your own terminal, save the
picture as  AssignmentN/output.png  and run  python tools/build_docs.py  again.
"""
import os
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USER, HOST = "rahul", "RahulOMEN"
DISTRO = "Ubuntu"

# ------------------------------------------------------------------ what to run
BUILD = {
    5: ["lex syntax.l", "yacc -d syntax.y", "cc lex.yy.c y.tab.c -lfl -o syncheck"],
    6: ["lex tac.l", "yacc -d tac.y", "cc lex.yy.c y.tab.c -lfl -o tac"],
    7: ["gcc optimizer.c -o optimizer"],
    8: ["gcc codegen.c -o codegen"],
}

SHOTS = {
    5: {
        "output.png": BUILD[5] + ["./syncheck < input.txt"],
        "output2.png": ["cat input2.txt", "./syncheck < input2.txt",
                        "cat input3.txt", "./syncheck < input3.txt",
                        "cat input4.txt", "./syncheck < input4.txt"],
    },
    6: {
        "output.png": BUILD[6] + ["cat input.txt", "./tac < input.txt"],
        "output2.png": ["cat input2.txt", "./tac < input2.txt"],
    },
    7: {
        "output.png": BUILD[7] + ["cat input.txt", "./optimizer < input.txt"],
        "output2.png": ["cat input2.txt", "./optimizer < input2.txt"],
    },
    8: {
        "output.png": BUILD[8] + ["cat input.txt", "./codegen < input.txt"],
        "output2.png": ["cat input2.txt", "./codegen < input2.txt"],
    },
}


# -------------------------------------------------------------------- run in WSL
def wsl_path(win_path):
    drive, rest = os.path.splitdrive(os.path.abspath(win_path))
    return "/mnt/" + drive[0].lower() + rest.replace("\\", "/")


def run_in_wsl(folder, command):
    """Run one command inside `folder` (stdout and stderr together) and return its text."""
    p = subprocess.run(
        ["wsl", "-d", DISTRO, "--cd", wsl_path(folder), "--", "bash", "-s"],
        input=(command + " 2>&1\n").encode(), capture_output=True)
    return p.stdout.decode("utf-8", "replace").replace("\x00", "").replace("\r", "")


# ------------------------------------------------------------------ draw terminal
BG, FG = (12, 12, 12), (204, 204, 204)
GREEN, BLUE = (22, 198, 12), (59, 120, 255)
SIZE, COLS, PAD = 22, 100, 16
FONT_FILE = r"C:\Windows\Fonts\CascadiaMono.ttf"


def load_font(bold=False):
    f = ImageFont.truetype(FONT_FILE, SIZE)
    if bold:
        try:
            f.set_variation_by_name("Bold")
        except Exception:
            pass
    return f


def cells_for_prompt(path):
    text = [(USER + "@" + HOST, GREEN), (":", FG), (path, BLUE), ("$ ", FG)]
    return [(ch, col, col != FG) for (t, col) in text for ch in t]


def wrap(cells):
    rows = [cells[i:i + COLS] for i in range(0, len(cells), COLS)]
    return rows or [[]]


def render(folder_name, steps, out_png):
    """steps = [(command, output_text), ...]"""
    home = "~"
    cwd = "/mnt/c/Users/Rahul V S/OneDrive/Desktop/CD LAB/" + folder_name
    rows = []
    # like the earlier screenshots: first a cd into the assignment folder
    cd_cmd = 'cd "%s"' % cwd
    rows += wrap(cells_for_prompt(home) + [(c, FG, False) for c in cd_cmd])
    for cmd, output in steps:
        rows += wrap(cells_for_prompt(cwd) + [(c, FG, False) for c in cmd])
        for line in output.rstrip("\n").split("\n") if output.strip() else []:
            rows += wrap([(c, FG, False) for c in line.expandtabs(8)])
    rows += wrap(cells_for_prompt(cwd) + [(" ", FG, False)])       # final prompt with cursor

    fr, fb = load_font(), load_font(bold=True)
    adv = fr.getlength("M")
    line_h = int(SIZE * 1.3)
    width = int(COLS * adv + 2 * PAD)
    height = line_h * len(rows) + 2 * PAD
    img = Image.new("RGB", (width, height), BG)
    d = ImageDraw.Draw(img)
    for r, row in enumerate(rows):
        for c, (ch, col, bold) in enumerate(row):
            d.text((PAD + c * adv, PAD + r * line_h), ch, font=fb if bold else fr, fill=col)
    # blinking-cursor block after the last prompt
    last = rows[-1]
    x = PAD + (len(last) - 1) * adv
    d.rectangle([x + 2, PAD + (len(rows) - 1) * line_h + 3,
                 x + adv - 2, PAD + (len(rows) - 1) * line_h + line_h - 3], fill=FG)
    img.save(out_png)
    return width, height


def make(number):
    folder = os.path.join(ROOT, "Assignment%d" % number)
    for out_name, commands in SHOTS[number].items():
        steps = []
        for cmd in commands:
            steps.append((cmd, run_in_wsl(folder, cmd)))
        w, h = render("Assignment%d" % number, steps, os.path.join(folder, out_name))
        print("Assignment%d/%s  %dx%d" % (number, out_name, w, h))


if __name__ == "__main__":
    wanted = [int(a) for a in sys.argv[1:]] or sorted(SHOTS)
    for n in wanted:
        make(n)
