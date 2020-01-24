BIN=venv/bin/

install:
	virtualenv venv -p python3
	$(BIN)pip install -r requirements.txt

run:
	$(BIN)python src/main.py

test:
	$(BIN)py.test