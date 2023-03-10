run:
	textual run --dev chatui/main.py

console:
	textual console

lint:
	pre-commit run --all-files
