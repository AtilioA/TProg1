MAIN := trab1.py

all:
	python3 ${MAIN}

int:
	python3 -i ${MAIN}

time:
	time python3 ${MAIN}

clean:
	rm -r __pycache__

cleanW:
	rmdir /s /q __pycache__
