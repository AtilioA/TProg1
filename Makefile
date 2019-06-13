MAIN := trab1.py

all:
	python3.6 ${MAIN}

int:
	python3.6 -i ${MAIN}

time:
	time python3.6 ${MAIN}

clean:
	rm -r __pycache__

cleanW:
	rmdir /s /q __pycache__
