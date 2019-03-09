
PYTHON_COMMAND=python3
MIN_PYTHON_VERSION="Python 3.5"

test: dependencies
	$(PYTHON_COMMAND) test.py

dependencies:
	[ `command -v $(PYTHON_COMMAND)` ] || (echo "Python 3 not installed" && false)
	(echo $(MIN_PYTHON_VERSION); python3 --version) | sort -r | tail -n 1 | \
		grep -q $(MIN_PYTHON_VERSION) || ( \
			echo "Minimum Python Version: " $(MIN_PYTHON_VERSION) " is required" && \
			false)
