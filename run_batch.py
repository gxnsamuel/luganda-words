"""
run_batch.py

Windows-friendly automation: runs clean_luganda_words.py over q1.txt ... q60.txt
in folder "q", writing cleaned output to a1.txt ... a60.txt in folder "a".
Missing q-files are skipped automatically.

Usage (from the same folder as clean_luganda_words.py):
    python run_batch.py
"""

import os
import subprocess

QDIR = "q"
ADIR = "a"
SCRIPT = "clean_luganda_words.py"
TOTAL = 60

os.makedirs(ADIR, exist_ok=True)

for i in range(1, TOTAL + 1):
    infile = os.path.join(QDIR, f"q{i}.txt")
    outfile = os.path.join(ADIR, f"a{i}.txt")

    if os.path.isfile(infile):
        subprocess.run(["python", SCRIPT, infile, outfile], check=False)
    else:
        print(f"Skipping: {infile} not found")

print("Batch processing complete.")