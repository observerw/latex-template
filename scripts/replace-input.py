"""
Replace \\input and \\include commands in a LaTeX file with the content of the included file.

ATTENTION: \\input and \\include must be placed at a separate line with no other content.

this will work:

\\input{sections/introduction.tex}

this will not work:

some text \\input{sections/introduction.tex}

this will work, but content after \\input will be ignored:

\\input{sections/introduction.tex} some text
"""

import argparse
from pathlib import Path
import re
import sys

tex_input_re = re.compile(r"^\s*\\input{(.*?)}")
tex_include_re = re.compile(r"^\s*\\include{(.*?)}")


def transform_line(base_path: Path, line: str):
    match = tex_input_re.match(line) or tex_include_re.match(line)
    if not match:
        return line

    include_path = match.group(1)
    if not include_path or not include_path.endswith(".tex"):
        raise ValueError(f"Invalid include path: {include_path}")

    include_path = Path(base_path / include_path)
    if not include_path.exists():
        raise FileNotFoundError(f"File {include_path} not found")

    return f"\n{include_path.read_text()}\n"


def transform(base_path: Path, input_path: Path):
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            yield transform_line(base_path, line)


def main(base_path: Path, input_path: Path, output_path: Path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(transform(base_path, input_path))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="input file")
    parser.add_argument("-o", "--output", help="output file")
    parser.add_argument("-b", "--base_path", help="base path for files")

    args = parser.parse_args()

    base_path = Path(args.base_path)
    input_path = Path(base_path / args.input)
    output_path = Path(base_path / args.output)

    if not input_path.exists():
        raise FileNotFoundError(f"File {input_path} not found")

    try:
        main(base_path, input_path, output_path)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        exit(1)

    print(f"File {input_path} transformed to {output_path}")
