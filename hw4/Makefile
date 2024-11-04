# Makefile for HW 4

# Variables
PYTHON = python3
SCRIPT = hw4.py
PIP = pip3

# Targets
.PHONY: all run clean requirements

all: requirements run

run:
	$(PYTHON) $(SCRIPT)

requirements:
	$(PIP) install matplotlib

clean:
	rm -f *.pyc
	rm -rf __pycache__
