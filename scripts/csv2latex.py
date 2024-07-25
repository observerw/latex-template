import argparse
from pathlib import Path

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="input file")

    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        raise FileNotFoundError(f"File {input_path} not found")
    
    text = input_path.read_text(encoding="utf-8")
    _, body = text.split('\n', 1)
    result = body.replace(',', ' & ').replace('\n', ' \\\\\n')

    print(result)