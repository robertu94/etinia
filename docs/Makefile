SOURCES := $(wildcard *.tex)
all : skills.tex $(SOURCES)
	latexmk -pdf 80Page.tex
clean :
	latexmk -c
skills.tex : skills.json
	../utilities/skill_util.py tex skills.json -o skills.tex
	touch 80Page.tex

