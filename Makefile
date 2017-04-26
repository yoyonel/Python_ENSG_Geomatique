BUILD = build
BOOKNAME = Cours_Python
LATEX_CLASS = report

all: book

book: epub html pdf

clean:
	rm -rf $(BUILD)

pdf: $(BUILD)/pdf/$(BOOKNAME).pdf

$(BUILD)/pdf/$(BOOKNAME).pdf: Cours_Python.tex
	mkdir -p $(BUILD)/pdf

	docker run \
		-it --rm \
		-v `pwd`:/source \
		-v /etc/group:/etc/group:ro \
		-v /etc/passwd:/etc/passwd:ro \
		-u $( id -u $USER ):$( id -g $USER ) \
		${DOCKER_ID_USER}/pandoc \
		bash -c "pdflatex -output-directory=$(BUILD)/pdf/ $^"

.PHONY: all book clean epub html pdf
