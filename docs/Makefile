SOURCES := $(wildcard *.tex)
all : skills.tex $(SOURCES)
	latexmk -pdf 80Page.tex
clean :
	latexmk -c
skills.tex : skills.ini
	../utilities/skillUtil.py tex skills.ini -o skills.tex
	touch 80Page.tex

