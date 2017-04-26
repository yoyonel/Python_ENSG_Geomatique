BUILD = build
COURSENAME = Cours_Python
PRESENTATION_PYTHON = Presentation_Python
PRESENTATION_PYTHON_OBJECT = Presentation_Python_objet

USER_ID = $(shell id -u ${USER})
GROUP_ID = $(shell id -g ${USER})

all: book

book: epub html pdf

clean:
	rm -rf $(BUILD)

pdf: $(BUILD)/pdf/$(COURSENAME).pdf

$(BUILD)/pdf/$(COURSENAME).pdf: Cours_Python.tex
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

# html: $(BUILD)/html/$(PRESENTATION_PYTHON).html
# $(BUILD)/html/$(PRESENTATION_PYTHON).html: $(PRESENTATION_PYTHON).md

html: build/html deploy_html

build/html: build/html/$(PRESENTATION_PYTHON).html build/html/$(PRESENTATION_PYTHON_OBJECT).html

build/html/$(PRESENTATION_PYTHON).html: $(PRESENTATION_PYTHON).md
	# 
	mkdir -p $(BUILD)/html

	docker run \
		-it --rm \
		-v `pwd`:/source \
		-v /etc/group:/etc/group:ro \
		-v /etc/passwd:/etc/passwd:ro \
		-u $(USER_ID):$(GROUP_ID) \
		${DOCKER_ID_USER}/pandoc \
		bash -c "pandoc \
					-s -t html5 \
					--template=template/ign-ensg-revealjs.html \
					--section-divs \
					-o $@ \
					$^ \
				"
	#

build/html/$(PRESENTATION_PYTHON_OBJECT).html: $(PRESENTATION_PYTHON_OBJECT).md
	# 
	mkdir -p $(BUILD)/html

	docker run \
		-it --rm \
		-v `pwd`:/source \
		-v /etc/group:/etc/group:ro \
		-v /etc/passwd:/etc/passwd:ro \
		-u $(USER_ID):$(GROUP_ID) \
		${DOCKER_ID_USER}/pandoc \
		bash -c "pandoc \
					-s -t html5 \
					--template=template/ign-ensg-revealjs.html \
					--section-divs \
					-o $@ \
					$^ \
				"
	#

deploy_html: build/html/reveal.js build/html/css build/html/img

build/html/reveal.js:
	@mkdir -p $(BUILD)/html
	@ln -s $(realpath reveal.js) build/html/.

build/html/css:
	@mkdir -p $(BUILD)/html
	@ln -s $(realpath css) build/html/.

build/html/img:
	@mkdir -p $(BUILD)/html
	@ln -s $(realpath img) build/html/.

run_html: build/html
	firefox build/html/$(PRESENTATION_PYTHON).html build/html/$(PRESENTATION_PYTHON_OBJECT).html

.PHONY: all book clean epub html pdf
