PYV:=$(shell python -c "import sys;t='{v[0]}{v[1]}'.format(v=list(sys.version_info[:2]));sys.stdout.write(t)")

MAIN := trab1.py
CC   := python$(PYV)

all:
	$(CC) ${MAIN}

int:
	$(CC) -i ${MAIN}

time:
	time $(CC) ${MAIN}

clean:
	rm -r __pycache__

cleanW:
	rmdir /s /q __pycache__
