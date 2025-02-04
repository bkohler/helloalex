# Makefile for compiling hello.c

CC = gcc
CFLAGS = -Wall
TARGET = hello

all: \$(TARGET)

\$(TARGET): hello.c
	\$(CC) \$(CFLAGS) -o \$(TARGET) hello.c

clean:
	rm -f \$(TARGET)
