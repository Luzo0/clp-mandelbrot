CC = gcc
CFLAGS = -fPIC -shared -O3 -I./include
PYTHON = python3

all: libmandelbrot.so

libmandelbrot.so: src/mandelbrot.c include/mandelbrot.h
	$(CC) $(CFLAGS) -o $@ src/mandelbrot.c

run: libmandelbrot.so
	cd src && $(PYTHON) main.py

clean:
	rm -f libmandelbrot.so