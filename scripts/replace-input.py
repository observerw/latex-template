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
import re
import sys
from pathlib import Path
from typing import Iterable

tex_input_re = re.compile(r"^\s*\\input{(.*?)}")
tex_include_re = re.compile(r"^\s*\\include{(.*?)}")


def transform(
    base_path: Path,
    input_path: Path,
    ignore_comment: bool = False,
) -> Iterable[str]:
    def transform_line(base_path: Path, line: str) -> Iterable[str]:
        match = tex_input_re.match(line) or tex_include_re.match(line)
        if not match:
            yield line
            return

        include_path = match.group(1)
        if not include_path:
            raise ValueError(f"Invalid include path: {include_path}")

        include_path = Path(base_path / include_path)
        if not include_path.suffix:
            include_path = include_path.with_suffix(".tex")

        if not include_path.exists():
            raise FileNotFoundError(f"File {include_path} not found")

        yield "\n"
        for transformed_line in transform(base_path, include_path, ignore_comment):
            if ignore_comment and transformed_line.strip().startswith("%"):
                continue

            yield transformed_line
        yield "\n"

    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            yield from transform_line(base_path, line)


def main(args: argparse.Namespace):
    base_path = Path(args.base_path)
    input_path = Path(base_path / args.input)
    output_path = Path(base_path / args.output)

    if not input_path.exists():
        raise FileNotFoundError(f"File {input_path} not found")

    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(
            transform(
                base_path,
                input_path,
                ignore_comment=args.ignore_comment,
            )
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="input file")
    parser.add_argument("-o", "--output", help="output file")
    parser.add_argument("-b", "--base_path", help="base path for files")
    parser.add_argument("--ignore-comment", help="ignore comments", action="store_true")

    args = parser.parse_args()

    try:
        main(args)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        exit(1)

    print(f"File {args.input_path} transformed to {args.output_path}")
