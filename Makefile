BUILD = build
BOOKNAME = Cours_Python
LATEX_CLASS = report

USER_ID = $(shell id -u ${USER})
GROUP_ID = $(shell id -g ${USER})

all: book

book: epub html pdf

clean:
	rm -rf $(BUILD)

pdf: $(BUILD)/pdf/$(BOOKNAME).pdf

$(BUILD)/pdf/$(BOOKNAME).pdf: Cours_Python.tex
	# 
	mkdir -p $(BUILD)/pdf

	# url: http://aty.sdsu.edu/bibliog/latex/LaTeXtoPDF.html
	docker run \
		-it --rm \
		-v `pwd`:/source \
		-v /etc/group:/etc/group:ro \
		-v /etc/passwd:/etc/passwd:ro \
		-u $(USER_ID):$(GROUP_ID) \
		${DOCKER_ID_USER}/pandoc \
		bash -c "pdflatex \
					-output-directory=$(BUILD)/pdf/ \
					$^ \
				"

.PHONY: all book clean epub html pdf
