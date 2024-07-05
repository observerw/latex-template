# check tlmgr, pdflatex, latexmk, texcount is installed
check:
	@echo "Checking dependencies..."
	@command -v tlmgr >/dev/null 2>&1 || { echo >&2 "I require tlmgr but it's not installed.  Aborting."; exit 1; }
	@command -v pdflatex >/dev/null 2>&1 || { echo >&2 "I require pdflatex but it's not installed.  Aborting."; exit 1; }
	@command -v latexmk >/dev/null 2>&1 || { echo >&2 "I require latexmk but it's not installed.  Aborting."; exit 1; }
	@command -v texcount >/dev/null 2>&1 || { echo >&2 "I require texcount but it's not installed.  Aborting."; exit 1; }

export:
	python3 scripts/replace-input.py -b $(shell pwd) -i main.tex -o export.tex

archive:
	git add . && git commit -m "archive" && git archive --format zip -o archive.zip HEAD