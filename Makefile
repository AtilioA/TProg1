
# MAIN := trab1.py
# CC   := python

# all:
# 	$(CC) ${MAIN}

# int:
# 	$(CC) -i ${MAIN}

# time:
# 	time $(CC) ${MAIN}

clean:
	rm -r __pycache__

cleanW:
	rmdir /s /q __pycache__
