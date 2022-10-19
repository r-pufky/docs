# Minimal makefile for Sphinx documentation
#
# Override options by using {VAR}={VALUE} on the CLI.
#
#   make html SPXBUILDDIR=/tmp/other
#

# Sphinx settings
SPXOPTS	     ?=
SPXBUILD     ?= sphinx-build
SPXSRCDIR    = source
SPXDIR	     = sphinx
SPXVENVDIR   = /opt/venvs/sphinx-docs
SPXVENV	     = $(SPXVENVDIR)/bin/activate
SPXBUILDDIR  = /tmp/docs
SPXTARGETDIR = docs

help:
	@echo "  make deps"
	@echo "      Install required package dependencies for doc generation."
	@echo
	@echo "  make install"
	@echo "      Install virtual environment for sphinx doc generation."
	@echo
	@echo "  make purge_cache"
	@echo "      Purges docs Python cache, build cache."
	@echo
	@echo "  make clean"
	@echo "      Removes all doc build artifacts & virtual environment."
	@echo
	@echo "  make html"
	@echo "      Build non-optimized docs in $(SPXBUILDDIR). Used for testing."
	@echo
	@echo "  make linkcheck"
	@echo "      Verifies docs links resolve properly."
	@echo
	@echo "  make copy"
	@echo "      Copies optimized docs in $(SPXBUILDDIR) to $(SPXTARGETDIR)."
	@echo "      Use 'make docs' or 'make docs_html'."
	@echo
	@echo "  make docs"
	@echo "      Build optimized docs in $(SPXBUILDDIR) to $(SPXTARGETDIR)."
	@echo "      COMMON COMMAND."

.PHONY: help Makefile

deps:
	@echo 'Verifying sphinx dependencies ...'
ifeq ($(OS_ID),debian)
	@sudo apt install python3-pip python3-venv
endif
ifeq ($(OS_ID),manjaro)
	@sudo pacman -Syu python-pip python-virtualenv
endif
	@echo 'Done.'

install:
	@echo 'Setting up sphinx python virtual environment ...'
	@sudo mkdir -p $(SPXVENVDIR)
	@sudo chown $(USER):$(USER) $(SPXVENVDIR)
	@python3 -m venv $(SPXVENVDIR)
	@. $(SPXVENV); python3 -m pip install --quiet --requirement $(SPXDIR)/requirements.txt
	@echo 'Done.'

purge_cache:
	@echo 'Cleaning sphinx cache ...'
	-@rm -rfv "$(SPXBUILDDIR)"
	-@find "$(SPXDIR)" -type d -name '__pycache__' -exec rm -rfv {} \;
	@echo 'Done.'

clean: purge_cache
	@echo 'Cleaning sphinx directories ...'
	-@rm -rfv "$(SPXVENVDIR)"
	@echo 'Done.'

html:
	@. $(SPXVENV); $(SPXBUILD) -M html "$(SPXSRCDIR)" "$(SPXBUILDDIR)" -j auto -c "$(SPXDIR)" $(SPXOPTS) $(O)

linkcheck:
	@. $(SPXVENV); $(SPXBUILD) -M linkcheck "$(SPXSRCDIR)" "$(SPXBUILDDIR)" -j auto -c "$(SPXDIR)" $(SPXOPTS) $(O)

copy:
	@mkdir -p $(SPXTARGETDIR)
	@touch $(SPXTARGETDIR)/.nojekyll
	@cp -av $(SPXBUILDDIR)/html/* "$(SPXTARGETDIR)"
	@rm -v "$(SPXTARGETDIR)/objects.inv"
	@rm -v "$(SPXTARGETDIR)/genindex.html"
	@rm -rfv "$(SPXTARGETDIR)/_sources"

docs: html copy
