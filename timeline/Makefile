ALL:=$(wildcard *.md)
ALL_PNG:=$(ALL:.md=.pdf)

all: $(ALL_PNG) 

%.pdf: %.md
	mmdc -t forest -f -i $< -o $@

cont:
	 find . -name '*.md' | entr make

